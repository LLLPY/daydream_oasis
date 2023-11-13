---

next: false

---



<BlogInfo id="433"/>

```python
from tkinter import *

root=Tk();root.title('Scale');root.geometry('800x300+500+200')

#设置一个标签
l1=Label(root,text='好好学习,天天向上!',bg='black',fg='white')
l1.place(relx=0.1,rely=0.4)
def test1(value):
    print('滑块的值:',value)
    newFont=('宋体',value)
    l1.config(font=newFont) #重新配置字体和字体的大小

#from_:最小值 to:最大值 length:滑块我的长度 tickinterval:刻度(间隔) orient=HORIZONTAL:让滑动条是水平的(默认是垂直的)
s1=Scale(root,from_=10,to=50,length=200,tickinterval=10,orient=HORIZONTAL,command=test1)
s1.set(20) #初始值设为20
s1.place(relx=0.3,rely=0.8)

root.mainloop()
```



<ActionBox />
