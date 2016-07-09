from django.conf.urls import url

urlpatterns = [
	url(r'^$', 'PhoneBook.views.index',name='index'),
    url(r'^phonenum$', 'PhoneBook.views.phone',name='phonenum'),
    url(r'^(?P<pk>\d+)/$', 'PhoneBook.views.phone',name='phonenum'),
    url(r'^add/$', 'PhoneBook.views.add',name='add'),
    url(r'^delete/$', 'PhoneBook.views.delete',name='delete'),
    url(r'^(?P<pk>\d+)/detail/$', 'PhoneBook.views.detail',name='datail'),
    url(r'^login/$', 'PhoneBook.views.login',name='login'),
]