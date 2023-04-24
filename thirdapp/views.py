from django.shortcuts import render


def index(request) :
    return render(request,
                  "thirdapp/index.html")

def getCartList(request) :

    return render(request,
                  "thirdapp/cart/cart_list.html",
                  {})

def getTest(request) :

    return render(request,
                  "thirdapp/test.html",
                  {})
############페이징 처리

def include_view(request) :

    return render(request,
                  "thirdapp/include/include_view.html",
                  {})

