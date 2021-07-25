import mongoengine
from datetime import datetime
from django.db import models
# Create your models here.
class PttTitle(mongoengine.Document):
    url=mongoengine.StringField(max_length=200,blank=True,null=True)
    title=mongoengine.StringField(max_length=100,blank=True,null=True)
    type=mongoengine.StringField(max_length=50,blank=True,null=True)
    cdate=mongoengine.DateTimeField(auto_now_add=True,null=None)

class PixivArt(mongoengine.Document):
    title=mongoengine.StringField(max_length=500,blank=True,null=True)
    userName=mongoengine.StringField(max_length=500,blank=True,null=True)
    tag=mongoengine.StringField(max_length=30,blank=True,null=True)
    artUrl=mongoengine.StringField(max_length=500,blank=True,null=True)
    imgUrl=mongoengine.StringField(max_length=500,blank=True,null=True)
    cdate=mongoengine.DateTimeField(null=None)
