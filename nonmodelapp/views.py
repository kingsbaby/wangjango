from django.shortcuts import render
from django.http import HttpResponse

## DB처리를 위한 사용자 라이브러리
from nonmodelapp.model_db_class.member import member as mem 
from nonmodelapp.model_db_class.cart import cart
from nonmodelapp.model_db_class.lprod import lprod
from nonmodelapp.model_db_class.join import join 

### 이메일 처리를 위한 사용자 라이브러리
from nonmodelapp.email_util import email_util

### 페이징 처리를 위한 라이브러리 
from django.core.paginator import Paginator 
from nonmodelapp.file_util.file_util import File_Util




### 최초 nonmodel root 페이지
def index(request) :
    return render(request,
                  "nonmodelapp/index.html",
                  {})

### 회원 전체 조회
def getMemberList(request) :
        # mem_list = Member.objects.all()
    mem_list =mem.getMemberList()
    return render(request,
                "nonmodelapp/member/mem_list.html",
                {"mem_list" : mem_list})
                

 
 ### 회원 상세조회 :한건조회
def getMemberView(request) :
    try :
            
        mem_id = request.GET.get("mem_id", "a001")
        ###기존의 models.py호출 형태에서 
        # 우리가 만든 model_db 내에 파일 사용

        #mem_view = Member.objects.get(mem_id = mem_id)
        mem_view = mem.getMember(mem_id)

    except : 
        msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!');
                    location.href = '/nonmodel/mem_list/'
                </script>
            
            """
        return HttpResponse(msg)
       
    return render(request,
                    "nonmodelapp/member/mem_view.html",
                    {"mem_view" : mem_view,
                    "mem_id" :mem_id})
 
### 회원정보 수정 폼 페이지
def getMemUpdateForm(request) :
        try :
            mem_id = request.GET.get("mem_id", "ERROR")
            mem_view = mem.getMember(mem_id)

        except : 

            msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!');
                    location.href = '/nonmodel/mem_list/'
                </script>
            """
            return HttpResponse(msg)

    # return HttpResponse()
        return render(request,
                    "nonmodelapp/member/mem_update_form.html",
                    {"mem_id" : mem_id,
                    "mem_view" : mem_view})
       

def getMemUpdate(request) :
    try : 
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
        mem_add1 = request.POST["mem_add1"]

        # msg = "아이디 : {} / 패스워드 : {} / 주소 : {}".format(mem_id,
        #                                                     mem_pass,
        #                                                     mem_add1)
        rs_msg = mem.setMemberUpdate(mem_pass, mem_add1,mem_id)
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
                location.href = '/nonmodel/mem_view/?mem_id={}'
            </script>
    """.format(mem_id)
    
    return HttpResponse(msg)



def getCartList(request) :
    cart_list = cart.getCartList()


    return render(request,
                   "nonmodelapp/cart/cart_list.html",
                   {"cart_list" : cart_list })


###로그인 화면 페이지 처리 
def login_form(request) :

    return render(request,
                   "nonmodelapp/login/login_form.html",
                   {})


### 로그인 인증 처리하기
def login_chk(request) :
    mem_id   = request.POST["mem_id"]
    mem_pass = request.POST["mem_pass"]

    mem_view = mem.getLoginChk(mem_id, mem_pass)

    if mem_view.get("RS") == "Data_None" : 

        msg = """
            <script type="text/javascript">
                alert('아이디 또는 패스워드를 확인해주세요!!.');
                history.go(-1);
            </script>
        """ 

    elif mem_view.get("RS") == "DB_ERROR" :

        msg ="""
            <script type="text/javascript">
                alert('아이디 또는 패스워드를 확인해주세요!!.');
                history.go(-1);
            </script>
        """ 

    
    ### 로그인 상태를 유지하기 위한 기능 : 세션 sessetion 처리  
    # - request객체 내에 존재하는 session 변수를 사용해서
    # - 서버 영역에 값을 저장해 놓는 기능
    # - 사용자가 로그아웃 또는 브라우저를 종료하면 서버와의 접속이 끊어지고,
    # - 이때, request 객체 내이 있는 session변수 내에 key들은 삭제 됩니다.

    # - session변수는 딕셔너리 타입의 변수로 key값과 value 값을 넣어주면됨
    # - request 객체는 html 페이지 어디에서든 사용가능하기에
    #- session 변수도 views  및 html 어디서든지 사용가능
    #   (request 객체를 사용할수 있는 모든곳 ..)
    request.session["ses_mem_id"] = mem_id
    request.session["ses_mem_name"] = mem_view.get("mem_name")

    msg = """
            <script type="text/javascript">
                alert('환영합니다. [{}]님 로그인 되었습니다.!.');
                location.href = '/';
            </script>
        """.format(mem_view.get("mem_name"))

    return HttpResponse(msg)
    
### 로그아웃 처리하기
def logout_chk(request) :
    ### 로그아웃의 의미 : session 정보를 삭제하면 됨...
    request.session.flush()

    msg = """
        <script type='text/javascript'>
        alert('로그아웃 되었습니다.');
        location.href = '/';
        </script>
    """
    return HttpResponse(msg)
    

def getCartInsertForm(request):

     return render(request,
                   "oracleapp/cart/cart_insert_form.html",
                   {})
    #  4번:


def getCartInsert(request):
    try:

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

    

        """
        Insert Into cart
            (cart_member, cart_prod, cart_qty, cart_no)
        Values
            (cart_member값, cart_prod값, cart_qty값, cart_no값)
        """
        # Cart.objects.create(cart_member = cart_member,
        #                     cart_prod = cart_prod,
        #                     cart_qty = cart_qty,
        #                     cart_no = cart_no)
        # # 3번 : 없음.
        msg = """
                <script type='text/javascript'>
                alert('정상적으로 저장되었습니다!');
                location.href = '/oracle/cart_list';
                </script>
        """
        # 4번 : 
        return HttpResponse(msg)

    except : 

        msg = """
            <script type='text/javascript'>
                alert('잘못된 접근입니다!');
                location.href = '/oracle/mem_cart_list/'
            </script>

        """
        return HttpResponse(msg)


  ###### 상품분류 검색에 의한 상품상세조회
def getSearchProd(request):
    lprod_gu = request.GET.get("lprod_gu", "")
    prod_id = request.GET.get("prod_id", "")

    ###상품분류 selectbox에 들어갈 내용 조회하기
    # lprod_selbox = lprod.getLprodList()
    lprod_selbox = join.getSelBox_Lprod()

    ### 상품 selectbox에 들어갈 내용 DB조회하기
    # - 최초에는 상품분류가 선택이 안되어 있기에
    # - 조회된 상품분류에서 첫번째 상품분류의 값을 이용해서
    # - 상품을 조회해서 상품 selectbox의 값을 채웁니다.
    if lprod_gu == "" :
        lprod_gu = lprod_selbox[0]["lprod_gu"] 

    prod_selbox = join.getSelBox_Lprod_Prod(lprod_gu)

    ### 선택된 상품분류 및 선택된 상품에 대해서
    #   - 상품 상세내용 조회하기
    ### - 최초에는 상품이 선택되어 있찌 않기에
    #   - prod_selbox에서 조회된 결과 중에 첫번째 값을 이용 
    if prod_id == "" :
         prod_id = prod_selbox[0]["prod_id"]
    prod_view = join.getLprod_Prod_Buyer(lprod_gu,
                                         prod_id)

    return render(request,
                        "nonmodelapp/search_prod/search_prod.html",
                        {"lprod_selbox" : lprod_selbox,
                         "prod_selbox" : prod_selbox,
                         "prod_view" : prod_view,
                         "lprod_gu" : lprod_gu,
                         "prod_id" : prod_id})

###########[메일 발송 처리하기 ] ##########
#####    메일 발송을 위한 폼 화면처리 
def getEmailForm(request) :
    return render(request,
                  "nonmodelapp/email_form/email_form.html",
                  {})

### 메일 발송 처리하기
def emailSend(request) :
    emails    = request.POST.get("emails","")
    title     = request.POST.get("title", "")
    content   = request.POST.get("content", "")

    ## 여러건의 이메일 주소가 있는 경우까지 처리
    # - 리스트 타입으로 생성
    emails_list = emails.replace(" ","").split(",")
  


    
### 이메일 전송시키기 email_util 사용
    # send_chk = email_util.SendEmail(emails_list,
    #                                    title, 
    #                                    content)
    send_chk = email_util.SendEmail(emails_list,
                                     title, 
                                     content)


### 이메일 성공여부에 따른 페이지 전환처리(script)
# - 성공
    if send_chk > 0 :
        msg = """
            <script type='text/javascript'>
                alert('성공적으로 메일이 발송되었습니다!');
                location.href = '/nonmodel/'
        </script>
        """

# - 실패 
    else : 
        msg = """
            <script type='text/javascript'>
                alert('메일 발송이 실패하였습니다.!');
                history.go(-1);
            </script>
        """

    return HttpResponse(msg)


######## 페이징 처리하기 ########
# - 페이지 처리를 위해서는 Paginator 라이브러리 필요함
# - 주문(장바구니) 전체리스트 목록을 샘플로 진행 
def getCartListPaging(request) :
    #현재 페이지 번호 받기
    now_page = request.GET.get("page","1")

    ### 전송되는 모든 값들은 문자열 타입 (""임)
    # - 따라서, 정수타입을 사용하고자 한다면 변환해야함
    now_page = int(now_page)


    ### 주문(장바구니) 전체데이터 조회 --------------
    cart_list = cart.getCartList()

    ###################################################
    ###            # 한화면에 10개 행씩 추출          ###
    ###################################################
    ###  화면에 보여줄 행의 갯수 정의


    ### 화면에 보여줄 행의 갯수 정의
    num_row = 10 

    ### Pagenator 라이브러리를 이용해서 행의 갯수 자르기
    # - Paginator 클래스 객체 생성하기 
    p = Paginator(cart_list, num_row)

    ### 현재 페이지번호(now_page)에 해당하는 10개 행 추출
    #- HTML에서 for문으로 데이터 출력에 사용하는 데이터임
    rows_data = p.get_page(now_page)


    ###################################################
    ###         하단 페이지 번호 영역 처리            ###
    ###################################################
    ### 시작 페이지 번호(start_page) 계산하기
    start_page = (now_page-1) // num_row * num_row + 1


    ### 종료 페이지 번호(end_page) 계산하기
    end_page = start_page + 9

    ### 종료페이지 번호(end_page)가 종료 행의 갯수가보다 크면..
    if end_page > p.num_pages :
        end_page = p.num_pages


     ###################################################
    ###        다음/이전버튼 처리                    ###
    ###################################################
    ###  
    ### 다음/ 이전버튼을 보여줄지 여부처리 
    is_prev = False # 이전
    is_next = False # 다음

    ### 이전버튼을 보여줄지 여부처리 
    if start_page > 1 :
        is_prev = True

    ### 다음 버튼을 보여줄지 여부처리 
    if end_page < p.num_pages :
        is_next = True

    context = {
        ### 화면에 보여줄 10개의 행을 담고 있는 데이터 
        "cart_list" : rows_data,
        ### 페이지 번호의 시작(start_page)~ 종료(end_page)범위
        "page_range" : range(start_page, end_page+1),
        ### 이전 버튼 보여줄지 여부 
        "is_prev" : is_prev,
        ### 다음 버튼 보여줄지 여부
        "is_next" : is_next,
        ### 시작번호(start_page)
        "start_page" : start_page,
        ### 선택된 페이지 번호가 현재페이지가 같은지 여부 확인용
        "now_page" : now_page
    }



    return render(request,
                    "nonmodelapp/paging/cart_list.html",
                    context)

##############File upload 임 여기부터 복붙하기 04/21
def getFileInsertForm(request) :
    return render(request,
                  "nonmodelapp/file_UpDown/file_insert_form.html",
                  {})
### File Upload 처리하기
def setFileInsert(request) :
    try :
        title = request.POST.get("title")

        if request.FILES.get("file_nm") is not None :
            file_nm = request.FILES.get("file_nm")
        else:
            file_nm = ""
    except :
        pass

    if file_nm != "" :

    #############[ File Upload 처리하기 ]##############
    ### - 파일 업로드 폴더 위치 지정
        upload_dir = "./nonmodelapp/static/nonmodelapp/file_UpDown/"
        download_dir = "./nonmodelapp/static/nonmodelapp/file_UpDown/"

        ### 파일(이미지)를 페이지에 보여줄 경우 : 폴더 전체 경로 지정
        img_dir = "/static/nonmodelapp/file_UpDown/"

        ### File_Util 클래스 생성하기 
        fu = File_Util()

        ### 초기값 셋팅(설정하기)
        fu.setUpload(file_nm, upload_dir, img_dir , download_dir)

        ### 파일 업로드 실제 수행하기 ******
        fu.fileUpload()


        ############### [업로드된 파일 정보 조회] #############
        ### 파일 사이즈 
        file_size = fu.file_size
        ###업로드된 파일명
        filename = fu.filename
        ### <img> 태그에 넣을 src 전체 경로
        img_full_name = fu.img_full_name
        ### (DB 저장용) 다운로드 전체경로+파일명
        download_full_name = fu.download_full_name

        ########[Database 이용시]
        # 컬럼은 두개사용 : img_full_name, download_full_name

    msg = """
            <p>img_full_name : {0}</p>
            <p>file_size : {1}</p>
            <p>filename : {2}</p>
            <p>다운로드 파일명 :
                <a href='/nonmodel/file_down/?download_full_name={3}'>{2}</a> 
            </p>
            <p><img src='{0}'></p>
        """.format(img_full_name, file_size, filename, download_full_name)
        
    return HttpResponse(msg)


### File Download 처리하기
def setFileDown(request) :
    download_full_name = request.GET.get("download_full_name")

    ### File_Util 클래스 생성하기
    fu = File_Util()

    ### 다운로드할 위치 : 전체경로 넣어wnrl
    fu.setDownload(download_full_name)

    ### 브라우저에서 파일 다운로드 시키기 
    return fu.fileDownload()
    #return HttpResponse("go go")

#### [페이지 내에 코드포함 처리]
def include_view(request) :
      return render(request,
                    "nonmodelapp/include/include_view.html",
                {})

#### [페이지 내에 코드포함 처리]
def include_view2(request) :
      return render(request,
                    "nonmodelapp/include/include_view2.html",
                {})

#### [페이지 내에 실행결과 포함 처리] : extends] ###

### main extends 화면
def extends_view(request) :
      return render(request,
                    "nonmodelapp/extends/extends_view.html",
                {})

### 블록 1
def block_view1(request) :
      return render(request,
                    "nonmodelapp/extends/01_block_view.html",
                {})

### 블록 2
def block_view2(request) :
      return render(request,
                    "nonmodelapp/extends/02_block_view.html",
                {})

### 블록 3
def block_view3(request) :
      return render(request,
                    "nonmodelapp/extends/03_block_view.html",
                {})

### 블록 - mem_list
def block_mem_list(request) :
    mem_list =mem.getMemberList()
    return render(request,
                    "nonmodelapp/extends/mem_list.html",
                {"mem_list":mem_list})

#### [비동기방식 처리] : extends] ###
   
### main extends 화면
def load_view(request) :
    return render(request,
                    "nonmodelapp/jquery_load/load_view.html",
                {})

def load_view1(request) :
    return render(request,
                    "nonmodelapp/jquery_load/load_view1.html",
                {})

def load_view2(request) :
    return render(request,
                    "nonmodelapp/jquery_load/load_view2.html",
                {})

def load_view3(request) :
    return render(request,
                    "nonmodelapp/jquery_load/load_view3.html",
                {})




