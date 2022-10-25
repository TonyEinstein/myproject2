# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 20:28
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : test_form_signup.py

from django.test import TestCase
from ..forms import SignUpForm


class SignUpFormTest(TestCase):

    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)


