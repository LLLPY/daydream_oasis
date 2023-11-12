---

next: false

---



<BlogInfo id="529"/>

> 摸鱼之余，跟着官方文档把协程这块过了一下。


### 体验协程


```python
import asyncio
import time
    

async def say_afeter(delay,msg):
    await asyncio.sleep(delay)
    print(msg)



async def test():
    start=time.time()    
    await say_afeter(1,'hello world')
    await say_afeter(2,'hello python')
    end =time.time()
    print('execute cost %f'%(end- start))


if __name__=="__main__":
    asyncio.run(test())
```


![](https://img-blog.csdnimg.cn/61b96ef8afaf4288a1ec1929b51e9481.png)



### create_task并发执行

```python
import asyncio
from time import sleep,time
from turtle import st

async def say_after(delay,words):
    await asyncio.sleep(delay)
    print(words)



async def test():
    
    start=time()
    task1=asyncio.create_task(say_after(1,'hello world'))
    task2=asyncio.create_task(say_after(2,'hello python'))    
    mid=time()
    await task1
    await task2
    end=time()
    #使用create_task后，task1和task2并发运行，从耗时结果也可以看到，task1和task2总共耗时2s左右
    print('execute cost %f --- %f'%(mid-start,end-start)) 
    



if __name__ == '__main__':
    asyncio.run(test())
```

![](https://img-blog.csdnimg.cn/0ea645b466854337af64eabfc1cf5524.png)

### 可等待对象

```python
import asyncio
from operator import ne



#可等待对象
'''
如果一个对象可以在await语句中使用，那么它就是可等待对象。
可等待的对象有三种类型：
    1.协程
    2.任务
    3.Future


#协程
    1.协程函数：使用async定义的函数被称为协程函数
    2.协程对象：协程函数返回的对象就是协程对象

#任务
    通过asyncio.create_task(async fun)可以将一个协程函数func转成一个任务，任务会被自动调度执行

#Future
    1.Future是一种特殊的低层级可等待对象，表示一个异步操作的最终结果。
    2.当一个Future对象被等待，这意味着协程将保持等待直到该Future对象在其他地方的操作完毕。
    3.通常情况下，没有必要在应用层面创建Future对象



'''



#协程
async def nested():
    for i in  range(10):
        print('hello python!')
    return 200



async def test():
    
    
    #协程
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested() #仅仅调用协程函数，而不使用await关键字，它是不会被执行的
    
    print(await nested())
    
    
    
    #task
    '''
    通过create_task将协程函数封装成任务后，它会被自动调度执行
    '''
    task=asyncio.create_task(nested())
    print(type(task),task)
    #在这里可以取消任务
    # task.cancel()
    
    
    
    await task #可以使用await关键字等待任务被执行完成后再继后面的任务
    
    print('task之后的代码被执行了！！！！')
    
    
    
    #Future
    
    
    
    
    

if __name__ == '__main__':
    asyncio.run(test())
```


![](https://img-blog.csdnimg.cn/536a2fb0b5ce4c818ab1ab5c90b1aa5d.png)

### 运行asyncio程序


```python
import asyncio

async def say_hello():
    print('hello python!')

async def test():
    await say_hello()
    
    #下面这条语句会执行失败，因为在一个asyncio事件循环内部不能有其他的asyncio事件循环
    # asyncio.run(say_hello())
    
    return 'coroutine done!'

    
if  __name__ == '__main__':


    #asyncio.run(coro,*,debug=False)  
    '''
        1.执行coroutine coro并返回结果
        2.run函数会执行传入的协程，负责管理asyncio事件循环，终结异步生成器，关闭线程池等。
        3.当有其他的asyncio事件循环在同一个线程中运行时，不能调用它。
        4.如果debug=True，将以调试模式运行
        5.run函数总是会创建一个新的事件循环并在结束的时候关闭它，它应当被当作asyncio程序的主入口点，理想情况下应当只被调用一次
    
    '''
    res=asyncio.run(test())
    print(res)

```

![](https://img-blog.csdnimg.cn/1e4caa1c240e415f9276a24f8d5b73d1.png)

### 创建任务


```python
import asyncio
from secrets import randbelow


async def say_hello():
    print('hello world!')


def done(task):
    print(1111,task)


async def test():
    task=asyncio.create_task(say_hello())
    await task
    #asyncio.create_task(coro,*,name=None)
    '''
         将coro封装成一个Task并调度其执行。
         name：为Task设定名称，同时可以使用Task.set_name()来设定
    
    '''    
    
    task.set_name('say hello!')
    print(task.get_name())
    
    
    
    
    background_tasks=set()
    for i in range(10):
        task=asyncio.create_task(say_hello())
        
        background_tasks.add(task)  
        
        task.add_done_callback(background_tasks.discard)
        # task.add_done_callback(done)
        
        await task #等待task执行完成
        
    
    print(background_tasks)
        



if __name__ == '__main__':
    asyncio.run(test())
```

![](https://img-blog.csdnimg.cn/fea94cd985784f5aaf040a91e9d7ef78.png)

### sleep休眠


```python
import asyncio
import datetime

async def say_delay(delay,words):
    
    #阻塞一秒后返回一个打印函数
    say=await asyncio.sleep(delay,lambda a:print(a))
    
    say(words)
    #asyncio.sleep(delay,result=None)
    '''
        1.delay指定阻塞的秒数。
        2.如果指定了result，则当协程完成时将其返回给调用者
        3.sleep()总会挂起当前任务，以允许其他任务执行。
        4.将delay设为0将提供一个经优化的路径以允许其他任务运行。这可供长期间运行的函数以避免
          在函数调用的全程中阻塞事件循环。
    '''
    
    
#程序运行 n s，每秒打印当前日期
async def show_date_in_time(n):
    loop=asyncio.get_running_loop()
    end=loop.time()+n
    while True:
        if loop.time()>end:break
        
        print(datetime.datetime.now())  

        await asyncio.sleep(1)
        
        
        
async def test():
    await say_delay(1,'hello world!')
    await show_date_in_time(5)
    
    
    

if __name__ == '__main__':
    asyncio.run(test())
```

![](https://img-blog.csdnimg.cn/a0d0c4a26ddf450489146f00a55f48f0.png)





<ActionBox />
