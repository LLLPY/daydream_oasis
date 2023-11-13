import os
import re
from blog.models import Blog, Tag
from django.db import transaction

old_dir = r'C:\Users\LLL03\Desktop\daydream_oasis\daydream_oasis_front\docs\blog'


def replace(file_path):
    content = None
    with open(file_path, 'r', encoding='utf8') as f:
        content = f.read()

    with open(file_path, 'w', encoding='utf8') as f:

        # 匹配blog_id
        res = re.search(r'<BlogInfo id="(\d+)".*?/>', content)
        if res:
            blog_id = res.group(1)
            blog_obj = Blog.objects.filter(id=blog_id).first()
            if blog_obj:

                # 匹配标签
                tag_list = re.search(r'<BlogInfo.*?tag_list="(.*?)".*?/>',
                                     content)
                if tag_list:
                    tag_str = tag_list.group(1).replace('[', '').replace(
                        ']', '').replace(' ', '').replace("'", '').split(',')
                    tag_list = list(filter(lambda tag: tag, tag_str))
                    for tag in tag_list:
                        tag_obj = Tag.objects.filter(title=tag).first()
                        if tag_obj not in blog_obj.tag_list.all():
                            blog_obj.tag_list.add(tag_obj)

                # 替换掉bloginfo
                content = re.sub(r'<BlogInfo.*?/>',
                                 f'<BlogInfo id="{blog_id}"/>', content)
                blog_obj.content = content

                # 找到第一个图片链接
                first_img_url = re.search(r'!\[.*\]\((.*?)\)', content)
                if first_img_url:
                    first_img_url = first_img_url.group(1)
                    blog_obj.avatar = first_img_url
                else:
                    blog_obj.avatar = 'http://www.lll.plus/media/image/default_blog_avatar.jpg'
                blog_obj.save()

        f.write(content)


def rename(file_path):
    content = None
    with open(file_path, 'r', encoding='utf8') as f:
        content = f.read()
    os.remove(file_path)
    file_name = str(file_path).split(os.sep)[-1]
    new_file_name = re.sub(r'^\d+\.','',file_name)
    cur_dir = os.path.dirname(file_path)
    new_file_path = os.path.join(cur_dir,new_file_name)
    print(new_file_path)
    with open(new_file_path, 'w', encoding='utf8') as f:
        f.write(content)


@transaction.atomic
def tree(_dir):

    for path in os.listdir(_dir):
        cur_path = os.path.join(_dir, path)
        if os.path.isdir(cur_path):
            tree(cur_path)
        else:
            rename(cur_path)


def main():
    tree(old_dir)


@transaction.atomic
def tag_strip():
    for tag in Tag.objects.all():
        tag.title = tag.title.replace(' ', '').strip()
        print(tag.title)
        tag.save()

@transaction.atomic
def aaaa():
    for blog in Blog.objects.all():
        # print(blog.tag_list.all())
        blog.title = re.sub(r'^\d+\.','',blog.title)
        blog.save()


if __name__ == '__main__':
    main()
