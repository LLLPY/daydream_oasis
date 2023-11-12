---

next: false

---



<BlogInfo id="704"/>

```python
# SQLite3数据库操作的基本流程
''':cvar
1.导入相关库或模块
2.使用connect()连接数据库并获得数据库连接对象
3.使用con.cursor()获取游标对象 (con为连接对象)
4.使用游标对象的方法来操作数据库(实现插入修改删除)
5.使用close()方法关闭游标对象和数据库连接，减小数据库服务器的压力

'''

# 1.导入相关库
import sqlite3

# 2.创建连接 (connect()方法中有两个常用的参数:database,数据的文件目录 timeout,访问数据的超时设定)
con = sqlite3.connect('C:/Users/LLL/Desktop/python/python基础(演练)/数据库编程/SQLite3数据库/demo1.db')
# 判断是否连接成功
print(con)

# 3.创建游标对象
cur = con.cursor()
# 编写创建表的sql语句
sql = '''create table t_person(
        pno INTEGER primary key autoincrement,
        pname VARCHAR not null,
        age INTEGER
        )'''
# 4.使用游标对象提供的方法来操作数据库
# 执行sql
try:
    cur.execute(sql)
    print('创建表成功!')
except Exception as result:
    print(result)
    print('创建表失败!')
finally:
    # 5.关闭游标对象和数据库连接
    cur.close()
    con.close()

```



<ActionBox />
