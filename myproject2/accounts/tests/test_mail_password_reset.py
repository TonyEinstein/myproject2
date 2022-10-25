# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 16:39
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : test_mail_password_reset.py
# 创建⼀个特定的⽂件来测试电⼦邮件
# 抓取应⽤程序发送的电⼦邮件，并检查主题⾏，正⽂内容以及发送给谁



from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.response = self.client.post(reverse('password_reset'), { 'email': 'john@doe.com' })
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[Django Boards] Please reset your password', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm', kwargs={'uidb64': uid,'token': token})
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn('john', self.email.body)
        self.assertIn('john@doe.com', self.email.body)

    def test_email_to(self):
        self.assertEqual(['john@doe.com',], self.email.to)















