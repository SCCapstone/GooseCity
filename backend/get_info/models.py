from django.db import models

# Create your models here.

#一个是用户信息
class user_info(models.Model):
    id=models.AutoField("用户id",primary_key=True)
    username=models.CharField("用户姓名",max_length=225,null=False,blank=False)
    password=models.CharField("用户密码",max_length=225,null=False,blank=False)
    class Meta:
        db_table="user_info"

#一个是商品信息
class shoping_info(models.Model):
    id=models.AutoField("商品id",primary_key=True)
    title=models.CharField(max_length=225,null=False,blank=False)
    link=models.CharField("商品连接地址",max_length=225,null=True,blank=True)
    desc=models.TextField("商品描述",default="该商品未添加详情描述")
    image=models.CharField("商品图片url",max_length=225,null=True,blank=True)
    price=models.FloatField("商品价格",default="0.0")
    # count=models.IntegerField("商品的销售数量",default=0)

    class Meta:
        db_table="shopping_info"


#一个是购物车
class shopping_cart(models.Model):
    id=models.AutoField("ID",primary_key=True)
    user_id=models.ForeignKey(user_info,on_delete=models.SET_NULL,null=True,blank=True,related_name="userid")
    item_id=models.ForeignKey(shoping_info,on_delete=models.SET_NULL,null=True,blank=True,related_name="itemid")
    num_product=models.IntegerField("购物车中商品数量",default=1)

    class Meta:
        db_table="shopping_cart"




#