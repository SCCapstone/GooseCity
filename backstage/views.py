from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from .models import *
import pandas as pd
import json
# Create your views here.


#判断用户是否登录
def exist_sess(request):
    username=request.session.get("username")
    userid=request.session.get("userid")
    flag=request.session.get("flag")
    #判断是否存在有该用户
    userinfo=user_info.objects.filter(id=userid,username=username,superuser=1).exists()
    return userinfo
#退出登录
def logout(request):
    request.session.flush()
    return redirect(reverse("backstage:login"))
#登录界面
def login(request):
    if request.method=='POST':
        username=request.POST.get("name")
        password=request.POST.get("password")
        print(username)
        print(password)
        flag=user_info.objects.filter(username=username,password=password,superuser=1).exists()
        if flag:
            userinfo=user_info.objects.get(username=username,password=password)
            request.session['username']=username
            request.session['userid']=userinfo.id
            request.session['flag'] = userinfo.superuser
            return JsonResponse({"exist_count":1},safe=False)
        else:
            return JsonResponse({"exist_count":0},safe=False)

    else:
        return render(request,"administrator/login.html")


def welcome(request):
    flag = exist_sess(request)
    if flag:
        info={
            'product_count' :product.objects.all().count(),
            'user_count' :user_info.objects.filter(superuser=0).count(),
            'admin_count' : user_info.objects.filter(superuser=1).count(),
            'score_count' :score.objects.all().count(),
        }
        data_list, count_list = echart_data()

        return render(request,"administrator/welcome.html",context={"info":info,  "data_list":json.dumps(data_list),
            "count_list":str(count_list)})
    else:
        return redirect(reverse("backstage:login"))


def index(request):
    flag=exist_sess(request)
    if flag:
        info={
            "adminname":request.session.get("username")
        }
        return render(request,"administrator/index.html",context={"info":info})
    else:
        return redirect(reverse("backstage:login"))


#产品列表
def order(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            datas=[]

            products=product.objects.all().order_by("-create_at")
            for product_info in products:

                info={
                    "product_id":product_info.id,
                    "product_name":product_info.productname,
                    "product_image":str(product_info.image),
                    "product_desc":product_info.desc,
                    "create_at":product_info.create_at,
                    "update_at":product_info.change_at,
                    "userid":product_info.user.id,
                    "username":product_info.user.username,
                    "price":product_info.price
                }
                datas.append(info)
            paginator = Paginator(datas, 10,2)
            page = request.GET.get('page',"1")
            try:
                current_page = paginator.page(page)
                # todo: 注意捕获异常
            except PageNotAnInteger:
                # 如果请求的页数不是整数, 返回第一页。
                current_page = paginator.page(1)
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                books = paginator.page(paginator.num_pages)
            context={
                "datas":current_page,
                'paginator': paginator
            }
            return render(request,"administrator/order-list.html",context=context)
        else:
            select_type=int(request.POST.get("select_type"))
            keyword=request.POST.get("product_name")
            if select_type==-1:
                datas = []

                products = product.objects.all()
                for product_info in products:
                    info = {
                        "product_id": product_info.id,
                        "product_name": product_info.productname,
                        "product_image": str(product_info.image),
                        "product_desc": product_info.desc,
                        "create_at": product_info.create_at,
                        "update_at": product_info.change_at,
                        "userid": product_info.user.id,
                        "username": product_info.user.username
                    }
                    datas.append(info)
                paginator = Paginator(datas, 10, 2)
                page = request.GET.get('page', "1")
                try:
                    current_page = paginator.page(page)
                    # todo: 注意捕获异常
                except PageNotAnInteger:
                    # 如果请求的页数不是整数, 返回第一页。
                    current_page = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    books = paginator.page(paginator.num_pages)
                context = {
                    "datas": current_page,
                    'paginator': paginator
                }
                return render(request, "administrator/order-list.html", context=context)
            if select_type==0:
                datas = []

                products = product.objects.filter(productname__icontains=keyword)
                for product_info in products:
                    info = {
                        "product_id": product_info.id,
                        "product_name": product_info.productname,
                        "product_image": str(product_info.image),
                        "product_desc": product_info.desc,
                        "create_at": product_info.create_at,
                        "update_at": product_info.change_at,
                        "userid": product_info.user.id,
                        "username": product_info.user.username
                    }
                    datas.append(info)
                paginator = Paginator(datas, 10, 2)
                page = request.GET.get('page', "1")
                try:
                    current_page = paginator.page(page)
                    # todo: 注意捕获异常
                except PageNotAnInteger:
                    # 如果请求的页数不是整数, 返回第一页。
                    current_page = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    books = paginator.page(paginator.num_pages)
                context = {
                    "datas": current_page,
                    'paginator': paginator
                }
                return render(request, "administrator/order-list.html", context=context)
            if select_type==1:
                datas = []

                products = user_info.objects.get(username=keyword).user.all()
                for product_info in products:
                    info = {
                        "product_id": product_info.id,
                        "product_name": product_info.productname,
                        "product_image": str(product_info.image),
                        "product_desc": product_info.desc,
                        "create_at": product_info.create_at,
                        "update_at": product_info.change_at,
                        "userid": product_info.user.id,
                        "username": product_info.user.username
                    }
                    datas.append(info)
                paginator = Paginator(datas, 10, 2)
                page = request.GET.get('page', "1")
                try:
                    current_page = paginator.page(page)
                    # todo: 注意捕获异常
                except PageNotAnInteger:
                    # 如果请求的页数不是整数, 返回第一页。
                    current_page = paginator.page(1)
                except EmptyPage:
                    # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                    books = paginator.page(paginator.num_pages)
                context = {
                    "datas": current_page,
                    'paginator': paginator
                }
                return render(request, "administrator/order-list.html", context=context)

    else:
        return redirect(reverse("backstage:login"))


#产品添加
def product_add(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            return render(request,"administrator/product_add.html")
        else:
            #首先获取登录者的信息
            userid=request.session.get("userid")
            user=user_info.objects.get(pk=userid)
            productname=request.POST.get("productname")
            desc=request.POST.get("desc")
            try:
                price=float(request.POST.get("price"))
            except:
                print("*"*20)
                print(request.POST.get("price"))
                price=0.0
            image=request.FILES.get("file")
            product_demo=product()
            product_demo.productname=productname
            product_demo.image=image
            product_demo.desc=desc
            product_demo.user=user
            product_demo.price=price
            product_demo.save()
            return JsonResponse({"flag":1},safe=False)

    else:
        return redirect(reverse("backstage:login"))


#产品修改
def product_change(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            #首先获取产品id
            product_id=request.GET.get("id")
            #获取商品信息
            product_demo=product.objects.get(id=product_id)
            #商品信息获取
            info={
                "id":product_demo.id,
                "productname":product_demo.productname,
                "image":product_demo.image,
                "desc":product_demo.desc,
                "price":product_demo.price,
                "create_at":product_demo.create_at,
                "userid":product_demo.user.id,
                "username":product_demo.user.username
            }
            return render(request,"administrator/product_change.html",context={"info":info})
        if request.method=='POST':
            #首先获取产品信息
            id=request.POST.get("id")
            productname=request.POST.get("productname")
            desc=request.POST.get("desc")
            image=request.FILES.get("file")
            try:
                price=float(request.POST.get("price"))
            except:
                print("---"*20)
                print(request.POST.get("price"))
                price=0.0
            #获取产品信息
            product_demo=product.objects.get(pk=id)
            if image:
                product_demo.image=image
            product_demo.productname=productname
            product_demo.desc=desc
            product_demo.price=price
            product_demo.save()
            return JsonResponse({"flag":1},safe=False)
    else:
        return redirect(reverse("backstage:login"))



#产品删除
def product_delete(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            #获取产品的id
            id=request.GET.get("id")
            #获取产品信息
            product_demo=product.objects.get(pk=id)
            product_demo.delete()
            return JsonResponse({"flag":1},safe=False)
    else:
        return redirect(reverse("backstage:login"))



#用户管理界面
def user_list(request):
    flag = exist_sess(request)
    if flag:
        if request.method == 'GET':
            user_list=user_info.objects.filter(superuser=0)

            return render(request, "administrator/user-list.html",context={"infos":user_list})
    else:
        return redirect(reverse("backstage:login"))

#用户删除
def user_delete(request):
    flag = exist_sess(request)
    if flag:
        if request.method == 'GET':
            #获取用户的id
            id=request.GET.get("id")
            user_demo=user_info.objects.get(pk=id)
            user_demo.delete()
            return JsonResponse({"flag":1},safe=False)



    else:
        return redirect(reverse("backstage:login"))





#用户推荐界面
def member_similar(request):
    flag = exist_sess(request)
    if flag:
        get_all_user_score()
        userid_list = user_info.objects.all().values("id")
        # print(list(userid_list))
        similar_information = []
        for user_id in list(userid_list):
                # 用户相似列表，最相似的用户id，推荐的产品
                # print(user_id['id'])
            if score.objects.filter(user_id=user_info.objects.get(pk=user_id['id'])).exists():
                    similar_dict, similar_id, product_list = recommend(user_id['id'])
                    echarts_data1 = json.loads(similar_dict).keys()
                    echarts_data2 = json.loads(similar_dict).values()

                    people_name = user_info.objects.filter(id=similar_id).values("id")
                    s_m_id = list(score.objects.filter(user_id=similar_id).values("product_id"))
                    people_l_m = []
                    for product_id in s_m_id:
                        m_n = list(product.objects.filter(pk=product_id['product_id']).values("productname"))[0]['productname']
                        people_l_m.append(m_n)
                    info = {
                        "userid": user_id['id'],
                        "desc": json.loads(similar_dict),
                        "echarts_data1": list(echarts_data1),
                        "echarts_data2": list(echarts_data2),
                        "people_name": list(people_name)[0],
                        "people_looked_moive": people_l_m,
                    }
                    try:
                        product_id = list(product_list.keys())[-1]
                        product_score = list(product_list.values())[-1]
                        product_info = product.objects.filter(pk=product_id).values("image", "productname", "desc").first()
                        info["product_scroe"]=product_score
                        info["product_info"]=product_info
                    except:
                        pass
                        print("没有推荐的产品")


                    similar_information.append(info)
        print(similar_information)
        context = {
            "similar_information": similar_information

        }

        return render(request,"administrator/member-similar.html",context=context)
    else:
        return redirect(reverse("backstage:login"))


#管理员添加界面
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


#管理员的添加与修改
def admin_list(request):
    flag = exist_sess(request)
    if flag:
        superuser=user_info.objects.filter(superuser=1)

        return render(request,"administrator/admin-list.html",context={"infos":superuser,"userid":request.session.get("userid")})
    else:
        return redirect(reverse("backstage:login"))

def admin_change(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            #首先获取个人信息
            userid=request.session.get("userid")
            user_demo=user_info.objects.get(pk=userid)

            return render(request, "administrator/admin-edit.html",context={"info":user_demo})
        else:
            userid = request.session.get("userid")
            user_demo = user_info.objects.get(pk=userid)
            phone=request.POST.get("phonenum")
            old_password=request.POST.get("old_password")
            new_password=request.POST.get("new_password")
            if old_password == user_demo.password:
                user_demo.password=new_password
                user_demo.phonenum=phone
                user_demo.save()
                return JsonResponse({"flag":1},safe=False)
            else:
                return JsonResponse({"flag": 0}, safe=False)

    else:
        return redirect(reverse("backstage:login"))

def admin_add(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='POST':
            username=request.POST.get("username")
            password=request.POST.get("repass")
            phonenum=request.POST.get("phonenum")
            user=user_info()
            user.username=username
            user.password=password
            user.email=username
            user.superuser=1
            user.phonenum=phonenum
            user.save()
            return JsonResponse({"flag":1},safe=False)
        else:
            return render(request, "administrator/admin-add.html")
    else:
        return redirect(reverse("backstage:login"))





#用户相似度页面，并进行产品的推荐
def similar(request):
    flag = exist_sess(request)
    if flag:
        return render(request,"administrator/member-similar.html")
    else:
        return redirect(reverse("backstage:login"))







#数据分析部分
#按照时间段进行可视化展示
def echart_data():
    product_list=product.objects.all().values("create_at")
    product_info = []
    product_data = pd.DataFrame(list(product_list))
    print("-"*20)
    print(product_data)

    data_group = pd.to_datetime(product_data['create_at'])

    # 开始按照年，计算每一年上传的数量
    data_years = data_group.dt.year
    info = data_years.value_counts()
    year_list = info.to_dict()
    # 根据年内的数据
    # print(year_list)
    for demo in year_list:
        years = demo
        # 某一年下的月的数量信息
        information = {}

        month_group = data_group.loc[data_group.dt.year == demo]
        month_info = month_group.dt.month.value_counts().to_dict()
        # print(month_info)
        for m in month_info:
            # 某月下的信息量

            day_grop = month_group.loc[month_group.dt.month == m]
            day_info = day_grop.dt.day.value_counts().to_dict()
            # print(day_info)
            # 某日下的信息量
            for d in day_info:

                hour_group = day_grop.loc[day_grop.dt.day == d]
                hour_info = hour_group.dt.hour.value_counts().to_dict()
                # print(hour_info)
                # 某时下的数据量
                for h in hour_info:

                    minute_group = hour_group.loc[hour_group.dt.hour == h]
                    # print(minute_group)
                    minute_info = minute_group.dt.minute.value_counts().to_dict()
                    # print(minute_info)
                    for mi in minute_info:
                        info = {
                            "time": str(years) + "-" + str(m) + "-" + str(d) + " " + str(h) + ":" + str(mi),
                            "count": minute_info[mi]
                        }
                        product_info.append(info)

    # print(movie_info)
    movie_df = pd.DataFrame(product_info)
    # print(movie_df)
    # print(movie_df['time'].sort_values(ascending=True).tolist())
    # print(movie_df['count'].sort_values(ascending=True).tolist())
    return movie_df['time'].sort_values(ascending=True).tolist(),movie_df['count'].sort_values(ascending=False).tolist()



#算法实现部分

#获取全部用户的评分
def get_all_user_score():
    data_values=list(score.objects.all().values("user_id_id","product_id_id","score"))
    global user_item
    data=pd.DataFrame(data_values)
    # print(data)
    user_item=data.pivot(index='user_id_id',columns='product_id_id',values='score')
    # print(user_item)

#向量
def build_xy(user_id1,user_id2):
    bool_array = user_item.loc[user_id1].notnull() & user_item.loc[user_id2].notnull()
    #筛选出用户1与用户2共同评论出的产品

    return user_item.loc[user_id1, bool_array], user_item.loc[user_id2, bool_array]


# 皮尔逊相关系数user_id1表示的是去匹配的用户，user_id2数主要用户
def pearson(user_id1, user_id2):
    #对相同产品的得分
    x, y = build_xy(user_id1, user_id2)
    #取均值
    mean1, mean2 = x.mean(), y.mean()
    # 分母
    denominator = (sum((x-mean1)**2)*sum((y-mean2)**2))**0.5
    try:
        value = sum((x - mean1) * (y - mean2)) / denominator
    except ZeroDivisionError:
        value = 0
    # print(str(user_id1)+"与"+str(user_id2)+"的相似度为"+str(value))
    return round(value,2)

# 计算最相似的邻居
def computeNearestNeighbor(user_id):
    # print(json.dumps(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).to_dict()))
            #计算所有用户的相似度，   #得到最相似的用户
    print(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).nlargest(1).index[0])
    return json.dumps(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).to_dict()),user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).nlargest(1).index[0]


#用户相似列表，最相似的用户id，推荐的电影
def recommend(user_id):
    #用户的相似比,以及相似度最高的用户id
    user_similar,most_similar=computeNearestNeighbor(user_id)
    #找到用户没有评论过，相似用户评论过的物品从高到底进行排序
    product_list=user_item.loc[most_similar, user_item.loc[user_id].isnull() & user_item.loc[most_similar].notnull()].sort_values().to_dict()

    return user_similar,most_similar,product_list





#模板
def tempalte(request):
    flag = exist_sess(request)
    if flag:
        pass
    else:
        return redirect(reverse("backstage:login"))
