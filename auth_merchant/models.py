from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=50)

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    GENDER_CHOICES = (
        ('MEN', 'MEN'),
        ('WOMEN', 'WOMEN')
    )
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', null=True)
    description = models.TextField()
    orginal_price = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=0)
    quntity = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, null=True, choices=GENDER_CHOICES)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)