from django.urls import path

### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views

urlpatterns = [
    ### http://127.0.0.1:8000/front/
    path('', views.index),

    ### http://127.0.0.1:8000/front/image/
    path('image/', views.imageView),

    ### http://127.0.0.1:8000/front/css_1/
    path('css_1/', views.cssView1),

    ### http://127.0.0.1:8000/front/css_2/
    path('css_2/', views.cssView2),

    ### http://127.0.0.1:8000/front/css_3/
    path('css_3/', views.cssView3),

    ### http://127.0.0.1:8000/front/javascript1/
    path('javascript1/', views.javascriptView1),

    ### http://127.0.0.1:8000/front/javascript2/
    path('javascript2/', views.javascriptView2),

    ### http://127.0.0.1:8000/front/javascript3/
    path('javascript3/', views.javascriptView3),

    ### http://127.0.0.1:8000/front/01_html/
    path('01_html/', views.htmlView01),

    ### http://127.0.0.1:8000/front/02_link/
    path('02_link/', views.linkView),

    ### http://127.0.0.1:8000/front/03_link/
    path('03_link/', views.linkView2),

    ### http://127.0.0.1:8000/front/04_css/
    path('04_css/', views.linkView3),     

    ### http://127.0.0.1:8000/front/05_table/
    path('05_table/', views.tableView),

    ### http://127.0.0.1:8000/front/05_table/
    path('06_table/', views.tableView2),

    ### http://127.0.0.1:8000/front/05_table/
    path('07_ul/', views.ulView),

    ### http://127.0.0.1:8000/front/08_div/
    path('08_div/', views.divView),

    ### http://127.0.0.1:8000/front/09_dive/
    path('09_div/', views.divView2),

    ### http://127.0.0.1:8000/front/10_iframe/
    path('10_iframe/', views.iframeView),


 #######################[CSS]########################
    ### http://127.0.0.1:8000/front/01_table/
    path('01_table/', views.cssTableView),

    ### http://127.0.0.1:8000/front/02_table/
    path('02_table/', views.cssTableView2),

    ### http://127.0.0.1:8000/front/03_csNav/
    path('03_nav/', views.cssNavView),

    ### http://127.0.0.1:8000/front/01_inputForm/
    path('01_InputForm/', views.jsInputFormView),

    ### http://127.0.0.1:8000/front/02_login/
    path('02_login/', views.jsLogin),

      ### http://127.0.0.1:8000/front/03_radioButton/
    path('03_radioButton/', views.radioButtonView),

     ### http://127.0.0.1:8000/front/04_radio/
    path('04_radio/', views.jsRadio),

     ### http://127.0.0.1:8000/front/05_checkbox/
    path('05_checkBox/', views.checkBoxView),


   # ---------------
   ### http://127.0.0.1:8000/front/05_checkbox/
    path('05_checkBox/', views.checkBoxView),



    ###------------jquery---------------------------
   ### http://127.0.0.1:8000/front/01_Jquery/
   path('01_jquery/',views.jqueryView1),

   ### http://127.0.0.1:8000/front/02_slideJquery/
   path('02_slideJquery/',views.slideJqueryView2),
   




    ##############bootstrap############################
    ### http://127.0.0.1:8000/01_bootstrap/
    path('01_bootstrap/', views.bootstrap),

   ### http://127.0.0.1:8000/02_bootstrap_table/
    path('02_bootstrap_table/', views.bootstrap_table),

    ### http://127.0.0.1:8000/03_bootstrap_form/
    path('03_bootstrap_form/', views.bootstrap_form),
]
