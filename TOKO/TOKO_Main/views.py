from django.shortcuts import render, HttpResponse, redirect
from TOKO_Main.models import Contact,Product,Order,OrderItem
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
# Create your views here.

#home page
def index(request):
    # return HttpResponse("HI FIRST TIME HERE!!!!")
    product=Product.objects.all()#all product is accessed
    context={
        'product':product
    }
    # if request.user.is_anonymous:
    #     return redirect("/login.html")
    return render(request,"index.html",context)


#user creation,login,logout
def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        customer=User.objects.create_user(username=username,email=email,password=pass1)
        customer.first_name=first_name
        customer.last_name = last_name
        customer.save()

        # messages.success(request, "Registerd")
        return redirect('/')

    return render(request,"Registration/register.html")

def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            # messages.success(request, "SUBMITTED")
            return redirect('/')

        else:
            # No backend authenticated the credentials
            # messages.error(request, "ERROR! Invalid Credentials")
            return redirect('/login')

    return render(request, "Registration/login.html")

def logout_user(request):
    logout(request)
        # Redirect to a success page.
    return redirect("/")

#contact page
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        desc=request.POST.get('desc')
        usercontact=Contact(name=name,email=email,phone=phoneno,desc=desc,date=datetime.today())
        usercontact.save()
        messages.success(request,"SUBMITTED")
    return render(request, template_name="contact.html")

#product detail
def product_detail(request,id):
    product=Product.objects.filter(id=id).first()
    context={
        'product':product,
    }
    return render(request,"product_details.html",context)


# Cart function
@login_required(login_url="/login")
def cart_add(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/login")
def item_clear(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product)
    return redirect("cart_detail")

@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request,"cart/cart_detail.html")

@login_required(login_url="/login")
def checkout(request):
    return render(request,"cart/checkout.html")


@login_required(login_url="/login")
def placeorder(request):
    if request.method=="POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid)
        mobileno = request.POST.get('mobile')
        cart=request.session.get('cart')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        town = request.POST.get('town')
        addresstype = request.POST.get('addresstype')
        state = request.POST.get('state')
        totalamt = request.POST.get('totalamt')
        order=Order(
            user=user,
        address = address,
        town = town,
        addresstype =addresstype ,
        state = state,
        mobile = mobileno,
        pincode = pincode,
        payment = totalamt,
        )
        order.save()

        for i in cart:
            Item=OrderItem(
                user=user,
                image=cart[i]['image'],
            product =cart[i]['name'] ,
            order =order,
            quantity =cart[i]['quantity'] ,
            price = cart[i]['price'] ,
            )
            Item.save()

    return render(request,"cart/placeorder.html")

def success(request):
    return render(request,"cart/thank_you.html")
def orders(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(id=uid)

    order=OrderItem.objects.filter(user=user)

    context={
        'orders':order,
    }
    print(context)

    return render(request,"cart/orders.html",context)


def search(request):
    query=request.GET['query']

    product = Product.objects.filter(name__icontains=query)  # all product is accessed
    context = {
        'product': product
    }
    return render(request,"search.html",context)