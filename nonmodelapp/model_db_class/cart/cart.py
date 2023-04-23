from nonmodelapp.model_db_class import db_sql

#전체 조회하기 
def getCartList():

    sql ="""
        Select * 
        From cart
        Order By cart_no desc
    """
    return db_sql.getList(sql)

#한건 조회하기 




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



def setCartUpdate(cart_no,cart_prod, cart_qty, cart_member) :

    sql ="""
        insert into cart (
            cart_no, cart_prod,cart_qty, cart_member
            ) Valeus (
               '{}', '{}', '{}', '{}'
            )
        )
        """.format(cart_no, cart_prod, cart_qty, cart_member)
    return db_sql.setCUD(sql)



