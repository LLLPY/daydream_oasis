---

next: false

---



<BlogInfo id="1100"/>

```python
#图像识别 -- 识别二维码
import pytesseract
from PIL import Image

#打开要识别的图片
imag = Image.open('code.png')
#识别图片中的文字信息
imag_str = pytesseract.image_to_string(imag)
print(imag_str)
```



<ActionBox />
