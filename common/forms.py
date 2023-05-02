from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User ### 모델스 가져오는거

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")