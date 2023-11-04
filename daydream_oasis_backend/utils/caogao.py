# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/10/9 23:19  
import os
from django.db import transaction
import re
from blog.models import Tag, Blog
from blog.models import Category
import datetime

# TODO 数据导入数据库
from user.models import User

old_dir = r'C:\Users\LLL03\Desktop\daydream_oasis\daydream_oasis_front\docs\blog'
res = {}


# 分类转入数据库
@transaction.atomic
def category(_dir, depth=0):
    parent_name = _dir.split(os.sep)[-1]
    print(f'parent:{parent_name}')
    parent = Category.get_by_name(parent_name)
    if not parent:
        parent = Category()
        parent.title = parent_name
        parent.creator_id = 1
        parent.depth = depth
        parent.save()

    for cur_path in os.listdir(_dir):
        new_path = os.path.join(_dir, cur_path)
        if os.path.isdir(new_path):
            print(f'child:{cur_path}')
            child = Category.get_by_name(cur_path)
            if not child:
                child = Category()
                child.parent = parent
                child.title = cur_path
                child.creator_id = 1
                child.depth = parent.depth + 1
                child.save()

            category(new_path, depth + 1)


# 标签
tag_set = set()


@transaction.atomic
def import_tag(_dir, ):
    for cur_path in os.listdir(_dir):
        abs_path = os.path.join(_dir, cur_path)
        if os.path.isfile(abs_path):
            if cur_path.endswith('.md'):
                with open(abs_path, 'r', encoding='utf8') as f:
                    content = f.read()
                    pattern = r'''<BlogInfo.*title="(.*)" author="(.*)" pv=0 read_times=0 pre_cost_time=(.*) category="(.*)" tag_list="(.*)" create_time="(.*)" update_time="(.*)" />'''
                    res = re.findall(pattern, content)
                    if res:
                        tag_str: str = res[0][4]
                        tag_list = tag_str.replace('[', '').replace(']', '').replace("'", '').split(',')
                        for tag in tag_list:
                            if tag and tag not in tag_set and not Tag.objects.filter(title=tag).exists():
                                tag_obj = Tag()
                                tag_obj.title = tag
                                tag_obj.creator_id = 1
                                tag_obj.save()
                            tag_set.add(tag)
        else:
            import_tag(abs_path)


@transaction.atomic
def import_user():
    import json
    from user.models import User
    import os
    dir_name = os.path.dirname(os.path.abspath(__file__))
    user_list = json.load(open(os.path.join(dir_name, 'user.json'), 'r', encoding='utf8'))
    print(user_list)
    for user_dic in user_list:
        user = User(**user_dic)
        user.save()


blog_id = 1


@transaction.atomic
def import_blog(_dir):
    global blog_id
    category = _dir.split(os.sep)[-1]
    for cur_path in os.listdir(_dir):
        abs_path = os.path.join(_dir, cur_path)
        if os.path.isfile(abs_path):
            if cur_path.endswith('.md'):
                with open(abs_path, 'r', encoding='utf8') as f:
                    content = f.read()
                    pattern = r'''<BlogInfo.*title="(.*)" author="(.*)" pv=0 read_times=0 pre_cost_time=(.*) category="(.*)" tag_list="(.*)" create_time="(.*)" update_time="(.*)" />'''
                    res = re.findall(pattern, content)

                    if res:
                        res = res[0]

                        title, author, pre_cost_time, category, tag_list, create_time, update_time = res
                        pre_cost_time = pre_cost_time.strip('"')
                        tag_str: str = res[4]
                        tag_list = tag_str.replace('[', '').replace(']', '').replace("'", '').split(',')
                        new_blog_info = '''<BlogInfo id="{}" title="{}" author="{}" pv=0 read_times=0 pre_cost_time="{}" category="{}" tag_list="{}" create_time="{}" update_time="{}" />'''.format(
                            blog_id,
                            title,
                            author,
                            pre_cost_time,
                            category,
                            tag_list,
                            create_time,
                            update_time
                        )
                        content = re.sub(pattern, new_blog_info, content)


                    else:
                        title, author, pre_cost_time, category, tag_list, create_time, update_time = '', '白日梦想猿', 0, category, [], datetime.datetime.now().strftime(
                            '%Y.%m.%d %H:%M:%S'), datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')

                        new_blog_info = '''<BlogInfo id="{}" title="{}" author="{}" pv=0 read_times=0 pre_cost_time="{}" category="{}" tag_list="{}" create_time="{}" update_time="{}" />'''.format(
                            blog_id,
                            title,
                            author,
                            pre_cost_time,
                            category,
                            tag_list,
                            create_time,
                            update_time
                        )
                        content = new_blog_info + content

                    with open(abs_path, 'w', encoding='utf8') as ff:
                        ff.write(content)

                    blog_obj = Blog()
                    blog_obj.id = blog_id
                    blog_obj.title = title
                    author_obj = User.get_by_username(author)
                    if not author_obj:
                        print(author)
                    blog_obj.author = author_obj
                    if category == 'leetcode100题':
                        category = 'leetcode'
                    elif category in ['爬虫学习', 'python爬虫', '爬虫学习']:
                        category = '爬虫'
                    elif category == 'c plus plus':
                        category = 'c++'
                    elif category == '人工智能':
                        category = 'AI'
                    elif category == 'JavaScript':
                        category = 'js学习'
                    elif category == 'web开发':
                        category = 'Web开发编程'
                    elif category == 'oracle':
                        category = '数据库编程'
                    elif category == 'os模块的学习':
                        category = '文件'
                    elif category in ['pygame', '学生成绩管理系统']:
                        category = 'GUI编程'
                    elif category == 'seaborn':
                        category = 'seaborn学习'

                    category_obj = Category.get_by_name(category)
                    if not category_obj:
                        print(2222, category, category_obj)
                    blog_obj.category = category_obj
                    for tag in tag_list:
                        tag_obj = Tag.objects_all.filter(title=tag).first()
                        if tag_obj:
                            blog_obj.tag_list.add(tag_obj)

                    create_time = '.'.join(create_time.split('.')[:-1]) if create_time.count('.') == 3 else create_time
                    update_time = '.'.join(update_time.split('.')[:-1]) if update_time.count('.') == 3 else update_time
                    blog_obj.create_time = datetime.datetime.strptime(create_time, '%Y.%m.%d %H:%M:%S')
                    blog_obj.update_time = datetime.datetime.strptime(update_time, '%Y.%m.%d %H:%M:%S')
                    blog_obj.content = content
                    blog_obj.save()
                    print(1111111, blog_id)
                    blog_id += 1
        else:
            import_blog(abs_path)


def main():
    # category(old_dir)
    # tree(old_dir)
    # import_user()
    import_blog(old_dir)


if __name__ == '__main__':
    main()
