# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/12 22:51  
from django import template

register = template.Library()


# 自定义的分页标签
@register.simple_tag
def custom_paginator(page, num_total_pages=9, num_back_pages=3):
    '''
    page: 分页的页码对象；在views.py中创建的；
    num_total_pages：预定义整个分页器展示10个页码；
    num_back_pages：预定义，当前页码后面少于4个页码的时候，分页器开始滚动，最后无法滚动的除外。


    分页的情况：(默认展示10个分页按钮，并且保证当前点击的页码后面至少是4个页码)
    总页数如果没有超过10页，则页码全部展示，且没有滚动符...
    总页数超过10页的情况：
    1.从第一页到第6页，点击哪一个页码，这个页码被选中，并且整个分页器没有滚动，没有...省略符；
    2.从第7页到第36页，分页器滚动，所点击的页码始终位于中心位置，且出现...省略符；预定义当前选中页码前面是3个页码(不包含1和...)后面展示4个页码；
    3.从第37页开始往后，分页器不滚动，所点击的页码不位于中心位置；
    :return:

    '''
    html = ''
    if page.paginator.num_pages <= num_total_pages:
        # 分页的总页数不超过10页，不考虑当前点击的页码是否是中心位置了：
        for x in range(1, page.paginator.num_pages + 1):
            html += '<span><a href="?page=%s">%s</a></span>' % (x, x)
        return html
    elif page.number <= num_total_pages - num_back_pages:
        for x in range(1, num_total_pages + 1):
            html += '<span><a href="?page=%s">%s</a></span>' % (x, x)
        return html
    # (num_total_pages - num_back_pages - 3):预定义当前选中页码前面是3个页码(不包含1和...)
    elif num_total_pages - (
            num_total_pages - num_back_pages - 3) <= page.number <= page.paginator.num_pages - num_back_pages:
        html += '''
        <span><a href="?page=1">1</a></span>
        <span class="disabled"><a href="?page=%s">...</a></span>
        '''
        # 1...2 3 4 5 6 7 8 9
        for x in range(page.number - (num_total_pages - num_back_pages - 3), page.number + num_back_pages + 1):
            html += '<span><a href="?page=%s">%s</a></span>' % (x, x)
        return html
    else:
        # 最后无法滚动的部分
        html += '''
        <span><a href="?page=1">1</a></span>
        <span class="disabled"><a href="?page=%s">...</a></span>
        '''
        for x in range(page.paginator.num_pages - (num_total_pages - num_back_pages - 3) - num_back_pages,
                       page.paginator.num_pages + 1):
            html += '<span><a href="?page=%s">%s</a></span>' % (x, x)
        return html
