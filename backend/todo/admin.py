from django.contrib import admin
from .models import Todo


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'description', 'link', 'image', 'condition', 'prices', 'free_returns')
# Register your models here.


admin.site.register(Todo, TodoAdmin)




