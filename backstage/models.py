from django.db import models

# Create your models here.
#user table
class user_info(models.Model):
    id=models.AutoField("userid",primary_key=True,null=False,blank=False)
    username=models.CharField("user name",max_length=30,null=False,blank=False,unique=True)
    password=models.CharField("user pw",max_length=30,null=False,blank=False)
    email=models.CharField("Email",max_length=30,null=False,blank=False,unique=True)
    phonenum=models.CharField("Phone number",max_length=30,null=False,blank=False,unique=True)
    superuser=models.IntegerField("identity",default=0,choices=((0,"general user"),(1,"administrator")))
    position=models.CharField("address",default="Null",null=True,blank=True,max_length=200)
    # money=models.FloatField("")
    class Meta:
        db_table="user_info"

#Product sheet
class product(models.Model):
    id=models.AutoField("product id",primary_key=True,null=False,blank=False)
    productname=models.CharField("product name",max_length=225,null=False,blank=False)
    price=models.FloatField("Price",default=0.0)
    desc=models.TextField("product description",default="The uploader is lazy and has nothing to introduce",max_length=288)
    image=models.ImageField("Product Image",upload_to="upload/%Y%m%d")
    create_at=models.DateTimeField("add time",auto_now_add=True)
    change_at=models.DateTimeField("edir time",auto_now=True)
    user=models.ForeignKey(user_info,related_name="user",on_delete=models.CASCADE,default=None)
    class Meta:
        db_table="product"

#Product Rating Form
class score(models.Model):
    user_id=models.ForeignKey(user_info,on_delete=models.CASCADE,related_name="userid")
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,related_name="productid")
    score=models.IntegerField(default=0)
    class Meta:
        db_table="score"

#shopping cart
class cart(models.Model):
    user_id=models.ForeignKey(user_info,on_delete=models.CASCADE,related_name="cuser")
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,related_name="cproduct")
    num=models.IntegerField(default=1)
    flag=models.IntegerField(default=0,choices=((0,"Shopping cart"),(1,"Buy")))
    class Meta:
        db_table="cart"