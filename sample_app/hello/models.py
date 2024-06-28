from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class  CustomUser(AbstractUser):
    class meta:
      db_table = 'custom_users'
      
    gender = models.CharField(verbose_name="性別", max_length=1, default=2) # 0=man,1=woman 2=不明
    age = models.IntegerField(verbose_name="年齢", null=True, blank=True)
    birth_date = models.DateField(verbose_name="生年月日", null=True, blank=True)
    address = models.TextField(verbose_name="住所", null=True, blank=True)
      


class Publisher(models.Model):
    class Meta:
        db_table = "publishers"
        
    name = models.CharField(verbose_name="出版社" , max_length=255)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    class Meta:
        db_table = "authors"
        
    name = models.CharField(verbose_name="著者名", max_length=255)
    
    #おまじない
    def __str__(self):
        return self.name
        
class Book(models.Model):
    class Meta:
        db_table = "books"
        
        
    title = models.CharField(verbose_name="タイトル", max_length=255)
    publisher = models.ForeignKey(Publisher, verbose_name="出版社" , on_delete=models.PROTECT)
    author = models.ManyToManyField(Author, verbose_name="著者")
    price = models.IntegerField(verbose_name="価格", null=True, blank=True)
    description = models.TextField(verbose_name="詳細", null=True, blank=True )
    publish_date = models.DateField(verbose_name="発売日")
    
    def __str__(self):
        return self.title