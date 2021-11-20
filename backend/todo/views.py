from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import TodoSerializer,UserSerializer
from .models import Todo,User
from django.http import HttpResponse
import json
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class userView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
            

 
def hello(request):
    return HttpResponse("Hello world ! ")

def login(request):
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    try:
        user = User.objects.get(email=email)
        if(user is None or (user.password!=pwd)):
            res_data = {"errorMsg":"unautharized"}
            return HttpResponse(json.dumps(res_data),content_type="application/json",status=200)
        else:
            res_data = {"errorMsg":"success"}
            return HttpResponse(json.dumps(res_data),content_type="application/json",status=200)
    except:
        res_data = {"errorMsg":"unautharized"}
        return HttpResponse(json.dumps(res_data),content_type="application/json",status=200)



              
    
def register(request):
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    queryset = User.objects.all()
    user = User.objects.filter(email=email)
    if len(user)==0:
        User(len(queryset)+1,email,pwd).save()
        res_data = {"errorMsg":"success"}
        return HttpResponse(json.dumps(res_data),content_type="application/json",status=200)
    else:
        res_data = {"errorMsg":"User Already Exists"}
        return HttpResponse(json.dumps(res_data),content_type="application/json",status=200)


        


