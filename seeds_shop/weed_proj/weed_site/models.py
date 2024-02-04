import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    login = models.TextField(unique=True, null=True)
    password_hash = models.TextField()

class Category(models.Model):
    name = models.TextField()

class Admins(models.Model):
    user_id = models.IntegerField()

class Products(models.Model):
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    pics = ArrayField(
        models.TextField(),
        null=True
    )
    category = ArrayField(
        models.IntegerField(null=True),
        null=True, default=[]
    )
    count = models.IntegerField(null=True)
    count_pack = models.IntegerField(null=True)


class Orders(models.Model):
    user_id = models.IntegerField()
    email = models.TextField(null=True)
    prods_id = models.JSONField()
    final_price = models.FloatField(null=True)
    status = models.TextField(null=True, default='Создан')
    name = models.TextField(null=True)
    tg = models.TextField(null=True)
    city = models.TextField(null=True)
    address = models.TextField(null=True)
    phone = models.TextField(null=True)
    pay = models.TextField(null=True)
    post = models.TextField(null=True)
    message = models.TextField(null=True)
    admin_mess = models.TextField(null=True)
    data = models.DateField(default=datetime.date.today)
    prods_dict = models.JSONField(default={})

class Reviews(models.Model):
    user_id = models.IntegerField()
    user_name = models.TextField(null=True)
    prod_id = models.IntegerField()
    prod_name = models.TextField(null=True)
    rating = models.IntegerField()
    comment = models.TextField()

class Basket(models.Model):
    user_id = models.IntegerField()
    prod_id = models.IntegerField()
    count = models.IntegerField()

class Article(models.Model):
    title = models.TextField()
    text = models.TextField()
    pics = ArrayField(
        models.TextField(),
        null=True
    )
    content = models.TextField(null=True)
