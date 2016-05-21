from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from PhoneBook.models import MessageUser,PhoneNumber
from .form import AddForm,LoginForm,UpdateForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context import RequestContext
from django.template.defaulttags import register

@register.filter
def get(d, key_name):
	return d.get(key_name,'')

# Create your views here.
def phone(request):  #通讯录首页
	messageuser=MessageUser.objects.all()
	PhoneNum={} #记录联系人id：电话归属地：电话
	Label={} #记录联系人id、电话归属地标签
	for each in messageuser:
		num=[] #记录电话
		label=[]
		phonenum={} #记录电话归属地：电话
		a=each.user_phonenum.all().values()
		# Label[each.id]=a.PhoneLabel
		for i in range(len(a)):
			num.append(a[i]['PhoneNum'])
			label.append(a[i]['PhoneLabel'])
		for x in range(len(num)):
			phonenum[a[x]['PhoneLabel']]=num[x]
		Label[each.id]=label
		PhoneNum[each.id]=phonenum
	return render(request,'phone.html',{'messageuser':messageuser,'PhoneNum':PhoneNum,'Label':Label})

def add(request):    #添加联系人
	if request.method=='POST':
		addform=AddForm(request.POST)
		label=request.POST.getlist('label')
		phone=request.POST.getlist('add_phone')
		if addform.is_valid():
			Name=addform.cleaned_data['add_name']
			Address=addform.cleaned_data['add_address']
			Other=addform.cleaned_data['add_other']
			new_user=MessageUser.objects.get_or_create(Name=Name,Address=Address,Other=Other)
			user_id=new_user[0].id
			for i in range(len(label)-1,-1,-1):
				PhoneLabel=label[i]
				PhoneNum=phone[i]
				new_phone=PhoneNumber.objects.get_or_create(PhoneNum=PhoneNum,user_id=user_id,PhoneLabel=PhoneLabel)
			if request.POST.get("Save"):
				return HttpResponseRedirect('../')
			else:
				return HttpResponseRedirect('.')
	else:
		addform=AddForm()
	return render(request, 'add.html',{'addform':addform})

def detail(request,pk):  #联系人详细信息
	user=MessageUser.objects.get(pk=pk) #查找到当前联系人
	phonenumber=PhoneNumber.objects.filter(user_id=pk) #联系人对应的PhoneNumber（原数据库中含有的）
	label=[]
	phonenum=[]
	Label={} #字典存Label 方便html调用
	PhoneNum={} #字典存电话 方便html调用
	for i in range(len(phonenumber)): #联系人有几个电话号码
		label.append(phonenumber[i].PhoneLabel)
		phonenum.append(phonenumber[i].PhoneNum)
	for i in range(len(label)):
		Label[i]=label[i]	
		PhoneNum[i]=phonenum[i]
	Length=[]
	for i in range(1,len(Label)):
		Length.append(i)

	if request.method=='POST':
		updateform=UpdateForm(request.POST)
		label=request.POST.getlist('label')
		phone=request.POST.getlist('update_phone') #页面得到的电话，列表

		if updateform.is_valid():
			user.Name=updateform.cleaned_data['update_name']
			user.Address=updateform.cleaned_data['update_address']
			user.Other=updateform.cleaned_data['update_other']
			user.save()
			if(len(phonenumber)>len(phone)): #如果数据库中的电话多余页面中的电话，要作删除动作
				for i in range(len(phone),len(phonenumber)):  #删除多出的电话
					phonenumber[i].delete()
					for j in range(len(label)-1,-1,-1):    #剩下的电话更新
						phonenumber[j].PhoneLabel=label[j]
						phonenumber[j].PhoneNum=phone[j]
						phonenumber[j].save()
			elif(len(phonenumber)<len(phone)): #如果数据库中电话少于页面中的电话，要作添加动作
				for j in range(len(phone)-1,len(phonenumber)-1,-1): #多余页面的电话新增
					PhoneNumber.objects.get_or_create(PhoneNum=phone[j],user_id=pk,PhoneLabel=label[j])
				for i in range(len(phonenumber)-1,-1,-1): #页面中的电话更新
					phonenumber[i].PhoneLabel=label[i]
					phonenumber[i].PhoneNum=phone[i]
					phonenumber[i].save()
			else: #相等就直接更新
				for i in range(len(label)-1,-1,-1):    #剩下的电话更新
					phonenumber[i].PhoneLabel=label[i]
					phonenumber[i].PhoneNum=phone[i]
					phonenumber[i].save()
			if request.POST.get("Update"):
				return HttpResponseRedirect('../../')
	else:
		updateform=UpdateForm(initial={
				'update_name':user.Name,
				'update_address':user.Address,
				'update_other':user.Other
			}
		)
	return render(request, 'detail.html',{'user':user,'updateform':updateform,'Label':Label,'PhoneNum':PhoneNum,'Length':Length})

def delete(request):
	if request.method=='POST':
		values=request.POST.getlist('single') #取得type="checkbox" 的value值，列表
		for each in values:
			user=MessageUser.objects.get(pk=each)
			user.delete()
			phone=PhoneNumber.objects.filter(user_id=each)
			for each_phone in phone:
				each_phone.delete()
		return HttpResponseRedirect('..')

	messageuser=MessageUser.objects.all()
	PhoneNum={} #记录联系人id：电话归属地：电话
	Label={} #记录联系人id、电话归属地标签
	for each in messageuser:
		label=[]
		phonenum={} #记录电话归属地：电话
		phone=PhoneNumber.objects.filter(user_id=each.id)
		for each_phone in phone:
			label.append(each_phone.PhoneLabel)
			phonenum[each_phone.PhoneLabel]=each_phone.PhoneNum
		PhoneNum[each.id]=phonenum
		Label[each.id]=label
	return render(request,'delete.html',{'messageuser':messageuser,'PhoneNum':PhoneNum,'Label':Label})

# def login(request):
# 	if request.method=='GET':   #进入注册页面
# 		form=LoginForm()        #注册表单，用户名，密码
# 		return render_to_response('login.html',RequestContext(request,{'form':form,}))
# 	else:                       #注册页面，填写注册信息
# 		# form=LoginForm(request.POST)     #1
# 		form=LoginForm()
# 		if form.is_valid():
# 			# username=request.POST.get('username','')    #2
# 			# password=request.POST.get('password','')    #3    1，2，3一起
# 			username=form.cleaned_data['username']
# 			password=form.cleaned_data['password']
# 			user=auth.authenticate(username=username,password=password)
# 			if user is not None and user.is_active:
# 				auth.login(request, user)
# 				return render_to_response('phone.html',RequestContext(request))
# 			else:
# 				return render_to_response('login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
# 		else:
# 			return render_to_response('login.html',RequestContext(request,{'form':form,}))		
