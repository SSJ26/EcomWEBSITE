from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from imageshow.settings import BASE_DIR,MEDIA_ROOT
from .forms import *
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, authenticate, logout
from .forms import UserSignupform

# Create your views here.
@login_required(login_url='/login')
def index(request):
    print(MEDIA_ROOT)
    categorylist = Category.objects.all()
    imagelist = []
    for category in categorylist:
        image = Product.objects.filter(category=category)
        imagelist.append(image)
    print('imagelist',imagelist)
    return render(request,'index.html',{'imagelist':imagelist,"categorylist":categorylist})


@login_required(login_url='/login')
def upload_img(request):
    form=Imageform(request.POST,request.FILES)
    nameProd=request.POST.get('name')
    # if Product.objects.filter(name=nameProd).exists():
    #     error = "This Product Name Already Exist"
    #     return render(request,'upload_img.html',{'form':form,'error':error})
    # print(namelist)
    
    if request.method=='POST':
        if(form.is_valid):
            # if nameProd not in namelist:
            try:
                # form.created_by=request.user
                # form+='<tr><th><label for="created_by">Created by:</label></th><td><input type="text" name="created_by" required id="created_by"></td></tr>'
                print(type(form))
                product = form.save()
                print(product)
                product.created_by=request.user
                product.save()
                return redirect('/')
            except Exception as e:
                print(e)
                return render(request,'upload_img.html',{'form':form})
        else:
            error = "Invalid Form"
            return render(request,'upload_img.html',{'form':form,'error':error})
    form=Imageform()
    return render(request,'upload_img.html',{'form':form})


def login_user(request):
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            message="Please Log In"
            login(request,user)
            return redirect('/')
        else:
            message="Please Log In"
            error="Please Sign Up and Register"
            form=UserSigninform()
            return render(request,'login.html',{'form':form,"button":"Log In","button2":"Sign Up","url":"signup",'error':error,'message':message})
    form=UserSigninform()
    message="Please Log In"
    return render(request,'login.html',{'form':form,"button":"Log In","button2":"Sign Up","url":"signup",'message':message})
def signup(request):
   
    if request.method=='POST':
        form = UserSignupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            error="Please Write Correct Details"
            form = UserSignupform()
            message="Please Sign Up"
            return render(request,'login.html',{'form':form,"button":"Sign Up","button2":"Login","url":"login",'error':error,'message':message})

    form = UserSignupform()
    message="Please Sign Up"
    return render(request,'login.html',{'form':form,"button":"Sign Up","button2":"Login","url":"login",'message':message})
def logout_user(request):
    logout(request)
    return redirect('/login')

def delete_product(request,id):
    p=Product.objects.get(id=id)
    p.delete()
    return redirect('/')
def myproducts(request):

    # imagelist=Product.objects.filter(created_by=request.user)
    # print(imagelist)
    # return render(request,'index.html',{'imagelist':imagelist,"edit":"edit"})

    categorylist=Category.objects.all().exclude(name='porns')
    imagelist=[]
    for category in categorylist:
        image=Product.objects.filter(created_by=request.user,category=category)
        imagelist.append(image)
    return render(request,'index.html',{'imagelist':imagelist,'categorylist':categorylist,"edit":"edit"})


def likes(request,id):
    product = Product.objects.get(id=id)
    count=product.likes
    product.likes=count+1
    product.save()
    return redirect('/')
def edit(request,id):
    product_edit=Product.objects.get(id=id)
    form=Imageform(instance=product_edit)
    
    if request.method=='POST':
        form=Imageform(request.POST,request.FILES,instance=product_edit)
        if(form.is_valid):
            
            # if nameProd not in namelist:
            try:
                # form.created_by=request.user
                # form+='<tr><th><label for="created_by">Created by:</label></th><td><input type="text" name="created_by" required id="created_by"></td></tr>'
                
                product = form.save()
                product.created_by=request.user
                product.save()
                return redirect('/myproducts',id=Product.id)
            except Exception as e:
                print(e)
                return render(request,'upload_img.html',{'form':form})
        else:
            error = "Invalid Form"
            return render(request,'upload_img.html',{'form':form,'error':error})
    return render(request,'upload_img.html',{'form':form})

def category(request):
    form=Categoryform(request.POST,request.FILES)
    if(request.method=='POST'):
        if form.is_valid():
            form.save()
            return redirect('/')
    form=Categoryform()
    return render(request,'category.html',{'form':form})

def contact(request):
    form=Contactform(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    form=Contactform()
    return render(request,'contact.html',{'form':form})



def buy_product(request,id,**args):
    print(args['args'])
    item=Product.objects.get(id=id)
    return render(request,'checkout.html',{"item":item,"cart":args['args']})

def place_order(request,id):
    # logic to save buy product 
    item=Product.objects.get(id=id)
    ordered_item=Buy.objects.create(product_id=item, user_id=request.user, seller_id=item.created_by)
    return redirect('/order_history')


def order_history(request):
    imagelist=Buy.objects.filter(user_id=request.user)
    return render(request,'order_history.html',{"imagelist":imagelist})


# def sell(request,id):
#     item=Product.objects.get(id=id)
#     print(item)
#     imagelist=Buy.objects.create(product_id=item,seller_id=request.user)
#     print(imagelist.seller_id,imagelist.product_id)
#     return redirect('/history_sellers')

def history_sellers(request):
    imagelist=Buy.objects.filter(seller_id=request.user)
    print(imagelist)
    return render(request,'seller.html',{'imagelist':imagelist})
    


def remove_from_cart(request,id):
    item=Product.objects.get(id=id)
    ordered_item=Buy.objects.create(product_id=item, user_id=request.user, seller_id=item.created_by)
    # delete cart object 
    cart=Cart.objects.filter(user_id=request.user,product_id=item)
    cart.delete()
    
    return redirect('/order_history')
    
def cartbuy(request,id):
    return 

def cart_product(request,id):
    # item=Product.objects.get(id=id)
    # userid = request.user
    # create cart method 1
    # cart = Cart.objects.create(
    #     product_id = item,
    #     user_id=request.user,
    # )
    # create cart method 2
    # cart = Cart(product_id=item,user_id=request.user)
    # cart.save()
    # create cart method 3
    # cart = Cart()
    # cart.product_id=item
    # cart.user_id=request.user
    # cart.save()
    item=Product.objects.get(id=id)
    cart=Cart.objects.create(product_id=item,user_id=request.user)
    return redirect('/usercart')

def usercart(request):
    # fetch the cart products of the login user
    imagelists = Cart.objects.filter(user_id=request.user)
    imagelist = []
    for i in imagelists:
        imagelist.append(i.product_id)
    print(imagelist)
    return render(request,'cart.html',{"imagelist":imagelist})
