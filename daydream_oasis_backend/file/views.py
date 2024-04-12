import uuid

from rest_framework import viewsets
from rest_framework.decorators import action

from common.drf.decorators import login_required
from common.drf.response import ErrResponse, SucResponse
from file.models import File
from utils import tools


class FileViewSet(viewsets.ModelViewSet):

    # 图片上传服务
    @action(methods=['post'], detail=False)
    @login_required
    def upload(self, request, *args, **kwargs):
        file = request.FILES.get('file') or request.FILES.get('file[]')

        content_type = file.content_type.split('/')[0]
        content_type = 'other' if content_type in ['', 'application'] else content_type
        # 1.图片的大小限制在2M以内
        # 2.视频的大小限制在200M以内
        # 3.音频的大小限制在50M以内
        # 4.文档的大小限制在20M以内
        # 5.其他的大小限制在200M以内
        if file.size > File.type_size_dict[content_type][0] * File.MB:
            return ErrResponse(message=f'上传失败,{content_type}最大支持{File.type_size_dict[content_type][0]}MB！')

        # 基于时间戳的uuid，防止文件重名
        uid = uuid.uuid1()
        filename_list = file.name.rsplit('.', 1)
        filename_list.insert(1, uid.hex)
        filename = '.'.join(filename_list)
        file.name = filename
        file = File.create(request.user, File.type_size_dict[content_type][1], file)

        data = {
            'filename': filename,
            'content_type': content_type,
            'url': tools.get_full_media_url(file.path)
        }
        return SucResponse(data=data)
