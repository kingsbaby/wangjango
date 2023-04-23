from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
### 최초 페이지 
def index(request) :
    return render(request,
                  "frontapp/index.html",
                  {})

### 이미지 보여주기
def imageView(request) :
    return render(request,
                  "frontapp/01_image.html",
                  {})

### CSS 테스트-1
def cssView1(request):
    return render(request,
                  "frontapp/02_css1.html",
                  {})

### CSS 테스트-2
def cssView2(request):
    return render(request,
                  "frontapp/02_css2.html",
                  {})

### CSS 테스트-2
def cssView3(request):
    return render(request,
                  "frontapp/02_css3.html",
                  {})

### javascript 테스트-1
def javascriptView1(request):
    return render(request,
                  "frontapp/01_javascript1.html",
                  {})

### javascript 테스트-1
def javascriptView2(request):
    return render(request,
                  "frontapp/01_javascript2.html",
                  {})

### javascript 테스트-3
def javascriptView3(request):
    return render(request,
                  "frontapp/01_javascript3.html",
                  {})

### html  1
def htmlView01(request):
    return render(request,
                  "frontapp/html/01_html.html",
                  {})

### html link 4개
def linkView(request):
    return render(request,
                  "frontapp/html/02_link.html",
                  {})

### 02_link페이지 링크처리를 javascript함수 호출방식으로
def linkView2(request):
    return render(request,
                  "frontapp/html/03_link.html",
                  {})

### 04 css처리 
def linkView3(request):
    return render(request,
                  "frontapp/html/04_css.html",
                  {})

### 05 table 테스트
def tableView(request):
    return render(request,
                  "frontapp/html/05_table.html",
                  {})

### 06 table 테스트
def tableView2(request):
    context =    {"id" :"b001",
                  "name":"홍길동2",
                  "addr":"광주광역시 소촌동 1-2"}
    c_list = [context, context, context]
    return render(request,"frontapp/html/06_table.html",
                      {"c_list": c_list})

### 07 ul 테스트
def ulView(request):
    return render(request,
                  "frontapp/html/07_ul.html",
                  {})


### 08 div 테스트
def divView(request):
    return render(request,
                  "frontapp/html/08_div.html",
                  {})

### 09 div 테스트
def divView2(request):
    return render(request,
                  "frontapp/html/09_div.html",
                  {})

### 10 iframe 테스트
def iframeView(request):
    return render(request,
                  "frontapp/html/10_iframe.html",
                  {})

###############[CSS]########################
### 01 table 테스트
def cssTableView(request):
    return render(request,
                  "frontapp/css/01_table.html",
                  {})

### 02 table 테스트
def cssTableView2(request):
    return render(request,
                  "frontapp/css/02_table.html",
                  {})

### 03 nav 테스트
def cssNavView(request):
    return render(request,
                  "frontapp/css/03_nav.html",
                  {})
################# javascript #####################
## 01 jsinputform 테스트
def jsInputFormView(request):
    return render(request,
                  "frontapp/js/01_InputForm.html",
                  {"no" : "20",
                   "mem_id" : "a001222",
                   "mem_pass" : "asdf1234"})

###입력 폼에서 넘어오는 값 처리 
# - 브라우저 url에 입력해서 들어오면 안됨
# - --> 오류원인 : 전달 받는 값이 없기 때문에 ...
# - 입력 포의 버튼(이벤트)를 통해서만 접근 가능한 함수
def jsLogin(request) :
    ###처리순서
    # 1.요청 데이터 받기
    # - 전송방식에 따라 구분하여 받기 : 조건처리
    # - 모든 데이터는 딕셔너리 타입으로 전송됨
    # - POST 및 GET은 딕셔너리 변수가 됨
    if request.method == "POST" : 
        ###
        no       = request.POST["no"]
        mem_id   = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]



    elif request.method() == "GET" :
        no       = request.GET["no"]
        mem_id   = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"]

    # 2. 요청 데이터를 이용해서 DB 처리
    # - Database에 임의 테이블(testTB)이 있다고 가정
    # - 컬럼은 p_id,p_pw가 있다고 가정
    p_id = "a001"
    p_pw = "asdf"

    """
        아래 if (p_id == mem_id) and (p_pw == mem_pass) 이 조건을 
        SQL구문으로 만들어주세요..
        테이블(testTB) , 컬럼은 p_id, p_pw, p_no

    select  no, p_id as id, p_pw as pw
    from testTB 
    where p_id = mem_id 
        and p_pw = mem_pass
    Order By id Asc 

    - 전송받은 값을 모두 저장시키는 SQL 구문은?
       Insert into testTB (no, p_id, p_pw) values(no, mem_id, mem_pass);

    -no와 패스워드(p_pw)의 값을 전송받은 값으로 수정하려고 합니다.
    - 단 아이디가 mem_id로 전송받은 아이디에 대해서 

    update 테이블명 set 수정내용  where 조건;
    정답
    update testTB 
    set no = no , p_pw = mem_pw
    where p_id = mem_id ;

    -전송받은 아이디에 대한 정보를 삭제해 주세요 ...
    delete 
    from testTB
    where p_id = mem_id;
    """


    ### 전송받은 mem_id와 p_id가 같고
    #   mem_pw와 p_pw가 같다면 아래 처럼 전달받은 값 모두 응답 처리
    #   -아이디 또는 패스워드 중에 하나라도 같지 않다면
    #    응답 메시지(rs_msg)로 "아이디 또는 패스워드가 같지않습니다."를 
    #    응답해 주려고 합니다.
    #   if 문 뒤 먼저 오는거 왼쪽이 기준값 임 
    if (p_id == mem_id) and (p_pw == mem_pass) :
       # 3. DB처리 결과를 응답하기(html 파일 또는 메시지 이용)
        rs_msg = "no ={} / mem_id={} / mem_pass={}".format(no,
                                                       mem_id,
                                                       mem_pass)
    else : 
        rs_msg = "아이디 또는 패스워드가 같지않습니다."


    if (p_id == mem_id) and (p_pw == mem_pass) :
       # 3. DB처리 결과를 응답하기(html 파일 또는 메시지 이용)
        rs_msg = """
        <script type='text/javascript'>
            alert('정상적으로 로그인 되었습니다!!');
          //다시 fromt페이지로
            location.href = '/front/';
        </script>
        """

    else : 
        rs_msg = """
         <script type='text/javascript'>
            alert('아이디 또는 패스워드를 확인해 주세요!!');
            //history.fo(-1) 바로전으로 이동(뒤로가기와 같음)
            history.go(-1);
         </script>
        """

    
    return HttpResponse(rs_msg)

#render역할 

### 03 radioButton 테스트
def radioButtonView(request):
    return render(request,
                  "frontapp/js/03_radioButton.html",
                  {})

### 라디오버튼 데이터 처리 
def jsRadio_backup (request):  
    if request.method=="POST":
        #p_city   = request.POST["city"]
        if request.POST.get("city") !="" :
            p_city   = request.POST.get("city")
        else : 
             rs_msg = """
         <script type='text/javascript'>
                alert('잘못된 접근입니다.!!');
                history.go(-1);
            </script>
        """
             return HttpResponse(rs_msg)

    elif request.method=="GET":
        if request.GET.get("city") !="" :
        #p_city   = request.GET["city"]
            p_city   = request.GET.get("city")
        else : 
             rs_msg = """
         <script type='text/javascript'>
                alert('잘못된 접근입니다.!!');
                history.go(-1);
            </script>
        """




### 라디오버튼 데이터 처리 
def jsRadio(request):
    try :
        if request.method == "POST" : 
            p_city       = request.POST["city"]
            # p_city       = request.POST.get("city")
        
        elif request.method == "GET" :
            p_city       = request.GET["city"]
            # p_city       = request.GET.get("city")
    except :
        rs_msg = """
                <script type='text/javascript'>
                    alert('잘못된 접근입니다!!!');
                    history.go(-1);
                </script>
                """
        return HttpResponse(p_city)

    return HttpResponse(p_city)


### 05 checkbox 테스트
def checkBoxView(request):
    return render(request,
                  "frontapp/js/05_checkBox.html",
                  {})

###################jquery#####################
def jqueryView1(request):
    
    return render(request,"frontapp/jquery/01_jquery.html")


def slideJqueryView2(request):
    
    return render(request,"frontapp/jquery/02_slideJquery.html")



# -------------------------------------------------------
################# bootstrap #####################
def bootstrap(request):
    return render(request,
                  "frontapp/bootstrap/01_bootstrap.html",
                  {})

def bootstrap_table(request):
    return render(request,
                  "frontapp/bootstrap/02_bootstrap_table.html",
                  {})

def bootstrap_form(request):
    return render(request,
                  "frontapp/bootstrap/03_bootstrap_form.html",
                  {})