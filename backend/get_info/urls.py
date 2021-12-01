from django.urls import path
from . import views
urlpatterns=[
    path("login/",views.login,name="login"),
    path("all_shopping/",views.index,name="index"),
    path("search/",views.search,name="search"),
    path("add_shopping/",views.add_shopping,name="add_shopping"),
    path("change_info_shopping/",views.change_info_shopping,name="change_info_shopping"),
    path("del_shopping_product/",views.del_shopping_product,name="del_shopping_product"),
    path("get_shopping_card/",views.get_shopping_card,name="get_shopping_card"),
    path("add_shopping_card/",views.add_shopping_card,name="add_shopping_card"),
    path("change_shopping_num/",views.change_shopping_num,name="change_shopping_num"),
    path("del_shopping_cart/",views.del_shopping_cart,name="del_shopping_cart"),

]
