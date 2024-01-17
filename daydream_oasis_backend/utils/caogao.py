import re

import requests
import hashlib
from PIL import Image
from io import BytesIO
from blog.models import Blog


class ReplaceExternalLinks(object):
    link_pattern = re.compile(r'!\[\]\((http[s]{0,1}://.*)\)')

    def upload(self, f_name, con):
        headers = {
            'cookie': 'auth_token=310a8eab2346e3004fe0dc37765de31754f8e6890ab406ba4edbab94ce2cf155:1rPYWL:Tecy87to3sbJ1AzzImmHDkmknHAMRuRl0dhkMmtZNZ8; expires=Tue, 23 Jan 2024 01:45:41 GMT; Max-Age=604800; Path=/'
                      'content',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0',

        }

        url = 'http://www.lll.plus/api/file/upload/'
        res = requests.post(url, files={'file': (f_name, con, 'image')}, headers=headers)
        return res.json()

    def download(self, url):
        print(f'222222:{url}')
        res = requests.get(url).content
        res = self.compress_image(res, 2 * 1024 * 1024)
        f_name = hashlib.md5(url.encode('utf8')).hexdigest() + '.jpg'
        return f_name, res

    def url_mask(self, match_obj):

        match_str = match_obj.group(0)
        start_idx = match_str.find('http')
        match_str = match_str[start_idx:len(match_str) - 1]
        print(111111, match_str)
        if match_str.startswith('http://www.lll.plus'):
            return match_str
        else:
            res = self.download(match_str)
            res = self.upload(*res)
            print(res)
            return '![](' + res['data']['url'] + ')'

    def run(self):
        li = Blog.objects.all()
        li.reverse()
        for blog in li:
            print(66666,blog.id)
            try:
                content = blog.content
                if re.findall(self.link_pattern, content):
                    content = re.sub(self.link_pattern, self.url_mask, content)
                    blog.content = content
                    blog.save()
                    blog.save_md()
            except Exception as e:
                print(f'{blog.id}错误：e')
    def compress_image(self, input_bytes, max_size):
        image = Image.open(BytesIO(input_bytes))
        image = image.convert("RGB")  # 将图片转换为RGB模式
        output_buffer = BytesIO()
        image.save(output_buffer, format='JPEG', optimize=True, quality=85)  # 初始压缩

        while output_buffer.tell() > max_size:  # 如果图片大小超过指定大小
            output_buffer = BytesIO()
            image.save(output_buffer, format='JPEG', optimize=True, quality=75)  # 降低质量再次压缩

        return output_buffer.getvalue()


if __name__ == '__main__':
    aaa = ReplaceExternalLinks()
    res = aaa.download('https://img-blog.csdnimg.cn/20210713170154954.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70')
    with open('aaa.jpg', 'wb') as f:
        f.write(res[1])