from django.contrib import admin
from django.urls import path
from TOKO_Main import views

urlpatterns = [
    path("",views.index,name="home"),
    path("login",views.login_user,name="login"),
path("register",views.register,name="register"),
path("search",views.search,name="search"),
path("contact",views.contact,name="contact"),
path("logout",views.logout_user,name="logout"),
path("product/<int:id>/",views.product_detail,name="product"),

#additonal
path('cart/add/<int:id>/',views.cart_add,name='cart_add'),
path('cart/item_clear/<int:id>/',views.item_clear,name='item_clear'),
path('cart/item_increment/<int:id>/',views.item_increment,name='item_increment'),
path('cart/item_decrement/<int:id>/',views.item_decrement,name='item_decrement'),
path('cart/cart_clear/',views.cart_clear,name='cart_clear'),
path('cart/cart_detail',views.cart_detail,name='cart_detail'),
path('cart/checkout',views.checkout,name='checkout'),
path('cart/checkout/placeorder',views.placeorder,name='placeorder'),
path("success",views.success,name="success"),
path("orders",views.orders,name="orders"),

]
