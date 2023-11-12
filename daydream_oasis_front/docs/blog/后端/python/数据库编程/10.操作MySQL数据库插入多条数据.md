---

next: false

---



<BlogInfo id="705"/>

```python
import pymysql

#创建来接对象
con=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='python_db')

#创建游标对象
cur=con.cursor()
#编写插入的sql语句
sql='''insert into t_student(sname,age,score) values(%s,%s,%s)'''

try:
    #执行插入的sql语句
    cur.executemany(sql,[('Kim',19,89),('jerry',18,78)])
    #事务提交
    con.commit()
    print('数据插入成功!')
except Exception as e:
    print(e)
    #书事务回滚
    con.rollback()
    print('数据插入失败!')
finally:
    con.close()
```



<ActionBox />
