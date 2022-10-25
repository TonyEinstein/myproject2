from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from .forms import NewTopicForm, PostForm
from .models import Board, Topic, Post

"""
视图是接收 httprequest  对象并返回⼀个 httpresponse  对象的Python函
数。接收 request 作为参数并返回 response 作为结果。
"""
# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})
"""
写完返回什么之后，现在必须告诉Django什么时候会调⽤这个view。这需要在urls.py⽂件中完成。
"""

def board_topics(request, pk): #主题列表页面的视图函数
    """
    在  DEBUG=False  的⽣产环境中,如果访问失败增加一个404 Page Not Found 的⻚⾯,
    而不是500 Internal ServerError 的⻚⾯
    """
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, 'topics.html', {'board': board,'topics':topics})

# 使用装饰器之后，现在如果⽤户没有登录，将被重定向到登录⻚⾯
@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # user = User.objects.first()  # TODO:重定向到创建的主题页面，后面加入回帖功能的时候就不再需要
    # 更新重定向地址
    if request.method == 'POST':
        form = NewTopicForm(request.POST) #如果是POST,那么实例化一个将post数据传递给form的form实例。
        if form.is_valid(): #让django验证数据
            topic = form.save(commit=False)  #将数据存入数据库
            topic.board = board
            topic.starter = request.user #这里原来是user，因为发布主题的用户需要是当然用户，也就是登录了才能发布。
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),topic=topic,created_by=request.user)
            return redirect('topic_posts', pk=pk,topic_pk=topic.pk)
    else: #如果请求是get,那么初始化一个空表单，因为不用提交数据。
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board,'form': form})

def topic_posts(request, pk, topic_pk):
    """
    正在间接地获取当前的版块，记住，主题（topic）模型是关联版块（Board）模型的，
    所以我们可以访问当前的版块
    """
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})


# 受 @login_required  保护的视图，以及简单的表单处理逻辑;【回复帖子功能】
@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})




