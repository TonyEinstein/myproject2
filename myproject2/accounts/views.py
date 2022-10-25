
# 视图py文件一般实现业务逻辑
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect

from .forms import SignUpForm

"""
关于render的解释：render 把模板’myapp/index.html’ 和数据 ‘foo’: ‘bar’ 内容 渲染在了一起返回给了前台。
参数解释：
    request:　用于生成响应的请求对象
    template_name:　要使用的模板的完整名称, 可选的参数
    context:　添加到模板上下文的一个字典. 默认是一个空字典. 如果字典中的某个值是可调用的, 
             视图将在渲染模板之前调用它.
    content_type:　 生成的文档要使用的MIME类型. 默认为DEFAULT_CONTENT_TYPE设置的值. 默认为"text/html"
    status:　响应的状态码. 默认为200
    useing:　用于加载模板的模板引擎的名称
"""


# Create your views here.
def signup(request):
    # form.save()创建一个User实例，并且将创建的用户作为参数传给login函数，手动验证用户，之后视图将用户重定向到主页。
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        # 这里和上面不需要再使用UserCreationForm()，因为可以使用SignUpForm，SignUpForm已经继承了UserCreationForm
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})