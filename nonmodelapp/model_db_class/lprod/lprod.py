from nonmodelapp.model_db_class import db_sql


### 상품분류 정보 전체 조회하기 
def getLprodList() :
    ###sql 구문만들기
    sql = """
        select lprod_gu,lprod_nm 
        from lprod 
        order by lprod_nm ASC
    """
    return db_sql.getList(sql)