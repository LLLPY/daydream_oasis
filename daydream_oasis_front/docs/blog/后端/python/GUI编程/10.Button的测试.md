---

next: false

---



<BlogInfo id="418"/>

```python
from tkinter import *
from tkinter import messagebox

#定义一个Application类，继承自Frame
class Application(Frame):

    #初始化
    def __init__(self,master=None):

        #调用父类方法
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    #定义创建组件的方法
    def createWidget(self):
        # anchor=SW : 文本的位置:西南方
        self.button1=Button(self,text='登录',command=self.denlu,anchor=SW,width=30,heigh=10)
        self.button1.pack()

    def denlu(self):
        messagebox.showinfo('登录','登录成功!')

if __name__ == '__main__':
    root=Tk()
    root.title('登录界面')
    root.geometry('400x300+500+250')
    #创建对象
    app=Application(root)
    #进入事件循环状态
    app.mainloop()
```



<ActionBox />
