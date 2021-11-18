from django.db import models


# Create your models here.
class Todo(models.Model):
    product_name = models.CharField(max_length=120)
    description = models.TextField()
    link = models.TextField()
    image = models.TextField()
    condition = models.CharField(max_length=120)
    prices = models.CharField(max_length=120)
    free_returns = models.BooleanField(default=False)

    def _str_(self):
        return self.product_name

class User(models.Model):
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def _str_(self):
        return self.email

