from django.contrib import admin
from .models import MessageUser
# Register your models here.
class MessageUserAdmin(admin.ModelAdmin):
	# list_display=('Name','PhoneNum','Address','UpdateTime')
	list_display=('Name','Address','UpdateTime')

admin.site.register(MessageUser,MessageUserAdmin)