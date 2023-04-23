from nonmodelapp.model_db import db_sql

def allview() :

    sql = """
    select cart_member, cart_no,cart_prod,cart_qty
    from cart
    """
    return db_sql.getList(sql)

