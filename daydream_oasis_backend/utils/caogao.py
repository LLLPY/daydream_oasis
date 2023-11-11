import os
import re

old_dir = r'C:\Users\LLL03\Desktop\daydream_oasis\daydream_oasis_front\docs\blog'


def replace(file_path):
    content = None
    with open(file_path, 'r+', encoding='utf8') as f:
        content = f.read()
        pattern = r'''!\[.*?\]\([\.\\](.*?media).*?\)'''
        res = re.findall(pattern,content)
        if res:
            print(file_path)
            pattern = r'''\]\([\.\/].*?media/image'''
            content = re.sub(pattern, '](http://www.lll.plus/media/image', content)
            print(res)
        else:
            content = None
        # print(res)
        # 找到有链接的地方
    # if content:
        # with open(file_path, 'w', encoding='utf8') as f:
            # f.write(content)


# 替换所有链接
def tree(_dir):
    for path in os.listdir(_dir):
        cur_path = os.path.join(_dir, path)
        if os.path.isfile(cur_path):
            replace(cur_path)
            # return
        else:
            tree(cur_path)

tree(old_dir)


# s = 'aaaxxaf88f'

# res = re.sub(r'\d+','mmm',s)

# print(res)