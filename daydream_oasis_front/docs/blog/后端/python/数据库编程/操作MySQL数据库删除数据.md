---

next: false

---



<BlogInfo id="708"/>

```python
import pymysql

con=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='python_db')
cur=con.cursor()
sql='delete from t_student where sname=%s'
try:
    cur.execute(sql,('Kim',))
    con.commit()
    print('数据删除成功!')
except Exception as e:
    print(e)
    con.rollback()
    print('数据删除失败!')
finally:
    con.close()
```



<ActionBox />
