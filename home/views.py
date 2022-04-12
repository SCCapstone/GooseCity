from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from backstage.models import *
import pandas as pd
import os
from sale.settings import BASE_DIR
import json
from alipay import AliPay
from datetime import datetime
import time
# Create your views here.


def exist_sess(request):
    username=request.session.get("username")
    userid=request.session.get("userid")

    userinfo=user_info.objects.filter(id=userid,username=username,superuser=0).exists()
    return userinfo

def logout(request):
    request.session.flush()
    return redirect(reverse("home:login"))

def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        flag=user_info.objects.filter(username=username,password=password).exists()
        if flag:
            userinfo=user_info.objects.get(username=username,password=password)
            request.session['username']=username
            request.session['userid']=userinfo.id
            request.session['flag']=userinfo.superuser
            return JsonResponse({"flag":1},safe=False)
        else:
            return JsonResponse({"flag":0},safe=False)

    else:
        return render(request,"login/login.html")

def register(request):
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        phonenum=request.POST.get("phonenum")
        password=request.POST.get("password")
        try:
            userinfo=user_info()
            userinfo.username=username
            userinfo.password=password
            userinfo.email=email
            userinfo.phonenum=phonenum
            userinfo.save()
            return JsonResponse({"flag":1},safe=False) #
        except:
            return JsonResponse({"flag":0},safe=False)
    else:
        return render(request,"login/register.html")

def count_cart(request):
    flag=exist_sess(request)
    if flag:
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        cart_demo=cart.objects.filter(user_id=user_demo,flag=0)
        count=len(cart_demo)
        return cart_demo,count
    else:
        return redirect(reverse("home:login"))

def index(request):
    flag = exist_sess(request)
    if flag:

        userid=request.session.get("userid")
        user=user_info.objects.get(pk=userid)

        info={
            "score_num":score.objects.filter(user_id=user).count(),
            "product_num":product.objects.all().count(),
            "user_count":user_info.objects.filter(superuser=0).all().count(),
            "flag":0
        }

        data=pd.DataFrame(score.objects.all().values("product_id_id","score"))
        count_demo,count=count_cart(request)
        if data.shape[0]!=0:
            try:
                productid=data.groupby(by="product_id_id").mean().sort_values(by="score",ascending=False).reset_index().loc[0,"product_id_id"]
                info["product_info"]=product.objects.get(pk=productid)

                score_height = list(data.groupby(by="product_id_id").mean().sort_values(by="score", ascending=False).reset_index().loc[
                    :3, "product_id_id"])
                product_list=product.objects.filter(pk__in=score_height)
                info['product_list']=product_list

                get_all_user_score()
                if score.objects.filter(user_id=user_info.objects.get(pk=userid)).exists():
                    similar_dict, similar_id, product_list = recommend(userid)

                    try:

                        product_id = list(product_list.keys())[-1]
                        product_score = list(product_list.values())[-1]
                        product_info = product.objects.filter(pk=product_id).values("id","image", "productname", "desc").first()
                        info["product_scroe"] = product_score
                        info["product_info"] = product_info
                        info['flag'] = 1
                    except:
                        pass

                product_all=product.objects.all().order_by("-create_at")[:8]
                info['last_product']=product_all
                height_score_list = list(score.objects.filter(user_id=user).order_by("-score").values("score"))
                if len(height_score_list) != 0:
                    info['height_score'] = height_score_list[0]['score']
                return render(request,"index/index2.html",context={"info":info,"cart_demo":count_demo,"count":count})
            except:
                height_score_list = list(score.objects.filter(user_id=user).order_by("-score").values("score"))
                if len(height_score_list) != 0:
                    info['height_score'] = height_score_list[0]['score']
                product_all = product.objects.all().order_by("-create_at")[:8]
                info['last_product'] = product_all
                return render(request, "index/index2.html", context={"info": info,"cart_demo":count_demo,"count":count})
        else:
            height_score_list = list(score.objects.filter(user_id=user).order_by("-score").values("score"))
            if len(height_score_list) != 0:
                info['height_score'] = height_score_list[0]['score']
            product_all = product.objects.all().order_by("-create_at")[:8]
            info['last_product'] = product_all
            return render(request, "index/index2.html", context={"info": info,"cart_demo":count_demo,"count":count})
    else:
        return redirect(reverse("home:login"))


def detail_page(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            id=request.GET.get("id")
            count_demo, count = count_cart(request)
            product_demo=product.objects.get(pk=id)
            scores=product_demo.productid.all()
            username = request.session.get("username")
            userid = request.session.get("userid")
            user_demo = user_info.objects.get(
                id=userid,
                username=username
            )
            cart_demo=cart.objects.filter(user_id=user_demo,product_id=product_demo,flag=0).exists()
            if cart_demo:
                info={

                        "userid":request.session.get("userid"),
                        "product":product_demo,
                        "username":scores,
                        "cart_demo":cart_demo
                }
            else:
                info = {
                    "userid": request.session.get("userid"),
                    "product": product_demo,
                    "username": scores,
                }

            return render(request,'index/single.html',context={"info":info,"cart_demo":count_demo,"count":count,"count_demo":cart_demo})
        else:
            user_id=request.session.get("userid")
            user_demo=user_info.objects.get(pk=user_id)
            product_id=int(request.POST.get("product_id"))
            product_demo=product.objects.get(pk=product_id)
            try:
                score_demo=int(request.POST.get("score"))
                if score_demo>10 or score_demo<0:
                    score_demo = 0
            except:
                score_demo=0
            exist_demo=score.objects.filter(user_id=user_demo,product_id=product_demo).exists()
            if exist_demo:
                demo=score.objects.get(user_id=user_demo,product_id=product_demo)
                demo.score=score_demo
                demo.save()
            else:
                demo=score()
                demo.user_id=user_demo
                demo.product_id=product_demo
                demo.score=score_demo
                demo.save()
            return redirect(reverse("home:detail_page")+"?id={}".format(product_id))


    else:
        return redirect(reverse("home:login"))




def search(request):
    flag = exist_sess(request)
    if flag:
        keyword=request.GET.get("keyword")
        count_demo, count = count_cart(request)
        if keyword==None:
            product_list = product.objects.all()[:10]
            return render(request, 'index/search.html',
                          context={"infos": product_list, "cart_demo": count_demo, "count": count})
        else:
            product_list=product.objects.filter(productname__icontains=keyword)
            return render(request,'index/search.html',context={"infos":product_list,"cart_demo":count_demo,"count":count,"keyword":keyword})
    else:
        return redirect(reverse("home:login"))


def tempalte(request):
    flag = exist_sess(request)
    if flag:
        pass
    else:
        return redirect(reverse("home:login"))


def get_all_user_score():
    data_values=list(score.objects.all().values("user_id_id","product_id_id","score"))
    global user_item
    data=pd.DataFrame(data_values)
    # print(data)
    user_item=data.pivot(index='user_id_id',columns='product_id_id',values='score')


def build_xy(user_id1,user_id2):
    bool_array = user_item.loc[user_id1].notnull() & user_item.loc[user_id2].notnull()


    return user_item.loc[user_id1, bool_array], user_item.loc[user_id2, bool_array]



def pearson(user_id1, user_id2):

    x, y = build_xy(user_id1, user_id2)

    mean1, mean2 = x.mean(), y.mean()

    denominator = (sum((x-mean1)**2)*sum((y-mean2)**2))**0.5
    try:
        value = sum((x - mean1) * (y - mean2)) / denominator
    except ZeroDivisionError:
        value = 0
    return round(value,2)


def computeNearestNeighbor(user_id):

    return json.dumps(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).to_dict()),user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).nlargest(1).index[0]


def recommend(user_id):
    user_similar,most_similar=computeNearestNeighbor(user_id)
    product_list=user_item.loc[most_similar, user_item.loc[user_id].isnull() & user_item.loc[most_similar].notnull()].sort_values().to_dict()

    return user_similar,most_similar,product_list


def user_person(request):
    flag = exist_sess(request)
    if flag:
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        cart_list = cart.objects.filter(user_id=user_demo,flag=0)
        count_demo, count = count_cart(request)
        # return render(request,"user/index.html",{
        #     "user_info":user_demo,
        #     "cart_list":cart_list
        # })
        return render(request,"user/demo.html",{
            "user_info":user_demo,
            "cart_list":cart_list,"cart_demo":count_demo,"count":count,
            "con": "Added shopping cart"
        })
    else:
        return redirect(reverse("home:login"))




def user_person2(request):
    flag = exist_sess(request)
    if flag:
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        id=request.GET.get("id")
        product_demo=product.objects.get(pk=id)
        count_demo, count = count_cart(request)
        exist_demo=cart.objects.filter(user_id=user_demo,flag=0,product_id=product_demo).exists()
        if exist_demo:
            pass
        else:
            cart_demo=cart.objects.create(user_id=user_demo,product_id=product_demo,flag=0)
        cart_list = cart.objects.filter(user_id=user_demo, flag=0, product_id=product_demo)
        return render(request,"user/demo.html",{
            "user_info":user_demo,
            "cart_list":cart_list,"cart_demo":count_demo,"count":count,
            "con":"An item to make a purchase"
        })
    else:
        return redirect(reverse("home:login"))








def shopping_cart(request):
    flag = exist_sess(request)
    if flag:
        username=request.session.get("username")
        userid=request.session.get("userid")
        user_demo=user_info.objects.get(
            id=userid,
            username=username
        )
        cart_list=cart.objects.filter(user_id=user_demo)

    else:
        return redirect(reverse("home:login"))

def add_cart(request):
    flag = exist_sess(request)
    if flag:
        username=request.session.get("username")
        userid=request.session.get("userid")
        user_demo=user_info.objects.get(
            id=userid,
            username=username
        )
        product_id=int(request.GET.get("productid"))
        product_demo=product.objects.get(pk=product_id)
        if cart.objects.filter(user_id=user_demo,product_id=product_demo,flag=0).exists():
            demo=cart.objects.get(user_id=user_demo, product_id=product_demo,flag=0)
            demo.num=demo.num+1
        else:
            cart.objects.create(user_id=user_demo,product_id=product_demo)
        return JsonResponse({"flag":1})

    else:
        return redirect(reverse("home:login"))



def get_alipay():
    alipay_public_path=os.path.join(BASE_DIR,"home","key","alipay_public_2048.txt")
    app_private_path=os.path.join(BASE_DIR,"home","key","app_private_2048.txt")

    alipay_public_string=""
    app_private_string = ""
    with open(alipay_public_path,"r") as tf:
        alipay_public_string=tf.read()
    with open(app_private_path,"r") as tf:
        app_private_string=tf.read()

    alipay=AliPay(
        appid="2021000119609704",
        alipay_public_key_string=alipay_public_string,
        app_private_key_string=app_private_string,
        app_notify_url=None,
        sign_type="RSA2"
    )
    return alipay

def buy_manager(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            card_id=int(request.GET.get("cart_id"))
            username = request.session.get("username")
            userid = int(request.session.get("userid"))
            user_demo = user_info.objects.get(id=userid, username=username)
            card_demo=cart.objects.get(user_id=user_demo,pk=card_id)
            alipay=get_alipay()
            order_string=alipay.api_alipay_trade_page_pay(
                subject=card_demo.product_id.productname,
                out_trade_no=card_demo.pk,
                total_amount=card_demo.num*card_demo.product_id.price,
                return_url="http://127.0.0.1:8000/exist_buy/?card_id="+str(card_demo.pk),
                notify_url=None,
            )
            url="https://openapi.alipaydev.com/gateway.do?"+order_string
            return redirect(url)

#判断支付是否成功
def exist_buy(request):
    alipay=get_alipay()
    params=request.GET.dict()
    sign=params.pop("sign",None)
    card_id = params.pop("card_id")
    status=alipay.verify(params,sign)
    if status:
        username = request.session.get("username")
        userid = int(request.session.get("userid"))
        user_demo = user_info.objects.get(id=userid, username=username)
        card_demo = cart.objects.get(user_id=user_demo, pk=int(card_id))
        card_demo.flag=1
        card_demo.save()
        return redirect("home:done_s")
    else:
        return  redirect("home:user_person")

def credit_buy(request):
    flag = exist_sess(request)
    if flag:
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        cart_id = int(request.GET.get("cartid"))
        cart_demo = cart.objects.get(pk=cart_id,user_id=user_demo,flag=0)
        credit_demo=credit_card.objects.filter(user_card=user_demo).exists()
        if len(user_demo.position)==0 or len(user_demo.phonenum)==0:
            return JsonResponse({"flag": 2})
        else:
            if credit_demo:
                cart_demo.flag=1
                cart_demo.save()
                return JsonResponse({"flag": 1})

            else:
                return JsonResponse({"flag": 0})

    else:
        return redirect(reverse("home:login"))

def change_count(request):
    flag = exist_sess(request)
    if flag:
        if request.method == 'GET':
            id=int(request.GET.get("id"))
            num=int(request.GET.get("num"))
            username = request.session.get("username")
            userid = int(request.session.get("userid"))
            user_demo=user_info.objects.get(id=userid,username=username)
            cart_demo=cart.objects.get(pk=id,user_id=user_demo)
            cart_demo.num=num
            cart_demo.save()
            return JsonResponse({"flag":1})


def change_cart(request):
    flag = exist_sess(request)
    if flag:
        product_id=int(request.GET.get("product_id"))
        product_demo=product.objects.get(pk=product_id)
        num=int(request.GET.get("num"))
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        cart_demo = cart.objects.get(user_id=user_demo,
                                     product_id=product_demo,
                                     flag=0)
        cart_demo.num=num
        cart_demo.save()
        return JsonResponse({"flag": 1})

    else:
        return redirect(reverse("home:login"))


def delete_cart(request):
    flag = exist_sess(request)
    if flag:
        product_id=int(request.GET.get("productid"))
        product_demo=product.objects.get(pk=product_id)
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        cart_demo = cart.objects.get(user_id=user_demo,
                                     product_id=product_demo,
                                     flag=0)
        cart_demo.delete()
        return JsonResponse({"flag": 1})

    else:
        return redirect(reverse("home:login"))

def delete_cart2(request):
    flag = exist_sess(request)
    if flag:
        id=request.GET.get("id")
        product_id=int(request.GET.get("productid"))
        product_demo=product.objects.get(pk=product_id)
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        cart_demo = cart.objects.get(user_id=user_demo,
                                     pk=id,
                                     product_id=product_demo,
                                     flag=0)
        cart_demo.delete()
        return redirect(reverse("home:user_person"))

    else:
        return redirect(reverse("home:login"))

def change_info(request):
    flag = exist_sess(request)
    if flag:
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        credit_demo=credit_card.objects.filter(user_card=user_demo).exists()
        info={}
        if credit_demo:
            credit = credit_card.objects.get(user_card=user_demo)
            info={
                "id":credit.pk,
                "username":credit.username,
                "card_num":credit.card_num,
                "date":credit.date
            }
        if request.method=='GET':
            count_demo, count = count_cart(request)
            return render(request,"user/person_info.html",{"info":user_demo,"user_info":user_demo,"credit_demo":info,"cart_demo":count_demo,"count":count})
        if request.method=='POST':
            username=request.POST.get("username")
            email=request.POST.get("email")
            # password=request.POST.get("password")
            phonenum=request.POST.get("phonenum")
            position=request.POST.get("position")
            if len(username)==0:
                return JsonResponse({"flag": 4})
            if len(position)>200:
                return JsonResponse({"flag": 3})
            try:
                if user_demo.username!=username:
                    user_demo.username=username

                if user_demo.email!=email:
                    user_demo.email=email


                if user_demo.phonenum!=phonenum:
                    user_demo.phonenum=phonenum

                user_demo.position=position
                user_demo.save()
                return JsonResponse({"flag":1})
            except:
                return JsonResponse({"flag":2})

    else:
        return redirect(reverse("home:login"))








def done_s(request):
    flag = exist_sess(request)
    if flag:
        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        cart_list = cart.objects.filter(user_id=user_demo,flag=1)
        count_demo, count = count_cart(request)
        try:
            prod=product.objects.all()
            data2=pd.DataFrame(prod.values())
            data=pd.DataFrame(cart_list.values())

            data=pd.merge(left=data,right=data2,left_on="product_id_id",right_on="id",how="inner")
            data['sum']=data['num']*data['price']
            cart_list=json.loads(data.to_json(orient="records"))
        except:
            pass
        return render(request,"user/index2.html",{
            "user_info":user_demo,
            "cart_list":cart_list,"cart_demo":count_demo,"count":count
        })
    else:
        return redirect(reverse("home:login"))

def purchases(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            username = request.session.get("username")
            userid = request.session.get("userid")
            user_demo = user_info.objects.get(
                id=userid,
                username=username
            )
            produced=request.GET.get("produced")
            print(produced)
            product_demo=product.objects.get(pk=produced)
            cart.objects.create(user_id=user_demo,product_id=product_demo,flag=0)
            return JsonResponse({"flag":1})
    else:
        return redirect(reverse("home:login"))


def update_credit_card(request):
    flag = exist_sess(request)
    if flag:
        if request.method == 'POST':
            username = request.session.get("username")
            userid = request.session.get("userid")
            user_demo = user_info.objects.get(
                id=userid,
                username=username
            )
            credit_id=request.POST.get("credit_id")
            username=request.POST.get("username")
            number=str(request.POST.get("number"))
            date=request.POST.get("date")
            dat=date
            if len(username)==0:
                return JsonResponse({"mag": "The name cannot be blank", "flag": 0})
            if len(date)==7:
                dat=date+"-28"
            now = datetime.now().strftime("%Y-%m")
            try:
                ft = time.mktime(time.strptime(date, "%Y-%m"))
            except:
                ft=time.mktime(time.strptime(date,"%Y-%m"))
            st=time.mktime(time.strptime(now,"%Y-%m"))
            if number.isdigit():
                if len(number)==11:
                    if ft>=st:
                        if credit_id:
                            try:
                                credit_demo=credit_card.objects.get(pk=credit_id,user_card=user_demo)
                                credit_demo.username=username
                                credit_demo.card_num=number
                                credit_demo.date=dat
                                credit_demo.save()
                                return JsonResponse({"mag":"Information updated successfully","flag":1})
                            except:
                                return JsonResponse({"mag": "Wrong date","flag":0})
                        else:
                            try:
                                credit_card.objects.create(user_card=user_demo,
                                                           username=username,
                                                           card_num=number,
                                                           date=date)
                                return JsonResponse({"mag": "successfully added", "flag": 1})
                            except:
                                return JsonResponse({"mag": "Wrong date","flag":0})
                    else:
                        return JsonResponse({"mag": "The card is out of date", "flag": 0})

                else:
                    return JsonResponse({"mag": "Credit card 11 Numbers","flag":0})
            else:
                return JsonResponse({"mag": "The credit card number must be numerical","flag":0})
    else:
        return redirect(reverse("home:login"))
