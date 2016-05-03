from django.db import models
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

# Create your models here.
class MessageUser(models.Model):
	Name=models.CharField(max_length=100) #姓名
	
	# PhoneNum=models.IntegerField() #电话
	phone_regex=RegexValidator(regex=r'^\d{11}$',message='''Phone number 
		must be entered in the format: 13588888888. Up to 11 digits allowed. ''')
	PhoneNum=models.CharField(validators=[phone_regex],blank=True,max_length=11)
	UpdateTime=models.DateTimeField('更新时间',auto_now=True,blank=True)

	Address=models.TextField(blank=True)		#住址
	Other=models.TextField(blank=True)    #其他


	def __str__(self):
		# return r'%s %s %s' %(self.Name,self.PhoneNum,self.Address)
		return self.Name

	# def get_absolute_url(self):
	# 	return reverse('datail',args=(self.pk,))

	class Meta():
		ordering=['-UpdateTime']