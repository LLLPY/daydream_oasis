---

next: false

---



<BlogInfo id="590"/>

```python
import pandas as pd

'''
pandas.read_json(path_or_buf=None,orient=None,typ='frame',lines=False)
    orient
'''

# 读取json
data = pd.read_json('data.json', orient='records', lines=False)
print(data)

# 保存json orient:指定json文件的存储格式,可选参数有:split records index columns values
data.to_json('demo3.json', orient='records', lines=True)
#lines:是否存储在多行 默认lines=False是存储在一行
```



<ActionBox />
