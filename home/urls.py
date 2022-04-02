from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("",views.index,name="index"),
    path("detail_page/",views.detail_page,name="detail_page"),
    path("search/",views.search,name="search"),
    path("shopping_cart/",views.shopping_cart,name="shopping_cart"),
    path("add_cart/",views.add_cart,name="add_cart"),
    path("change_cart/",views.change_cart,name="change_cart"),
    path("delete_cart/",views.delete_cart,name="delete_cart"),
    path("delete_cart2/",views.delete_cart2,name="delete_cart2"),
    path("user_person/",views.user_person,name="user_person"),
    path("user_person2/",views.user_person2,name="user_person2"),
    path("change_info/",views.change_info,name="change_info"),
    path("done_s/",views.done_s,name="done_s"),
    path("buy_manager/",views.buy_manager,name="buy_manager"),
    path("credit_buy/",views.credit_buy,name="credit_buy"),
    path("change_count/",views.change_count,name="change_count"),
    path("exist_buy/",views.exist_buy,name="exist_buy"),
    path("purchase/",views.purchases,name="purchase"),
    path("update_credit_card/",views.update_credit_card,name="update_credit_card")
]