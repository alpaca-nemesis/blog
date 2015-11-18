from django import forms

class messageForm(forms.Form):
	name = forms.CharField(max_length=30)
	mail = forms.CharField()
	phone = forms.CharField()
	content = forms.CharField()