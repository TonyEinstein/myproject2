# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 22:11
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : forms.py

from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5,'placeholder': 'What is on your mind'}
    ),
        max_length=4000,
        help_text='The max length of the text is 4000.')

    class Meta:
        """
        fields  列表中的  subject  引⽤ Topic 类中的 subject field(字段)。
        定义了⼀个叫做  message  的额外字段。它⽤来引⽤ Post 中我们想要保存的 message。
        """
        model = Topic
        fields = ['subject', 'message']

from .models import Post

class PostForm(forms.ModelForm):
    # 回帖子的表单
    class Meta:
        model = Post
        fields = ['message', ]