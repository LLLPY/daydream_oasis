---

next: false

---



<BlogInfo id="939"/>

```python
"""
在使用print(对象名)希望在控制台输出自己自定义的内容时，可以使用这个方法
"""

class Cat:

    def __str__(self):

        #注意：必须返回字符窜
        return "我是小猫[%s]"%self.name
    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了"%new_name)

    def __del__(self):
        #在一个对象被“干掉”的时候执行（对象被从内存中删除）
        print("%s bye bye"%self.name)

#tom是一个全局变量
tom = Cat("Tom")
print(tom)
print(tom.name)
#del关键字可以删除一个对象
#一旦del被调用完成，对象的生命周期结束
del tom
print("*" * 50)
#del tom
```



<ActionBox />
