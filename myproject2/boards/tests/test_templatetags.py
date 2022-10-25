# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 22:56
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : test_templatetags.py
from django import forms
from django.test import TestCase

from ..templatetags.form_tags import field_type, input_class

"""
创建了⼀个⽤于测试的表单类，然后添加了覆盖两个模板标记中可能出现的场景的测试⽤例。
"""

class ExampleForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ('name', 'password')

class FieldTypeTests(TestCase):
    def test_field_widget_type(self):
        form = ExampleForm()
        self.assertEquals('TextInput', field_type(form['name']))
        self.assertEquals('PasswordInput', field_type(form['password']))

class InputClassTests(TestCase):
    def test_unbound_field_initial_state(self):
        form = ExampleForm() # 没有绑定表单，即空表单，也就是没有输入账号密码
        self.assertEquals('form-control ', input_class(form['name']))

    def test_valid_bound_field(self):
        form = ExampleForm({'name': 'john', 'password': '123'}) # 绑定了表单、无效表单
        self.assertEquals('form-control is-valid', input_class(form['name']))
        self.assertEquals('form-control ', input_class(form['password']))

    def test_invalid_bound_field(self):
        form = ExampleForm({'name': '', 'password': '123'})# 绑定了表单，但是无效表单
        self.assertEquals('form-control is-invalid', input_class(form['name']))