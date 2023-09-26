from rest_framework.decorators import action
from daydream_oasis_backend.config.base import BASE_DIR
import os
from rest_framework import viewsets, mixins
from .serializers import FrontConfigSerializers
from common.drf.response import SucResponse
from utils import tools
import re
from utils.cache import cache

# @tools.action_log()
class FrontConfigViewSet(viewsets.GenericViewSet, mixins.DestroyModelMixin):
    '''前端配置的接口'''

    # queryset = None
    serializer_class = FrontConfigSerializers

    # 博客的绝对路径
    blog_dir = os.path.join(BASE_DIR, '..', 'daydream_oasis_front', 'docs', 'blog')

    @classmethod
    def clear_preffix(cls, path):
        '''清理掉路径的前缀'''
        return str(path).replace(str(cls.blog_dir).replace('blog', ''), '').replace('\\', '/')

    @classmethod
    def format_dir_path(cls, path):
        path = path.strip('/')
        return f'/{path}/'

    @classmethod
    def tree(cls, dir, start_depth=1, max_depth=5, include_files=['.md', ], exclude_files=['index.md']):

        res = {'text': cls.clear_preffix(dir).split('/')[-1], 'collapsible': True, 'collapsed': False, 'items': []}
        # start_depth += 1
        # if start_depth > max_depth: return res
        # 根据文件的创建时间排序后再获取文件列表
        for path in sorted(os.listdir(dir), key=lambda _path: os.stat(os.path.join(dir, _path)).st_ctime):

            cur_path = os.path.join(dir, path)

            # 判断当前路径是不是目录
            is_dir = os.path.isdir(cur_path)
            if is_dir:
                res['items'].append(cls.tree(cur_path, start_depth, max_depth, include_files, exclude_files))
            else:
                for suffix in include_files:
                    # 只添加指定类型的文件
                    if cur_path.endswith(suffix) and path.strip('/') not in exclude_files:
                        res['items'].append({'text': path.replace('.md', ''), 'link': cls.clear_preffix(cur_path)})
                        break
        return res

    @action(methods=['get', ], detail=False)
    def get_nav_config(self, request, *args, **kwargs):
        ...

    @classmethod
    def sorted_list(cls, data):
        '''对文件名进行排序'''
        data.sort(key=lambda item: chr(int(re.match(r'\d+', item['text']).group())) if re.match(r'\d+', item['text']) else item['text'])
        for item in data:
            if item.get('items'):
                cls.sorted_list(item.get('items'))
        return data


    @action(methods=['get', ], detail=False)
    @cache(30)
    def get_sidebar_config(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        res = self.tree(self.blog_dir)['items']
        res = self.sorted_list(res)
        return SucResponse(data=res)



if __name__ == '__main__':
    for path in os.listdir('.'):
        print(dir(path))
