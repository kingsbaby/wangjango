from nonmodelapp.model_db import db_sql
#db_sql로 import 변경
########전체조회
def getMemberList() : 

    ## 구문작성     
    sql = """
    select mem_id, mem_pass, mem_name, mem_add1
    from member
    """

    return db_sql.getList(sql)

### 회원 한건 조회하기 
def getMember(mem_id) :
     
    sql = """
    select mem_id, mem_pass, mem_name, mem_add1
    from member
    where mem_id = '{}' 
    """.format(mem_id)

    return db_sql.getView(sql)

###수정 처리하기
def setMemberUpdate(mem_pass, mem_add1, mem_id) :
   ## 구문작성     
    sql = """
    Update member
        Set mem_pass = '{}',
            mem_add1 = '{}'
    Where mem_id = '{}' 
    """.format(mem_pass, mem_add1, mem_id)

    return db_sql.setUpdate(sql)

