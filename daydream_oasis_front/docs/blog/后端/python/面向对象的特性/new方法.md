---

next: false

---



<BlogInfo id="950"/>

```python
#单例设计模式
#目的：让类创建的对象，在系统中只有唯一的一个实例
#每一次执行类名（）返回的对象，内存地址是相同的
#创建一个类对象
class MusicPlayer(object):

    instance = None

    #初始化设置
    def __init__(self):
        print("播放器初始化.......")

    #__new__是python内置的静态方法
    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")

        #为对象分配空间
        if cls.instance == None:
            cls.instance = super().__new__(cls)

        #返回对象引用
        return cls.instance


#创建多个实例
player1=MusicPlayer()
print(player1)

player2=MusicPlayer()
print(player2)

player3=MusicPlayer()
print(player3)
```



<ActionBox />
