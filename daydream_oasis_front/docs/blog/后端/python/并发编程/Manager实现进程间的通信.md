---

next: false

---



<BlogInfo id="507"/>

```python
import multiprocessing



def func():

    d['name']='autumn'
    l.append('autumn')

    pass




if __name__ == '__main__':
    # multiprocessing.set_start_method()

    with multiprocessing.Manager() as manger:
        d=manger.dict() #创建一个字典数据类型
        l=manger.list() #创建一个列表数据类型

    d['name']='Tom'
    l.append('Tom')
    p=multiprocessing.Process(target=func)
    p.start()
    p.join()

    print(d)
    print(l)














```



<ActionBox />
