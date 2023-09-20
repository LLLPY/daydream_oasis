from rest_framework.decorators import action
from daydream_oasis_backend.config.base import BASE_DIR
import os
from rest_framework import viewsets, mixins
from .serializers import FrontConfigSerializers
from common.drf.response import SucResponse
from utils import tools

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
        return str(path).replace(str(cls.blog_dir.replace('blog','')), '').replace('\\', '/')

    @classmethod
    def tree(cls, dir, start_depth=1, max_depth=5, include_files=['.md', ]):

        res = {'text': cls.clear_preffix(dir), 'collapsible': True, 'collapsed': False, 'items': []}

        # 根据文件的创建时间排序后再获取文件列表
        for path in sorted(os.listdir(dir), key=lambda _path: os.stat(os.path.join(dir, _path)).st_ctime):

            cur_path = os.path.join(dir, path)

            # 判断当前路径是不是目录
            is_dir = os.path.isdir(cur_path)
            if is_dir:
                start_depth += 1
                if start_depth > max_depth: break

                res[cls.clear_preffix(cur_path)] = cls.tree(cur_path, start_depth, max_depth, include_files)
            else:
                for suffix in include_files:
                    # 只添加指定类型的文件
                    if cur_path.endswith(suffix):
                        res['items'].append({'text': path, 'link': cls.clear_preffix(cur_path)})
                        break
        return res

    @action(methods=['get', ], detail=False)
    def get_nav_config(self, request, *args, **kwargs):
        ...

    @action(methods=['get', ], detail=False)
    def get_sidebar_config(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        res = self.tree(self.blog_dir)
        del res['text'], res['collapsible'], res['collapsed'], res['items']
        return SucResponse(data=res)


    # @classmethod
    # def get_markdown(cls):



if __name__ == '__main__':
    for path in os.listdir('.'):
        print(dir(path))
