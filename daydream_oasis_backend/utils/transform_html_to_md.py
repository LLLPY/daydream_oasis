import os
import re
import datetime

_id = 1


def clear_path(path):
    return re.sub(r'\d+_|\d+\.|\(|\)|（|）|%|-|lll', '', path)


def to_md(content, type_, title, category, create_time, update_time, callback=None):
    '''内容转为md格式'''
    global _id
    author = '白日梦想猿'
    tag_list = [category]
    create_time = datetime.datetime.fromtimestamp(create_time).strftime('%Y.%m.%d %H:%M:%S')
    update_time = datetime.datetime.fromtimestamp(update_time).strftime('%Y.%m.%d %H:%M:%S')
    avg_speed = 400  # 除以3的原因：内容中除了中文以外可能还有英文
    read_time = 60 * (len(content) / avg_speed) / 3
    minute = int(read_time) // 60
    seconds = int(read_time) % 60
    pre_cost_time = f'{minute}分{seconds}秒'
    content = f'''
<BlogInfo id="{_id}" title="{title}" author="{author}" pv=0 read_times=0 pre_cost_time={pre_cost_time} category="{category}" tag_list="{tag_list}" create_time="{create_time}" update_time="{update_time}" />

```{type_}
{content}
```
'''
    _id += 1
    res = {'id': _id, 'title': title, 'category': category, 'tag_list': tag_list, 'content': content,
           'create_time': create_time, 'update_time': update_time}
    if callback:
        # 存入数据库
        callback(**res)
    return res


# 把一个目录下的所有文件都转成md格式，并保存到相应的文件夹中
def copy_dir(old_dir, new_dir, include_file, exclude_file, exclude_dir):
    number = 1

    # 根据文件的创建时间排序后再获取文件列表
    for path in sorted(os.listdir(old_dir), key=lambda _path: os.stat(os.path.join(old_dir, _path)).st_ctime):

        cur_path = os.path.join(old_dir, path)
        create_time = os.stat(cur_path).st_ctime
        update_time = os.stat(cur_path).st_mtime
        category = clear_path(os.path.dirname(cur_path).split(os.sep)[-1])

        # 判断当前路径是不是目录r
        is_dir = os.path.isdir(cur_path)

        new_path = clear_path(os.path.join(new_dir, path))
        if is_dir and path not in exclude_dir:
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            copy_dir(cur_path, new_path, include_file, exclude_file, exclude_dir)
        else:
            file_name = ''.join(path.split('.')[:-1])
            if file_name in exclude_file:
                continue
            file_name = re.sub(r'\d+|_', '', file_name)
            for suffix in include_file:
                if path.endswith(suffix):
                    new_path_dir = os.path.dirname(new_path)
                    new_path_dir = clear_path(new_path_dir)
                    file_name = f'{number}.{clear_path(file_name)}'
                    new_file_path = os.path.join(new_path_dir, f'{file_name}.md')
                    type_mapping = {
                        'py': 'python',
                        'html': 'html',
                        'vue': 'vue',
                    }
                    type_ = type_mapping.get(path.split('.')[-1])
                    with open(cur_path, 'r', encoding='utf8') as f:
                        try:
                            with open(new_file_path, 'w', encoding='utf8') as ff:
                                res = to_md(f.read(), type_, file_name, category, create_time, update_time)
                                ff.write(res['content'])
                            number += 1
                        except Exception as e:
                            print(e)


if __name__ == '__main__':
    old_dir = r'C:\Users\LLL03\Desktop\python\1.python基础(演练)'
    # new_dir = r'C:\Users\LLL03\Desktop\demo'
    new_dir = r'C:\Users\LLL03\Desktop\daydream_oasis\daydream_oasis_front\docs\blog\blog'
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    exclude_dir = {
        '__pycache__', '.idea', '.git', 'images', 'dist', '.vs', 'build', '.vscode', 'cache',
        'node_modules', '项目', 'venv', 'image', 'test', 'AAA', 'fonts', '.ipynb_checkpoints', 'imgs',
        'project-demo', 'scrapy学习', 'tools', '爬取的数据', '全网霉霉图片', '网页模板', 'css', 'js',
        'web开发总结', '后端学习', 'SQLite3数据库', 'video', 'image', 'HAPPY', '程序设计比赛', '数学模型',
        'GitHub的学习', 'TS',
    }
    include_file = ['.py', '.html', '.vue']
    exclude_file = ['caogao', 'demo', 'test', '__init__']
    copy_dir(old_dir, new_dir, include_file, exclude_file, exclude_dir)
