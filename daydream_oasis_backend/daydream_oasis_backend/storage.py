from io import BytesIO

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont


# 添加水印
class WatermarkStorage(FileSystemStorage):

    # 处理逻辑
    def save(self, name, content, max_length=None):
        # 如果是图片且不是gif动图才进行加水印操作
        if 'image' in content.content_type and not str(name).endswith('gif'):

            # 加水印
            image = self.watermark_with_text(content, 'www.lll.plus', 'skyblue')
            content = self.convert_image_to_file(image, name)
        return super().save(name, content, max_length=max_length)

    # 将打上水印后的图片对象转换为文件对象
    def convert_image_to_file(self, image, name):
        temp = BytesIO()
        image.save(temp, format('PNG'))
        file_size = temp.tell()
        return InMemoryUploadedFile(temp, None, name, 'image/png', file_size, None)

    # 打水印
    def watermark_with_text(self, file_obj, text, color, fontfamily=None):
        image = Image.open(file_obj).convert('RGBA')
        draw = ImageDraw.Draw(image)
        width, height = image.size
        margin = 10
        if fontfamily:
            font = ImageFont.truetype(fontfamily, int(height / 10))
        else:
            font = None

        textWidth = draw.textlength(text, font)
        x = (width - textWidth - margin)  # 计算横轴位置
        y = (height - margin)  # 计算纵轴位置

        draw.text((x, y), text, color, font)
        return image
