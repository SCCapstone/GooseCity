from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from backstage.models import *
import pandas as pd
import json
import json
# Create your views here.

#Determine if the user is logged in
def exist_sess(request):
    username=request.session.get("username")
    userid=request.session.get("userid")
    #Determine whether the user exists
    userinfo=user_info.objects.filter(id=userid,username=username,superuser=0).exists()
    return userinfo
#sign out
def logout(request):
    request.session.flush()
    return redirect(reverse("home:login"))
#login interface
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
#Registration interface
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



def index(request):
    flag = exist_sess(request)
    if flag:
        #First get user information
        userid=request.session.get("userid")
        user=user_info.objects.get(pk=userid)
        # Number of products reviewed
        info={
            "score_num":score.objects.filter(user_id=user).count(),
            "product_num":product.objects.all().count(),
            "user_count":user_info.objects.filter(superuser=0).all().count(),
            "flag":0
        }
        # Take the product with a higher score
        data=pd.DataFrame(score.objects.all().values("product_id_id","score"))

        if data.shape[0]!=0:
            try:
                productid=data.groupby(by="product_id_id").mean().sort_values(by="score",ascending=False).reset_index().loc[0,"product_id_id"]
                info["product_info"]=product.objects.get(pk=productid)
                #4 products with high ratings
                score_height = list(data.groupby(by="product_id_id").mean().sort_values(by="score", ascending=False).reset_index().loc[
                    :3, "product_id_id"])
                product_list=product.objects.filter(pk__in=score_height)
                info['product_list']=product_list
                #Get a list of recommended products
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
                        # wrong id
                        print("wrong id")




                #Access to product categories
                product_all=product.objects.all().order_by("-create_at")[:8]
                info['last_product']=product_all

                return render(request,"index/index.html",context={"info":info})
            except:
                height_score_list = list(score.objects.filter(user_id=user).order_by("-score").values("score"))
                if len(height_score_list) != 0:
                    info['height_score'] = height_score_list[0]['score']
                product_all = product.objects.all().order_by("-create_at")[:8]
                info['last_product'] = product_all
                return render(request, "index/index.html", context={"info": info})
        else:
            height_score_list = list(score.objects.filter(user_id=user).order_by("-score").values("score"))
            if len(height_score_list) != 0:
                info['height_score'] = height_score_list[0]['score']
            product_all = product.objects.all().order_by("-create_at")[:8]
            info['last_product'] = product_all
            return render(request, "index/index.html", context={"info": info})
    else:
        return redirect(reverse("home:login"))


def detail_page(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            id=request.GET.get("id")
            #Find information about this product
            print(id)
            product_demo=product.objects.get(pk=id)
            scores=product_demo.productid.all()
            #Find relevant shopping cart information
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

            return render(request,'index/single.html',context={"info":info})
        else:
            user_id=request.session.get("userid")
            user_demo=user_info.objects.get(pk=user_id)
            product_id=int(request.POST.get("product_id"))
            product_demo=product.objects.get(pk=product_id)
            try:
                score_demo=int(request.POST.get("score"))
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
        if keyword==None:
            product_list = product.objects.all()[:10]
        else:
            product_list=product.objects.filter(productname__icontains=keyword)
        return render(request,'index/search.html',context={"infos":product_list})
    else:
        return redirect(reverse("home:login"))


def tempalte(request):
    flag = exist_sess(request)
    if flag:
        pass
    else:
        return redirect(reverse("home:login"))
#Algorithm implementation part

#Get the ratings of all users
def get_all_user_score():
    data_values=list(score.objects.all().values("user_id_id","product_id_id","score"))
    global user_item
    data=pd.DataFrame(data_values)
    # print(data)
    user_item=data.pivot(index='user_id_id',columns='product_id_id',values='score')

#vector
def build_xy(user_id1,user_id2):
    bool_array = user_item.loc[user_id1].notnull() & user_item.loc[user_id2].notnull()
    #Filter out the products commented by user 1 and user 2

    return user_item.loc[user_id1, bool_array], user_item.loc[user_id2, bool_array]


# The Pearson correlation coefficient user_id1 represents the user to be matched, and user_id2 counts the main users
def pearson(user_id1, user_id2):
    #Score for the same product
    x, y = build_xy(user_id1, user_id2)
    #AVG
    mean1, mean2 = x.mean(), y.mean()
    # denominator
    denominator = (sum((x-mean1)**2)*sum((y-mean2)**2))**0.5
    try:
        value = sum((x - mean1) * (y - mean2)) / denominator
    except ZeroDivisionError:
        value = 0
    # The similarity between print(str(user_id1)+" and "+str(user_id2)+" is "+str(value))
    return round(value,2)

# Calculate the most similar neighbors
def computeNearestNeighbor(user_id):
    # print(json.dumps(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).to_dict()))
            #Calculate the similarity of all users, #get the most similar users
    return json.dumps(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).to_dict()),user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).nlargest(1).index[0]


#User similarity list, most similar user ids, recommended movies
def recommend(user_id):
    #The similarity ratio of users, and the user id with the highest similarity
    user_similar,most_similar=computeNearestNeighbor(user_id)
    #Find the items that users have not commented on, and sort items from high to bottom that similar users have commented on
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

        return render(request,"user/index.html",{
            "user_info":user_demo,
            "cart_list":cart_list
        })
    else:
        return redirect(reverse("home:login"))




def shopping_cart(request):
    flag = exist_sess(request)
    if flag:
        #Get user information
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
        #Get user information
        username=request.session.get("username")
        userid=request.session.get("userid")
        user_demo=user_info.objects.get(
            id=userid,
            username=username
        )
        #Get product information
        product_id=int(request.GET.get("productid"))
        product_demo=product.objects.get(pk=product_id)
        cart.objects.create(user_id=user_demo,product_id=product_demo)
        return JsonResponse({"flag":1})

    else:
        return redirect(reverse("home:login"))


def change_cart(request):
    flag = exist_sess(request)
    if flag:
        # get product id
        product_id=int(request.GET.get("product_id"))
        product_demo=product.objects.get(pk=product_id)

        #Get modifications to modify product quantity
        num=int(request.GET.get("num"))
        # Get user information
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
        # get product id
        product_id=int(request.GET.get("productid"))
        product_demo=product.objects.get(pk=product_id)
        # Get user information
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
        # get product id
        product_id=int(request.GET.get("productid"))
        product_demo=product.objects.get(pk=product_id)
        # Get user information
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
        return redirect(reverse("home:user_person"))

    else:
        return redirect(reverse("home:login"))

def change_info(request):
    flag = exist_sess(request)
    if flag:
        # Get user information

        username = request.session.get("username")
        userid = request.session.get("userid")
        user_demo = user_info.objects.get(
            id=userid,
            username=username
        )
        if request.method=='GET':
            return render(request,"user/person_info.html",{"info":user_demo,"user_info":user_demo})
        if request.method=='POST':
            username=request.POST.get("username")
            email=request.POST.get("email")
            # password=request.POST.get("password")
            phonenum=request.POST.get("phonenum")
            position=request.POST.get("position")
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

        return render(request,"user/index.html",{
            "user_info":user_demo,
            "cart_list":cart_list
        })
    else:
        return redirect(reverse("home:login"))