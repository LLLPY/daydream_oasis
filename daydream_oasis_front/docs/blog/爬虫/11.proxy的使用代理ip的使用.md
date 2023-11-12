---

next: false

---



<BlogInfo id="1087"/>

```python
from urllib.request import Request,build_opener,ProxyHandler
from fake_useragent import UserAgent

headers = {
    'User-agent':UserAgent().chrome
}

url = 'http://www.baidu.com'

request = Request(url,headers=headers)

#设置代理ip
hander = ProxyHandler({'http':'51.158.111.242:8811'})     #{'ip类型(http/https)':'(账号):(密码@)IP地址'}
opener = build_opener(hander)
response = opener.open(request)
contents = response.read().decode()

print(contents)
```



<ActionBox />
