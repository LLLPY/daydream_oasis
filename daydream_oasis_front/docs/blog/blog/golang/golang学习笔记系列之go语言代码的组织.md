
<BlogInfo title="golang学习笔记系列之go语言代码的组织" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=21 category="golang" tag_list="['golang']" create_time="2022.09.10 17:33:14.948806" update_time="2022.09.13 19:59:17" />

^^^^^^^^^
<h2>&nbsp;</h2>

<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" style="-webkit-user-select:none; background-color:hsl(0, 0%, 90%); display:block; margin:auto; transition:background-color 300ms" /></p>

<h2>代码的组织</h2>

<p>go应用使用<strong>包</strong>和<strong>模块</strong>来组织代码，包对应到文件系统就是文件夹，模块就是go的源文件。一个包中可以有很多模块，或者多个子包。</p>

<ul>
	<li>包&lt;-----&gt;文件夹</li>
	<li>模块&lt;-----&gt;go文件</li>
</ul>

<h3>项目管理工具</h3>

<p>早期的go项目使用gopath来管理项目，不方便而且容易出错，从golang1.11开始使用gomod管理项目，除此之外，还有第三方项目管理工具，例如govendor。</p>

<h4>go mod包管理步骤</h4>

<ol>
	<li>创建项目 &nbsp; &nbsp; =======&gt; &nbsp; &nbsp; &nbsp; mkdir go_pro</li>
	<li>初始化项目 =======&gt; &nbsp; &nbsp; &nbsp; 进入到项目的根目录，go mod init go_pro</li>
	<li>创建包 &nbsp; &nbsp; &nbsp; &nbsp; =======&gt; &nbsp; &nbsp; &nbsp; 在项目中创建新的包</li>
	<li>创建模块 &nbsp; &nbsp; =======&gt; &nbsp; &nbsp; &nbsp; 在项目中直接创建模块或者在新创的包中创建模块</li>
	<li>相互调用 &nbsp; &nbsp; =======&gt; &nbsp; &nbsp; &nbsp; 项目中各模块之间可以相互调用</li>
</ol>

