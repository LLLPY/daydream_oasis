---

next: false

---



<BlogInfo id="1086"/>

```python
from urllib.request import build_opener,Request
from fake_useragent import UserAgent

url = 'http://www.baidu.com'
headers = {'User-Agent':UserAgent().chrome}
request = Request(url,headers=headers)
opner = build_opener()
response = opner.open(request)
contents = response.read().decode()
print(contents)
```



<ActionBox />
