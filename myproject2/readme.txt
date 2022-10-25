注意：django框架中每个py文件的前面的注释就是叫你如何去使用那个文件的。


1.在虚拟环境中安装django：
    pip install django==1.11.4

2.创建新的django项目：
    django-admin startproject myproject
文件解释：
    manage.py：使⽤django-admin命令⾏⼯具的快捷⽅式。它⽤于运⾏与我们项⽬相关的管理命令。
               我们将使⽤它来运⾏开发服务器，运⾏测试，创建迁移等等。
    __init.py：这个空⽂件告诉python这个⽂件夹是⼀个python包。
    settings.py：这个⽂件包含了所有的项⽬配置。将来我们会⼀直提到这个⽂件！
    urls.py：这个⽂件负责映射我们项⽬中的路由和路径。例如，如果你想在访问URL  / about/  时显示某些内容，
             则必须先在这⾥做映射关系。
    wsgi.py：该⽂件是⽤于部署的简单⽹关接⼝。你可以暂且先不⽤关⼼她的内容，就先让他在那⾥就好了。

3.启动django运行项目：
    python manage.py runserver

如何启动app应用程序:
    python manage.py startapp [app_label]

4.两个重要概念:
app：是⼀个可以做完成某件事情的Web应⽤程序。⼀个应⽤程序通常
      由⼀组models(数据库表)，views(视图)，templates(模板)，tests(测试) 组成。

project：是配置和应⽤程序的集合。⼀个项⽬可以由多个应⽤程序或⼀个应⽤程序组成。
         project项目内可能有多个app文件夹，project项目内肯定有一个project文件夹存放项目的一些文件。

5.创建app应用程序目录：
        django-admin startapp boards  【到manage.py⽂件所在的⽬录并执⾏】
  app目录下文件解读:
        migrations/：在这个⽂件夹⾥，Django会存储⼀些⽂件以跟踪你在models.py⽂件中创建的变更，
                       ⽤来保持数据库和models.py的同步。
        admin.py：这个⽂件为⼀个django内置的应⽤程序Django Admin的配置⽂件。
        apps.py：这是应⽤程序本身的配置⽂件。
        models.py：这⾥是我们定义Web应⽤程序数据实例的地⽅。models会由Django⾃动转换为数据库表。
        tests.py：这个⽂件⽤来写当前应⽤程序的单元测试。
        views.py：这是我们处理Web应⽤程序请求(request)/响应(resopnse)周期的⽂件。

6.创建了应⽤程序，配置⼀下项⽬以便启⽤这个应⽤程序:

添加新的应用程序到settings.py的 INSTALLED_APPS  变量(一个列表)：
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'boards', #上面空格一行以区分内置和添加的区别
  ]

7.在views.py中写一些函数返回东西。

8.views写完返回什么之后，现在必须告诉Django什么时候会调⽤这个view。这需要在urls.py⽂件中完成。

9.创建文件0001_initial.py：【该文件是告诉django创建数据库】
    python manage.py makemigrations
    该文件代表了应⽤程序模型的当前状态。

    迁移⽂件将被翻译成SQL语句。
    如果您熟悉SQL，则可以运⾏以下命令来检验将是要被数据库执⾏的SQL指令:
            python manage.py sqlmigrate boards 0001

10.将⽣成的迁移⽂件应⽤到数据库：
    python manage.py migrate  #创建表结构





11.使用shell启动django进行调试：
使⽤manage.py ⼯具加载我们的项⽬来启动 Python shell:
    python manage.py shell
项⽬将被添加到 sys.path  并加载Django。这意味着可以在项⽬中导⼊我们的模型和其他资源并使⽤它。


12.在应用程序的目录中的test.py写测试用例，比如写返回状态码：
    需要继承test下的这个TestCase类

    如何运行单元测试:python manage.py test
    测试时显示更详细的信息：python manage.py test --verbosity=2
    verbosity=2是将显示级别设置的更高一些，0是无输出，1是正常输出，2是详细输出。
测试的时候可以指定测试的app： python manage.py test boards
也可以直接指定测试的文件(文件名):
    python manage.py test boards.tests.test_view_topic_posts






