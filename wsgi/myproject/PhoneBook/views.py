from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from PhoneBook.models import MessageUser
from .form import AddForm,LoginForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context import RequestContext


# Create your views here.

def index(request):
	return HttpResponse("Hello World!")

def test(request):
	return HttpResponse("陈亮 ChenLiang")

# def index(request):  #主页
# 	content='欢迎光临号码不离，We Are All Here!'
# 	#return HttpResponse('欢迎光临号码不离，We Are All Here!')
# 	return render(request,'index.html',{'content':content})

def phone(request):  #通讯录首页
	messageuser=MessageUser.objects.all()
	return render(request,'phone.html',{'messageuser':messageuser})

def updata(request):  #更新数据
	messageuser=MessageUser.objects.all()
	return render(request,'updata.html',{'messageuser':messageuser})

def add(request):    #添加联系人
	if request.method=='POST':
		addform=AddForm(request.POST)
		if addform.is_valid():
			Name=addform.cleaned_data['add_name']
			PhoneNum=addform.cleaned_data['add_phone']
			Address=addform.cleaned_data['add_address']
			Other=addform.cleaned_data['add_other']
			# Name=addform.cleaned_data['add_name']
			new_user=MessageUser.objects.get_or_create(Name=Name,PhoneNum=PhoneNum,Address=Address,Other=Other)
			if request.POST.get("Save"):
				return HttpResponse('添加成功！')
			else:
				return HttpResponseRedirect('.')

	else:
		addform=AddForm()
	return render(request, 'add.html',{'addform':addform})

def detail(request,pk):  #联系人详细信息
	user=MessageUser.objects.get(pk=pk)
	if request.method=='POST':
		user.delete()
		return HttpResponseRedirect('../..')
	return render(request, 'detail.html',{'user':user})

def delete(request):
	if request.method=='POST':
		values=request.POST.getlist('single') #取得type="checkbox" 的value值，列表
		for each in values:
			user=MessageUser.objects.get(pk=each)
			user.delete()
		return HttpResponseRedirect('..')
	messageuser=MessageUser.objects.all()
	return render(request,'delete.html',{'messageuser':messageuser})

def login(request):
	if request.method=='GET':   #进入注册页面
		form=LoginForm()        #注册表单，用户名，密码
		return render_to_response('login.html',RequestContext(request,{'form':form,}))
	else:                       #注册页面，填写注册信息
		# form=LoginForm(request.POST)     #1
		form=LoginForm()
		if form.is_valid():
			# username=request.POST.get('username','')    #2
			# password=request.POST.get('password','')    #3    1，2，3一起
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user=auth.authenticate(username=username,password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return render_to_response('phone.html',RequestContext(request))
			else:
				return render_to_response('login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
		else:
			return render_to_response('login.html',RequestContext(request,{'form':form,}))		
