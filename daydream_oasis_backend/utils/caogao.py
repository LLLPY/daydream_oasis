import os
import re

old_dir = r'C:\Users\LLL03\Desktop\daydream_oasis\daydream_oasis_front\docs\blog'


def replace(file_path):
    content = None
    with open(file_path, 'r+', encoding='utf8') as f:
        content = f.read()

    with open(file_path, 'w', encoding='utf8') as f:
        content = f'''---\n
next: false\n
---\n

{content}
\n
<ActionBox />
'''
        f.write(content)


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