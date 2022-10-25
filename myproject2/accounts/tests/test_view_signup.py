from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
# Create your tests here.

# 该测试文件有问题

from ..views import signup
# from ..forms import SignUpForm

class SignUpTests(TestCase):
    def test_signup_status_code(self):# 测试状态码（200=success）
        url = reverse('signup')
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):# URL /signup/ 是否返回了正确的视图函数。
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):# 测试响应中是否有 CSRF token
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):# 测试响应中是否有表单
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)

    def test_form_inputs(self):
        '''
        测试：验证模板中的HTML输⼊：
        视图必须包含五个输入:csrf、用户名、电子邮件、密码1、密码2
        '''
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"',2)



class SuccessfulSignUpTests(TestCase): #测试⼀个成功的注册功能
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        '''
        有效的表单提交应该将用户重定向到主页
        '''
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):# 测试能否成功创建用户
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        创建到任意页面的新请求。
        在成功注册之后，结果响应的上下文现在应该有一个“用户”。
        '''
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignUpTests(TestCase): #⽤于数据⽆效的注册⽤例

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {}) # 提交一个空字典

    def test_signup_status_code(self):
        # 无效的表单提交应该返回到相同的页面
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        # 测试表单错误
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        # 测试：如果想注册的用户名已经存在，是否提示想注册的用户名已经存在
        self.assertFalse(User.objects.exists())






