---

next: false

---



<BlogInfo id="1090"/>

```python
from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

#用于错误查找和判断
url = 'http://www.baidu.com'
headers = {
    'User-agent':UserAgent().chrome
}
try:
    request = Request(url,headers=headers)
    response = urlopen(request)
    contents = response.read().decode()
    print(contents)
except URLError as result:
    print(result)
    if result.args == ():
        print('服务器错误!,403错误码:11001')
    else:
        print('地址错误!404')

```



<ActionBox />
