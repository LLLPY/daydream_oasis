---

next: false

---



<BlogInfo id="711"/>

```python
#导入模块
import sqlite3

#创建连接
con=sqlite3.connect('C:/Users/LLL/Desktop/python/python基础(演练)/数据库编程/SQLite3数据库/demo1.db')

#创建游标对象
cur=con.cursor()
#编写插入sql语句
sql='insert into t_person(pname,age) values(?,?)'
try:#插入可能成功可能失败
    #执行sql插入一条数据
    cur.execute(sql,('张三',17))
    #提交事务
    con.commit()
    print('插入数据成功!')
except Exception as r:
    print(r)
    #事务回滚
    con.rollback()
    print('数据插入失败!')
finally:
    #关闭游标对象
    cur.close()
    #关闭数据库连接
    con.close()
```



<ActionBox />
