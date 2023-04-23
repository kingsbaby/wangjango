from django.urls import path
from . import views


urlpatterns = [

   path('',views.index),

    #http://127.0.0.1:8000/oracle/
    path('index/',views.index),
 
    #####회원관리##############
    #http://127.0.0.1:8000/nonmodel/mem_list
    path('mem_list/',views.getMemberList),

    #http://127.0.0.1:8000/nonmodel/mem_view
    path('mem_view/',views.getMemberView),

    #http://127.0.0.1:8000/nonmodel/mem_update_form/
    path('mem_update_form/',views.getMemUpdateForm),

    #http://127.0.0.1:8000/nonmodel/mem_updateForm/
    path('mem_update/',views.getMemUpdate),

    #http://127.0.0.1:8000/nonmodel/cart_view/
    path('cart_list/',views.getCartList),

    ########## 로그인 처리 ##############

    #http://127.0.0.1:8000/nonmodel/login_form/
    path('login_form/',views.login_form),

    #http://127.0.0.1:8000/nonmodel/login_chk/
    path('login_chk/',views.login_chk),

    #http://127.0.0.1:8000/nonmodel/logout_chk/
    path('logout_chk/',views.logout_chk),
   


    ######################
    #http://127.0.0.1:8000/nonmodel/logout_chk/
    path('cart_insert_form/',views.getCartInsertForm),
 
    #http://127.0.0.1:8000/nonmodel/logout_chk/
    path('cart_insert/',views.getCartInsert),


    ###########검색에 의한 상품상세조회 처리 #############
    #http://127.0.0.1:8000/nonmodel/search_prod/
    path('search_prod/',views.getSearchProd),

    ###########이메일 발송 처리 #############

    #http://127.0.0.1:8000/nonmodel/email_form/
    path('email_form/',views.getEmailForm),
 
    #http://127.0.0.1:8000/nonmodel/email_send/
    path('email_send/',views.emailSend),

    ##############페이징 처리 #######################
    #http://127.0.0.1:8000/nonmodel/cart_list_page//
    path('cart_list_page/',views.getCartListPaging),
    
    #http://127.0.0.1:8000/nonmodel/file_insert_form//
    path('file_insert_form/',views.getFileInsertForm),

    #http://127.0.0.1:8000/nonmodel/file_insert_form//
    path('file_insert/',views.setFileInsert),
 
    #http://127.0.0.1:8000/nonmodel/file_down//
    path('file_down/',views.setFileDown),
 
 


]