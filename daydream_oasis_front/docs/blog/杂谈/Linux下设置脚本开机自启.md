---

next: false

---



<BlogInfo id="1061"/>

**核心思想:把要启动的脚本放到系统的"服务"目录下,系统在开机,重启时就会运行脚本程序**

### 1.切换到系统目录:/etc/init.d

在终端中执行命令:cd /etc/init.d  
![在这里插入图片描述](https://img-blog.csdnimg.cn/6921f6c21e94460ea06fd1d8d6493bd0.png)

### 2.编辑启动脚本文件

在终端中执行命令:sudo vim testDac(testDac为脚本文件名)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/197dd7addd77482dbafdb042bd74dfa9.png)  
第一行是为了说明该文件为bash脚本  
第二行是为了指定运行级别  
最后一行指定的是需要启动的程序的完整路径  
编辑完成后保存退出

### 3.授权

执行命令:sudo chmod 755 testDac  
![在这里插入图片描述](https://img-blog.csdnimg.cn/35100e8e2b004f2b9c845d43e5ace7a3.png)

### 4.加入开机启动服务列表

执行命令:chkconfig --add testDac  
![在这里插入图片描述](https://img-blog.csdnimg.cn/60df612cca6c4419aefb3fb7e1b16eb5.png)

### 5.查看服务列表,检查是否启动成功

执行命令:chkconfig --list  
![在这里插入图片描述](https://img-blog.csdnimg.cn/11123801d0cb44f2b558e9fa3858fc83.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70)  
如果列表中有你添加的脚本名说明添加成功!(我这里对应最后一行)

### 6.重启测试(查看进程中是否包含脚本程序)

执行命令:ps aux | grep dac(dac是你的程序名)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/e4d4d672909c4fd78d2160f4892c67af.png)  
如果在显示的列表的最后一列中有你的程序的路径(我这里对应的第三行),说明你的程序已经启动,至此,开机自启就实现了!

  


<ActionBox />
