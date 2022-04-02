from django.urls import path
from . import views
app_name="backstage"
urlpatterns=[
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("register/",views.register,name="register"),
    path("",views.index,name="index"),
    path("welcome/",views.welcome,name="welcome"),
    path("order/",views.order,name="order"),
    path("product_add/",views.product_add,name="product_add"),
    path("product_change/",views.product_change,name="product_change"),
    path("product_delete/",views.product_delete,name="product_delete"),
    path("user_list/",views.user_list,name="user_list"),
    path("similar/",views.similar,name="similar"),
    path("user_delete/",views.user_delete,name="user_delete"),
    path("admin_list/",views.admin_list,name="admin_list"),
    path("admin_add/",views.admin_add,name="admin_add"),
    path("admin_change/",views.admin_change,name="admin_change"),
    path("member_similar/",views.member_similar,name="member_similar")
]