import os
import pprint


def tree(dir):
    res = {'text': dir, 'collapsible': True, 'collapsed': False, 'items': []}

    # 根据文件的创建时间排序后再获取文件列表
    for path in sorted(os.listdir(dir), key=lambda _path: os.stat(os.path.join(dir, _path)).st_ctime):

        cur_path = os.path.join(dir, path)

        # 判断当前路径是不是目录
        is_dir = os.path.isdir(cur_path)
        if is_dir:
            res[path] = tree(cur_path)
        else:
            res['items'].append({'text': path, 'link': cur_path})

    return res


# 使用示例
directory = '.'
tree_dict = tree(directory)
pprint.pprint(tree_dict)
