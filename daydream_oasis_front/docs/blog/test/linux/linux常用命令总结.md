
<BlogInfo title="linux常用命令总结" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=214 category="linux" tag_list="['Linux', '命令']" create_time="2022.08.28 16:09:51.732363" update_time="2022.08.28 16:10:14" />

^^^^^^^^^
<h1>linux常用命令总结</h1>

<p><strong>若图片无法正常显示，可以下载附件中的pdf查看。</strong></p>

<p>&nbsp;</p>

<h2>1.重启和关机</h2>

<p>重启和关机需要系统管理员用户权限。</p>

<p><strong>重启</strong></p>

<pre>
<code>init 6或者 reboot
</code></pre>

<p><strong>关机</strong></p>

<pre>
<code>init 0或者 shutdown 或者 halt
</code></pre>

<blockquote>
<p>如果没有执行关机命令，强制断电或关闭本地虚拟机的窗口，会导致linux操作系统文件的损坏，严重的可能导致操作系统无法正常启动。</p>
</blockquote>

<h2>2.清屏</h2>

<p>清除当前屏幕上显示的内容.</p>

<pre>
<code>clear
</code></pre>

<p>​</p>

<h2>3.查看服务器的地址</h2>

<pre>
<code>ip addr (ifconfig也可以进行查看)
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-xYzXNxeP-1661673888873)(/home/lll/snap/typora/57/.config/Typora/typora-user-images/image-20220828092647043.png)]</p>

<h2>4.事件操作</h2>

<p><strong>当前时间</strong></p>

<pre>
<code>date
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-i1ew5gyZ-1661673888876)(/home/lll/snap/typora/57/.config/Typora/typora-user-images/image-20220828092848342.png)]</p>

<p><strong>设置时区为中国上海时间</strong></p>

<pre>
<code>cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
</code></pre>

<p><strong>设置时间</strong></p>

<pre>
<code>date -s &quot;yyyy-mm-dd hh:ii:ss&ldquo;
#例如: date -s &quot;2022-8-28 09:30:30&quot;
</code></pre>

<h2>5.目录和文件</h2>

<p>文件系统就像一棵树，树干是/（根）目录，树枝是子目录，树枝后面还有树枝（子目录中还有子目录），树枝最好是树叶，目录的最后是文件。</p>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-GLELcPe1-1661673888878)(/home/lll/snap/typora/57/.config/Typora/typora-user-images/image-20220828094300615.png)]</p>

<p>严谨的说，文件名是由<strong>目录</strong>+<strong>文件名</strong>组成的。</p>

<ul>
	<li>从根目录开始，包含完整的目录名和文件名的是绝对路径。</li>
	<li>登录linux后，一定处在目录树的某个目录中，这个目录称之为当前工作目录，简称<strong>当前目录</strong>。</li>
	<li>文件的<strong>相对路径</strong>就是相对于当前目录所在的路径。</li>
	<li>一个圆点.表示当前工作目录。</li>
	<li>两个圆点&hellip;表示当前工作目录的上一级目录。</li>
</ul>

<p><strong>查看当前目录</strong></p>

<pre>
<code>pwd
</code></pre>

<p><strong>切换目录</strong></p>

<pre>
<code>cd 目录
#例如：
进入/etc目录: cd /etc
切换到上一级目录：cd ..
</code></pre>

<p><strong>列出目录和文件信息</strong></p>

<pre>
<code>ls 

#列出目录的详细信息：ls -l

#列出/etc目录下的内容： ls /etc

</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-qcmKYuEm-1661673888879)(/home/lll/snap/typora/57/.config/Typora/typora-user-images/image-20220828151515683.png)]</p>

<p><strong>文件的权限</strong></p>

<table>
	<thead>
		<tr>
			<th>number</th>
			<th>permission type</th>
			<th>symbol</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>no permission</td>
			<td>&mdash;</td>
		</tr>
		<tr>
			<td>1</td>
			<td>excute</td>
			<td>&ndash;x</td>
		</tr>
		<tr>
			<td>2</td>
			<td>write</td>
			<td>-w-</td>
		</tr>
		<tr>
			<td>3</td>
			<td>excute(1)+write(2)</td>
			<td>-wx</td>
		</tr>
		<tr>
			<td>4</td>
			<td>read</td>
			<td>r&ndash;</td>
		</tr>
		<tr>
			<td>5</td>
			<td>read(4)+execute(1)</td>
			<td>r-x</td>
		</tr>
		<tr>
			<td>6</td>
			<td>read(4)+write(2)</td>
			<td>rw-</td>
		</tr>
		<tr>
			<td>7</td>
			<td>read(4)+write(2)+excute(1)</td>
			<td>rwx</td>
		</tr>
	</tbody>
</table>

<p>对于通过ls -l查到的权限如下：</p>

<pre>
<code>drwxrwxr-x 4 lll lll 4096 Aug 28 11:14 aaa

#以drwxrwxr-x为例：
第一个位置的值表示当前是文件还是目录，-表示一个文件，d表示为一个目录
接着后三个位置的值表示的是创建者对该文件的权限,rwx即可读可写可执行
之后接着三个位置的值表示的是组对该文件的权限，rwx即可读可写可执行
最后的三个未知的值表示的是其他对该文件的权限，r-x即可读可执行不可写

</code></pre>

<p><strong>修改文件的权限</strong></p>

<p>方式一：chmod permission filename</p>

<pre>
<code>chmod ugo filename
u：user 对应于user的权限
g：group 对应于用户所在group的权限
o：other 对应于other的权限

例如：对于文件a.txt，让user可读可写写可执行，让group和other都没有权限
chmod 700 a.txt

</code></pre>

<p>方式二：通过符号修改</p>

<table>
	<thead>
		<tr>
			<th>operator</th>
			<th>description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>+</td>
			<td>增加一个权限</td>
		</tr>
		<tr>
			<td>-</td>
			<td>删除一个权限</td>
		</tr>
		<tr>
			<td>=</td>
			<td>修改一个权限</td>
		</tr>
	</tbody>
</table>

<pre>
<code>#例如，对于a.txt文件

#删除user在它上面的写权限
chmod u-w a.txt

#增加other在它上面的执行和写权限
chmod o+wx a.txt

#修改user的权限为可读可写可执行
chmod u=rwx a.txt

#修改所有的权限为可读可写可执行
chmod a=rwx a.txt	

</code></pre>

<p><strong>正则表达式</strong></p>

<p>正则表达式又称规则表达式，通配符，目录和文件名都支持正则表达式，正则表达式的规则比较多，比较常用的两种是：星号&ldquo;*&rdquo;和问号&ldquo;?&rdquo;。</p>

<p>星号&ldquo;*&rdquo;：匹配任意数量的字符。</p>

<p>问号&ldquo;?&rdquo;匹配任意的一个字符。</p>

<pre>
<code>#列出/tmp目录下以systemd开头的文件或目录
ls /tmp/systemd*
</code></pre>

<p><strong>创建目录</strong></p>

<pre>
<code>mkdir 目录名

#创建一个aaa目录：mkdir aaa
</code></pre>

<p><strong>创建文件</strong></p>

<pre>
<code>touch 文件名
当前路径下创建一个a.txt文件：touch a.txt
绝对路径下创建一个a.txt文件：touch /home/a.txt
</code></pre>

<p><strong>删除文件和目录</strong></p>

<pre>
<code>rm 文件名
参数：
-f 强制删除
-r 删除目录

#删除/tmp目录下的所有内容
rm -rf /tmp

#同时也可以结合正则表达式一起使用
删除/tmp目录下以.tar结尾的文件：rm -rf /tmp/*.tar 
</code></pre>

<p><strong>移动文件和目录</strong></p>

<pre>
<code>mv 旧目录或文件名 新目录或文件名
如果第二个参数是已经存在的目录，则把第一个参数（旧目录或文件）移动到该目录中。
</code></pre>

<ol>
	<li>
	<p>使用mv实现文件重命名的效果,，将当前目录下的.a.txt文件重命名为b.txt</p>

	<pre>
<code>mv a.txt b.txt
</code></pre>
	</li>
	<li>
	<p>如果bbb目录存在，以下命令将把当前工作目录下的a.txt文件移动到bbb目录中</p>

	<pre>
<code>mv a.txt bbb
</code></pre>
	</li>
	<li>
	<p>bbb/ccc目录不存在，以下命令将把当前工作目录下的a.txt文件改名为/bbb/ccc</p>

	<pre>
<code>mv a.txt bbb/ccc
</code></pre>
	</li>
</ol>

<p><strong>复制文件和目录</strong></p>

<pre>
<code>cp [-r] 旧目录或者文件名 新目录或者文件名
选项-r是复制目录，如果没有选项-r就只复制文件。
</code></pre>

<ol>
	<li>
	<p>复制文件a.txt的内容到b.txt（没有b.txt文件就会新建）</p>

	<pre>
<code>cp a.txt b.txt
</code></pre>
	</li>
	<li>
	<p>复制目录aaa到bbb/ccc</p>

	<pre>
<code>cp -r aaa bbb/ccc
#如果bbb/ccc目录不存在，就会把将aaa目录下的所有东西复制到bbb/aaa目录下

#如果bbb/ccc目录存在，就会复制到bbb/ccc/aaa下

</code></pre>
	</li>
</ol>

<h2>6.打包和压缩</h2>

<p><strong>打包</strong></p>

<pre>
<code>tar -zcvf 压缩包名 需要打包的文件1/目录1 需要打包的文件2/目录2 ...需要打包的文件n/目录n

参数含义：
-z：通过gzip的支持进行压缩/解压缩，此时文件最好为*.tar.gz
-c：创建压缩文件
-v：显示细节
-f：要操作的文件名

#例如：将目录aaa和bbb以及文件a.txt都压缩到test.tar.gz压缩包中
tar -zcvf test.tar.gz aaa bbb a.txt
</code></pre>

<p><strong>解压</strong></p>

<pre>
<code>tar -zxvf 压缩包名 解压到的目录

参数含义：
-z：通过gzip的支持进行压缩/解压，此时文件最好为*.tag.gz
-x：解压缩
-v：显示细节
-f：要操作的文件名

#例如：将test.tar.gz解压到bbb目录下
tar -zxvf test.tar.gz bbb
</code></pre>

<h2>7.判断网络是否连通</h2>

<pre>
<code>ping ip地址/域名

例如：检查是否可以连接上百度
ping www.baidu.com
</code></pre>

<h2>8.显示文本文件的内容</h2>

<p><strong>显示整个文件的内容</strong></p>

<pre>
<code>cat 文件名1 文件名2 ... 文件名n
</code></pre>

<p><strong>分页显示文件的内容</strong></p>

<pre>
<code>more 文件名1 文件名2 ... 文件名n
</code></pre>

<p><strong>显示文件尾部的内容</strong></p>

<p>tail 命令可用于查看文件的内容，有一个常用的参数 -f 常用于查阅正在改变的日志文件。</p>

<p>tail -f filename 会把 filename 文件里的最尾部的内容显示在屏幕上，并且不断刷新，只要 filename 更新就可以看到最新的文件内容。</p>

<pre>
<code>tail 文件名
</code></pre>

<h2>9.输出命令</h2>

<pre>
<code>echo &quot;内容&quot;|$变量 [&gt; 输出文件路径]

#直接在终端输出内容：
echo &quot;hello&quot;

#在终端中输出变量的值：
echo $path

#将内容输出到a.txt文件
echo &quot;hello&quot; &gt; a.txt

</code></pre>

<h2>10.搜索文件中的内容</h2>

<pre>
<code>grep [-c] &quot;内容&quot; 文件名

#如果内容中没有空格等特殊字符，可以不用双引号括起来

#例如：在views.py文件中搜索request
grep &ldquo;request&rdquo; views.py

#如果使用-c则显示的是行数

</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-lyd6ay99-1661673888880)(/home/lll/snap/typora/57/.config/Typora/typora-user-images/image-20220828115002228.png)]</p>

<h2>11.统计文本文件的行数，单词数和字节数</h2>

<pre>
<code>wc 文件名
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-MXzaEdwB-1661673888880)(/home/lll/snap/typora/57/.config/Typora/typora-user-images/image-20220828114445527.png)]</p>

<h2>12.查看系统磁盘空间使用情况</h2>

<pre>
<code>df [-h] [-T]
参数含义：
-h：以方便阅读的方式显示
-T：列出文件系统类型
</code></pre>

<p>[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-0FrjeuoY-1661673888881)(/home/lll/snap/typora/57/.config/Typora/typora-user-images/image-20220828115527303.png)]</p>

<p>&nbsp;</p>

<p><strong>​附件</strong></p>

<p><a href="/media/file/2022/08/28/linux常用命令总结.pdf" target="_blank">linux常用命令总结.pdf</a></p>

