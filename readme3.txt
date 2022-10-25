1.表单处理:Forms(表单) ⽤来处理我们的输⼊。【表单没有数据、不受约束】
标准的做法是通过 HTML 表单实现，⽤户输⼊⼀些数据，将其提交给服务器，然后服务器处理它。
虽然表单处理过程很复杂、但是django已经使过程简单并自动化，不管 HTML 的表单多么简单，总是使⽤Form API。

2.<form> 标签中的 method 属性：会告诉浏览器我们想如何与服务器通信。【关于表单的method属性逻辑、是在视图函数中写的】
HTTP 规范定义了⼏种 request methods(请求⽅法)。但是在⼤部分情况下，只需要使⽤ GET 和 POST 两种 request(请求)类型。
两种最常用的请求:
    GET ⽤于从服务器请求数据。每当点击了⼀个链接或者直接在浏览器中输⼊了⼀个⽹址时，就创建⼀个 GET 请求。

    POST ⽤于想更改服务器上的数据的时候。每次发送数据给服务器都会导致资源状态的变化，应该使⽤ POST 请求发送数据。
Django 使⽤ CSRF Token(Cross-Site Request Forgery Token) 保护所有的POST 请求。
这是⼀个避免外部站点或者应⽤程序向我们的应⽤程序提交数据的安全措施。应⽤程序每次接收⼀个 POST 时，
都会先检查 CSRFToken。如果这个 request 没有 token，或者这个 token是⽆效的，它就会抛弃提交的数据。
csrf_token 的模板标签：{% csrf_token %}
关于csrf_token需要注意的两点:
    (1)它是与其它表单数据一起提交的隐藏字段:
        <input type="hidden" name="csrfmiddlewaretoken" value="jG2o6aWj65YGaqzCtjzRZ9KmY32">
    (2)需要设置 HTML 输⼊的 name，name 将被⽤来在服务器获取数据:
        <input type="text" class="form-control" id="id_subject" name="subject">
        <textarea class="form-control" id="id_message" name="message"rows="5"></textarea>
        针对以上两个name如何检索数据:
                    subject = request.POST['subject']
                    message = request.POST['message']


3.创建表单的正确姿势:
ModelForm  是  Form  的⼦类，它与 model 类相关联。在 boards ⽂件夹（应用程序app）下创建⼀个新的⽂件  forms.py,py文件中
的基类需要继承forms.ModelForm，如果直接用forl为继承对象的话、那将不能与model关联。
然后使用模板代码(类似{% block %})来写html模板。

4. 复⽤表单模板：即可以在项目中重复使用模板。
在templates ⽂件夹中,创建新的文件夹名为includes，在includes文件夹中创建from.html。
然后在includes的同级的html(比如new_topic.html)的某个代码块中使用{% include 'includes/form.html' %}来放置
form.html的代码到new_topic.html的代码块中，相当于一个引用。


5.用户注册：实现注册、登录、注销、密码重置和密码修改
要管理以上的用户功能，需要另起一个应用：django-admin startapp accounts 【在manage.py文件所在同一目录执行】
然后将这个app('accounts')添加到setting的INSTALLED_APPS中。然后依次添加路由、视图函数，以及必要的修改模板。
    django使用UserCreationForm函数可以创建注册表单。


<!--form在模版中的渲染方式:【以下的单对{}中加入%以让django能够解析，双对{}直接不用加%】
    {{form.as_p}} 渲染表单为一系列的p标签，每个p标签包含一个字段;
    {{form.as_ul}}渲染表单为一系列的li标签，每个li 标签包含一个字段，它不包含ul标签;
    {for field in form} 通过迭代form，获取其中的所有field。field可引用的包括{{ field.label_tag }} , {{ field }} , {{ field.errors }};
    {{ field.label_tag }}输出为field的label元素
    {{ field }}输出为field的input
    {{ field.errors }} field的errors元素（errors一般在form验证出错的时候显示）
-->

6.控制台收发Email(其实就是模拟发送真实电子邮件，实则是虚拟的)
  编辑 settings.py模块并将 EMAIL_BACKEND  变量添加到⽂件的末尾：
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

密码重置过程需要四个视图：
    带有表单的⻚⾯，⽤于启动重置过程；
    ⼀个成功的⻚⾯，表示该过程已启动，指示⽤户检查其邮件⽂件夹等；
    检查通过电⼦邮件发送token的⻚⾯;
    ⼀个告诉⽤户重置是否成功的⻚⾯;
这些视图是内置的，我们不需要执⾏任何操作，我们所需要做的就是将路径添加到 urls.py并且创建模板。







