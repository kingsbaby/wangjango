from nonmodelapp.model_db_class.db_util_def import DB_util 


### 전체 조회하기
def getList(sql):
    ### 클래스 생성시키기
    # 클래스 생성과 동시에 conn정보와 cursor 정보를 가지고 있음
    # - 클래스 내에 변수들은 별도로 받아오지 않아도 되며, 직접 접근가능함
    db_util = DB_util()

    list_row = db_util.getFetchAll(sql)

    return list_row


### 한건 조회하기
def getView(sql) :

    ### 클래스 생성시키기
    db_util = DB_util()

    ### 딕셔너리로 변경하기
    dict_row = db_util.getFetchOne(sql)

    return dict_row


### 입력/삭제/수정 처리하기
def setCUD(sql):
    
    ### 클래스 생성시키기
    db_util = DB_util()
    
    db_util.setCUD(sql)

    return "ok"
