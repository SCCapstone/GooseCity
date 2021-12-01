from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import defaultdict
import json
from itertools import chain
# Create your views here.
from django.core import serializers
from .models import user_info,shoping_info,shopping_cart

#用户登录操作
@csrf_exempt
def login(request):
    print("jinru")
    if request.method=='POST':
        username=request.POST.get("email")
        password=request.POST.get("password")
        user=user_info.objects.filter(username=username,password=password)
        if user.count()==1:
            request.session['id']=user[0].id
            request.session['username']=username
            request.session['password']=password
            return JsonResponse({"errorMsg":"success","token":username},safe=False)
        else:
            return JsonResponse({"errorMsg":"fail","token":"error"},safe=False)

def logout(request):
    request.session.flush()
    return JsonResponse({"errorMsg": "fail", "token": "error"}, safe=False)

def index(request):
    #从数据库中获取商品列表
    # shopping_list=shoping_info.objects.all().values("id","title","desc","image","price","count")
    shopping_list=shoping_info.objects.all()
    print(shopping_list)
    return JsonResponse(serializers.serialize("json",shopping_list),safe=False,)

#实现物品的的查找
def search(request):
    #首先过去关键词
    keyword=request.GET.get("keyword")
    #通过关键词进行模糊查询
    #分别根据商品名称以及商品描述进行检索
    shopping_list1=shoping_info.objects.filter(title__icontains=keyword)
    shopping_list2=shoping_info.objects.filter(desc__icontains=keyword)
    # shopping_list=chain(shopping_list2,shopping_list1).distinct()
    shopping_list=(shopping_list2|shopping_list1).distinct()
    shopping_info=defaultdict()
    shopping_info['search_results']=[]
    i=0
    for demo in shopping_list:
        i+=1
        info={
            "position":i,
            "title":demo.title,
            "link":demo.link,
            "image":demo.image,
            "prices":[
                {
                    "value":demo.price,
                    "raw":"${}".format(demo.price)
                }
            ]
        }
        shopping_info['search_results'].append(info)
    return JsonResponse(shopping_info,safe=False)

#商品的添加
@csrf_exempt
def add_shopping(request):
    if request.method=='POST':
        try:
            title=request.POST.get("title")
            desc=request.POST.get("desc")
            link=request.POST.get("link")
            image=request.POST.get("image")
            price=request.POST.get("price")
            produce=shoping_info()
            produce.title=title
            produce.desc=desc
            produce.image=image
            produce.price=price
            produce.link=link
            produce.save()
            return JsonResponse({"flag":1},safe=False) #1表示添加成功
        except:
            return JsonResponse({"flag": 0}, safe=False)  # 0表示添加失败


#商品信息的修改
@csrf_exempt
def change_info_shopping(request):
    if request.method=='POST':
        try:
            #首先获取商品的id
            id=request.POST.get("id")
            #获取商品信息
            title = request.POST.get("title")
            desc = request.POST.get("desc")
            link = request.POST.get("link")
            image = request.POST.get("image")
            price = request.POST.get("price")
            produce=shoping_info.objects.filter(id=id).first()
            produce.title=title
            produce.desc=desc
            produce.image=image
            produce.price=price
            produce.link=link
            produce.save()
            return JsonResponse({"flag":1},safe=False) #1表示添加成功
        except:
            return JsonResponse({"flag": 0}, safe=False)  # 0表示添加失败

#商品信息的删除
@csrf_exempt
def del_shopping_product(request):
    if request.method=='POST':
        try:
            #首先获取商品的id
            id=request.POST.get("id")
            produce = shoping_info.objects.filter(id=id).first()
            produce.delete()
            return JsonResponse({"flag": 1}, safe=False)  # 1表示添加成功
        except:
            return JsonResponse({"flag": 0}, safe=False)  # 0表示添加失败


#获取购物车中的列表信息
def get_shopping_card(request):
    #首先获取用户的信息
    #假设用户的信息为id=1
    id=request.session.get("id")
    print(id)
    user=user_info.objects.filter(id=id).first()
    # user=user_info.objects.filter(id=1).first()
    #获取该用户对应下的所有购物车信息
    user_shopping=shopping_cart.objects.filter(user_id=user)
    shop_cart=defaultdict()
    shop_cart["search_results"]=[]
    j=0
    for i in user_shopping:
        j=j+1
        info={
            "position":j,
            "epid":i.item_id.id,
            "title":i.item_id.title,
            "link":i.item_id.link,
            "image":i.item_id.image,
            "condition":"Brand New",
            "is auction":False,
            "buy_it_now":True,
            "free_returns":False,
            "num_product":i.num_product,
            "prices":{
                "value":i.item_id.price,
                "raw":"${}".format(i.item_id.price)
            }
        }
        shop_cart["search_results"].append(info)
    return JsonResponse(shop_cart,safe=False)

#向购物车中加入商品或者修改商品数量
def add_shopping_card(request):
    try:
        #获取用户信息

        id = request.session.get("id")
        user=user_info.objects.filter(id=id).first()
        #获取商品信息
        item_id=request.GET.get("itemid")
        #首先判断该用户之前是否添加过该商品
        item = shoping_info.objects.filter(id=item_id).first()
        item_exist=shopping_cart.objects.filter(user_id=user,item_id=item)
        if item_exist.count()==0:
            print("第一次添加到购物车")
            shop_cart=shopping_cart()
            shop_cart.user_id=user
            shop_cart.item_id=item
            shop_cart.num_product=1
            shop_cart.save()
        else:
            print("非第一次添加到购物车")
            change_num=shopping_cart.objects.filter(user_id=user,item_id=item).first()
            change_num.num_product+=1
            change_num.save()

        return JsonResponse({"flag":1},safe=False) #1表示添加成功
    except:
        return JsonResponse({"flag": 0}, safe=False) #0表示添加失败

#修改购物车商品的数量
def change_shopping_num(request):
    try:
        #获取用户信息
        id = request.session.get("id")
        user=user_info.objects.filter(id=id).first()
        #获取商品信息
        item_id=request.GET.get("itemid")
        #获取修改的商品数量
        num_product=request.GET.get("num_product")
        #首先判断该用户之前是否添加过该商品
        item = shoping_info.objects.filter(id=item_id).first()
        item_exist=shopping_cart.objects.filter(user_id=user,item_id=item).first()

        item_exist.num_product=num_product
        item_exist.save()
        return JsonResponse({"flag":1},safe=False) #1表示添加成功
    except:
        return JsonResponse({"flag": 0}, safe=False) #0表示添加失败


#将物品从购物车中删除
@csrf_exempt
def del_shopping_cart(request):
    #首先获取用户信息
    # try:
        if request.method=='POST':
            print(request.POST)
            id = request.session.get("id")
            user=user_info.objects.filter(id=id)
            #获取善品信息
            #首先获取要删除的商品id
            item_id=request.POST.get("itemid")
            item=shoping_info.objects.filter(id__in=item_id)
            user_item_list=shopping_cart.objects.filter(user_id=user,item_id__in=item)
            user_item_list.delete()
            return JsonResponse({"flag": 1}, safe=False)

    # except:
    #     return JsonResponse({"flag":0},safe=False)




