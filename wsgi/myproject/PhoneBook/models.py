from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

# Create your models here.

class MessageUser(models.Model):
	Name=models.CharField(max_length=100) #姓名
	
	Address=models.TextField(blank=True)		#住址
	Other=models.TextField(blank=True)    #其他
	UpdateTime=models.DateTimeField('更新时间',auto_now=True,blank=True) #时间1

	def __str__(self):
		return self.Name

	class Meta():
		ordering=['-UpdateTime']


class PhoneNumber(models.Model):
	user=models.ForeignKey(MessageUser,related_name="user_phonenum") 
	#one to many 一个人可以有几个电话号码，一个电话号码只对应一个人

	phone_regex=RegexValidator(regex=r'^\d{11}$',message='''Phone number 
		must be entered in the format: 13588888888. Up to 11 digits allowed. ''')
	PhoneNum=models.CharField(validators=[phone_regex],blank=True,max_length=11)
	PhoneLabel=models.CharField(max_length=100)  #电话归属地 电话标签

	UpdateTime=models.DateTimeField('更新时间',auto_now=True,blank=True) #时间2 与时间1对比，显示最新
	
	class Meta():
		ordering=['-UpdateTime']	