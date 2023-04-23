from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
# Create your models here.


class Cart(models.Model) :
    cart_member = CharField(max_length=15, null = False)
    ### cart_no만 PK로 지정 
    cart_no      = CharField(primary_key=True, max_length=13,null=False)
    cart_prod    = CharField(max_length=10, null=False)
    cart_qty     = IntegerField(max_length=8, null=False)


    class Meta : 
    ### 실제 사용할 테이블 이름 정의
        db_table = "cart"

        ### 사용할 앱 이름 정의
        app_label = "secondapp"

        ### 외부 데이터베이스에 테이블 존재여부 확인
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # --> 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed = False

