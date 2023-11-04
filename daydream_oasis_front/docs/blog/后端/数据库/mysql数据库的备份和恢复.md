
<BlogInfo id="998" title="mysql数据库的备份和恢复" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="92" category="数据库" tag_list="['mysql', '              备份', '              恢复']" create_time="2023.07.08 00:34:30.326272" update_time="2023.07.08 00:34:30.326287" />

### 前言

> 最近发现租用的轻量应用服务器快要到期了，于是马上就租用了一台新的服务器，至于为什么没有直接续费旧的服务器，有两个主要原因：1.旧的服务器宽带太低了，最高峰值只有5Mbps（也就只有几百k的样子），所以大多数时候网页加载还是有一点延迟的；2.太贵了，之前是通过学生优惠购买的，原价需要1000多，所以还是打算话几百钱买一个便宜点的。

![image.161bb6b01cd811eeb56f1f971a1babd2.png](../../../media/image/2023/07/07/image.161bb6b01cd811eeb56f1f971a1babd2.png)

### 峰值计算

有的小伙伴可能不知道5Mbps是怎么算出的只有几百k的。我这里说明一下：

首先，bps的意思是bit per second，就是每秒多少bit的意思，bit是计算机中处理信息的最小单位，一般情况下，1Byte=8bit。

所以：5Mb = 5×1024K b(it)= 5×1024/8KB=640KB

虽然说计算出来有640KB，但是我在实际使用情况中也就300KB左右的样子，所以还是有点不够用！

### 开始

我的博客系统的所有数据都是存在当前这台服务器的mysql里面的，现在有了新的服务器，所以需要将全部数据进行转移，我记得这不是我第一次进行mysql的数据转移了，因为这已经是我第三次租服务器了，之前也进行了一次数据库的转移，但是，当时也是用的mysql的数据库备份和恢复功能，但是没有成功，因为当时两台服务器的数据库版本不一致，这次我两个mysql的版本都是8.0，所以打算将这个备份和恢复的过程记录一下，也方便以后工作中如果需要的时候能够方便查找到。

其实mysql中进行备份和恢复非常简单，方法也有很多，我这里就介绍一下使用mysqldump这个指令来进行备份和恢复！

#### 备份

mysqldump能够备份单个表，多个表，也能备份单个数据库，多个数据库，以及所有数据库，相关的指令如下：


```shell script
#备份指定的数据表
mysqldump -u username 数据库名 [表名1] [表名2] ... >备份文件名;

#备份指定的数据库
mysqldump -u username 数据库名 > 备份文件名;

#备份所有数据库
mysqldump -u username --all-databases > 备份文件名;
```


#### 实操


```shell script
mysqldump -uroot -p blog_plus > blog_plus.sql
```

![image.fb6ed1941cdc11eeb56f1f971a1babd2.png](../../../media/image/2023/07/07/image.fb6ed1941cdc11eeb56f1f971a1babd2.png)

### 恢复

恢复的操作和备份“相反”，就是将数据从文件恢复到数据库中，命令如下：


```shell script
mysql -u username -p 数据库名 < 恢复的文件名;
```

#### 实操


```python
#新建数据库
mysql -uroot -p
create database blog_plus chatset=utf8mb4;

#恢复
mysql -uroot -p blog_plus < 2023_7_8_blog_plus.sql;
```

##### 1.将备份的文件下载到新的服务器

因为我的博客系统有文件下载的功能，因此我直接将备份的文件copy到了博客系统的指定目录下，在新的服务器上通过wget下载即可；

![image.f738bfe61ce011eeb56f1f971a1babd2.png](../../../media/image/2023/07/08/image.f738bfe61ce011eeb56f1f971a1babd2.png)

##### 2.新建一个同名的数据库

在进行恢复时，如果没有在mysql中建立数据库，在执行恢复操作时会报错，为了和原数据库保持一致，应该在新的服务器上新建一个数据库，并且同原数据库名。

![image.0c8111b81ce211eeb56f1f971a1babd2.png](../../../media/image/2023/07/08/image.0c8111b81ce211eeb56f1f971a1babd2.png)

最后查看数据表发现导入成功！

![image.61ac4e1e1ce211eeb56f1f971a1babd2.png](../../../media/image/2023/07/08/image.61ac4e1e1ce211eeb56f1f971a1babd2.png)

### 结尾

这次的mysql备份和恢复过程比较顺利，一次性都成功了，不过这只是数据，对于整个项目，还有源代码，nginx和uwsgi的配置文件，运行环境等的准备；目前步骤还比较繁琐，希望后续能够写一个一键部署之类的脚本，加油！


