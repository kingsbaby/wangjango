"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from mainapp import views
# from firstapp import views as v1
# from secondapp import views as v2
### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
###

urlpatterns = [
    ### http://127.0.0.1:8000/
    path('', views.index),
    ### http://127.0.0.1:8000/index
    path('index/', views.index),
    
    # http://127.0.0.1:8000/first/
    path('first/', include('firstapp.urls')),
    
    # http://127.0.0.1:8000/second/
    path('second/', include('secondapp.urls')),

    # http://127.0.0.1:8000/main/
    path('main/', include('mainapp.urls')),

    # http://127.0.0.1:8000/front/
    path('front/', include('frontapp.urls')),


    # http://127.0.0.1:8000/front/
    path('oracle/', include('oracleapp.urls')),

    # http://127.0.0.1:8000/nonmodels
    path('nonmodel/', include('nonmodelapp.urls')),
 
    # http://127.0.0.1:8000/third
    path('third/', include('thirdapp.urls')),


    path('admin/', admin.site.urls),
    
]
