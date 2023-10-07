
<BlogInfo title="golang学习笔记系列之标识符，关键字以及命名规则" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=96 category="golang" tag_list="['golang']" create_time="2022.09.10 17:48:20.288849" update_time="2022.09.13 19:58:21" />

^^^^^^^^^
<h3>&nbsp;</h3>

<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" style="-webkit-user-select:none; background-color:hsl(0, 0%, 90%); display:block; margin:auto; transition:background-color 300ms" /></p>

<h3>标识符</h3>

<p>标识符的英文是<strong>identifier</strong>，通俗地讲，就是给变量，常量，函数，结构体，数组，切片，接口起名字。</p>

<h4>标识符的规范要求</h4>

<ul>
	<li>由数字，字母，下划线组成</li>
	<li>不能以数字开头</li>
	<li>区分大小写</li>
	<li>尽量做到见名知意</li>
</ul>

<pre>
<code>//正确的标识符
var abc string
var a12 int
var _123 int[]

//错误的标识符
var 123abc int //不能以数字开头
var abc&amp;afa string //出现了未知的字符
</code></pre>

<h3>关键字</h3>

<p>Go 共有 25 个保留关键字，各有其作用，不能用作<a href="https://so.csdn.net/so/search?q=%E6%A0%87%E8%AF%86%E7%AC%A6&amp;spm=1001.2101.3001.7020">标识符</a>。Go 的 25 个关键字按照作用可以分为 3 类，分别为包管理、程序实体声明与定义与程序流程控制。</p>

<pre>
<code>包管理（2个）：
	import	package

程序实体声明与定义（8个）：
	chan	const	func	interface	map	struct	type	var

程序流程控制（15个）：
	break	case	continue	default	defer	else	fallthrough	
	for		go		goto		if		range	return	select		switch
</code></pre>

<p>除了上面的保留关键字，go语言还有36个预定义标识符，其中包含了基本类型名称和一些基本的内置函数，如下表：</p>

<table>
	<thead>
		<tr>
			<th>append</th>
			<th>bool</th>
			<th>byte</th>
			<th>cap</th>
			<th>close</th>
			<th>complex</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>complex64</td>
			<td>complex128</td>
			<td>uint16</td>
			<td>copy</td>
			<td>false</td>
			<td>float32</td>
		</tr>
		<tr>
			<td>float64</td>
			<td>imag</td>
			<td>int</td>
			<td>int8</td>
			<td>int16</td>
			<td>uint32</td>
		</tr>
		<tr>
			<td>int32</td>
			<td>int64</td>
			<td>iota</td>
			<td>len</td>
			<td>make</td>
			<td>new</td>
		</tr>
		<tr>
			<td>nil</td>
			<td>panic</td>
			<td>unit64</td>
			<td>print</td>
			<td>println</td>
			<td>real</td>
		</tr>
		<tr>
			<td>recover</td>
			<td>string</td>
			<td>true</td>
			<td>uint</td>
			<td>uint8</td>
			<td>uintprt</td>
		</tr>
	</tbody>
</table>

<h3>命名规则</h3>

<h4>区分大小写</h4>

<p>命名规则涉及变量，常量，全局函数，结构，接口，方法等的命名。go语言从语法层面进行了以下限定：任何需要对外暴露的名字必须以大写字母开头，不需要对外暴露的则应该以小写字母开头。</p>

<p>当命名以一个大写字母开头，如：Hello，那么使用这种形式的标识符的对象就<strong>可以被外部包的代码所使用</strong>（前提是导入了这个包），这被称为导出（类似于java中的public）；命名如果以小写字母开头，则<strong>对包外是不可见的</strong>，但是它们在整个包的内部是可见并可用的（类似于java中的private）。</p>

<p><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/323ed093cd0d48509e4e920bff1a6e49.png#pic_center" /></p>

<h4>包名称</h4>

<p>保持package的名称和目录一致，尽量采取有意义的包名，简洁明了，尽量不要和标准库冲突。包名应该为<strong>小写</strong>单词，不要使用下划线或者混合大小写。</p>

<h4>文件名</h4>

<p>尽量采取简洁明了的文件名，简短，有意义，应该为<strong>小写</strong>单词，使用<strong>下划线</strong>分割各个单词。</p>

<h4>结构体命名</h4>

<p>一般采用驼峰命名法，首字母根据访问控制来规定大小写。</p>

<pre>
<code>//客户订单
type CustomerOrder struct {
    Name string
    Address string 
}

order := CustomerOrder{&quot;tom&quot;, &quot;上海&quot;}
</code></pre>

<h4>接口命名</h4>

<p>命名规则同结构体。</p>

<p>单个函数的结构名以&ldquo;er&rdquo;作为后缀，例如：Reader，Writer。</p>

<pre>
<code>type Reader interface {
    Read(p []byte) (n int, err error) 
    
}
</code></pre>

<h4>变量命名</h4>

<p>基本命名规则同结构体，但遇到特有名词时，需要遵循以下规则：</p>

<ul>
	<li>
	<p>如果变量为私有，且特有名词为首个单词，则使用小写，如appService若变量类型为bool，则名称应以Has，Is，Can或Allow开头</p>
	</li>
	<li>
	<pre>
<code>var isExist bool
var hasConflict bool
var canManage bool
var allowGitHook bool
</code></pre>
	</li>
</ul>

<h4>常量命名</h4>

<p>常量均使用大写字母组成，并且使用下划线分割单词。</p>

<pre>
<code>const APP_URL = &ldquo;http://www.lll.plus&rdquo;
</code></pre>

<p>如果是枚举类型的常量，需要首先创建相应的类型</p>

<pre>
<code>type Scheme string

const (
	HTTP Scheme = &quot;http&quot;
    HTTPS Scheme = &quot;https&quot;
)</code></pre>

