---

next: false

---



<BlogInfo id="809"/>

```python
# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2022/7/13 15:49  
from collections import abc
from keyword import iskeyword


class FrozenJSON:

    def __init__(self, mapping: abc.Mapping):

        self.__data = {}
        for k, v in mapping.items():

            if not k.isidentifier():  # 如果key不是一个合格python标识符就直接抛出异常
                raise KeyError(f'{k} is not a valid identifier.')

            if iskeyword(k):  # 如果key是关键字就在它的后面加一个下划线
                k += '_'

            self.__data[k] = v

    def __getattr__(self, item):
        if hasattr(self.__data, item):  # 如果有这个属性，就直接返回属性值
            return getattr(self.__data, item)
        else:
            return FrozenJSON.build(self.__data[item])  # 否则调用build方法

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):  # 如果是映射对象，将其转成FrozenJSON对象再返回
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):  # 如果是序列对象，将序列中的每一个对象转成RrozenJSON对象后再返回
            return [cls.build(item) for item in obj]
        else:
            return obj  # 如果既不是映射也不是序列就直接返回这个对象

    def __repr__(self):
        s = ''
        for k, v in self.__data.items():
            s += f'{k}:{v},'
        return s

    # def


if __name__ == '__main__':
    a = {
        'a': '1',
        'b': [{'hello': 'world'}],
        'c': {'bye': 'byebye'}
    }

    a_frozen_json = FrozenJSON(a)
    print(a_frozen_json.b[0])

    print(a_frozen_json.keys())

```



<ActionBox />
