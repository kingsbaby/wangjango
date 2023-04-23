from nonmodelapp.model_db import db_util_def as db_util


###  전체 조회하기
def getList(sql):

    ### DB 접속 정보 받아오기
    conn, cursor = db_util.getDBConn_Cursor()

    ### 구문실행하기
    cursor.execute(sql)

    ### 결과 추출하기
    rows = cursor.fetchall()

    list_row = db_util.getFetchAll(cursor,rows)

    ### DB 접속 해제하기
    db_util.DBClose(cursor,conn)

    return list_row



### 회원 한건 조회하기
def getView(sql) :
    ### DB 접속 정보 받아오기
    conn, cursor = db_util.getDBConn_Cursor()

    ### 구문실행하기
    cursor.execute(sql)

    ### 결과 추출하기
    row = cursor.fetchone()

    ### 딕셔너리로 변경하기
    dict_row = db_util.getFetchOne(cursor,row)

    ### DB 접속 해제하기
    db_util.DBClose(cursor,conn)

    return dict_row


### 수정 처리하기
def setUpdate(sql):
    conn, cursor = db_util.getDBConn_Cursor()

    ### 구문 실행하기    
    cursor.execute(sql)

    ### 데이터 수정/삭제/입력 시에 아래 적용해야함
    conn.commit()

    ### DB 접속해제하기
    db_util.DBClose(cursor,conn)

    return "ok"



def setDelelte(sql):
    conn, cursor = db_util.getDBConn_Cursor()

    ### 구문 실행하기    
    cursor.execute(sql)

    ### 데이터 수정/삭제/입력 시에 아래 적용해야함
    conn.commit()

    ### DB 접속해제하기
    db_util.DBClose(cursor,conn)

    return "delete-ok"





def setInsert(sql):
    conn, cursor = db_util.getDBConn_Cursor()

    ### 구문 실행하기    
    cursor.execute(sql)

    ### 데이터 수정/삭제/입력 시에 아래 적용해야함
    conn.commit()

    ### DB 접속해제하기
    db_util.DBClose(cursor,conn)

    return "insert-ok"
