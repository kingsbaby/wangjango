from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 최초 페이지 
def index(request) :
    return render(request,
                  "mainapp/index.html",
                  {})
    # return HttpResponse("go go....")

### main 페이지
def main(request) :
    return render(request,
                  "mainapp/main.html",
                  {})
    # return HttpResponse("mainapp....")