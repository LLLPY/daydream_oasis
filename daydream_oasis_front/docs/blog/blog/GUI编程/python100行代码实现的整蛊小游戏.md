
<BlogInfo title="python100行代码实现的整蛊小游戏" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=167 category="GUI编程" tag_list="['整蛊', '小游戏']" create_time="2022.05.06 21:45:51.882354" update_time="2022.09.15 20:43:00" />

^^^^^^^^^
<p>&nbsp;</p>

<h1><img alt="" src="https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png" style="height:48px; width:48px" /><img alt="" src="https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png" style="height:48px; width:48px" /><img alt="" src="https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png" style="height:48px; width:48px" />话不多说，直接看效果！（程序可在附件中下载）<img alt="" src="https://img-blog.csdnimg.cn/c8c19c7bafeb49958adf6290eba70f89.png" style="height:48px; width:48px" /><img alt="" src="https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png" style="height:48px; width:48px" /><img alt="" src="https://img-blog.csdnimg.cn/9dcbc3fb5daa4d5587a850a87340a456.png" style="height:48px; width:48px" /></h1>

<p>&nbsp;</p>

<p><img src="../media/image/2022/05/06/image-20220506214532-2.png" style="height:1080px; width:900px" /></p>

<p>源码总共有两个文件：Surprise.py和res2.py</p>

<p>Surprise.py的内容如下：</p>

<pre>
<code>from base64 import b64decode
from time import sleep
import tkinter as tk
from random import choice, randrange
from threading import Thread
from playsound import playsound
from res2 import s

#将音乐写入一个临时文件
with open(&#39;bg2.mp3&#39;,&#39;wb&#39;) as f:
    f.write(b64decode(s))

# 播放背景音乐
def playmusic():
    while True:
        playsound(&#39;bg2.mp3&#39;)


def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth() - 200
    height = window.winfo_screenheight()
    a = randrange(0, width)
    b = randrange(0, height)
    window.title(&#39;~SURPRISE~&#39;)
    window.geometry(&quot;200x50&quot; + &quot;+&quot; + str(a) + &quot;+&quot; + str(b))
    contents = [&#39;你是一个傻狍子!&#39;, &#39;你真的很傻!&#39;, &#39;哈哈哈哈哈~~&#39;, &#39;放心,电脑不会死机的~~&#39;, &#39;惊喜还在后面~&#39;,
                &#39;你太可爱了~&#39;, &#39;你太天真了~&#39;, &#39;我都被你秀到了~&#39;]
    a = choice(contents)
    colors = [&#39;#DC143C&#39;, &#39;#FFF0F5&#39;, &#39;#DB7093&#39;, &#39;#FF69B4&#39;, &#39;#FF1493&#39;, &#39;#C71585&#39;, &#39;#DA70D6&#39;, &#39;#D8BFD8&#39;, &#39;#DDA0DD&#39;,
              &#39;#EE82EE&#39;, &#39;#FF00FF&#39;, &#39;#FF00FF&#39;, &#39;#8B008B&#39;, &#39;#800080&#39;, &#39;#BA55D3&#39;, &#39;#9400D3&#39;, &#39;#9932CC&#39;, &#39;#4B0082&#39;,
              &#39;#8A2BE2&#39;, &#39;#9370DB&#39;, &#39;#7B68EE&#39;, &#39;#6A5ACD&#39;, &#39;#483D8B&#39;, &#39;#E6E6FA&#39;, &#39;#F8F8FF&#39;, &#39;#0000FF&#39;, &#39;#0000CD&#39;,
              &#39;#191970&#39;, &#39;#00008B&#39;, &#39;#000080&#39;, &#39;#4169E1&#39;, &#39;#6495ED&#39;, &#39;#B0C4DE&#39;, &#39;#778899&#39;, &#39;#708090&#39;, &#39;#1E90FF&#39;,
              &#39;#F0F8FF&#39;, &#39;#4682B4&#39;, &#39;#87CEFA&#39;, &#39;#87CEEB&#39;, &#39;#00BFFF&#39;, &#39;#ADD8E6&#39;, &#39;#B0E0E6&#39;, &#39;#5F9EA0&#39;, &#39;#F0FFFF&#39;,
              &#39;#E0FFFF&#39;, &#39;#AFEEEE&#39;, &#39;#00FFFF&#39;, &#39;#00FFFF&#39;, &#39;#00CED1&#39;, &#39;#2F4F4F&#39;, &#39;#008B8B&#39;, &#39;#008080&#39;, &#39;#48D1CC&#39;,
              &#39;#20B2AA&#39;, &#39;#40E0D0&#39;, &#39;#7FFFD4&#39;, &#39;#66CDAA&#39;, &#39;#00FA9A&#39;, &#39;#F5FFFA&#39;, &#39;#00FF7F&#39;, &#39;#3CB371&#39;, &#39;#2E8B57&#39;,
              &#39;#F0FFF0&#39;, &#39;#90EE90&#39;, &#39;#98FB98&#39;, &#39;#8FBC8F&#39;, &#39;#32CD32&#39;, &#39;#00FF00&#39;, &#39;#228B22&#39;, &#39;#008000&#39;, &#39;#006400&#39;,
              &#39;#7FFF00&#39;, &#39;#7CFC00&#39;, &#39;#ADFF2F&#39;, &#39;#556B2F&#39;, &#39;#9ACD32&#39;, &#39;#6B8E23&#39;, &#39;#F5F5DC&#39;, &#39;#FAFAD2&#39;, &#39;#FFFFF0&#39;,
              &#39;#FFFFE0&#39;, &#39;#FFFF00&#39;, &#39;#808000&#39;, &#39;#BDB76B&#39;, &#39;#FFFACD&#39;, &#39;#EEE8AA&#39;, &#39;#F0E68C&#39;, &#39;#FFD700&#39;, &#39;#FFF8DC&#39;,
              &#39;#DAA520&#39;, &#39;#B8860B&#39;, &#39;#FFFAF0&#39;, &#39;#FDF5E6&#39;, &#39;#F5DEB3&#39;, &#39;#FFE4B5&#39;, &#39;#FFA500&#39;, &#39;#FFEFD5&#39;, &#39;#FFEBCD&#39;,
              &#39;#FFDEAD&#39;, &#39;#FAEBD7&#39;, &#39;#D2B48C&#39;, &#39;#DEB887&#39;, &#39;#FFE4C4&#39;, &#39;#FF8C00&#39;, &#39;#FAF0E6&#39;, &#39;#CD853F&#39;, &#39;#FFDAB9&#39;,
              &#39;#F4A460&#39;, &#39;#D2691E&#39;, &#39;#8B4513&#39;, &#39;#FFF5EE&#39;, &#39;#A0522D&#39;, &#39;#FFA07A&#39;, &#39;#FF7F50&#39;, &#39;#FF4500&#39;, &#39;#E9967A&#39;,
              &#39;#FF6347&#39;, &#39;#FFE4E1&#39;, &#39;#FA8072&#39;, &#39;#FFFAFA&#39;, &#39;#F08080&#39;, &#39;#BC8F8F&#39;, &#39;#CD5C5C&#39;, &#39;#FF0000&#39;, &#39;#A52A2A&#39;,
              &#39;#B22222&#39;, &#39;#8B0000&#39;, &#39;#800000&#39;, &#39;#FFFFFF&#39;, &#39;#F5F5F5&#39;, &#39;#DCDCDC&#39;, &#39;#D3D3D3&#39;, &#39;#C0C0C0&#39;, &#39;#A9A9A9&#39;,
              &#39;#808080&#39;, &#39;#696969&#39;, &#39;#000000&#39;]
    color = choice(colors)
    try:
        tk.Label(window, text=a, bg=color,
                 font=(&#39;宋体&#39;, 17), width=20, height=4).pack()
    except:
        pass
    window.mainloop()


def last():
    window = tk.Tk()
    window.title(&#39;SURPRISE&#39;)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(str(width) + &quot;x&quot; + str(height) + &quot;00&quot;)
    tk.Label(window, text=&#39;END!!!&#39;, bg=&#39;red&#39;, font=(&#39;黑体&#39;, 30), width=100, height=30).pack()
    window.mainloop()


if __name__ == &#39;__main__&#39;:
    threads = []
    Thread(target=playmusic, daemon=True).start()

    for i in range(1000):
        sleep(0.01)
        t = Thread(target=boom)
        threads.append(t)
        sleep(0.5)
        threads[i].start()

    last()
</code></pre>

<p>res2.py文件是一个资源文件，有点大，链接：<a class="link-info" href="https://download.csdn.net/download/max_LLL/85304148" title="res2.py">res2.py</a></p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><strong>​附件</strong></p><p class="extera_file"><a href="/media/file/2022/09/15/surprise.exe" target="_blank">surprise.exe</a></p>
