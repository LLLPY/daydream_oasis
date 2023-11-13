---

next: false

---



<BlogInfo id="717"/>

```python
import pymysql

#创建连接对象
# con=pymysql.connect(host='171.41.9.122',user='root',password='12345',database='python_db',port=3306)
con = pymysql.connect(host='121.199.23.213', port=3306, user='test1', password='123456', database='	test1')

#创建游标对象
cur=con.cursor()

#编写创建表的sql语句
sql=''' create table t_student(
        sno int primary key auto_increment,
        sname varchar(30) not null,
        age int(2),
        score float(3,1)) 
        '''
try:
    #执行创建表的sql语句
    cur.execute(sql)
    print('创建表成功!')
except Exception as r:
    print(r)
    print('创建表失败!')
finally:
    #关闭数据库的连接
    con.close()
```



<ActionBox />
