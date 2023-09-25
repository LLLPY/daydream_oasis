
<BlogInfo title="《入门docker，这一篇就够了》" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=843 category="docker" tag_list="['容器', 'docker']" create_time="2022.08.11 11:52:31.299830" update_time="2022.08.11 11:52:31" />

^^^^^^^^^
<h1>docker的概述</h1>

<h2>docker出现的背景</h2>

<p>一款产品的上线往往会经过开发，上线等阶段，而开发往往在本地，上线则需要将产品跑在另一台机器上，而这样往往会出现一个问题：在自己本地跑的时候没有问题，但是上线跑就不行了。造成这个原因往往可能是因为开发和生产环境不同导致的，因此，为了解决这个问题，docker应运而生。</p>

<p>&nbsp;</p>

<p>有些图片失效，可以下载附件中的pdf查看。</p>

<h2>什么是docker</h2>

<p>官方解释：</p>

<p>Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker&rsquo;s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.</p>

<blockquote>
<p>一句话总结：docker是一个用于开发，发布和运行程序的开放平台，能够有效减少从开发到上线的延迟。实现这些功能的一个重要技术就是：<strong>容器技术</strong>，因此，也可以说，docker是容器技术的一个衍生品。在docker中，有三个重要的名词，分别是：dockerfile，images和container。</p>
</blockquote>

<h3>dockerfile</h3>

<p>Docker can build images automatically by reading the instructions from a&nbsp;<code>Dockerfile</code>.&nbsp;<strong>A&nbsp;<code>Dockerfile</code>&nbsp;is a text document that contains all the commands a user could call on the command line to assemble an image</strong>. Using&nbsp;<code>docker build</code>&nbsp;users can create an automated build that executes several command-line instructions in succession.</p>

<blockquote>
<p>一句话总结：dockerfile就是一个包含了生成一个镜像所需的所有命令的文本文件。</p>
</blockquote>

<h3>image</h3>

<p><strong>A Docker container image is a lightweight, standalone, executable package</strong>&nbsp;of software that includes everything needed to run an application:&nbsp;code,&nbsp;runtime,&nbsp;system tools,&nbsp;system libraries&nbsp;and&nbsp;settings.</p>

<blockquote>
<p>一句话总结：就是一个软件包。</p>
</blockquote>

<h3>container</h3>

<p><strong>A container is a standard unit of software</strong>&nbsp;that&nbsp;<strong>packages up code and all its dependencies so the application</strong>&nbsp;runs quickly and reliably from one computing environment to another.</p>

<blockquote>
<p>一句话总结：就是运行时的镜像。</p>
</blockquote>

<blockquote>
<p>对于这三者之间关系，我们可以这样理解：将dockerfile看做是源代码，image看做可执行的软件包，container是一个正在运行的程序，通过docker build将&rdquo;源代码&ldquo;dockerfile编译成&rdquo;可执行的包&ldquo;image，最后通过docker run执行这个包，就变成了container。</p>
</blockquote>

<blockquote>
<p>所以说，一个容器就是一个标准的软件单元，并且它打包了代码，以及运行这些代码需要的所有依赖。因此它具备以下特性：</p>

<ul>
	<li>轻量性：公用操作系统的内核，不需要系统核心以外的其他软件</li>
	<li>隔离性：每个容器都有自己独立运行需要的环境和依赖，容器与容器之间相互隔离</li>
	<li>安全性：因为隔离性的存在，所以保证了其安全性</li>
	<li>可移植性：docker创建了业界统一的标准，因此可以移植到任何系统</li>
</ul>
</blockquote>

<p><img alt="" src="https://img-blog.csdnimg.cn/img_convert/37a5d23a04724d8246a4ba7aa8b996bb.webp?x-oss-process=image/format,png" /></p>

<h2>docker与virtual machine</h2>

<p>官方解释：Containers and virtual machines have similar&nbsp;<strong>resource isolation</strong>&nbsp;and&nbsp;<strong>allocation</strong>&nbsp;benefits, but function differently because&nbsp;<strong>containers virtualize the operating system instead of hardware</strong>. Containers are more portable and efficient.</p>

<blockquote>
<p>因此，可以认为，docker和虚拟机相比，两者都有相似的资源隔离和分配功能，两者都是&rdquo;虚拟机&ldquo;，但是docker虚拟是操作系统，是软件层面的，而vm虚拟的是硬件，因此，docker具有更强的可移植性和效率。</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-mnnhCkAD-1660189637777)(C:UsersLLL03Desktoppython2.笔记image-20220730211234861.png)]</p>

<h1>docker的安装</h1>

<p>官方给出的安装方法有三种：</p>

<p>You can install Docker Engine in different ways, depending on your needs:</p>

<ul>
	<li><strong>Most users&nbsp;<a href="https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository">set up Docker&rsquo;s repositories</a>&nbsp;and install from them, for ease of installation and upgrade tasks. This is the recommended approach.</strong></li>
	<li>Some users download the DEB package and&nbsp;<a href="https://docs.docker.com/engine/install/ubuntu/#install-from-a-package">install it manually</a>&nbsp;and manage upgrades completely manually. This is useful in situations such as installing Docker on air-gapped systems with no access to the internet.</li>
	<li>In testing and development environments, some users choose to use automated&nbsp;<a href="https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script">convenience scripts</a>&nbsp;to install Docker.</li>
</ul>

<p>这里使用官方推荐方法进行安装，也就是set up Docker&rsquo;s repositories.</p>

<h3>1.移除已安装的docker</h3>

<pre>
<code>sudo apt-get remove docker docker-engine docker.io containerd runc
</code></pre>

<h3>2.更新下载索引同时下载一些依赖包</h3>

<pre>
<code>sudo apt-get update
 sudo apt-get install 
    ca-certificates 
    curl 
    gnupg 
    lsb-release
</code></pre>

<h3>3.添加docker官方的GPG key</h3>

<pre>
<code> sudo mkdir -p /etc/apt/keyrings
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
</code></pre>

<h3>4.设置下载源</h3>

<pre>
<code>echo 
  &quot;deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu 
  $(lsb_release -cs) stable&quot; | sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null
</code></pre>

<h3>5.安装Docker Engine</h3>

<p>（默认安装最新版本）</p>

<pre>
<code>sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
</code></pre>

<h3>6.检查是否安装成功</h3>

<p>在终端运行命令(测试用例)：</p>

<pre>
<code>docker run hello-world
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-XyWY6gwA-1660189637778)(C:UsersLLL03Desktoppython2.笔记image-20220731105512166.png)]</p>

<p>出现如上提示在，则说明安装成功！</p>

<h1>docker的常用命令</h1>

<h2>1.docker images:查看所有镜像</h2>

<blockquote>
<p>配置参数：</p>

<p>-a 显示所有:docker images -a</p>

<p>-q 只显示镜像ID:docker images -q</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-2X44IKE5-1660189637780)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731142834956.png)]</p>

<h2>2.docker pull:拉取一个镜像</h2>

<blockquote>
<p>例：拉取指定版本为5.0的redis到本地</p>

<p>docker pull redis:5.0</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-ZkUvCnB2-1660189637781)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731144200872.png)]</p>

<h2>3.docker rmi:删除一个镜像</h2>

<blockquote>
<p>可选参数：</p>

<p>-f 强制删除：docker rmi -f 镜像ID/镜像名</p>

<p>例：强制删除所有镜像：docker rmi -f $(docker images -aq)</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-STpNYc8J-1660189637782)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731145615982.png)]</p>

<h2>4.docker run：运行一个镜像</h2>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-rj71Uofi-1660189637782)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731140130349.png)]</p>

<pre>
<code> docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
 #options指定其他参数 image指定要启动的镜像 默认情况下是前台启动
 
 常用的可选参数：
 -d:后台运行
 -i:交互式的
 -t:为容器分配一个虚拟伪终端，通常与-i搭配使用
 -p:端口映射 -p port1:port2 port1为主机端口，port2为容器端口，将容器端口port2映射到主机端口port1
 -P:随机端口映射
 --name:为容器起一个别名
 -e:设置环境变量
 -v:绑定一个卷
</code></pre>

<blockquote>
<p>例：启动一个ubuntu</p>

<p>docker run ubuntu</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-fjLTzMhX-1660189637783)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731133812208.png)]</p>

<p>如图所示，在启动ubuntu后，hostname发生了变化，说明成功启动了ubuntu。</p>

<blockquote>
<p>例：启动一个nginx服务 同时将容器端口80映射到主机端口7777</p>

<p>docker run -it -p 7777:80 nginx /bin/bash</p>
</blockquote>

<h2>5.docker start:启动一个容器</h2>

<blockquote>
<p>docker start 容器id（默认后台启动）</p>

<p>可选参数：</p>

<p>-i 交互式的启动</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-Ct2nwdZi-1660189637784)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731160308358.png)]</p>

<h2>6.docker restart：重启一个容器</h2>

<blockquote>
<p>docker restart 容器id（默认后台重启）</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-XsdFnJiG-1660189637785)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731160303442.png)]</p>

<h2>7.docker stop:停止一个container</h2>

<blockquote>
<p>例：杀死正在运行的redis：docker stop $(docker ps -a --filter &ldquo;ancestor=redis&rdquo;)</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-UPuZHiB3-1660189637785)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731155354484.png)]</p>

<h2>8.docker rm:移除一个容器</h2>

<blockquote>
<p>可选参数：</p>

<p>-f:强制移除 docker rm -f (对于正在运行的容器可能无法删除，可以使用这个参数)</p>

<p>-v:同时移除卷 docker rm -v</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-dtU2qeUk-1660189637786)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731153246394.png)]</p>

<h2>9.exit:退出一个容器</h2>

<blockquote>
<p>默认情况下，在容器中输入exit后就会退出当前容器，同时容器会停止执行</p>

<p>如果想在退出容器后，容器继续在后台执行，可以使用快捷键：ctrl+Q+P</p>
</blockquote>

<h2>10.docker ps:查看当前正在运行的容器</h2>

<blockquote>
<p>可选参数：</p>

<p>-a 显示所有容器（包括当前不在运行的）：docker ps -a</p>

<p>-q 仅显示容器的id：docker ps -q</p>
</blockquote>

<h2>11.docker attach:进入一个容器</h2>

<blockquote>
<p>docker attach 容器id</p>
</blockquote>

<h2>12.docker exec:进入一个容器</h2>

<blockquote>
<p>docker exec -it 容器id /bin/bash #交互式的方式进入一个容器</p>

<p>exec和attach的区别在于：exec进入容器后会开启新的终端，attach进入容器后，是直接使用之前打开的终端</p>
</blockquote>

<h2>13.docker cp:拷贝内容</h2>

<blockquote>
<p>从容器中拷贝文件到本地：</p>

<p>docker cp 容器id:容器中的文件路径 本地中的路径</p>

<p>例：docker cp c2141be3b743:/home/hello.py /home</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-ksAbLgFM-1660189637787)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731164252387.png)]</p>

<h1>docker的其他命令</h1>

<h2>1.docker version：查看docker版本信息</h2>

<blockquote>
<p>docker version</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-nJs8U44J-1660189637788)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731163137194.png)]</p>

<h2>2.docker logs:查看容器日志</h2>

<blockquote>
<p>docker logs 容器id</p>
</blockquote>

<h2>3.docker info:查看docker的详细信息</h2>

<blockquote>
<p>docker info</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-SMtBOhvc-1660189637790)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220731163241608.png)]</p>

<pre>
<code> #所有命令
 attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container&#39;s changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container&#39;s filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container&#39;s filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

</code></pre>

<h1>docker进阶</h1>

<h2>1.如何提交一个自己的镜像</h2>

<blockquote>
<p>在日常开发中，比如我们开发到某一个阶段后，希望将当前的版本做一个记录保存下来，下次既可以直接运行这个版本，同时也不会影响项目的继续开发，此时我们可以通过docker commit命令来实现。</p>

<table>
	<thead>
		<tr>
			<th>Name, shorthand</th>
			<th>Default</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>--author</code>&nbsp;,&nbsp;<code>-a</code></td>
			<td>&nbsp;</td>
			<td>作者</td>
		</tr>
		<tr>
			<td><code>--change</code>&nbsp;,&nbsp;<code>-c</code></td>
			<td>&nbsp;</td>
			<td>Apply Dockerfile instruction to the created image</td>
		</tr>
		<tr>
			<td><code>--message</code>&nbsp;,&nbsp;<code>-m</code></td>
			<td>&nbsp;</td>
			<td>描述信息</td>
		</tr>
		<tr>
			<td><code>--pause</code>&nbsp;,&nbsp;<code>-p</code></td>
			<td><code>true</code></td>
			<td>Pause container during commit(提交期间暂停容器)</td>
		</tr>
	</tbody>
</table>

<p>例：将当前的centos运行情况等记录下来，生成一个新的镜像：</p>

<p>docker commit -a &ldquo;作者&rdquo; -m &ldquo;描述信息&rdquo; 容器id 镜像名:tag</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-tMEPhhi6-1660189637790)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220801114523685.png)]</p>

<h2>2.数据卷挂载</h2>

<blockquote>
<p>场景：通常情况下，我们将一个容器删除后，里面的数据也会一并被删除，但是有时候我们需要里面的数据，仅仅删除容器即可。</p>

<p>容器数据卷很好的解决了上述的问题，通过容器数据卷我们可以将数据同步到本地，与拷贝不同的是，容器数据卷将容器与本地&ldquo;打通&quot;，能够实时同步，并且是双向的，即在容器中生成的数据会同步到本地，同时在本地生成的文件也会同步到容器。</p>

<p>例：将容器中centos的/home目录的内容同步到本地的/home/docker-test目录</p>
</blockquote>

<pre>
<code>docker run -it -v /home/docker-test:/home centos /bin/bash
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-g7IA0oYj-1660189637791)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220801121857922.png)]</p>

<blockquote>
<p>通过docker inspect 容器id也可以查看到挂载信息：</p>
</blockquote>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-80GiuTIM-1660189637792)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220801122433936.png)]</p>

<h3>2.1具名挂载和匿名挂载</h3>

<blockquote>
<p>在对容器进行数据挂载时，不同的写法有不同的含义！</p>

<pre>
<code>#具名挂载
-v 卷名:容器内的路径

#匿名挂载
##不指定容器外的路径，默认存放在：/var/lib/docker/volumes
-v 容器的路径
##指定容器外的路径
-v 容器外的路径:容器内的路径 

#可以通过 docker volume inspect 卷名  来查看具体的信息
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-AmRO92Kk-1660189637792)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220801161636236.png)]</p>
</blockquote>

<pre>
<code>#同时也可以设置读写权限
#只读   设置只读权限后，就不能在容器内进行写操作了，但是可以在容器外进行写操作
-v 卷名:容器内路径:ro
#可读可写
-v 卷名:容器内路径:rw
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-iVfs4PY2-1660189637793)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220801162526215.png)]</p>

<h3>2.2通过dockerfile生成镜像的时候指定挂载卷</h3>

<pre>
<code>docker build -f /home/docker-test/dockerfile_ubuntu -t myubuntu:1.0 .

#dockerfile文件内容
#######################################################
FROM ubuntu 

VOLUME [&quot;volume01&quot;,&quot;volume02&quot;] #指定挂载的卷

CMD echo &quot;hello,i&#39;m building  a image...&quot;

CMD /bin/bash
######################################################
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-SCfn6Q1Z-1660189637794)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220801164846564.png)]</p>

<h3>2.3容器之间实现数据共享</h3>

<p>在启动容器的时候，通过&ndash;volumes-from 容器名 指定从哪个容器挂载,，这样可以实现容器之间的数据共享</p>

<pre>
<code>#启动一个容器
docker run -it  --name myubuntu01 myubuntu:1.0 /bin/bash

#再启动一个容器，同时挂载上面启动的容器
docker run -it  --name myubuntu02 --volumes-from myubuntu01 myubuntu:1.0 /bin/bash
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-mQYdh7ck-1660189637794)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220801171312987.png)]</p>

<h2>3.dockerFile</h2>

<blockquote>
<p>dockerfile是用来构建docker镜像的文件，是命令参数脚本。</p>
</blockquote>

<p>镜像的构建步骤：</p>

<ol>
	<li>编写一个dockerfile文件</li>
	<li>使用docker build命令</li>
	<li>docker run运行镜像</li>
	<li>docker push发布镜像</li>
</ol>

<h3><strong>dockerfile的指令</strong></h3>

<pre>
<code>FROM        # 指定基础镜像，一切从这里开始
MAINTAINER  # 镜像是谁写的，姓名+邮箱
RUN         # 镜像构建的时候要运行的命令
ADD         # 添加内容
WORKDIR     # 指定工作目录
VOLUME      # 指定挂载的卷
EXPOSE      # 要暴露的端口
CMD			# 指定这个容器启动的时候要运行的命令，只有最后一个生效，会被替代
ENTRYPOINT  # 指定这个容器启动的时候要运行的命令,可以追加命令
ONBUILD     # 当构建要给被继承的dockerfile的时候就会执行这个命令
COPY        # 类似于ADD，拷贝文件到镜像
ENV         # 设置环境变量
</code></pre>

<h3>构建一个自己ubuntu镜像</h3>

<pre>
<code>#编写知己的dockerfile文件
FROM ubuntu

MAINTAINER LLL&lt;2474605919@qq.com&gt;

ENV MYPATH /usr/local

WORKDIR $MYPATH

RUN apt-get update #更新下载包
RUN apt-get -y install vim #安装vim
RUN apt-get -y install net-tools

EXPOSE 80  

CMD echo $MYPATH

VOLUME [&quot;volume01&quot;,&quot;volume02&quot;]

CMD echo &quot;hello,i&#39;m building  a image...&quot;

CMD /bin/bash
#############################################################

#使用docker build构建
docker build -f dockerfile_ubuntu -t myubuntu:2.0 .
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-5zmNxlUZ-1660189637796)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220802103207412.png)]</p>

<pre>
<code>#使用docker run运行这个镜像
#发现vim是可使用的命令! 说明安装成功！
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-oNNVZphc-1660189637796)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220802103347757.png)]</p>

<h3>发布自己的镜像</h3>

<ol>
	<li>
	<p>在https://hub.docker.com/注册自己的账号</p>
	</li>
	<li>
	<p>使用docker login命令进行登录</p>

	<pre>
<code>docker login -u 用户名 -p 密码
</code></pre>

	<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-0JR1UN4H-1660189637797)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220803170509787.png)]</p>
	</li>
	<li>
	<p>使用docker push命令进行发布</p>

	<pre>
<code>docker tag 镜像id 用户名/镜像名:tag  #生成一个版本号
docker push 用户名/镜像名:tag    #提交
</code></pre>

	<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-vXXFzleJ-1660189637798)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220803171537787.png)]</p>
	</li>
</ol>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-tO56Lyz5-1660189637799)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220803171752808.png)]</p>

<p>如上，发布成功！</p>

<h2>4.docker网络</h2>

<h3>docker网络原理</h3>

<p>docker网络使用的是桥接模式，安装docker后，会在宿主机虚拟一个docker容器网桥(docker0)，在之后每启动一个容器时，docker都会根据docker网桥的网段分配一个ip给容器，称为container-ip，同时docker0是每个容器的默认网关。</p>

<p>因此在默认情况下，各个容器之间的网络是可以互通的。</p>

<p>容器与本地互通(默认情况下)</p>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-mR60aiHo-1660189637800)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805161205252.png)]</p>

<p>容器与容器之间互通(默认情况下)[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-PLJTD6NI-1660189637801)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805161749016.png)]</p>

<h3>docker的网络模式</h3>

<p>使用&ndash;net或&ndash;network指定网络模式</p>

<p>docker的网络模型有如下几种：</p>

<ul>
	<li>bridge:桥接，默认的模式，会为每一个容器分配ip，并将容器连接到虚拟网桥docker0上</li>
	<li>host：和宿主主机共享网络</li>
	<li>none：不配置网络，容器不能和外界相连</li>
</ul>

<p>docker默认的网络通信原理图：</p>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-LhomNPG3-1660189637802)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805170920055.png)]</p>

<h3>容器互联</h3>

<h4>&ndash;link</h4>

<blockquote>
<p>场景：虽然容器与容器之间可以互联，但是如果一个项目需要部署到多个容器中，容器之间的连接方式是通过具体ip相连的，如果服务一旦遇到问题需要重启镜像，那么由于为容器分配的ip是随机的，那么就需要从新为服务配置ip才能保证容器之间的连通。所以是否可以用一个具体的名字来代替某一个容器的ip来达到ip可变，名不变，通过名来相互连通？</p>
</blockquote>

<pre>
<code>#使用--link将当前容器与容器01&ldquo;连接&rdquo;
docker run -it --name ubuntu-net03 --link ubuntu-net01 ubuntu-net:1.0 /bin/bash
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-scVp1dmj-1660189637802)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805175611063.png)]</p>

<p>使用&ndash;link后的容器03之所以能够ping容器01的原因如下：<br />
首先我们知道在linux系统目录etc下有一个hosts文件，它用于建立ip映射，可以将一个域名映射到一个ip上，即我们直接通过域名访问即可，而这个域名具体指代哪个ip就交给系统来处理就行了。而使用&ndash;link后，就相当于在hosts文件中添加了一个域名-ip的对应关系，当然，这里的域名用的是容器的容器名和容器id，因此就可以直接通过容器名和容器id访问到了。</p>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-1Bo94GJR-1660189637803)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805175852185.png)]</p>

<h4>自定义网络</h4>

<blockquote>
<p>虽然使用&ndash;link解决了使用ip访问带来的问题，但相较于每次启动都使用&ndash;link，自定义网络更是一劳永逸，为了使两个容器能够互通，与每次启动添加&ndash;link相比，直接指定自己定义的网络更方便，也更便于维护。</p>
</blockquote>

<pre>
<code>#创建自己的网络
docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 mynet

#--driver指定模型
#--subbet指定子网
#--gateway指定网关
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-3dd9WWLv-1660189637804)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805184711784.png)]</p>

<blockquote>
<p>值得注意的是，不管是docker0，还是自定义网络，如果两个容器使用的是不同的网络，那么它们也是不能通过名字访问的，但是，对于这个问题，也有相应的解决方案！</p>
</blockquote>

<h4>网络连通</h4>

<p>docker network还提供了一个docker network connect命令，用于将一个容器添加到一个网络中，这样对于不是某一个网络中的容器要想和该网络中的容器连通，使用该命即可实现！</p>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-RwewGlfJ-1660189637804)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805190700562.png)]</p>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-R26awiaG-1660189637805)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805191036622.png)]</p>

<p>使用docker network inspect mynet命令可以对mynet的详细信息进行查看，发现在将ubuntu-net01加入mynet这个网络的同时，为它分配了一个新的ip！</p>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-gWXSXkz4-1660189637805)(C:UsersLLL03AppDataRoamingTypora	ypora-user-imagesimage-20220805191512588.png)]</p>

<h3>redis集群部署</h3>

<pre>
<code>#创建网卡
docker network create redis-net --subnet 192.161.0.0/16


# 这里如果提示权限不够的话使用 sudo su 进入root模式即可
for port in $(seq 1 6); 
do 
mkdir -p /mydata/redis/node-${port}/conf
touch /mydata/redis/node-${port}/conf/redis.conf
cat &lt;&lt; EOF &gt;/mydata/redis/node-${port}/conf/redis.conf
port 6379
bind 0.0.0.0
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
cluster-announce-ip 192.161.0.1${port}
cluster-announce-port 6379
cluster-announce-bus-port 16379
appendonly yes
EOF
done

# 使用脚本直接开启六个redis服务
for port in $(seq 1 6); 
do 
docker run -p 637${port}:6379 -p 1637${port}:16379 --name redis-${port} 
-v /mydata/reids/node-${port}/data:/data 
-v /mydata/redis/node-${port}/conf/redis.conf:/etc/redis/redis.conf 
-d --net redis-net --ip 192.161.0.1${port} redis redis-server /etc/redis/redis.conf
EOF
done

#随便进入一个redis
docker exec -it redis-1 /bin/sh

#创建集群
redis-cli --cluster create 192.161.0.11:6379 192.161.0.12:6379 192.161.0.13:6379 192.161.0.14:6379 192.161.0.15:6379 192.161.0.16:6379 --cluster-replicas 1

```#直接开启六个redis服务
for port in $(seq 1 6); 
do 
docker run -p 637${port}:6379 -p 1637${port}:16379 --name redis-${port} 
-v /mydata/reids/node-${port}/data:/data 
-v /mydata/redis/node-${port}/conf/redis.conf:/etc/redis/redis.conf 
-d --net redis-net --ip 192.161.0.1${port} redis redis-server /etc/redis/redis.conf
EOF
done

#随便进入一个redis
docker exec -it redis-1 /bin/sh

#创建集群
redis-cli --cluster create 192.161.0.11:6379 192.161.0.12:6379 192.161.0.13:6379 192.161.0.14:6379 192.161.0.15:6379 192.161.0.16:6379 --cluster-replicas 1

</code></pre>
<p><strong>​附件</strong></p><p class="extera_file"><a href="/media/file/2022/08/11/docker.pdf" target="_blank">docker.pdf</a></p>
