from rest_framework import serializers
from .models import Todo, User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'product_name', 'description', 'link', 'image', 'condition', 'prices', 'free_returns')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'password', 'shoppingCard')

