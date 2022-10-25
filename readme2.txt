什么是静态文件？
答：静态⽂件是指 CSS，JavaScript，字体，图⽚或者是⽤来组成⽤户界⾯的任何其他资源。
【虽然django能处理静态文件、但是静态文件一般有nginx等反向代理服务器提供、django解决业务逻辑;
管理静态文件的功能在INSTALLED_APPS  的 django.contrib.staticfiles 中找到】



1.在项⽬根⽬录中，除了 boards, templates 和myproject⽂件夹外，再创建⼀个名为static的新⽂件夹，
并在static⽂件夹内创建另⼀个名为css的⽂件夹,存放css文件，同理也可创建其它。
然后告诉django在哪里可以找到静态文件，可以在settings.py文件里面的STATIC_URL下面(下一行)设置路径，
比如：STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

2.如何加载使用静态文件(css、js、图片)？
使⽤了 Static Files App 模板标签  {% load static%}  。
模板标签 {% static %}  ⽤于构成资源⽂件完整URL，将返回静态文件路径。【之后实现html的模板框架即可实现网站大致模样】

3.使用django admin，首先，django admin一般用来做后台管理的，也就是网站管理员。
配置django admin：
    python manage.py createsuperuser  （这里是:admin,密码admin123）
    然后运行网站，即可进入管理员界面:http://127.0.0.1:8000/admin/

4.在django admin中添加模型与管理：
在admin.py中添加Board模型(这里模型也就是指app应用程序比如boards):
    from .models import Board
    admin.site.register(Board)

5.弄明白URLs 和 Forms：
URL 调度器（dispatcher） 和 URLconf (URL configuration) 是 Django应⽤中的基础部分。
⼀个项⽬可以有很多 urls.py 分布在多个应⽤（app）中。Django 需要⼀个url.py 作为⼊⼝。
这个特殊的 urls.py 叫做 根路由配置（root URLconf）。被默认定义在 settings.py 中：ROOT_URLCONF = 'myproject.urls'
'''
当 Django 接受⼀个请求(request)， 它就会在项⽬的 URLconf 中寻找匹配项。
他从  urlpatterns  变量的第⼀条开始，然后在每个  url  中去匹配请求的 URL。
如果 Django 找到了⼀个匹配路径，他会把请求(request)发送给  url  的第⼆个参数 视图函数（view function）。
urlpatterns  中的顺序很重要，因为 Django ⼀旦找到匹配就会停⽌往后搜索。
如果 Django 在 URLconf 中没有找到匹配项，他会通过 Page Not Found 的错误处理代码抛出⼀个 404 异常。
'''

如何创建url???:::
答：  【注意，加入的url路径名称在^$之间，如何都不加就代表首页，可以是多层(用/相隔)，
        这个内容是代表127.0.0.1:8080/后面的内容】
    (1)基础URL创建起来很容易。就只是个匹配字符串的问题。
       比如:创建一个about页面:url(r'^about/$', views.about, name='about'), #这里的about是视图函数
            那么about页面的视图函数:
                   def about(request): '''do something...''' return render(request, 'about.html')
    (2)高级urls路由:
    更⾼级的URL路由使⽤⽅法是通过正则表达式来匹配某些类型的数据并创建动态 URL。
    比如：匹配django用户模型里面所有有效的用户名：【注：user_profile是未知的用户名(视图函数，其实是函数返回的东西)】
    url(r'^(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile')。
    值得注意的是：如果写有正则匹配之后，那么其它符合匹配的url需要写在正则所在的url的前面，写在后面会被覆盖。
    当然，现实中这里的正则匹配的一般是(标识)数值型的ID或者字符串，作为一个动态页面。

    如何完成一个动态页面的编写(包括url+视图函数)，比如：
       第一【以数字id为标识】：
        url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics')
        def board_topics(request, pk): # do something..
        其中，P<pk>是要告诉 Django 将捕获到的值放⼊名为 pk 的关键字参数中。
        因为使⽤了  (?P<pk>\d+)  正则表达式，在  board_topics  函数中，关键字参数必须命名为 pk。
       第二【在视图函数使⽤任意名字的参数、不死死的写死于pk这个词,即名字⽆关紧要】,那应该这样定义:
          url(r'^boards/(\d+)/$', views.board_topics, name='board_topics')
           视图函数:
                def board_topics(request, board_id):#.....#
                或者 def board_topics(request, id):# do something...

6.单元测试中的setup方法：主要是用于创建实例来进行测试。
为了能在新测试中重⽤相同的 response。,可以将 url 和 response 移到了 setUp。
另外注意：django里面的单元测试一般指的是测试网站能不能正常运转，比如可能会出现html模板代码与某个py文件的配置不匹配等等


7.写超链接单元测试: 在tests.py文件中的类中增加测试超链接的方法即可。

8.实⽤URL模式列表（最常用的正则）:
参考链接：https://simpleisbetterthancomplex.com/references/2016/10/10/url-patterns.html
 （1）主键⾃增字段：
        正则表达式： (?P<pk>\d+)
        举例： url(r'^questions/(?P<pk>\d+)/$', views.question,name='question')
        有效url：/questions/934/
        捕获数据：{'pk': '934'}

 （2）Slug 字段：
        正则表达式： (?P<slug>[-\w]+)
        举例： url(r'^questions/(?P<pk>\d+)/$', views.question,name='question')
        有效url：/posts/hello-world/
        捕获数据：{'slug': 'hello-world'}

 （3）有主键的Slug 字段：
        正则表达式： (?P<slug>[-\w]+)-(?P<pk>\d+)
        举例： url(r'^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$',views.blog_post, name='blog_post')
        有效url：/blog/hello-world-159/
        捕获数据：{'slug': 'hello-world', 'pk': '159'}

 （4）Django⽤户名：
        正则表达式： (?P<username>[\w.@+-]+)
        举例： url(r'^profile/(?P<username>[\w.@+-]+)/$',views.user_profile, name='user_profile')
        有效url：/profile/vitorfs/
        捕获数据：{'username': 'vitorfs'}

（5）Year：
        正则表达式： (?P<year>[0-9]{4})
        举例： url(r'^articles/(?P<year>[0-9]{4})/$',views.year_archive, name='year')
        有效url：/articles/2016/
        捕获数据：{'year': '2016'}

（6）Year/Month：
        正则表达式： (?P<year>[0-9]{4})/(?P<month>[0-9]{2})
        举例： url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='month')
        有效url：/articles/2016/01/
        捕获数据：{'year': '2016', 'month': '01'}


9.重写 HTML 模板，创建⼀个 master page(⺟版⻚)，其他模板添加它所独特的部分。
每个创建的模板都 extend(继承) 这个特殊的模板,; {% block %}  标签,它⽤于在模板中保留⼀个空间，
⼀个"⼦"模板(继承这个⺟版⻚的模板)可以在这个空间中插⼊代码和 HTML。
在  {% block title %}  中设置了⼀个默认值 "Django Boards."。
如果我们在⼦模板中未设置  {% block title %}  的值它就会被使⽤。

加入母版页叫base.html，那么要想网页加入一些东西，就需要在子版页(比如home.html)上继承母版页，
在子板页上加入的内容，这些代表内容的代码会最终放置到base.html中的blocks部分。
子板页的第一行代码是: {% extends 'base.html' %}  表示继承base.html为母版页。
如何在block添加内容： 其实base.html母版页和子板页中的block位置是对应的。



10.如何改变字体：在需要改动的位置写<link>链接字体css文件即可














