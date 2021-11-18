from django.contrib import admin
from .models import Todo,User


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'description', 'link', 'image', 'condition', 'prices', 'free_returns')
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'password', 'shoppingCard')


admin.site.register(Todo, TodoAdmin)
admin.site.register(User, UserAdmin)



