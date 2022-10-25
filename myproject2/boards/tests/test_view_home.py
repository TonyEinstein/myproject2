# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 22:23
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : test_view_home.py
from django.test import TestCase
from django.urls import reverse, resolve

from boards.models import Board
from boards.views import home


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description = 'Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        """
        测试的是请求该URL后返回的响应状态码。状态码200意味着成功。
        """
        self.assertEquals(self.response.status_code, 200)  #测试返回值是否 是 登录200，注意这里有个属性调用res.status_cod

    def test_home_url_resolves_home_view(self):
        """
        将浏览器发起请求的URL与urls.py模块中列出的URL进⾏匹配。
        该测试⽤于确定URL / ,返回 home 视图。
        """
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        # 这个是写超链接的测试
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
        #基本上是在测试 response 主体是否包含⽂本  href="/boards/1/",即链接到board_topics_url