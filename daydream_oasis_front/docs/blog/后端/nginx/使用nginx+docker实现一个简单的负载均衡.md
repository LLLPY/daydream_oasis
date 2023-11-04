
<BlogInfo id="415" title="使用nginx+docker实现一个简单的负载均衡" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="319" category="nginx" tag_list="['nginx', '              负载均衡', '              docker']" create_time="2022.08.14 11:02:01.054565" update_time="2022.08.14 11:03:46" />


## 前言

对于一个服务，当并发请求量较大时，一个服务器可能就会处理不过来，这时候就需要加多台服务器，来处理这些并发的请求，而在这么多的服务器中，当前的请求具体大道哪台服务器上呢？这个时候我们就可以用到nginx提供的的负载均衡功能，我们可以根据每台服务器的配置，将配置好一点的服务器设置更高的权重；配置低一点的服务器就设置低一点的权重，这时候较多的请求就会打在配置好一点的服务器上，较少的请求就会打在配置差一点的服务器上，从而就实现了负载均衡。

因此要想实现一个负载均衡，前提条件是我们得有多台服务器，因为资源有限，我这里就以docker启动的每台容器当做一台服务器。同时我也会将nginx运行在一个单独的容器中，也将其假设成一个单独的服务器。这时候也相当于实现了反向代理的功能。

![](https://img-blog.csdnimg.cn/592f184d84a74b8cbcb7ab519cae5375.png)

##  提出需求

我们还是以需求驱动，有了需求之后，我们才好根据需求做出对应的决策，才好对症下药！假设我们有这样一个需求：
**访问我们服务的地址后，返回此时访问的真正的服务器的名称。**

大体架构如下：

![](https://img-blog.csdnimg.cn/bba7c7187e7b4b0eb89151fc40fccbc6.png)


我们假设总共有7台服务器，一台用作反向代理用，另外六台是真正提供服务的服务器。

## 开始

### 启动nginx

启动一个nginx，将容器端口80映射到本地的7777


```shell script
 docker run -it -p 7777:80 --name mynginx nginx /bin/bash
```

进入容器后启动nginx服务：

![](https://img-blog.csdnimg.cn/0b354b9877394e889617660f13a196eb.png)

 此时访问对应的网址就可以看到如下页面：

![](https://img-blog.csdnimg.cn/981cc0a6089a4c80b8b6431407c7171d.png)

 说明nginx启动成功！

### 启动一个Django容器
```shell script
docker run -it -p 8081:8000 --name server01 django /bin/bash
```

进入容器后，启动一个django项目：
```shell script
django-admin startproject sayhello 
```
进入sayhello目录下创建一个application

```shell script
python manage.py startapp app
```

启动django项目，检查是否启动成功
```shell script
python manage.py runserver 0.0.0.0:8000
```

分别在容器内部和本地都访问成功！

![](https://img-blog.csdnimg.cn/052172f3801940b8b44790fe724a360f.png)

在app的views.py中编写相应的视图函数，添加以下内容：


```python
import os
from django.http import HttpResponse

def get_host_name(request):
    host_name = os.environ.get('HOSTNAME', 'None')
    info = f'您当前访问的主机是:{host_name}'
    return HttpResponse(info)
```


在sayhello的urls中添加一条路由规则

![](https://img-blog.csdnimg.cn/64cc8e7ac7a24e439d974e0b00d93f47.png)

 编辑sayhello下的settings文件，允许所有主机访问：

![](https://img-blog.csdnimg.cn/95f98366485d4004a7990dbc7c4133bc.png)

 执行迁移
```shell script
python manage.py makemigrations

python manage.py migrate
```

重启启动django，之后再访问sayhello这条路径，就会发现它返回了主机名！

![](https://img-blog.csdnimg.cn/eb332f4d44854974970a698ad7f2316f.png)

 所以一台服务器部署成功！

### 部署多台服务器

#### 1.打包一个容器

## 首先将上面部署好的django打包成一个镜像，之后直接启动即可！


```shell script
docker commit -a "LLL@2474605919@qq.com" -m "打包已经部署好的django项目，之后直接使用就行了。" aab53c10b632 mydjango:1.0
```

![](https://img-blog.csdnimg.cn/fb6855adc36b4d59939ac19c51315e74.png)

####  2.开启多台服务


```shell script
docker run -it -p 8082:8000 --name server02 mydjango:1.0 /bin/bash
docker run -it -p 8083:8000 --name server03 mydjango:1.0 /bin/bash
docker run -it -p 8084:8000 --name server04 mydjango:1.0 /bin/bash
docker run -it -p 8085:8000 --name server05 mydjango:1.0 /bin/bash
docker run -it -p 8086:8000 --name server06 mydjango:1.0 /bin/bash
```


#### 3.在各个容器中启动django项目

```shell script
cd /usr/src/sayhello
python manage.py runserver 0.0.0.0:8000
```

nginx和6台django服务都启动成功！

![](https://img-blog.csdnimg.cn/116a06ab99b84992be50f9644d517d0c.png)

##  配置nginx文件实现反向代理和负载均衡

在/etc/nginx目录下配置nginx.conf文件，添加如下内容：

```shell script
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    upstream myserver {

       server 172.18.0.2:8000 weight=1;
       server 172.18.0.7:8000 weight=1;
       server 172.18.0.6:8000 weight=1;
       server 172.18.0.5:8000 weight=1;
       server 172.18.0.4:8000 weight=1;
       server 172.18.0.3:8000 weight=1;
      
   }

  upstream myserver2 {
    server 172.17.28.61:8081 weight=1;
    server 172.17.28.61:8082 weight=1;
    server 172.17.28.61:8083 weight=1;
    server 172.17.28.61:8084 weight=1;
    server 172.17.28.61:8085 weight=1;
    server 172.17.28.61:8086 weight=1;

}

  server {
    
    listen 80;
    server_name localhost;

    location /sayhello {
      proxy_pass http://myserver2;        
      
   }
   
}  
    include /etc/nginx/conf.d/*.conf;
}
```


![](https://img-blog.csdnimg.cn/8b9187bd471d41f480342d2a25c16468.png)

 负载均衡的核心配置就是upstream和proxy_pass这两项，在upstream中可以配置我们用来做负载均衡的服务器（
**也就是请求最后打到的真实服务器！，同时，如果当前nginx和不在这些服务器中，也就相当于同时做了反向代理！**
），当然，这里也可以指定做这个负载均衡的具体方法，我这里就是为每个服务器赋一个权重，权重越高的，命中的概率就越高。之后就是配置proxy_pass,只要保证代理的名称和刚刚配置的upstream名称一直就行。

## 检验

将上面的配置文件修改完成后，使用命令重新加载配置文件：

```shell script
nginx -s reload #对配置文件进行重新加载
```

在没有配置出错的前提下应该就可以访问成功了！在此之前，我们还是先理一下逻辑，我们绑定了那么多ip和端口，如果不理清楚，都不知道该访问哪个了！
![](https://img-blog.csdnimg.cn/4f3b8207408b41d2ac1e030905d422a5.png)
![](https://img-blog.csdnimg.cn/4f3b8207408b41d2ac1e030905d422a5.png)
![](https://img-blog.csdnimg.cn/4f3b8207408b41d2ac1e030905d422a5.png)

首先，我们为每一个django服务都分配了一个容器，在各自的容器中，它们都使用的是8000端口，然后我们又为每一个容器映射了一个本地端口，因此，不管是通过
**本地ip+映射的端口** 还是 **容器ip+8000** ****
，是都能访问得到的！然后我们又开启了一个容器来做nginx服务，我们使用本地端口7777（已添加到安全组）映射了nginx容器的80端口，然后在nginx中做了负载均衡，所以我们只需要访问7777端口，就会把请求打到nginx容器的80端口，然后再通过负载均衡，打到对应的django服务中！

因此，我们只需要访问通过公网ip+7777端口应该就能访问到啦！

访问地址：

<http://www.lll.plus:7777/sayhello/>

![](https://img-blog.csdnimg.cn/a02dd015fe924b36ae39bef14b616106.png)


可以看到，基本上前六次，每次的访问结果都不一样，第七次访问了第一次访问的服务，因为我为每一个服务配置的权重都是一样的，所以这和预期的结果也基本上是一直的！也算是大功告成啦！

## 配置负载均衡的其他方法

除了我上面使用的赋权重方法以外，还有其他的方法。

### 1.轮询（默认）

  * 请求被平均调度给多个服务器处理

```shell script
http {
  ...
  upstream myserver {
   server 192.168.1.2:8080;
   server 192.168.1.3:8080;
   ...
  }
  server {
  	  ...
	  location / {
	  	proxy_pass http://myserver;
	  }
  }
}
```

## 2.加权轮询算法

  * 给服务器列表的每个服务器都增加一个权重，权重高者，命中率越高。

```shell script
http {
	...
	upstream myserver {
	  server 192.168.1.2:8080 weight=10;
	  server 192.168.1.3:8080 weight=90;
	  ...
	}
	...
	server {
		...
		localtion / {
		  proxy_pass http:myserver;
		}
	}
}
```

## 3.ip_hash算法

  * 将客户端的ip进行hash运算，再根据运算结果打到某一台服务器，之后也会一直打到同一台服务器，可以解决session问题


```shell script
http {
	...
	upstream myserver {
		ip_hash;
		server 192.168.1.2:8080;
		server 192.168.1.3:8080;
		...
	}
	...
	server {
	    ...
		location / {
		  proxy_pass http://myserver;
		}
	}
}
```

## 4.最少连接数算法

  * 此种方式nginx会将请求转发到当前连接数较少的服务器


```shell script
http {
	...
	upstream myserver {
	  least_conn;
	  server 192.168.1.2:8080;
	  server 192.168.1.3:8080;
	  ...
	}
	...
	server {
	  ...
	  location / {
	    proxy_pass http://myserver;
	  }
	}
}
```

## 5.url_hash算法

  * 对客户端请求的url进行hash运算，将相同的url打到同一个服务器
  * _需要安装url_hash补丁_


```shell script
http {
  ...
  upstream myserver {
    server 192.168.1.2:8080;
    server 192.168.1.3:8080;
    ...
    hash $request_uri;
    hash_method crc32;
  }
  ...
  server {
    ...
    location / {
      proxy_pass http://myserver;
    }
  }
}
```


## 6.fair算法

  * 优先选择响应时间最短的服务器
  * 需要安装模块：nginx-upstream-fair-master

```shell script
http {
  ...
  upstream myserver {
    fair;
    server 192.168.1.2:8080;
    server 192.168.1.3:8080;
    ...
  }
  ...
  server {
    ...
    location / {
      proxy_pass http://myserver;
    }
  }
}
```

参考链接：[nginx配置负载均衡](https://blog.csdn.net/qq_34825514/article/details/124311144
"nginx配置负载均衡")


