from django.shortcuts import render
from django.http import HttpResponse

from .models import Member, Cart, MemCart , Prod , CartMemProd
# Create your views here.

### oracleapp의 index 페이지
def index(request) :
    return render(request,
                  "oracleapp/index.html",
                  {})
    # return HttpResponse("Oracle 페이지 입니다.")

######### [회원정보] ########
### 회원정보 전체 조회하기
def getMemberList(request) :
    ### 회원정보 전체 조회하기(ORM 방식)
    # Select * From member
    # all() : 전체 조회 함수
    mem_list = Member.objects.all()
    return render(request,
                  "oracleapp/member/mem_list.html",
                  {"mem_list" : mem_list})


### 회원정보 상세 조회하기

def getMemberView(request) :
    try :
        ### 변수 mem_id로 전달받기..
        # - 전달 받은 후 mem_id 출력하기
        # mem_id = request.GET["mem_id"]
        mem_id = request.GET.get("mem_id", "ERROR")

        ### 회원정보 상세(한건) 조회하기(ORM 방식)
        """
            Select * 
            From member
            Where mem_id = mem_id
        """
        ### 모델(M) 처리하기 (한건 조회 : get() 사용)
        # - get(Member.mem_id = 전송받은 mem_id)
        mem_view = Member.objects.get(mem_id = mem_id)

    except : 

        msg = """
            <script type='text/javascript'>
                alert('잘못된 접근입니다!');
                location.href = '/oracle/mem_list/'
            </script>
        
        """
        return HttpResponse(msg)
    
    #{"mem_id" : "아이디","mem_pass":"패스워드",
    # "mem_name":"이름", "mem_add1":"주소"}
    # return HttpResponse()
    return render(request,
                  "oracleapp/member/mem_view.html",
                  {"mem_view" : mem_view,
                   "mem_id" :mem_id})

### 회원정보 수정 폼 페이지
def getMemUpdateForm(request) :
        try :
            # 1. 전송데이터가 있으면 받기(get or post)
            # 2. DB 입력/수정/삭제/조회 시 models.py 처리
            # 3. DB처리 결과가 있으면 html에 넘겨주기..

            mem_id = request.GET.get("mem_id", "ERROR")

            #{"mem_id" : "아이디","mem_pass":"패스워드",
            # "mem_name":"이름", "mem_add1":"주소"}
            mem_view = Member.objects.get(mem_id = mem_id)

        except : 

            msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!');
                    location.href = '/oracle/mem_list/'
                </script>
            
            """
            return HttpResponse(msg)

    # return HttpResponse()
        return render(request,
                    "oracleapp/member/mem_update_form.html",
                    {"mem_id" : mem_id,
                    "mem_view" : mem_view})


 ### 회원정보 수정 폼 페이지
def getMemUpdate(request) :
    try : 
    # 1. 전송데이터가 있으면 받기(get or post)
        # 2. DB 입력/수정/삭제/조회 시 models.py 처리
        # 3. DB처리 결과가 있으면 html에 넘겨주기..

        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
        mem_add1 = request.POST["mem_add1"]

        # msg = "아이디 : {} / 패스워드 : {} / 주소 : {}".format(mem_id,
        #                                                     mem_pass,
        #                                                     mem_add1)

        ###수정시키기 : model 처리
        """
            Update member
                Set mem_pass = mem_pass,
                    mem_add1 = mem_add1
            Where mem_id = mem_id
        """
        Member.objects.filter(mem_id = mem_id).update(mem_pass=mem_pass,
                                                    mem_add1=mem_add1)
    except : 

        msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!');
                    location.href = '/oracle/mem_list/'
                </script>
            
            """
        return HttpResponse(msg)
        
    msg = """
            <script type='text/javascript'>
                alert('정상적으로 수정되었습니다!');
                location.href = '/oracle/mem_view/?mem_id={}'
            </script>
    """.format(mem_id)
    return HttpResponse(msg)



########주문(장바구니) 정보관리 ##########
def  getCartList(request) :
     ###1. 전달받을 파라메터 있으면 받기(get or post)
     ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
     ###3. Templates : html 생성   (html로 바꿔서)
     ###4. Model을 html에 넘기기 : returned render()

    # 1번 처리 : 없음
    # 2번 처리 : 전체 조회
    """
        Select *
        From cart;
    """
    cart_list = Cart.objects.all().order_by("-cart_no")
    """
       <car_list의 결과값의 모양(타입)>
       [{'cart_member':'a001', 'cart_no':'201901010000001',
       'cart_prod':'p10100001,'cart_qty': '23'},
       {'cart_member':'b001', 'cart_no':'201901010000001',
       'cart_prod':'p10100001,'cart_qty': '23'},
       {'cart_member':'c001', 'cart_no':'201901010000001',
       'cart_prod':'p10100001,'cart_qty': '23'}]
    """
    # 3번 처리 : cart_list.html 생성
    # 4번 처리 
    return render(request,
                   "oracleapp/cart/cart_list.html",
                   {"cart_list" : cart_list })
     

###주문(장바구니)상세정보 조회(한건 조회)
def  getCartView(request) :

    try:
        ###1. 전달받을 파라메터 있으면 받기(get or post)
        ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
        ###3. Templates : html 생성   (html로 바꿔서)
        ###4. Model을 html에 넘기기 : returned render()


        # 1번 처리
        cart_no   = request.GET.get("cart_no", "ERROR")
        cart_prod = request.GET.get("cart_prod", "ERROR")

        # 2번 처리 : 두개의 PK값을 이용해서 데이터 조회하기(한건조회)
        """
        select *
        from cart
        where cart_no = cart_no값 and cart_prod = cart_prod값
        """
        cart_view = Cart.objects.get(cart_no = cart_no,
                                    cart_prod = cart_prod)

    except : 

            msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!');
                    location.href = '/oracle/mem_list/'
                </script>
            
            """
            return HttpResponse(msg)


        # 3번 처리 : cart_view.html생성
        # 4번 처리 

    return render(request,
                    "oracleapp/cart/cart_view.html",
                    {"cart_no" : cart_no,
                        "cart_prod" : cart_prod,
                        "cart_view": cart_view})



###주문(장바구니)상세정보 조회(한건 조회)
def  getCartUpdateForm(request) :
    try:
        ###1. 전달받을 파라메터 있으면 받기(get or post)
        ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
        ###3. Templates : html 생성   (html로 바꿔서)
        ###4. Model을 html에 넘기기 : returned render()


        #1번처리
        cart_no   = request.GET.get("cart_no", "ERROR")
        cart_prod = request.GET.get("cart_prod", "ERROR")

        #2번처리
        cart_view = Cart.objects.get(cart_no = cart_no,
                            cart_prod = cart_prod)
        # 3번 처리 : cart_view.html생성
        # 4번 처리 

    except : 

            msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!');
                    location.href = '/oracle/mem_list/'
                </script>
            
            """
            return HttpResponse(msg)

    return render(request,
                   "oracleapp/cart/cart_update_form.html",
                   {"cart_no" : cart_no,
                    "cart_prod" : cart_prod,
                    "cart_view" : cart_view})



    ###주문(장바구니) 수정 처리하기
def getCartUpdate(request) :
     ###1. 전달받을 파라메터 있으면 받기(get or post)
     ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
     ###3. Templates : html 생성   (html로 바꿔서)
     ###4. Model을 html에 넘기기 : returned render()

     #1번 처리 
    cart_no   = request.POST.get("cart_no","ERROR")
    cart_prod = request.POST.get("cart_prod","ERROR")
    cart_qty  = request.POST.get("cart_qty","ERROR")

    # msg = "cart_no={} / cart_prob={} / cart_qty={}".format(cart_no,
    #                                                        cart_prod,
    #                                                        cart_qty)
    
    #2번 처리
    Cart.objects.filter(cart_no = cart_no,
                        cart_prod=cart_prod).update(cart_qty=cart_qty)
     

     #3번 : html 생성안함...
     #4번 처리
    msg = """
            <script type='text/javascript'>
                alert('정상적으로 수정되었습니다.!');
                location.href='/oracle/cart_view/?cart_no={}&cart_prod={}'
            </script>
        """.format(cart_no, cart_prod)
    return HttpResponse(msg)


### 주문(장바구니) 정보 삭제하기
def getCartDelete(request):
     ###1. 전달받을 파라메터 있으면 받기(get or post)
     ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
     ###3. Templates : html 생성   (html로 바꿔서)
     ###4. Model을 html에 넘기기 : returned render()

    #1번 처리
    # cart_no   = request.GET.get("cart_no","ERROR")
    # cart_prod = request.GET.get("cart_prod","ERROR")

    """
        if cart_no == "ERROR" or cart_prod == "ERROR" :
            msg = "<script type="...">
                    alert("잘못된 접근입니다.");
                    location.href = "list로 보내기"
                    </script>
                  "
            return HttpResponse(msg)
    """


    cart_no   = request.get("cart_no")
    cart_prod = request.get("cart_prod")
    # msg = "cart_no={} / cart_prob={}".format(cart_no, cart_prod)



   #2번 처리
    Cart.objects.filter(cart_no   = cart_no,
                        cart_prod = cart_prod).delete()
   # 3번 :없음
   # 4번 처리 

    msg = """
            <script type='text/javascript'>
                alert('정상적으로 삭제되었습니다.!');
                location.href='/oracle/cart_list/';
            </script>
        """.format(cart_no, cart_prod)
    return HttpResponse(msg)

### 주문(장바구니) 정보 저장 폼화면 처리  
def getCartInsertForm(request):
     ###1. 전달받을 파라메터 있으면 받기(get or post)
     ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
     ###3. Templates : html 생성   (html로 바꿔서)
     ###4. Model을 html에 넘기기 : returned render()

     # 1번 : 없음..
     # 2번 : 없음..
     # 3번 : 입력화면 만들기 : cart_insert_form
     return render(request,
                   "oracleapp/cart/cart_insert_form.html",
                   {})
    #  4번:


### 주문(장바구니) 저장 처리 
def getCartInsert(request):
    ###1. 전달받을 파라메터 있으면 받기(get or post)
    ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
    ###3. Templates : html 생성   (html로 바꿔서)
    ###4. Model을 html에 넘기기 : returned render()

    # 1번 : 있음..

    if request.method == "POST" :
        cart_member = request.POST.get("cart_member", "ERROR")
        cart_prod   = request.POST.get("cart_prod", "ERROR")
        cart_qty    = request.POST.get("cart_qty", "ERROR")
        cart_no     = request.POST.get("cart_no", "ERROR")
    elif request.method =="GET" :
        cart_member = request.GET.get("cart_member", "ERROR")
        cart_prod   = request.GET.get("cart_prod", "ERROR")
        cart_qty    = request.GET.get("cart_qty", "ERROR")
        cart_no     = request.GET.get("cart_no", "ERROR")

  
    # msg = "member={} / prod={} / qyt={} / no={}".format(cart_member,
    #                                                 cart_prod,
    #                                                 cart_qty,
    #                                                 cart_no)
    # 2번 : 있음.
    """
     Insert Into cart
        (cart_member, cart_prod, cart_qty, cart_no)
     Values
        (cart_member값, cart_prod값, cart_qty값, cart_no값)
    """
    Cart.objects.create(cart_member = cart_member,
                        cart_prod = cart_prod,
                        cart_qty = cart_qty,
                        cart_no = cart_no)
    # 3번 : 없음.
    msg = """
            <script type='text/javascript'>
               alert('정상적으로 저장되었습니다!');
               location.href = '/oracle/cart_list';
            </script>
    """
    # 4번 : 
    return HttpResponse(msg)

####### [ member join cart ] ##########
### 조인(join) 데이터를 사용하는 경우 
# - 여러 정보를 조회할 때 주로 join 사용
# - 조회를 제외한 정보입력/수정/삭제를 할 경우에는
# - 단일 class의 테이블 정보를 사용...
def  getMemCartList(request) :
     cart_list = MemCart.objects.all().order_by("-cart_no")
     return render(request,
                   "oracleapp/mem_cart/cart_list.html",
                   {"cart_list" : cart_list })

##### 조회 
def getMemCartView(request):
    try : 
        ###1. 전달받을 파라메터 있으면 받기(get or post)
        ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
        ###3. Templates : html 생성   (html로 바꿔서)
        ###4. Model을 html에 넘기기 : returned render()

        # 1번 : 있음..
        cart_no     = request.GET.get("cart_no", "ERROR")
        cart_prod   = request.GET.get("cart_prod", "ERROR")


        #2번처리 : 두개의 PK값을 이용해서 데이터 조회(한건조회_)
        cart_view   = MemCart.objects.get(cart_no = cart_no, 
                                        cart_prod = cart_prod)
        return render(request,
                    "oracleapp/mem_cart/cart_view.html",
                    {"cart_no" : cart_no,
                        "cart_view" : cart_view,
                        "cart_prod" : cart_prod})
    
    except : 

        msg = """
            <script type='text/javascript'>
                alert('잘못된 접근입니다!');
                location.href = '/oracle/mem_cart_list/'
            </script>
        
        """
        return HttpResponse(msg)

def getMemView(request):
    try :
            # 1번 : 있음..
        mem_id = request.GET.get("mem_id", "ERROR")
        
        #2번 처리 : model.py클래스 사용
        mem_view = Member.objects.get(mem_id=mem_id)


        # 조인이 이루어진 경우 여러건 조회됨
        # mem_view = MemCart.objects.distinct().select_related().filter(cart_membar__mem_id=mem_id).distinct()


        #3번처리 : html파일 생성하기
        #4번처리
        return render(request,
                    "oracleapp/mem_cart/mem_view.html",
                    {"mem_view" : mem_view})

    except : 

            msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!');
                    location.href = '/oracle/mem_cart_list/'
                </script>
            
            """
            return HttpResponse(msg)
    
###### 상품정보(Prod)###############
def getProdList(request) : 
        ###1. 전달받을 파라메터 있으면 받기(get or post)
        ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
        ###3. Templates : html 생성   (html로 바꿔서)
        ###4. Model을 html에 넘기기 : returned render()

        #1번 : 없음
        #2번 : 대기 
        #3번처리 : html파일 생성하기
        #4번처리
        prod_list = Prod.objects.all().order_by("prod_name")
        return render(request,
                    "oracleapp/prod/prod_list.html",
                    {"prod_list" : prod_list})

def getProdView(request) : 
        ###1. 전달받을 파라메터 있으면 받기(get or post)
        ###2. Model에서 CRUD 처리할게 있으면 처리하기(models.py)
        ###3. Templates : html 생성   (html로 바꿔서)
        ###4. Model을 html에 넘기기 : returned render()

        # 1,2번처리 
        #3번처리 : html파일 생성하기
        #4번처리
        prod_id = request.GET.get("prod_id", "ERROR")
        prod_view = Prod.objects.get(prod_id = prod_id)
        return render(request,
                    "oracleapp/prod/prod_view.html",
                    {"prod_view" : prod_view})


###상품정보 수정하기 폼 페이지 처리 

def getProdUpdateForm(request) :
    
    prod_id = request.GET.get("prod_id","ERROR")
    prod_view = Prod.objects.get(prod_id = prod_id)
    
    return render(request,
                        "oracleapp/prod/prod_update_form.html",
                        {"prod_view" : prod_view})

### 상품정보 수정하기 
def getProdUpdate(request) :
    prod_id      = request.POST["prod_id"] 
    prod_name    = request.POST["prod_name"]
    prod_cost    = request.POST["prod_cost"]
    prod_price   = request.POST["prod_price"]
    prod_sale    = request.POST["prod_sale"]

    Prod.objects.filter(prod_id = prod_id).update(prod_name=prod_name,
                                                  prod_cost=prod_cost,
                                                  prod_price=prod_price,
                                                  prod_sale=prod_sale
                                                  )
    
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 수정되었습니다!!');
            location.href='/oracle/prod_view/?prod_id={}';
        </script>
    """.format(prod_id)
       
    return HttpResponse(msg)


def getCartMemProdList(request) :
    cartmember = CartMemProd.objects.all()


    return render(request,
                  "oracleapp/cart_mem_prod/cart_mem_prod_list.html",
                  {"cartmember" : cartmember}
                )
     