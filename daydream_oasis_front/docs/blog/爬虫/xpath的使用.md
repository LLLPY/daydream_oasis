---

next: false

---



<BlogInfo id="1105"/>

```python
from lxml import etree
from fake_useragent import UserAgent
import requests

headers = {
    'User-agent':UserAgent().chrome
}
url = 'https://www.qidian.com/rank/yuepiao?style=1'

response = requests.get(url,headers=headers)
contents = response.text


e = etree.HTML(contents)
str = etree.tostring(e).decode()
print(str)

```



<ActionBox />
