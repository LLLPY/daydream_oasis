---

next: false

---



<BlogInfo id="427"/>

```python
from tkinter import *

button1_text = ('经典乐', '重金属', '日本风', '中国风', '流行风')
root = Tk()
root.title('钢琴按键的实现')
# f1为第一矩形区域，用来放置音乐的类型
f1 = Frame(root)  # 将和放置到根窗口中
f1.pack()
f2 = Frame(root)
f2.pack()
# 放置5个音乐类型按钮在f1中
for i in button1_text:
    Button(f1, text=i).pack(side='left', padx=10)  # 组件之间的横向间隔设为10
# 设置20个按键
for i in range(20):
    Button(f2, bg='black' if i % 2 == 0 else 'white', height=10, width=5, borderwidth=2, padx=1).pack(side='left')

root.mainloop()

```



<ActionBox />
