---

next: false

---



<BlogInfo id="382"/>


## **首先得隆重介绍一下nginx**

![](http://www.lll.plus/media/image/2022/01/25/image-20220125144628-1.png)

[_Nginx_  (engine x)是一个高性能的HTTP和反向代理web服务器，同时也提供了IMAP/POP3/SMTP服务。Nginx是由伊戈尔*赛索耶夫为俄罗斯访问量第二的Rambler.ru站点（俄文：Рамблер）开发的，第一个公开版本0.1.0发布于2004年10月4日。](https://baike.baidu.com/item/nginx/3817705?fr=aladdin)
[其将源代码以类BSD许可证的形式发布，因它的稳定性、丰富的功能集、简单的配置文件和低系统资源的消耗而闻名。2011年6月1日，nginx1.0.4发布。](https://baike.baidu.com/item/nginx/3817705?fr=aladdin)
[Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，在BSD-like协议下发行。其特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。](https://baike.baidu.com/item/nginx/3817705?fr=aladdin)

总结一下： **高性能，高稳定，低消耗，轻量级，占内存少，负载均衡**...优点太多就不一一介绍了！

一句话：牛逼！![](http://www.lll.plus/media/image/2022/01/25/image-20220125150008-2.gif)

亲身感受，在本站使用nginx提供静态文件服务后，发现性能真的提升了不少，之前加载完首页至少得5678s，现在应该不要3s，你们要是不信，可以亲自体会，链接放这里了：[0318-SPACE](http://www.lll.plus/)

![](http://www.lll.plus/media/image/2022/01/25/image-20220125151211-3.png)

有图有真相！![](http://www.lll.plus/media/image/2022/01/25/image-20220125151227-4.gif)![](http://www.lll.plus/media/image/2022/01/25/image-20220125151227-4.gif)![](http://www.lll.plus/media/image/2022/01/25/image-20220125151227-4.gif)



## **再看看nginx，uwsgi和django之间是怎么工作的！**

先说说我个人的理解吧，我根据我在配置中所得到的见解是这样的：首先我配置了nginx文件，之后配置了我项目的一个nginx配置文件，其中有一项配置是![](http://www.lll.plus/media/image/2022/01/25/image-20220125151837-5.png)，可以看到配置为listen
80，就是监听80这个端口（如果希望别人能访问到，这个端口是需要对外暴露的，所以不要忘记添加到安全组了！），也就是nginx在启动后会监听这个端口，那监听到的事务谁来处理呢？

继续看配置：

![](http://www.lll.plus/media/image/2022/01/25/image-20220125152511-6.png)

这里就是和uwsgi相关的配置了，(这里location就相当于路由中的定位 location / 就相当于你的域名（ip）+端口+/，  location
/static/就相当于域名（ip）+端口+/static/)，那么就是说，如果访问根目录，对应的规则就交给uwsgi来处理，这个地方就相当于nginx和uwsgi连通的配置接口了！

include uwsgi_params;这个是固定写法，如果你要使用uwsgi的话（uwsgi_params文件中包含了使用uwsgi的相关配置）

![](http://www.lll.plus/media/image/2022/01/25/image-20220125153537-7.png)

uwsgi_pass:127.0.0.1:180801 表示放行这个端口，换句话说location
/下的事情就交给127.0.0.1：18081这个端口对应的进程来处理了，也就是uwsgi来处理了！

再看看uwsgi的配置文件：

![](http://www.lll.plus/media/image/2022/01/25/image-20220125154231-8.png)

这个配置文件就不重点解说了，里面基本上每一行我都写入注释的，需要注意的就是chdir和uwsgi.ini文件之间的位置要搞清楚！

用一张图来描绘它们三者之间的关系应该就是下面这样的：

![](http://www.lll.plus/media/image/2022/01/25/image-20220125160251-9.png)


## **最后看看具体的配置过程吧！**

我使用的设备是Ubuntu 18.04.5 LTS x86_64(Py3.7.8)

## 1.下载
```shell script
下载nginx:sudo apt install nginx
下载uwsgi：pip install uwsgi

```

## 2.配置uwsgi.ini

准备工作做好之后，先来配置uwsgi吧！uwsgi.ini的配置文件如下：

```shell script
[uwsgi]  
#使用nginx连接时使用  
socket=127.0.0.1:18081  
#直接做web服务器使用  
#http=0.0.0.0:80

chdir=/MyBlog  
#项目中wsgi.py文件的目录，相对于项目目录  
wsgi-file=MyBlog/wsgi.py  
# 指定启动的工作进程数  
processes=8  
# 指定工作进程中的线程数  
threads=16  
master=True  
# 保存启动之后主进程的pid  
pidfile=uwsgi.pid  
# 设置uwsgi后台运行，用uwsgi.log保存日志信息  
daemonize=uwsgi.log

  
module=MyBlog.wsgi

#指定静态文件路径（使用nginx后就不需要了）  
#static-map = /static=/MyBlog/static  
```
其中chdir指的是你的django项目的根目录，配置了这个以后，其他的和文件相关的配置都会以这个根目录为起点去找其他的文件，比如wsgi-file就是指定wsgi文件的位置，我的是在MyBlog/MyBlog/wsgi.py下，所以我这里只用写MyBlog/wsgi.py即可！所以千万不要把这个配置错了！其他的配置就按照我的注释来吧！

## 3.配置nginx.conf

找到nginx的安装目录，默认是/etc/nginx，在该目录下有一个nginx.conf文件，编辑此文件，我的配置内容如下：

```shell script
user root; #以什么用户身份运行子进程  
worker_processes 1; #一般设置为核数 可以通过命令cat /proc/cpuinfo|grep "processor"|wc -l
查看核数  
#worker_cpu_affinity 01 10; #多核情况下启用，设置亲和度，每个worker绑定到一个核上。 如果是4核 则为 0001 0010
0100 #1000，以此类推

pid /var/run/nginx.pid;

events {  
    use epoll; #使用epoll提升并发能力，仅linux系统可用  
    worker_connections 1024; #单个worker同时连接的最大数  
}

http {  
    include   mime.types;  
    default_type application/octet-stream;  
      
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '  
                    '$status $body_bytes_sent "$http_referer" '  
                    '"$http_user_agent" "$http_x_forwarded_for"';  
      
      
    access_log  /var/log/nginx/access.log;  
    error_log  /var/log/nginx/error.log;  
      
    sendfile    on; #开启sendfile调用（即零复制技术），提高文件传输效率  
    tcp_nopush   on; #配置tcp_cork,它在配置sendfile后才会生效  
    keepalive_timeout  60; #keeplive超时时间  
      
    gzip on;  #开启gzip压缩  
    gzip_types text/plain application/x-javascript text/css text/javascript application/x-httpd-php application/json  
    text/json image/jpeg  image/gif  image/png  application/octet-stream; #gzip要处理的文件类型  
      
    include /etc/nginx/conf.d/*.conf;  #包含其他文件进来  
#     include conf.d/typeidea.conf;   #我们的配置文件  
#  include conf.d/myblog.conf;  
      
}
```

需要注意的是，你的项目的对应文件可以通过include
你的项目文件位置进行引入，或者直接写在http中也可以，我使用的是前者，即如代码中所见：include /etc/nginx/conf.d/*.conf;
#包含其他文件进来 我将我的所有的项目配置文件都放在/etc/nginx/conf.d这个目录下，通过这句话，可以一次性引入该目录下的所有配置文件。

## 4.配置项目的conf文件（在/etc/nginx/conf.d目录下）

```shell script
server  
{  
    listen 80;  
    server_name www.lll.plus;  
    charset utf-8;  
      
     include   mime.types;  
    default_type application/octet-stream;  
      
      location / {  
       include uwsgi_params;  
       uwsgi_connect_timeout  30; #设置uwsgi超时时间  
       uwsgi_pass 127.0.0.1:18081;  #端口要和uwsgi里配置的一样  
    }  
      
        
    location /static/{  
        alias /MyBlog/static/;  #静态资源路径  
    }  
        location /media/ {  
        alias  /MyBlog/static/media/;  
              
        }  
}
```

这里需要注意的是：![](http://www.lll.plus/media/image/2022/01/25/image-20220125162047-10.png)，一定不能忘记添加这个配置了！！！不添加这个的后果就是，所有文件的默认content_type都是application/otect格式，这个意味着什么呢？意味着连你的css/js文件也是这个格式，意味着在你其他配置都没有问题的情况下，但你兴高采烈的打开你的网站时，呈现出的却是一副你不想看到的样式。即使在nginx.conf中有配置过！也一定不要忘记在这里配置！我因为一开始没有配置这个，找了一天的bug，一直没有注意到，反复检查，因为一直找不到问题所在，最离谱的时候我都怀疑是不是我域名解析的配置是不是有问题???

在以上配置都没有问题后，那么就可以开始setup了！



## 5.启动

1.启动uwsgi

```shell script
命令：uwsfi uwsgi.ini      (在uwsgi目录下使用该命令，或者uwsgi uwsgi.ini的绝对位置)
```

2.启动nginx

```shell script
命令:service nginx restart
```
如果没有问题的话，访问你自己配置的域名+端口号应该就可以看到你自己的网页啦！

tip：我这里仅仅说明了uwsgi和nginx的相关配置而已，其他的django的一些相关配置没有说，比如如果使用nginx做文件服务的话，在settings中就必须指定STATIC_ROOT目录所在的位置，并且得使用collectstatic将所有的静态文件收集到该目录下，并且nginx中的静态文件的目录也必须和这个一致，那样nginx才能访问的到！千说万说都不如自己动手去做做！所以行动吧！少年~









<ActionBox />
