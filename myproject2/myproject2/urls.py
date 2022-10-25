"""myproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# 此文件是默认的根路由配置文件,已经⾃动配置好了，不需要去改变它任何东⻄。
from django.conf.urls import url
from django.contrib import admin
"""
解读导入的url函数：
    def url(regex, view, kwargs=None, name=None):
        regex： 匹配 URL patterns 的正则表达式。注意：正则表达式会忽略掉
                GET 或者 POST 后⾯的参数。在⼀个 http://127.0.0.1:8000/boards/?page=2 
                的请求中，只有 /boards/ 会被处理。
        view： 视图函数被⽤来处理⽤户请求，同时它还可以是django.conf.urls.include 函数的返回值，
                它将引⽤⼀个外部的urls.py⽂件，例如，你可以使⽤它来定义⼀组特定于应⽤的 URLs，使⽤前缀
                将其包含在根 URLconf 中。我们会在后⾯继续探讨这个概念。
        kwargs：传递给⽬标视图函数的任意关键字参数，它通常⽤于在可重⽤视图上进⾏⼀些简单的定制，不是经常使⽤它。
        name:： 该 URL 的唯⼀标识符。这是⼀个⾮常重要的特征。要始终记得为你的 URLs 命名。
                所以，很重要的⼀点是：不要在 views(视图) 或者 templates(模板) 中硬编码 URL，
                ⽽是通过它的名字去引⽤ URL。
"""

from boards import views  #因为urls.py所在的目录与views.py所在的目录平级，所以直接from
# from accounts import views as accounts_views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

"""
对于home视图，使⽤ ^$  正则，它将匹配⼀个空路径，也就是主⻚（这个URL：http://127.0.0.1:8000/ ）。
如果我想匹配的URL是http://127.0.0.1:8000/homepage/ ，那么我的URL正则表达式
就会是： url(r'^homepage/$', views.home, name='home')  。
其实这个也叫做路由，可以理解成一个路由指向代表一个页面。
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    # url(r'^about/$', views.about, name='about'),#例子:创建基础url，这里是创建一个about页面
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), #基于类的视图
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^$',views.home,name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),#添加主题列表页面
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # 密码重置路由:
    url(r'^reset/$',auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                         email_template_name='password_reset_email.html',
                                                         subject_template_name='password_reset_subject.txt'),name='password_reset'),

    url(r'^reset/done/$',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),

    url(r'^reset/complete/$',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    #密码修改
    url(r'^settings/password/$',
        auth_views.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),

    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),

    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    #pk  ⽤于唯⼀标识版块（Board）， topic_pk  ⽤于唯⼀标识该回复来⾃哪个主题。

    # 实现回复帖⼦的功能
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$',views.reply_topic, name='reply_topic'),
]
"""
    在密码重置视图中， template_name  参数是可选的。但我认为重新定义它是个好主意，因此视图和模板之间的链接⽐仅使⽤默认值更加明显。
"""

"""
分析⼀下  urlpatterns  和  url:
    其实url可以看作整个网站的每一个页面。
    而urlpatterns可以看作整个网站的所有页面的组成。

"""


