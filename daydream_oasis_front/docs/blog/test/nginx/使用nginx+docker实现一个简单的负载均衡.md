
<BlogInfo title="使用nginx+docker实现一个简单的负载均衡" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=319 category="nginx" tag_list="['nginx', '负载均衡', 'docker']" create_time="2022.08.14 11:02:01.054565" update_time="2022.08.14 11:03:46" />

^^^^^^^^^
<p><strong>&nbsp;目录</strong></p>

<p><a href="#%E5%89%8D%E8%A8%80" target="_self">前言</a></p>

<p><a href="#%C2%A0%E6%8F%90%E5%87%BA%E9%9C%80%E6%B1%82" target="_self">&nbsp;提出需求</a></p>

<p><a href="#%E5%BC%80%E5%A7%8B" target="_self">开始</a></p>

<p><a href="#%E5%90%AF%E5%8A%A8nginx" target="_self">启动nginx</a></p>

<p><a href="#%E5%90%AF%E5%8A%A8%E4%B8%80%E4%B8%AADjango%E5%AE%B9%E5%99%A8" target="_self">启动一个Django容器</a></p>

<p><a href="#%E9%83%A8%E7%BD%B2%E5%A4%9A%E5%8F%B0%E6%9C%8D%E5%8A%A1%E5%99%A8" target="_self">部署多台服务器</a></p>

<p><a href="#1.%E6%89%93%E5%8C%85%E4%B8%80%E4%B8%AA%E5%AE%B9%E5%99%A8" target="_self">1.打包一个容器</a></p>

<p><a href="#%C2%A02.%E5%BC%80%E5%90%AF%E5%A4%9A%E5%8F%B0%E6%9C%8D%E5%8A%A1" target="_self">&nbsp;2.开启多台服务</a></p>

<p><a href="#3.%E5%9C%A8%E5%90%84%E4%B8%AA%E5%AE%B9%E5%99%A8%E4%B8%AD%E5%90%AF%E5%8A%A8django%E9%A1%B9%E7%9B%AE" target="_self">3.在各个容器中启动django项目</a></p>

<p><a href="#%C2%A0%E9%85%8D%E7%BD%AEnginx%E6%96%87%E4%BB%B6%E5%AE%9E%E7%8E%B0%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%92%8C%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1" target="_self">&nbsp;配置nginx文件实现反向代理和负载均衡</a></p>

<p><a href="#%E6%A3%80%E9%AA%8C" target="_self">检验</a></p>

<p><a href="#%E9%85%8D%E7%BD%AE%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9A%84%E5%85%B6%E4%BB%96%E6%96%B9%E6%B3%95" target="_self">配置负载均衡的其他方法</a></p>

<p><a href="#1.%E8%BD%AE%E8%AF%A2%EF%BC%88%E9%BB%98%E8%AE%A4%EF%BC%89" target="_self">1.轮询（默认）</a></p>

<p><a href="#2.%E5%8A%A0%E6%9D%83%E8%BD%AE%E8%AF%A2%E7%AE%97%E6%B3%95" target="_self">2.加权轮询算法</a></p>

<p><a href="#3.ip_hash%E7%AE%97%E6%B3%95" target="_self">3.ip_hash算法</a></p>

<p><a href="#4.%E6%9C%80%E5%B0%91%E8%BF%9E%E6%8E%A5%E6%95%B0%E7%AE%97%E6%B3%95" target="_self">4.最少连接数算法</a></p>

<p><a href="#5.url_hash%E7%AE%97%E6%B3%95" target="_self">5.url_hash算法</a></p>

<p><a href="#6.fair%E7%AE%97%E6%B3%95" target="_self">6.fair算法</a></p>

<hr />
<p>&nbsp;</p>

<h1>前言</h1>

<p>对于一个服务，当并发请求量较大时，一个服务器可能就会处理不过来，这时候就需要加多台服务器，来处理这些并发的请求，而在这么多的服务器中，当前的请求具体大道哪台服务器上呢？这个时候我们就可以用到nginx提供的的负载均衡功能，我们可以根据每台服务器的配置，将配置好一点的服务器设置更高的权重；配置低一点的服务器就设置低一点的权重，这时候较多的请求就会打在配置好一点的服务器上，较少的请求就会打在配置差一点的服务器上，从而就实现了负载均衡。</p>

<p>因此要想实现一个负载均衡，前提条件是我们得有多台服务器，因为资源有限，我这里就以docker启动的每台容器当做一台服务器。同时我也会将nginx运行在一个单独的容器中，也将其假设成一个单独的服务器。这时候也相当于实现了反向代理的功能。</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/592f184d84a74b8cbcb7ab519cae5375.png" style="height:672px; width:900px" /></p>

<h1>&nbsp;提出需求</h1>

<p>我们还是以需求驱动，有了需求之后，我们才好根据需求做出对应的决策，才好对症下药！假设我们有这样一个需求：<strong>访问我们服务的地址后，返回此时访问的真正的服务器的名称。</strong></p>

<p>大体架构如下：</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/bba7c7187e7b4b0eb89151fc40fccbc6.png" style="height:501px; width:900px" /></p>

<p>&nbsp;</p>

<p>我们假设总共有7台服务器，一台用作反向代理用，另外六台是真正提供服务的服务器。</p>

<h1>开始</h1>

<h2>启动nginx</h2>

<p>启动一个nginx，将容器端口80映射到本地的7777</p>

<pre>
<code>docker run -it -p 7777:80  --name mynginx  nginx  /bin/bash
</code></pre>

<p>进入容器后启动nginx服务：</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/0b354b9877394e889617660f13a196eb.png" style="height:280px; width:900px" /></p>

<p>&nbsp;此时访问对应的网址就可以看到如下页面：</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/981cc0a6089a4c80b8b6431407c7171d.png" style="height:411px; width:900px" /></p>

<p>&nbsp;说明nginx启动成功！</p>

<h2>启动一个Django容器</h2>

<pre>
<code>docker run -it -p 8081:8000 --name server01 django /bin/bash</code></pre>

<p>进入容器后，启动一个django项目：</p>

<pre>
<code>django-admin startproject sayhello&nbsp;</code></pre>

<p>进入sayhello目录下创建一个application</p>

<pre>
<code>python manage.py startapp app</code></pre>

<p>启动django项目，检查是否启动成功</p>

<pre>
<code>python manage.py runserver 0.0.0.0:8000</code></pre>

<p>分别在容器内部和本地都访问成功！</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/052172f3801940b8b44790fe724a360f.png" style="height:418px; width:900px" /></p>

<p>在app的views.py中编写相应的视图函数，添加以下内容：</p>

<pre>
<code>import os
from django.http import HttpResponse


def get_host_name(request):
    host_name = os.environ.get(&#39;HOSTNAME&#39;, &#39;None&#39;)
    info = f&#39;您当前访问的主机是:{host_name}&#39;
    return HttpResponse(info)</code></pre>

<p>在sayhello的urls中添加一条路由规则</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/64cc8e7ac7a24e439d974e0b00d93f47.png" style="height:331px; width:672px" /></p>

<p>&nbsp;编辑sayhello下的settings文件，允许所有主机访问：</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/95f98366485d4004a7990dbc7c4133bc.png" style="height:393px; width:708px" /></p>

<p>&nbsp;执行迁移</p>

<pre>
<code>python manage.py makemigrations

python manage.py migrate</code></pre>

<p>重启启动django，之后再访问sayhello这条路径，就会发现它返回了主机名！</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/eb332f4d44854974970a698ad7f2316f.png" style="height:247px; width:760px" /></p>

<p>&nbsp;所以一台服务器部署成功！</p>

<h2>部署多台服务器</h2>

<h3>1.打包一个容器</h3>

<p>#首先将上面部署好的django打包成一个镜像，之后直接启动即可！</p>

<pre>
<code>docker commit -a &quot;LLL@2474605919@qq.com&quot; -m &quot;打包已经部署好的django项目，之后直接使用就行了。&quot; aab53c10b632 mydjango:1.0</code></pre>

<p><img alt="" src="https://img-blog.csdnimg.cn/fb6855adc36b4d59939ac19c51315e74.png" style="height:350px; width:671px" /></p>

<h3>&nbsp;2.开启多台服务</h3>

<pre>
<code>docker run -it -p 8082:8000 --name server02 mydjango:1.0 /bin/bash
docker run -it -p 8083:8000 --name server03 mydjango:1.0 /bin/bash
docker run -it -p 8084:8000 --name server04 mydjango:1.0 /bin/bash
docker run -it -p 8085:8000 --name server05 mydjango:1.0 /bin/bash
docker run -it -p 8086:8000 --name server06 mydjango:1.0 /bin/bash
</code></pre>

<h3>3.在各个容器中启动django项目</h3>

<pre>
<code>cd /usr/src/sayhello
python manage.py runserver 0.0.0.0:8000</code></pre>

<p>nginx和6台django服务都启动成功！</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/116a06ab99b84992be50f9644d517d0c.png" style="height:559px; width:703px" /></p>

<h2>&nbsp;配置nginx文件实现反向代理和负载均衡</h2>

<p>在/etc/nginx目录下配置nginx.conf文件，添加如下内容：</p>

<pre>
<code>user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  &#39;$remote_addr - $remote_user [$time_local] &quot;$request&quot; &#39;
                      &#39;$status $body_bytes_sent &quot;$http_referer&quot; &#39;
                      &#39;&quot;$http_user_agent&quot; &quot;$http_x_forwarded_for&quot;&#39;;

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
</code></pre>

<p><img alt="" src="https://img-blog.csdnimg.cn/8b9187bd471d41f480342d2a25c16468.png" style="height:735px; width:786px" /></p>

<p>&nbsp;负载均衡的核心配置就是upstream和proxy_pass这两项，在upstream中可以配置我们用来做负载均衡的服务器（<strong>也就是请求最后打到的真实服务器！，同时，如果当前nginx和不在这些服务器中，也就相当于同时做了反向代理！</strong>），当然，这里也可以指定做这个负载均衡的具体方法，我这里就是为每个服务器赋一个权重，权重越高的，命中的概率就越高。之后就是配置proxy_pass,只要保证代理的名称和刚刚配置的upstream名称一直就行。</p>

<h1>检验</h1>

<p>将上面的配置文件修改完成后，使用命令重新加载配置文件：</p>

<pre>
<code>nginx -s reload #对配置文件进行重新加载</code></pre>

<p>在没有配置出错的前提下应该就可以访问成功了！在此之前，我们还是先理一下逻辑，我们绑定了那么多ip和端口，如果不理清楚，都不知道该访问哪个了！<img alt="" src="https://img-blog.csdnimg.cn/4f3b8207408b41d2ac1e030905d422a5.png" style="height:36px; width:36px" /><img alt="" src="https://img-blog.csdnimg.cn/4f3b8207408b41d2ac1e030905d422a5.png" style="height:36px; width:36px" /><img alt="" src="https://img-blog.csdnimg.cn/4f3b8207408b41d2ac1e030905d422a5.png" style="height:36px; width:36px" /></p>

<p>首先，我们为每一个django服务都分配了一个容器，在各自的容器中，它们都使用的是8000端口，然后我们又为每一个容器映射了一个本地端口，因此，不管是通过<strong>本地ip+映射的端口</strong>还是<strong>容器ip+8000</strong><strong> </strong>，是都能访问得到的！然后我们又开启了一个容器来做nginx服务，我们使用本地端口7777（已添加到安全组）映射了nginx容器的80端口，然后在nginx中做了负载均衡，所以我们只需要访问7777端口，就会把请求打到nginx容器的80端口，然后再通过负载均衡，打到对应的django服务中！</p>

<p>因此，我们只需要访问通过公网ip+7777端口应该就能访问到啦！</p>

<p>访问地址：</p>

<p><a  href="http://www.lll.plus:7777/sayhello/" title="http://www.lll.plus:7777/sayhello/">http://www.lll.plus:7777/sayhello/</a>&nbsp;</p>
<p><img alt="" src="https://img-blog.csdnimg.cn/a02dd015fe924b36ae39bef14b616106.png" style="height:614px; width:900px" /></p>

<p>&nbsp;</p>

<p>可以看到，基本上前六次，每次的访问结果都不一样，第七次访问了第一次访问的服务，因为我为每一个服务配置的权重都是一样的，所以这和预期的结果也基本上是一直的！也算是大功告成啦！</p>

<h1>配置负载均衡的其他方法</h1>

<p>除了我上面使用的赋权重方法以外，还有其他的方法。</p>

<h2>1.轮询（默认）</h2>

<ul>
	<li>请求被平均调度给多个服务器处理</li>
</ul>

<pre>
<code>http {
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
</code></pre>

<h2>2.加权轮询算法</h2>

<ul>
	<li>给服务器列表的每个服务器都增加一个权重，权重高者，命中率越高。</li>
</ul>

<pre>
<code>http {
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
</code></pre>

<h2>3.ip_hash算法</h2>

<ul>
	<li>将客户端的ip进行hash运算，再根据运算结果打到某一台服务器，之后也会一直打到同一台服务器，可以解决session问题</li>
</ul>

<pre>
<code>http {
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
</code></pre>

<h2>4.最少连接数算法</h2>

<ul>
	<li>此种方式nginx会将请求转发到当前连接数较少的服务器</li>
</ul>

<pre>
<code>http {
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
</code></pre>

<h2>5.url_hash算法</h2>

<ul>
	<li>对客户端请求的url进行hash运算，将相同的url打到同一个服务器</li>
	<li><em>需要安装url_hash补丁</em></li>
</ul>

<pre>
<code>http {
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
</code></pre>

<h2>6.fair算法</h2>

<p>&nbsp;</p>

<ul>
	<li>优先选择响应时间最短的服务器</li>
	<li><em>需要安装模块：nginx-upstream-fair-master</em></li>
</ul>

<pre>
<code>http {
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
</code></pre>

<p>参考链接：<a class="link-info" href="https://blog.csdn.net/qq_34825514/article/details/124311144" title="nginx配置负载均衡">nginx配置负载均衡</a></p>

