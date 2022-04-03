from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from .models import *
import pandas as pd
import json
# Create your views here.


#Determine if the user is logged in
def exist_sess(request):
    username=request.session.get("username")
    userid=request.session.get("userid")
    flag=request.session.get("flag")
    #Determine whether the user exists
    userinfo=user_info.objects.filter(id=userid,username=username,superuser=1).exists()
    return userinfo
#sign out
def logout(request):
    request.session.flush()
    return redirect(reverse("backstage:login"))
#login interface
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


#Product List
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
                # todo: Be careful about catching exceptions
            except PageNotAnInteger:
                # If the requested number of pages is not an integer, the first page is returned.
                current_page = paginator.page(1)
            except EmptyPage:
                # If the requested page count is not within the legal page count range, return the last page of the result.
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
                    # todo: Be careful about catching exceptions
                except PageNotAnInteger:
                    # If the requested number of pages is not an integer, the first page is returned.
                    current_page = paginator.page(1)
                except EmptyPage:
                    # If the requested page count is not within the legal page count range, return the last page of the result.
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
                    # todo: Be careful about catching exceptions
                except PageNotAnInteger:
                    # If the requested number of pages is not an integer, the first page is returned.
                    current_page = paginator.page(1)
                except EmptyPage:
                    # If the requested page count is not within the legal page count range, return the last page of the result.
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
                    
                except PageNotAnInteger:
                    
                    current_page = paginator.page(1)
                except EmptyPage:
                    
                    books = paginator.page(paginator.num_pages)
                context = {
                    "datas": current_page,
                    'paginator': paginator
                }
                return render(request, "administrator/order-list.html", context=context)

    else:
        return redirect(reverse("backstage:login"))


#product addition
def product_add(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            return render(request,"administrator/product_add.html")
        else:
            #Get the login information first
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


#Product modification
def product_change(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            #First get the product id
            product_id=request.GET.get("id")
            #Get product information
            product_demo=product.objects.get(id=product_id)
            #Product information acquisition
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
            #Get product information first
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
            #Get product information
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



#Product remove
def product_delete(request):
    flag = exist_sess(request)
    if flag:
        if request.method=='GET':
            #Get the id of the product
            id=request.GET.get("id")
            #Get product information
            product_demo=product.objects.get(pk=id)
            product_demo.delete()
            return JsonResponse({"flag":1},safe=False)
    else:
        return redirect(reverse("backstage:login"))



#User management interface
def user_list(request):
    flag = exist_sess(request)
    if flag:
        if request.method == 'GET':
            user_list=user_info.objects.filter(superuser=0)

            return render(request, "administrator/user-list.html",context={"infos":user_list})
    else:
        return redirect(reverse("backstage:login"))

#User deletion
def user_delete(request):
    flag = exist_sess(request)
    if flag:
        if request.method == 'GET':
            #Get the user's id
            id=request.GET.get("id")
            user_demo=user_info.objects.get(pk=id)
            user_demo.delete()
            return JsonResponse({"flag":1},safe=False)



    else:
        return redirect(reverse("backstage:login"))





#User recommendation interface
def member_similar(request):
    flag = exist_sess(request)
    if flag:
        get_all_user_score()
        userid_list = user_info.objects.all().values("id")
        # print(list(userid_list))
        similar_information = []
        for user_id in list(userid_list):
                # User similarity list, most similar user ids, recommended products
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
                        print("No recommended products")


                    similar_information.append(info)
        print(similar_information)
        context = {
            "similar_information": similar_information

        }

        return render(request,"administrator/member-similar.html",context=context)
    else:
        return redirect(reverse("backstage:login"))


#Admin add interface
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


#Administrator's Addition and Modification
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
            #Get personal information first
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





#User similarity page and recommend products
def similar(request):
    flag = exist_sess(request)
    if flag:
        return render(request,"administrator/member-similar.html")
    else:
        return redirect(reverse("backstage:login"))







#Data analysis part
#Visualize display by time period
def echart_data():
    product_list=product.objects.all().values("create_at")
    product_info = []
    product_data = pd.DataFrame(list(product_list))
    print("-"*20)
    print(product_data)

    data_group = pd.to_datetime(product_data['create_at'])

    # Start by year, calculate the number of uploads per year
    data_years = data_group.dt.year
    info = data_years.value_counts()
    year_list = info.to_dict()
    # Based on data for the year
    # print(year_list)
    for demo in year_list:
        years = demo
        # Quantity information for months under a certain year
        information = {}

        month_group = data_group.loc[data_group.dt.year == demo]
        month_info = month_group.dt.month.value_counts().to_dict()
        # print(month_info)
        for m in month_info:
            # Amount of information in a month

            day_grop = month_group.loc[month_group.dt.month == m]
            day_info = day_grop.dt.day.value_counts().to_dict()
            # print(day_info)
            # amount of information on a given day
            for d in day_info:

                hour_group = day_grop.loc[day_grop.dt.day == d]
                hour_info = hour_group.dt.hour.value_counts().to_dict()
                # print(hour_info)
                # amount of data at a time
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



#Algorithm implementation part

#Get the ratings of all users
def get_all_user_score():
    data_values=list(score.objects.all().values("user_id_id","product_id_id","score"))
    global user_item
    data=pd.DataFrame(data_values)
    # print(data)
    user_item=data.pivot(index='user_id_id',columns='product_id_id',values='score')
    # print(user_item)

#vector
def build_xy(user_id1,user_id2):
    bool_array = user_item.loc[user_id1].notnull() & user_item.loc[user_id2].notnull()
    #Filter out the products commented by user 1 and user 2

    return user_item.loc[user_id1, bool_array], user_item.loc[user_id2, bool_array]


# Pearson correlation coefficient user_id1 represents the user to match, user_id2 is the main user
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
    
    return round(value,2)

# Calculate the most similar neighbors
def computeNearestNeighbor(user_id):
    # print(json.dumps(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).to_dict()))
           #Calculate the similarity of all users, #Get the most similar user
    print(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).nlargest(1).index[0])
    return json.dumps(user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).to_dict()),user_item.drop(user_id).index.to_series().apply(pearson, args=(user_id,)).nlargest(1).index[0]


#User similarity list, most similar user id, recommended movie
def recommend(user_id):
   #The similarity ratio of users, and the user id with the highest similarity
    user_similar,most_similar=computeNearestNeighbor(user_id)
    #Find users who have not commented, and sort items that have been commented by similar users from high to bottom
    product_list=user_item.loc[most_similar, user_item.loc[user_id].isnull() & user_item.loc[most_similar].notnull()].sort_values().to_dict()

    return user_similar,most_similar,product_list





#template
def tempalte(request):
    flag = exist_sess(request)
    if flag:
        pass
    else:
        return redirect(reverse("backstage:login"))
