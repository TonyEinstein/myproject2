# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 19:59
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : forms.py

# 扩展email字段；因为UserCreationForm不提供email 字段，所以需要创建一个文件来扩展她。
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm): #一个表单
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
