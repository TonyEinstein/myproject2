# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 22:24
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : test_view_new_topic.py
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from boards.forms import NewTopicForm
from boards.models import Post, Topic, Board
from boards.views import new_topic

# 该测试文件有问题！

class NewTopicTests(TestCase):
    def setUp(self):
        # 创建⼀个测试中使⽤的 Board 实例
        Board.objects.create(name='Django', description='Django board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        #用于创建测试的User实例,并假设有这一个用户

    def test_new_topic_view_success_status_code(self):
        # 检查发给 view 的请求是否成功
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        # 检查当Board不存在时view是否会抛出⼀个404的错误
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        # 检查是否正在使⽤正确的 view
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        # 确保导航能回到topics的列表
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url) #为了获取requetes提交过来的列表
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))

    def test_csrf(self):
        """
        由于 CSRF Token 是处理 Post 请求的基本部分，我们需要保证我们的 HTML 包含 token。
        """
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        """
        #发送有效的数据并检查视图函数是否创建了 Topic 和 Post 实例。
        """
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
       # 发送⼀个空字典来检查应⽤的⾏为。
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        self.assertEquals(response.status_code, 200)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        定期发送数据，检查应用行为，预期应⽤程序会验证并且拒绝空的subject 和 message。
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())

    def test_contains_form(self):
        """
        抓取上下⽂的表单实例，检查它是否是⼀个  NewTopicForm  。
        """
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)

    def test_new_topic_invalid_post_data(self):
        """
        确保数据⽆效的时候表单会显示错误。
        """
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors) #self.assertTrue(form.errors)无效时显示错误

class LoginRequiredNewTopicTests(TestCase):
    # 尝试在没有登录的情况下发送请求给 new topic 视图，
    # 期待的结果是请求重定向到登录⻚⾯。

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        self.url = reverse('new_topic', kwargs={'pk': 1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


