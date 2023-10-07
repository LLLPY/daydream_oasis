
<BlogInfo title="golang学习笔记系列之go语言的环境搭建-linux系统" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=5 category="golang" tag_list="['golang', '安装', '环境搭建']" create_time="2022.07.28 12:38:00" update_time="2022.09.10 18:08:00" />

^^^^^^^^^
<p><strong>目录</strong></p>

<p>&nbsp;</p>

<p><a href="#1.%E4%B8%8B%E8%BD%BDgolang">1.下载golang</a></p>

<p><a href="#2.%E5%AE%89%E8%A3%85">2.安装</a></p>

<p><a href="#2.1%E7%A7%BB%E9%99%A4%E4%B9%8B%E5%89%8D%E7%9A%84%E5%AE%89%E8%A3%85%E6%AE%8B%E7%95%99%EF%BC%8C%E5%90%8C%E6%97%B6%E5%AE%89%E8%A3%85%E5%BD%93%E5%89%8D%E7%89%88%E6%9C%AC">2.1移除之前的安装残留，同时安装当前版本</a></p>

<p><a href="#2.2%20%E6%B7%BB%E5%8A%A0%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F">2.2 添加环境变量</a></p>

<p><a href="#2.3%E6%A3%80%E6%9F%A5%E6%98%AF%E5%90%A6%E5%AE%89%E8%A3%85%E6%88%90%E5%8A%9F">2.3检查是否安装成功</a></p>

<p><a href="#3.%E7%BC%96%E5%86%99%E7%AC%AC%E4%B8%80%E4%B8%AAgo%E6%96%87%E4%BB%B6%C2%A0%EF%BC%81">3.编写第一个go文件&nbsp;！</a></p>

<hr />
<p>&nbsp;</p>

<h1>1.下载golang</h1>

<p>下载地址：<a class="link-info" href="https://golang.google.cn/dl/" title="golang">golang</a></p>

<p>如下图所示，找到golang的下载地址后，下载对应的linux版的最新版</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/de69d45f1c174e64a5009871286a6d64.png" style="height:811px; width:1200px" /></p>

<h1>2.安装</h1>

<p>我们按照官方给的提示安装：</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/e3cc07dee84745b0a405e8115cf53420.png" style="height:614px; width:833px" /></p>

<h2>2.1移除之前的安装残留，同时安装当前版本</h2>

<p>执行命令(普通用户可能权限不够，所以加了sudo)：</p>

<pre>
<code class="language-bash">sudo rm -rf /usr/local/go &amp;&amp; tar -C /usr/local -xzf go1.18.4.linux-amd64.tar.gz</code></pre>

<h2>2.2 添加环境变量</h2>

<p>执行命令：</p>

<pre>
<code class="language-bash">export PATH=$PATH:/usr/local/go/bin</code></pre>

<h2>2.3检查是否安装成功</h2>

<p>执行命令：</p>

<pre>
<code class="language-bash">go version</code></pre>

<p>&nbsp;如果提示了go语言的版本，就说明安装成功啦！</p>

<p><img alt="" src="https://img-blog.csdnimg.cn/28ba454d83824328a6f615ca2228563f.png" style="height:71px; width:719px" /></p>

<h1>3.编写第一个go文件&nbsp;！</h1>

<p>打开任一编辑器，输入如下代码(以hello.go命名文件)：</p>

<pre>
<code class="language-Go">package main
import "fmt"

func main()  {
	
	fmt.Println("hello,go!")
}

</code></pre>

<p>同目录下在终端中输入：</p>

<pre>
<code class="language-bash">go run hello.go</code></pre>

<p><img alt="" src="https://img-blog.csdnimg.cn/ce848144e51a43c8a4f31e4f99cdfe1e.png" style="height:157px; width:565px" /></p>

<p>&nbsp;如上，执行成功！</p>
