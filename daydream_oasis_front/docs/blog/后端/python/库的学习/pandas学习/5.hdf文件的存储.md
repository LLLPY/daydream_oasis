---

next: false

---



<BlogInfo id="589"/>

```python
import pandas as pd

''':cvar
HDF5文件的读取和存储需要指定一个键,值为要存储的DataFrame
pandas.read_hdf(path_or_buf,key=None,**kwargs)

    从h5文件中读取数据
    .path_or_buf:文件路径
    .key:读取的键
'''

#一般情况下 读取hdf5文件需要依赖tables库 可以先提前安装好 pip install tables

data=pd.read_hdf('')

#存储文件
data.to_hdf(path_or_buf='',key='123')

#再次读取的时候,需要指定键的名字
new_data=pd.read_hdf('',key='123')


#注意:
'''
优先选择使用hdf5文件存储
.hdf5在存储的时候支持压缩,使用的方式是blosc,这个是速度最快也是pandas默认支持的
.使用压缩可以提高磁盘的利用率,节省空间
.hdf5还是跨平台的,可以轻松迁移到Hadoop上面

'''
```



<ActionBox />
