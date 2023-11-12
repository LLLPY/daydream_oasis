---

next: false

---



<BlogInfo id="500"/>

```python
import threading

local = threading.local() #全局变量local

def process_student():
    student_name = local.name
    print('线程的名字:%s 学生的名称:%s'%(threading.current_thread().getName(),student_name))


def process_thread(name):
    local.name = name
    process_student()

if __name__ == '__main__':
    stu1 = threading.Thread(target=process_thread,args=('张三',),name='Thread-A')
    stu2 = threading.Thread(target=process_thread,args=('李四',),name='Thread-B')
    stu1.start()
    stu2.start()
    stu1.join()
    stu2.join()
```



<ActionBox />
