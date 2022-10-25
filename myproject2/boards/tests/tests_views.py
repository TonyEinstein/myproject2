# from django.contrib.auth.models import User
#
# 此文件已经被拆解拆分
# from ..forms import NewTopicForm
#
# """
# 该文件用来写测试用例
# """
#
#
# # Create your tests here.
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from django.urls import resolve
# from ..views import home, board_topics, new_topic  # 这里导入的其实是视图函数
# from ..models import Board, Topic, Post
#
#
# class HomeTests(TestCase):
#     def setUp(self):
#         self.board = Board.objects.create(name='Django', description = 'Django board.')
#         url = reverse('home')
#         self.response = self.client.get(url)
#
#     def test_home_view_status_code(self):
#         """
#         测试的是请求该URL后返回的响应状态码。状态码200意味着成功。
#         """
#         self.assertEquals(self.response.status_code, 200)  #测试返回值是否 是 登录200，注意这里有个属性调用res.status_cod
#
#     def test_home_url_resolves_home_view(self):
#         """
#         将浏览器发起请求的URL与urls.py模块中列出的URL进⾏匹配。
#         该测试⽤于确定URL / ,返回 home 视图。
#         """
#         view = resolve('/')
#         self.assertEquals(view.func, home)
#
#     def test_home_view_contains_link_to_topics_page(self):
#         # 这个是写超链接的测试
#         board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
#         self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
#         #基本上是在测试 response 主体是否包含⽂本  href="/boards/1/",即链接到board_topics_url
#
# class BoardTopicsTests(TestCase):
#     def setUp(self):
#         # 创建一个Board实例来用于测试，因为django针对当前数据库跑我的测试，
#         # 测试的时候会创建一个新的数据库，测试完后会自动销毁。
#         Board.objects.create(name='Django', description='Django board.')
#
#     def test_board_topics_view_success_status_code(self):
#         """
#         测试 Django是否对于现有的 Board 返回 status code(状态码) 200(成功)。
#         """
#         url = reverse('board_topics', kwargs={'pk': 1})
#         response = self.client.get(url) #为了获取requetes提交过来的列表
#         self.assertEquals(response.status_code, 200)
#
#     def test_board_topics_view_not_found_status_code(self):
#         """
#         测试Django 是否对于不存在于数据库的 Board 返回 status code 404(⻚⾯未找到)。
#         """
#         url = reverse('board_topics', kwargs={'pk': 99})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)
#
#     def test_board_topics_url_resolves_board_topics_view(self):
#         """
#         测试Django 是否使⽤了正确的视图函数去渲染 topics。
#         """
#         view = resolve('/boards/1/')  #Resolve函数测试你的网站的URL对应关系是否如你所愿
#         self.assertEquals(view.func, board_topics)
#
#     def test_board_topics_view_contains_link_back_to_homepage(self):
#         # 这里也是一个超链接的单元测试，目的是测试能否实现返回链接
#         board_topics_url = reverse('board_topics', kwargs={'pk': 1}) #reverse的第一个参数是urls.py的url中的name
#         response = self.client.get(board_topics_url)
#         homepage_url = reverse('home')
#         self.assertContains(response, 'href="{0}"'.format(homepage_url))
#
#     def test_board_topics_view_contains_navigation_links(self):
#         """
#         负责确保我们的 view 包含所需的导航链接。
#         """
#         board_topics_url = reverse('board_topics', kwargs={'pk': 1})
#         homepage_url = reverse('home')
#         new_topic_url = reverse('new_topic', kwargs={'pk': 1})
#         response = self.client.get(board_topics_url)
#         self.assertContains(response, 'href="{0}"'.format(homepage_url))
#         self.assertContains(response, 'href="{0}"'.format(new_topic_url))
#
# class NewTopicTests(TestCase):
#     def setUp(self):
#         # 创建⼀个测试中使⽤的 Board 实例
#         Board.objects.create(name='Django', description='Django board.')
#         User.objects.create_user(username='john', email='john@doe.com', password='123')
#         #用于创建测试的User实例,并假设有这一个用户
#
#     def test_new_topic_view_success_status_code(self):
#         # 检查发给 view 的请求是否成功
#         url = reverse('new_topic', kwargs={'pk': 1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#     def test_new_topic_view_not_found_status_code(self):
#         # 检查当Board不存在时view是否会抛出⼀个404的错误
#         url = reverse('new_topic', kwargs={'pk': 99})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)
#
#     def test_new_topic_url_resolves_new_topic_view(self):
#         # 检查是否正在使⽤正确的 view
#         view = resolve('/boards/1/new/')
#         self.assertEquals(view.func, new_topic)
#
#     def test_new_topic_view_contains_link_back_to_board_topics_view(self):
#         # 确保导航能回到topics的列表
#         new_topic_url = reverse('new_topic', kwargs={'pk': 1})
#         board_topics_url = reverse('board_topics', kwargs={'pk': 1})
#         response = self.client.get(new_topic_url) #为了获取requetes提交过来的列表
#         self.assertContains(response, 'href="{0}"'.format(board_topics_url))
#
#     def test_csrf(self):
#         """
#         由于 CSRF Token 是处理 Post 请求的基本部分，我们需要保证我们的 HTML 包含 token。
#         """
#         url = reverse('new_topic', kwargs={'pk': 1})
#         response = self.client.get(url)
#         self.assertContains(response, 'csrfmiddlewaretoken')
#
#     def test_new_topic_valid_post_data(self):
#         """
#         #发送有效的数据并检查视图函数是否创建了 Topic 和 Post 实例。
#         """
#         url = reverse('new_topic', kwargs={'pk': 1})
#         data = {
#             'subject': 'Test title',
#             'message': 'Lorem ipsum dolor sit amet'
#         }
#         response = self.client.post(url, data)
#         self.assertTrue(Topic.objects.exists())
#         self.assertTrue(Post.objects.exists())
#
#     def test_new_topic_invalid_post_data(self):
#         '''
#        # 发送⼀个空字典来检查应⽤的⾏为。
#         '''
#         url = reverse('new_topic', kwargs={'pk': 1})
#         response = self.client.post(url, {})
#         self.assertEquals(response.status_code, 200)
#
#     def test_new_topic_invalid_post_data_empty_fields(self):
#         '''
#         定期发送数据，检查应用行为，预期应⽤程序会验证并且拒绝空的subject 和 message。
#         '''
#         url = reverse('new_topic', kwargs={'pk': 1})
#         data = {
#             'subject': '',
#             'message': ''
#         }
#         response = self.client.post(url, data)
#         self.assertEquals(response.status_code, 200)
#         self.assertFalse(Topic.objects.exists())
#         self.assertFalse(Post.objects.exists())
#
#     def test_contains_form(self):
#         """
#         抓取上下⽂的表单实例，检查它是否是⼀个  NewTopicForm  。
#         """
#         url = reverse('new_topic', kwargs={'pk': 1})
#         response = self.client.get(url)
#         form = response.context.get('form')
#         self.assertIsInstance(form, NewTopicForm)
#
#     def test_new_topic_invalid_post_data(self):
#         """
#         确保数据⽆效的时候表单会显示错误。
#         """
#         url = reverse('new_topic', kwargs={'pk': 1})
#         response = self.client.post(url, {})
#         form = response.context.get('form')
#         self.assertEquals(response.status_code, 200)
#         self.assertTrue(form.errors) #self.assertTrue(form.errors)无效时显示错误
#
#
