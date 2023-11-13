---

next: false

---



<BlogInfo id="938"/>

```python
class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了"%new_name)

    def __del__(self):
        #在一个对象被“干掉”的时候执行（对象被从内存中删除）
        print("%s bye bye"%self.name)

#tom是一个全局变量
tom = Cat("Tom")
print(tom.name)
#del关键字可以删除一个对象
#一旦del被调用完成，对象的生命周期结束
tom.__del__()
print("*" * 50)
#del tom
```



<ActionBox />
