from django.shortcuts import render
from django.http import HttpResponse 
from .models import Cart

# Create your views here.


def second(request) :
    return HttpResponse("second 호출....")

def index(request) :
    return render(request,
                  "secondapp/index.html")

#############[회원정보]########
###회원정보 전체 조회
def getCartList(request) :
    ###회원정보 전체조회 
    
    cart_list = Cart.objects.all().order_by("-cart_no")
    
    
    return render(request,
                  "secondapp/cart/cart_list.html",
                  {"cart_list":cart_list})


def getCartView(request) :
    ###회원정보 전체조회 
    
    cart_no   = request.GET.get("cart_no", "ERROR")
    cart_prod = request.GET.get("cart_prod", "ERROR")

    cart_view = Cart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)

    
    return render(request,
                  "secondapp/cart/cart_view.html",
                  {"cart_no" : cart_no,
                    "cart_prod" : cart_prod,
                    "cart_view": cart_view})

def getUpdateForm(request) :
    ###회원정보 수정
    
    return render(request,
                  "secondapp/cart/cart_view.html",
                  {""})

