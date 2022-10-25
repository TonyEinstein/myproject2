# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 22:41
# @Author  : ChenRuhai
# @Email   : ruhai.chen@qq.com
# @File    : form_tags.py

# 创建自定义模板标签---以下两个函数都是模板标签，也叫模板过滤器
"""
模板过滤器的工作方式:
    ⾸先，我们将它加载到模板中，就像我们使⽤ widget_tweaks 或static 模板
    标签⼀样。请注意，在创建这个⽂件后，你将不得不⼿动停⽌开发服务器并
    重启它，以便Django可以识别新的模板标签。
"""

from django import template
register = template.Library()

@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)
"""
首先在html中引入头模板标签: {% load form_tags %}
在HTML中引用自定义模板 : {{ form.username|input_class }}

<!-- 如果表单没有被绑定，那么返回如下: -->
'form-control '

<!-- 如果表单被绑定且有效那么返回如下: -->
'form-control is-valid'


<!-- 如果表单被绑定且无效那么返回如下: -->
'form-control is-invalid'

"""





