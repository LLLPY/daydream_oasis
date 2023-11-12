---

next: false

---



<BlogInfo id="429"/>

```python
from tkinter import *
from tkinter import messagebox
root=Tk() #根窗口
root.title('Place布局管理')
root.geometry('400x300+500+200')

#创建一个Frame容器
f1=Frame(root,width=200,height=200,bg='blue')
f1.place(relx=0.25,rely=0.2)
def hel():
    messagebox.showinfo('惊喜','送你一朵玫瑰花!')
#在root窗口中添加一个按钮
Button(root,text='点我有惊喜!',command=hel).place(relx=0.4,y=0)
#在容器f1中添加一个按钮
Button(f1,text='点我有惊喜!',command=hel).place(x=50,y=50)
Label(f1,text='你好呀!').place(x=50,y=100,width=60,height=60,anchor='w')
Label(f1,text='你好呀!').place(x=110,y=100,width=60,height=60)


root.mainloop()
```



<ActionBox />
