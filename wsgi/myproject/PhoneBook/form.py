from django import forms
from django.contrib.auth.models import User

class AddForm(forms.Form):
	add_name=forms.CharField(
			required=True,
			error_messages={'required':'请输入姓名'},
			widget=forms.TextInput(
					attrs={
						'class':'form-control',
						'placeholder':r'姓名',
					}
				),
		)
	add_phone=forms.CharField(
			required=True,
			error_messages={'required':'请输入电话'},
			widget=forms.TextInput(
					attrs={
						'class':'form-control',
						'placeholder':r'电话',
					}
				),
		)
	add_address=forms.CharField(
			required=False,
			widget=forms.Textarea(
					attrs={
						'rows':3,
						'cols':30,
						'class':'form-control',
						'placeholder':r'地址',
					}
				),
		)
	add_other=forms.CharField(
			required=False,
			widget=forms.Textarea(
					attrs={
						'rows':3,
						'cols':30,
						'class':'form-control',
						'placeholder':r'其它',
					}
				),
		)

	def clean_add_phone(self):
		add_phone=self.cleaned_data['add_phone']
		if not re.match(r'^1\d{10}$', add_phone):
			raise forms.ValidationError('请填写正确的号码格式~')
		return add_phone	


class UpdateForm(forms.Form):
	update_name=forms.CharField(
			required=True,
			error_messages={'required':'请输入姓名'},
			widget=forms.TextInput(
					attrs={
						'class':'form-control',
						'placeholder':r'姓名',
					}
				),
		)
	update_phone=forms.CharField(
			required=True,
			error_messages={'required':'请输入电话'},
			widget=forms.TextInput(
					attrs={
						'class':'form-control',
						'placeholder':r'电话',
					}
				),
		)
	update_address=forms.CharField(
			required=False,
			widget=forms.Textarea(
					attrs={
						'rows':3,
						'cols':30,
						'class':'form-control',
						'placeholder':r'地址',
						# 'initial':r'foobar',
					},
				),
		)
	update_other=forms.CharField(
			required=False,
			widget=forms.Textarea(
					attrs={
						'rows':3,
						'cols':30,
						'class':'form-control',
						'placeholder':r'其它',
					}
				),
		)

class LoginForm(forms.Form):
	username=forms.CharField(
			required=True,
			label=r'用户名',
			error_messages={'required':'请输入用户名'},
			widget=forms.TextInput(
					attrs={
						'placeholder':r'用户名',
					}
				),
		)
	password=forms.CharField(
			required=True,
			label=r'密码',
			error_messages={'required':'请输入密码'},
			widget=forms.PasswordInput(
					attrs={
						'placeholder':r'密码',
					}
				),
		)
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(r'用户名和密码为必填项')
		else:
			cleaned_data=super(LoginForm,self).clean()