import os
import re
import datetime


def clear_path(path):
    return re.sub(r'\d+_|\d+\.|\(|\)|（|）|%|-|lll', '', path)


def to_md(content, type_, title, category, create_time, update_time):
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
<BlogInfo title="{title}" author="{author}" pv=0 read_times=0 pre_cost_time={pre_cost_time} category="{category}" tag_list="{tag_list}" create_time="{create_time}" update_time="{update_time}" />

```{type_}
{content}
```
'''
    print(content)
    return content


# 把一个目录下的所有文件都转成md格式，并保存到相应的文件夹中
def tree(old_dir, new_dir, file_types):
    number = 1
    # 根据文件的创建时间排序后再获取文件列表
    for path in sorted(os.listdir(old_dir), key=lambda _path: os.stat(os.path.join(old_dir, _path)).st_ctime):

        cur_path = os.path.join(old_dir, path)
        create_time = os.stat(cur_path).st_ctime
        update_time = os.stat(cur_path).st_mtime
        cagegory = clear_path(os.path.dirname(cur_path).split(os.sep)[-1])

        # 判断当前路径是不是目录r
        is_dir = os.path.isdir(cur_path)
        exclude_dir = {'__pycache__', '.idea', '.git', 'images', 'dist', '.vs', 'build', '.vscode', 'cache',
                       'node_modules', '项目', 'venv', 'image', 'test', 'AAA', 'fonts', '.ipynb_checkpoints', 'imgs',
                       'project-demo', 'scrapy学习', 'tools', '爬取的数据', '全网霉霉图片', '网页模板', 'css', 'js', 'imgs', 'web开发总结',
                       '后端学习', 'SQLite3数据库', 'video', 'image', 'HAPPY', '程序设计比赛', '数学模型', 'GitHub的学习', 'TS',
                       }
        new_path = os.path.join(new_dir, path)
        new_path = clear_path(new_path)
        if is_dir and path not in exclude_dir:
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            tree(cur_path, new_path, file_types)
        else:
            file_name = ''.join(path.split('.')[:-1])
            if file_name in ['caogao', 'demo', 'test', '__init__']: continue
            file_name = re.sub(r'\d+|_', '', file_name)
            include_file = ['.py', '.html', '.vue']
            for suffix in include_file:
                if path.endswith(suffix):
                    with open(cur_path, 'r', encoding='utf8') as f:
                        new_path_dir = os.path.dirname(new_path)
                        new_path_dir = clear_path(new_path_dir)
                        file_name = clear_path(file_name)
                        file_name = f'{number}.{file_name}'
                        new_file_path = os.path.join(new_path_dir, f'{file_name}.md')
                        # print(new_file_path)
                        try:
                            with open(new_file_path, 'w', encoding='utf8') as ff:
                                if path.endswith('.py'):
                                    type_ = 'python'
                                elif path.endswith('.html'):
                                    type_ = 'html'
                                elif path.endswith('.vue'):
                                    type_ = 'vue'

                                ff.write(to_md(f.read(), type_, file_name, cagegory, create_time, update_time))
                            number += 1
                        except Exception as e:
                            print(111111, e)


if __name__ == '__main__':
    old_dir = r'C:\Users\LLL03\Desktop\python\1.python基础(演练)'
    # new_dir = r'C:\Users\LLL03\Desktop\demo'
    new_dir = r'C:\Users\LLL03\Desktop\daydream_oasis\daydream_oasis_front\docs\blog\python'
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)

    file_types = set()
    tree(old_dir, new_dir, file_types)
    print(file_types)
