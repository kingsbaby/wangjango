from nonmodelapp.model_db_class import db_sql


### 상품분류 정보 전체 조회하기 
def getSelBox_Lprod() :
    ###sql 구문만들기
    sql = """
        select Distinct lprod_gu, lprod_nm
        from lprod, prod
        where lprod_gu = prod_lgu
        order by lprod_nm ASC
    """
    return db_sql.getList(sql)



### 선택된 상품분류에 대한 상품정보 조회하기
# - 상품selectbox에 넣을 값 조회
def getSelBox_Lprod_Prod(lprod_gu) :
    ### SQL 구문만들기
    sql = """
        select prod_id, prod_name
        from lprod, prod
        where lprod_gu = prod_lgu
            and lprod_gu = '{}'
        Order by prod_name ASC
    """.format(lprod_gu)

    return db_sql.getList(sql)

### 선택된 상품분류에 대한 
# - 상품 상세조회처리
def getLprod_Prod_Buyer(lprod_gu, prod_id) :
    ### SQL 구문만들기
    sql = """
        select lprod_nm,
            prod_name, prod_sale,
            buyer_name , buyer_add1
        from lprod,prod,buyer
        where lprod_gu = prod_lgu
            and buyer_id = prod_buyer
            and lprod_gu = '{}'
            and prod_id = '{}'
        """.format(lprod_gu, prod_id)
    
    return db_sql.getView(sql)
