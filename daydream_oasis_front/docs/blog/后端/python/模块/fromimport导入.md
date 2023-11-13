---

next: false

---



<BlogInfo id="741"/>

```python
from lll01_测试模块1 import say_hello as say1_hello
from  lll02_测试模块2 import say_hello as say2_hello
from  lll01_测试模块1 import Dog
from lll02_测试模块2 import Cat
dog = Dog
print(dog)
cat = Cat
print(cat)
say1_hello()
say2_hello()


#当导入的多个模块中，有相同的工具名时，在使用该工具时，后导入的会覆盖前面导入的
#这时，可以使用 as 关键字给该工具起别名
#再调用不同模块中的工具，就不会出现错误
```



<ActionBox />
