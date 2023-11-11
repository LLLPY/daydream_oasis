---

next: false

---



<BlogInfo id="447" title="python100行代码实现的整蛊小游戏" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="167" category="GUI编程" tag_list="['整蛊', '              小游戏']" create_time="2022.05.06 21:45:51.882354" update_time="2022.09.15 20:43:00" />



![](https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png)
![](https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png)
![](https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png)
话不多说，直接看效果！（程序可在附件中下载）
![](https://img-blog.csdnimg.cn/c8c19c7bafeb49958adf6290eba70f89.png)
![](https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png)
![](https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png)

![](http://www.lll.plus/media/image/2022/05/06/image-20220506214532-2.png)

源码总共有两个文件：Surprise.py和res2.py

Surprise.py的内容如下：


```python
from base64 import b64decode
from time import sleep
import tkinter as tk
from random import choice, randrange
from threading import Thread
from playsound import playsound
from res2 import s

#将音乐写入一个临时文件
with open('bg2.mp3','wb') as f:
    f.write(b64decode(s))

# 播放背景音乐
def playmusic():
    while True:
        playsound('bg2.mp3')


def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth() - 200
    height = window.winfo_screenheight()
    a = randrange(0, width)
    b = randrange(0, height)
    window.title('~SURPRISE~')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    contents = ['你是一个傻狍子!', '你真的很傻!', '哈哈哈哈哈~~', '放心,电脑不会死机的~~', '惊喜还在后面~',
                '你太可爱了~', '你太天真了~', '我都被你秀到了~']
    a = choice(contents)
    colors = ['#DC143C', '#FFF0F5', '#DB7093', '#FF69B4', '#FF1493', '#C71585', '#DA70D6', '#D8BFD8', '#DDA0DD',
              '#EE82EE', '#FF00FF', '#FF00FF', '#8B008B', '#800080', '#BA55D3', '#9400D3', '#9932CC', '#4B0082',
              '#8A2BE2', '#9370DB', '#7B68EE', '#6A5ACD', '#483D8B', '#E6E6FA', '#F8F8FF', '#0000FF', '#0000CD',
              '#191970', '#00008B', '#000080', '#4169E1', '#6495ED', '#B0C4DE', '#778899', '#708090', '#1E90FF',
              '#F0F8FF', '#4682B4', '#87CEFA', '#87CEEB', '#00BFFF', '#ADD8E6', '#B0E0E6', '#5F9EA0', '#F0FFFF',
              '#E0FFFF', '#AFEEEE', '#00FFFF', '#00FFFF', '#00CED1', '#2F4F4F', '#008B8B', '#008080', '#48D1CC',
              '#20B2AA', '#40E0D0', '#7FFFD4', '#66CDAA', '#00FA9A', '#F5FFFA', '#00FF7F', '#3CB371', '#2E8B57',
              '#F0FFF0', '#90EE90', '#98FB98', '#8FBC8F', '#32CD32', '#00FF00', '#228B22', '#008000', '#006400',
              '#7FFF00', '#7CFC00', '#ADFF2F', '#556B2F', '#9ACD32', '#6B8E23', '#F5F5DC', '#FAFAD2', '#FFFFF0',
              '#FFFFE0', '#FFFF00', '#808000', '#BDB76B', '#FFFACD', '#EEE8AA', '#F0E68C', '#FFD700', '#FFF8DC',
              '#DAA520', '#B8860B', '#FFFAF0', '#FDF5E6', '#F5DEB3', '#FFE4B5', '#FFA500', '#FFEFD5', '#FFEBCD',
              '#FFDEAD', '#FAEBD7', '#D2B48C', '#DEB887', '#FFE4C4', '#FF8C00', '#FAF0E6', '#CD853F', '#FFDAB9',
              '#F4A460', '#D2691E', '#8B4513', '#FFF5EE', '#A0522D', '#FFA07A', '#FF7F50', '#FF4500', '#E9967A',
              '#FF6347', '#FFE4E1', '#FA8072', '#FFFAFA', '#F08080', '#BC8F8F', '#CD5C5C', '#FF0000', '#A52A2A',
              '#B22222', '#8B0000', '#800000', '#FFFFFF', '#F5F5F5', '#DCDCDC', '#D3D3D3', '#C0C0C0', '#A9A9A9',
              '#808080', '#696969', '#000000']
    color = choice(colors)
    try:
        tk.Label(window, text=a, bg=color,
                 font=('宋体', 17), width=20, height=4).pack()
    except:
        pass
    window.mainloop()


def last():
    window = tk.Tk()
    window.title('SURPRISE')
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(str(width) + "x" + str(height) + "00")
    tk.Label(window, text='END!!!', bg='red', font=('黑体', 30), width=100, height=30).pack()
    window.mainloop()


if __name__ == '__main__':
    threads = []
    Thread(target=playmusic, daemon=True).start()

    for i in range(1000):
        sleep(0.01)
        t = Thread(target=boom)
        threads.append(t)
        sleep(0.5)
        threads[i].start()

    last()
```

res2.py文件是一个资源文件，有点大，链接：[res2.py](https://download.csdn.net/download/max_LLL/85304148
"res2.py")

**​附件**
[surprise.exe](http://www.lll.plus/media/file/2022/09/15/surprise.exe)





<ActionBox />
