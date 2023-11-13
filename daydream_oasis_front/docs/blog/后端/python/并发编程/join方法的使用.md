---

next: false

---



<BlogInfo id="512"/>

```python
from multiprocessing import Process
from time import sleep


def run_test(name,thinking):
    print('子进程开始...')
    print('我的小名叫(思考中).....')
    sleep(thinking)
    print('',name)
    print('子进程结束...')

'''
if __name__ == '__main__':
    print('主进程开始....')
    ti = int(input('您希望电脑思考几秒回答你:'))
    p = Process(target=run_test,args=('小明',ti))

    print('子进程调用start方法')
    p.start()

    # 希望以下的语句在子进程运行完再输出，可以使用sleep，让主进程休息的时间比子进程休息的时间长即可
    sleep(ti + 0.1)
    print('主进程结束...')
'''

if __name__ == '__main__':
    print('主进程开始....')
    print('创建子进程实例对象....')
    ti = int(input('您希望电脑思考几秒回答你:'))
    p = Process(target=run_test,args=('小明',ti),name='小小明')
    print('调用子进程。。。')
    p.start()

    #主进程等待子进程的结束，再执行子进程以下的主进程中的语句
    p.join()
    #同时可以传入一个参数，设置等待时间的上限:如果超过这个时间，即使子进程还没有运行结束，主进程任然会运行子进程以下的主进程中的语句
    print('主进程结束....')
    print('子进程的别名是:',p.name)
    print('%s的ID是:%d'%(p.name,p.pid))






```



<ActionBox />
