"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
# from PhoneBook.views import index as views_index

urlpatterns = [
	# url(r'^index/$', views_index,name='ZhuYe'),
	#url(r'^index/', 'PhoneBook.views.index',name='ZhuYe'),
    url(r'^admin/', admin.site.urls),

	url(r'^$', 'PhoneBook.views.index', name='index'),
	url(r'^test/$', 'PhoneBook.views.test', name='test'),

    url(r'^phonenum/$', 'PhoneBook.views.phone',name='phonenum'),
    url(r'^phonenum/updata/$', 'PhoneBook.views.updata',name='updata'),
    url(r'^phonenum/(?P<pk>\d+)/$', 'PhoneBook.views.phone',name='phonenum'),
    url(r'^phonenum/add/$', 'PhoneBook.views.add',name='add'),
    url(r'^phonenum/delete/$', 'PhoneBook.views.delete',name='delete'),
    url(r'^phonenum/(?P<pk>\d+)/detail/$', 'PhoneBook.views.detail',name='datail'),
    url(r'^login/$', 'PhoneBook.views.login',name='login'),
]
