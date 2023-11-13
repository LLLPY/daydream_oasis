---

next: false

---



<BlogInfo id="1092"/>

```python
from requests import *
from fake_useragent import UserAgent

headers = {
    'User-agent':UserAgent().chrome
}

url = ''

form_data = {
    'uesr':'账号',
    'password':'密码'
}
#无需对form_data进行转码
response = post(url,data=form_data,headers=headers)
contents = response.text
print(contents)
```



<ActionBox />
