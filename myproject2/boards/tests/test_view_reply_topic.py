# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 14:14
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : test_view_reply_topic.py

"""
⾃定义了测试⽤例基类ReplyTopicTestCase。然后所有四个类将继承这个测试⽤例。
测试视图是否受 @login_required  装饰器保护，然后检查HTML输⼊，状态码。最后，我们测试⼀个有效和⽆效的表单提交。
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from boards.models import Topic, Post


class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all `reply_topic` view tests
    '''
    def setUp(self):
        # self.board = Board.objects.create(name='Django', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.
        board.pk, 'topic_pk': self.topic.pk})
class LoginRequiredReplyTopicTests(ReplyTopicTestCase):
    pass
    # # ...
class ReplyTopicTests(ReplyTopicTestCase):
    pass
class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    pass
class InvalidReplyTopicTests(ReplyTopicTestCase):
    pass