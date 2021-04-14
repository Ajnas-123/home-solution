from django.db import models

# Create your models here.

class user_tb(models.Model):
	username=models.CharField(max_length=30,default='')
	password=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=30,default='')
	phone=models.CharField(max_length=30,default='')
	place=models.CharField(max_length=30,default='')
	address=models.CharField(max_length=30,default='')





class worker_tb(models.Model):
	username=models.CharField(max_length=30,default='')
	password=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=30,default='')
	phone=models.CharField(max_length=30,default='')
	place=models.CharField(max_length=30,default='')
	address=models.CharField(max_length=30,default='')


class complaint_tb(models.Model):
	userid=models.ForeignKey(user_tb,on_delete=models.CASCADE)
	workerid=models.ForeignKey(worker_tb,on_delete=models.CASCADE)
	date=models.CharField(max_length=30,default='')
	complaint=models.CharField(max_length=30,default='')

class admin_tb(models.Model):
	username=models.CharField(max_length=30,default='')
	password=models.CharField(max_length=100,default='')

class gallery_tb(models.Model):
	image=models.ImageField(upload_to='img',default='')
















