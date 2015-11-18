from django import forms

class messageForm(forms.Form):
	name = forms.CharField(max_length=30)
	mail = forms.CharField()
	phone = forms.CharField()
	content = forms.CharField()

class loginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class userForm(forms.Form):
	username = forms.CharField()
	email = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2= forms.CharField(label='Confirm',widget=forms.PasswordInput)
	def pwd_validate(self,p1,p2):
		return p1==p2