---

next: false

---



<BlogInfo id="707"/>

```python
import pymysql

con=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='python_db')
cur=con.cursor()

sql='update t_student set sname=%s where sno=%s' #修改指定sno的sname的值
try:
    cur.execute(sql,('Nobody',1))
    con.commit()
    print('数据修改成功!')
except Exception as e:
    print(e)
    con.rollback()
    print('数据修改失败!')
finally:
    con.close()
```



<ActionBox />
