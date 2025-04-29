"""
URL configuration for TOKO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/',admin.site.urls),
    path("",include("TOKO_Main.urls")),
path("login",include("TOKO_Main.urls")),
path("logout",include("TOKO_Main.urls")),
path("register",include("TOKO_Main.urls")),
path("search",include("TOKO_Main.urls")),
path("contact",include("TOKO_Main.urls")),
path("product/<int:id>/",include("TOKO_Main.urls")),
path("cart/cart_detail/",include("TOKO_Main.urls")),
#additonal cart
path("cart/add/<int:id>/",include("TOKO_Main.urls")),
path("cart/item_clear/<int:id>/",include("TOKO_Main.urls")),
path("cart/item_increment/<int:id>/",include("TOKO_Main.urls")),
path("cart/item_decrement/<int:id>/",include("TOKO_Main.urls")),
path("cart/cart_clear/",include("TOKO_Main.urls")),
path("cart/checkout/",include("TOKO_Main.urls")),
path("cart/checkout/placeorder",include("TOKO_Main.urls")),
path("success",include("TOKO_Main.urls")),
path("orders",include("TOKO_Main.urls")),


]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

