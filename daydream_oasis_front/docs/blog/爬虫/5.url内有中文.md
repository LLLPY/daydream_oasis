---

next: false

---



<BlogInfo id="1122"/>

```python
from urllib.request import Request,urlopen
from urllib.parse import quote
url = 'https://cn.bing.com/search?q=%E5%B0%9A%E5%AD%A6%E5%A0%82&PC=U316&FORM=CHROMN' #当url中含有中文时，会提示url格式错误，需对其进行转码
#url = 'https://cn.bing.com/search?q={}&PC=U316&FORM=CHROMN',format(quote('尚学堂'))


headers = {

    'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
}

request = Request(url,headers=headers)

response = urlopen(request)

print(response.read().decode())
```



<ActionBox />
