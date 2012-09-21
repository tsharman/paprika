from django import forms

class NewUserForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField()
  email = forms.EmailField()
  business_name = forms.CharField(max_length=100)
