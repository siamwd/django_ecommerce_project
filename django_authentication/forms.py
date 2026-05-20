from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password']