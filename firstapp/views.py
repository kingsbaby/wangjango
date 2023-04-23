from django.shortcuts import render

### 사용자 브라우저로 응답을 하기위한
#   라이브러리 불러들이기
from django.http import HttpResponse

# Create your views here.
def testPage(request) :
    return HttpResponse("Django OK...")

### 최초 페이지 
def index(request) :
    msg = """
        <h3>Index Page 입니다.</h3>
        <hr/>
        <p>
            HTML 코드 잘 실행됩니다.
        </p>
    """
    # return HttpResponse(msg)
    return render(request,
                  "firstapp/index.html",
                  {"key":"value잘 나옴",
                   "key2" : "value2..."})