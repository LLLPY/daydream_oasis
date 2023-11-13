---

next: false

---



<BlogInfo id="493"/>

```python
import threading
from time import sleep
from multiprocessing import Queue


# 创建线程1
def fun1(q, time):
    print('start:fun1')
    list = [1, 2, 3, 4, 5]
    for i in list:
        print('写入:', i)
        q.put(i)
        sleep(time)
    print('end:fun1')


def fun2(q, time):
    print('start:fun2')
    for i in range(q.qsize()):
        print('读取:', q.get())
        sleep(time)
    print('end:fun2')


if __name__ == '__main__':
    q = Queue(5)
    # 创建线程
    p1 = threading.Thread(target=fun1, name='线程1', args=(q, 1))
    p2 = threading.Thread(target=fun2, args=(q, 1), name='线程2')

    # 启动线程
    p1.start()

    p1.join()

    p2.start()

    # 等待

    p2.join()

    print('over!')
    print('线程1的名字:', p1.getName())
    print('线程2的名字:', p2.getName())
    print('线程1是否还在活动:', p1.is_alive())
    print('线程2是否还在活动:', p2.is_alive())
    p1.setName('fun1')
    print('线程1的新名字叫:', p1.getName())

```



<ActionBox />
