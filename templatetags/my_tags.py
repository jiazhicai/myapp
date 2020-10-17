from django import template
register = template.Library()

# 装饰器自定义过滤器
@register.filter
def my_filter(v1, v2):
    return v1 * v2

# 装饰器自定义标签
@register.simple_tag
def my_tag1(v1, v2, v3):
    return v1 * v2 * v3

# 使用自定义标签和过滤器前，要在html文件body 的最上方中导入该py文件
# {% load my_tags %}

# 在HTML中使用自定义过滤器
# {{l1|my_filter:22}}

#在HTML中使用自定义标签
# {% my_tag1 l1 22 33 %}

from django.utils.safestring import mark_safe
@register.simple_tag
def my_html(v1, v2):
    temp_html = "<input type='text' id='%s' class='%s' />" %(v1, v2)
    return mark_safe(temp_html)

