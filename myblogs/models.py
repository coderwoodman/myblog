from django.db import models

class Blog(models.Model):
    blogid = models.IntegerField()
    blogtitle = models.CharField(maxlength=20)
    author = models.CharField(maxlength=20)
    blogcontent = models.TextField()
    blogdesc = models.CharField(maxlength=256)
    createtime = models.DateTimeField(auto_now_add)
    lastchagetime = models.DateTimeField(auto_now)
    creartor = models.CharField(maxlength=50)

class MyUser(models.Model):
    userid = models.CharField(maxlength=50)
    username = models.CharField(maxlength=50)
    age = models.IntegerField() 

