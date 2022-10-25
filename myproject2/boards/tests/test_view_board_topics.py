# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 22:24
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : test_view_board_topics.py
from django.test import TestCase
from django.urls import reverse, resolve

from boards.models import Board
from boards.views import board_topics


class BoardTopicsTests(TestCase):
    def setUp(self):
        # 创建一个Board实例来用于测试，因为django针对当前数据库跑我的测试，
        # 测试的时候会创建一个新的数据库，测试完后会自动销毁。
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        """
        测试 Django是否对于现有的 Board 返回 status code(状态码) 200(成功)。
        """
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url) #为了获取requetes提交过来的列表
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        """
        测试Django 是否对于不存在于数据库的 Board 返回 status code 404(⻚⾯未找到)。
        """
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        """
        测试Django 是否使⽤了正确的视图函数去渲染 topics。
        """
        view = resolve('/boards/1/')  #Resolve函数测试你的网站的URL对应关系是否如你所愿
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        # 这里也是一个超链接的单元测试，目的是测试能否实现返回链接
        board_topics_url = reverse('board_topics', kwargs={'pk': 1}) #reverse的第一个参数是urls.py的url中的name
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    def test_board_topics_view_contains_navigation_links(self):
        """
        负责确保我们的 view 包含所需的导航链接。
        """
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))