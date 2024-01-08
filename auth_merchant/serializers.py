from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', "first_name"]

    def create(self, data):
        user = User.objects.create(username = data.get("username"), first_name = data.get("first_name"))
        user.set_password(data.get("password"))
        user.save()
        return user
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ["id", "name", "age"]
        # exclude = ["id"]
        fields = "__all__"

    def validate(self, data):
        if data.get("age") < 18:
            raise serializers.ValidationError({'error', "age must be greater then 18"})

        return data
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]
    
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Books
        fields = "__all__"
        # depth = 1

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # user = UserSerializer()
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1