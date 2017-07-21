#coding = utf-8
from django.db import models
from django.contrib import admin
from django.db.models import permalink
from a.fileds import ThumbnailImageField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Item(models.Model):
    text = models.TextField(default='')
    times = models.CharField(max_length=50)


class Tag(models.Model):
    """
    标签
    """

    name = models.CharField('名称', max_length=16)
class Category(models.Model):
    """
    分类
    """
 
    name = models.CharField('名称', max_length=16)
class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    dianzan = models.PositiveIntegerField('点赞', default=0) 
    look = models.PositiveIntegerField('浏览量', default=0) 
    chapin = models.PositiveIntegerField('差评', default=0)
    commen = models.PositiveIntegerField('评论', default=0)  
class Comment(models.Model):
    """
    评论
    """
 
    blog = models.ForeignKey(Blog, verbose_name='博客')
 
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
 
    created = models.DateTimeField('发布时间', auto_now_add=True)
class Day(models.Model):
    """
    日志
    """
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)


class PhotoItem(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'pk': self.id})

class Photo(models.Model):
    item = models.ForeignKey(PhotoItem)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)
        
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'pk': self.id})