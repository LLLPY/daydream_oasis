
<BlogInfo title="golang学习笔记系列之基本数据类型" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=543 category="golang" tag_list="['golang']" create_time="2022.09.10 17:57:57.594559" update_time="2022.09.13 19:56:52" />

^^^^^^^^^
<p>&nbsp;</p>

<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" style="-webkit-user-select:none; background-color:hsl(0, 0%, 90%); display:block; margin:auto; transition:background-color 300ms" /></p>

<h2>基本数据类型</h2>

<p>在go语言中，数据类型用于声明函数和变量。</p>

<p>数据类型的出现是为了把数据分成所需内存大小不同的数据，编程的时候需要用大数据的时候才去申请大内存，需要小数据的时候就去申请小的内存，就可以充分利用空间。</p>

<p>go语言按类别有以下几种数据：</p>

<table>
	<thead>
		<tr>
			<th>类型</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>布尔类型</td>
			<td>布尔类型的值只可以是常量true或false。一个简单的例子：var flag=true</td>
		</tr>
		<tr>
			<td>数字类型</td>
			<td>数字类型包括整型int，浮点型float32和浮点型float64；同时支持复数。（注意：<strong>不能用0或者非0表示条件判断</strong>）</td>
		</tr>
		<tr>
			<td>字符串类型</td>
			<td>字符串就是一串固定长度的字符连接起来的字符序列。go语言的字符串是由单个字节连接起来的，go语言的字符串的字节使用utf8编码标识unicode文本。</td>
		</tr>
		<tr>
			<td>派生类型</td>
			<td>派生类型包括：指针类型，数组类型，切片类型，结构体类型，channel类型，接口类型，map类型等等</td>
		</tr>
	</tbody>
</table>

<h3>整数类型</h3>

<p>go语言也有基于架构的类型，例如：int，uint和uintptr。</p>

<table>
	<thead>
		<tr>
			<th>类型</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>uint8</td>
			<td>无符号8位整型（0到255）</td>
		</tr>
		<tr>
			<td>uint16</td>
			<td>无符号16位整数（0到65535）</td>
		</tr>
		<tr>
			<td>uint32</td>
			<td>无符号32位整数（0到4294967295）</td>
		</tr>
		<tr>
			<td>uint64</td>
			<td>无符号64位整数（0到18446744073709551616）</td>
		</tr>
		<tr>
			<td>int8</td>
			<td>有符号8位整数（-128到127）</td>
		</tr>
		<tr>
			<td>int16</td>
			<td>有符号16位整数（-32768到32767）</td>
		</tr>
		<tr>
			<td>int32</td>
			<td>有符号32位整数（-2147483648到2147483647）</td>
		</tr>
		<tr>
			<td>int64</td>
			<td>有符号64位整数（-9223372036854775808到9223372036854775807）</td>
		</tr>
	</tbody>
</table>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;math&quot;
	&quot;unsafe&quot;
)

func main() {

	var a uint8
	var b uint16
	var c uint32
	var d uint64

	fmt.Printf(&quot;a: %v %T %dB  %v~%v
&quot;, a, a, unsafe.Sizeof(a), 0, math.MaxUint8)
	fmt.Printf(&quot;b: %v %T %dB  %v~%v
&quot;, b, b, unsafe.Sizeof(b), 0, math.MaxUint16)
	fmt.Printf(&quot;c: %v %T %dB  %v~%v
&quot;, c, c, unsafe.Sizeof(c), 0, math.MaxUint32)
	fmt.Printf(&quot;d: %v %T %dB  %v~%v
&quot;, d, d, unsafe.Sizeof(d), 0, math.MaxInt64)

	var e int8
	var f int16
	var g int32
	var h int64
	fmt.Printf(&quot;e: %v %T %dB  %v~%v
&quot;, e, e, unsafe.Sizeof(e), math.MinInt8, math.MaxInt8)
	fmt.Printf(&quot;f: %v %T %dB  %v~%v
&quot;, f, f, unsafe.Sizeof(f), math.MinInt16, math.MaxInt16)
	fmt.Printf(&quot;g: %v %T %dB  %v~%v
&quot;, g, g, unsafe.Sizeof(g), math.MinInt32, math.MaxInt32)
	fmt.Printf(&quot;h: %v %T %dB  %v~%v
&quot;, h, h, unsafe.Sizeof(h), math.MinInt64, math.MaxInt64)

	var i float32
	var j float64
	fmt.Printf(&quot;i: %v %T %dB  %v~%v
&quot;, i, i, unsafe.Sizeof(i), -math.MaxFloat32, math.MaxFloat32)
	fmt.Printf(&quot;j: %v %T %dB  %v~%v
&quot;, j, j, unsafe.Sizeof(j), -math.MaxFloat64, math.MaxFloat64)

	var k complex64
	var l complex128
	fmt.Printf(&quot;k: %v %T %dB  
&quot;, k, k, unsafe.Sizeof(k))
	fmt.Printf(&quot;l: %v %T %dB  
&quot;, l, l, unsafe.Sizeof(l))

}

/*
a: 0 uint8 1B  0~255
b: 0 uint16 2B  0~65535
c: 0 uint32 4B  0~4294967295
d: 0 uint64 8B  0~9223372036854775807
e: 0 int8 1B  -128~127
f: 0 int16 2B  -32768~32767
g: 0 int32 4B  -2147483648~2147483647
h: 0 int64 8B  -9223372036854775808~9223372036854775807
i: 0 float32 4B  -3.4028234663852886e+38~3.4028234663852886e+38
j: 0 float64 8B  -1.7976931348623157e+308~1.7976931348623157e+308
k: (0+0i) complex64 8B  
l: (0+0i) complex128 16B 
*/

</code></pre>

<h3>进制的相互转换</h3>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//十进制的数
	a := 10

	fmt.Printf(&quot;a的十进制表示a: %d
&quot;, a)
	fmt.Printf(&quot;a的二进制表示a: %b
&quot;, a)
	fmt.Printf(&quot;a的八进制表示a: %o
&quot;, a)
	fmt.Printf(&quot;a的十六进制表示a: %x
&quot;, a)

	//定义一个八进制的数 以0开头
	b := 077

	fmt.Printf(&quot;b的十进制表示a: %d
&quot;, b)
	fmt.Printf(&quot;b的二进制表示a: %b
&quot;, b)
	fmt.Printf(&quot;b的八进制表示a: %o
&quot;, b)
	fmt.Printf(&quot;b的十六进制表示a: %x
&quot;, b)

	//定义一个十六进制的数 以0x开头
	c := 0x111

	fmt.Printf(&quot;c的十进制表示a: %d
&quot;, c)
	fmt.Printf(&quot;c的二进制表示a: %b
&quot;, c)
	fmt.Printf(&quot;c的八进制表示a: %o
&quot;, c)
	fmt.Printf(&quot;c的十六进制表示a: %x
&quot;, c)

}

</code></pre>

<h3>浮点类型</h3>

<table>
	<thead>
		<tr>
			<th>类型</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>float32</td>
			<td>IEEE-754 32位浮点型数</td>
		</tr>
		<tr>
			<td>float64</td>
			<td>IEEE-754 64位浮点型数</td>
		</tr>
		<tr>
			<td>complex64</td>
			<td>32位实数和虚数</td>
		</tr>
		<tr>
			<td>complex128</td>
			<td>64位实数和虚数</td>
		</tr>
	</tbody>
</table>

<h3>其他数字类型</h3>

<table>
	<thead>
		<tr>
			<th>类型</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>byte</td>
			<td>类似uint8</td>
		</tr>
		<tr>
			<td>rune</td>
			<td>类似int32</td>
		</tr>
	</tbody>
</table>

<h3>字符串类型</h3>

<p>在go语言中，字符串使用双引号&quot;&quot;或者反引号来创建。双引号用来创建可解析的字符串，支持转义，但不能用来引用多行；反引号用来创建原生的字符串，可由多行组成，但不支持转义，并且可以包含除了反引号外其他所有字符。双引号创建可解析的字符串应用最广泛，反引号用来创建原生的字符串多用于书写多行消息，HTML以及正则表达式。</p>

<h4>字符串的拼接</h4>

<pre>
<code>package main

import (
	&quot;bytes&quot;
	&quot;fmt&quot;
	&quot;strings&quot;
)

func main() {

	//单行字符串 支持转义
	a := &quot;hello world&quot;

	//多行字符串 不支持转义
	b := `
			</code></pre>

<div>
<p><code>hello</code></p>
</div>

<p><code>` fmt.Printf(&quot;a: %v
&quot;, a) fmt.Printf(&quot;b: %v
&quot;, b) //字符串的拼接 s1 := &quot;hello&quot; s2 := &quot;world&quot; //1.加号拼接 res1 := s1 + &quot; &quot; + s2 fmt.Printf(&quot;s: %v
&quot;, res1) //2.字符串格式化 Sprintf res2 := fmt.Sprintf(&quot;%s %s&quot;, s1, s2) fmt.Printf(&quot;res2: %v
&quot;, res2) //3.strings.join() /* join会根据字符串数组得到内容，计算出一个拼接之后的字符串的长度，然后申请对应大小的内存，一个一个字符填入， 在已有一个数组的情况下，这种效率会很高，但是本来没有，去构造这个数组的代价也很高 */ res3 := strings.Join([]string{s1, s2}, &quot; &quot;) //第一个参数是字符串数组，第二个参数是连接符 fmt.Printf(&quot;res3: %v
&quot;, res3) //4.buffer.WriteString() /* 这个比较理想，可以当成可变字符串使用，对内存的增长也有优化，如果能预估字符串的长度，还可以使用buffer.Grow()接口来设置capacity 同时这是直接写到缓冲区，因此效率比较高 */ var buffer bytes.Buffer buffer.WriteString(s1) buffer.WriteString(s2) fmt.Printf(&quot;buffer.String(): %v
&quot;, buffer.String()) } </code></p>

<h4>转义字符</h4>

<p>go语言的字符串常见的转义字符包含回车，换行，单双引号，制表符等</p>

<table>
	<thead>
		<tr>
			<th>转义符</th>
			<th>含义</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td></td>
			<td>回车符号</td>
		</tr>
		<tr>
			<td>
</td>
			<td>换行符</td>
		</tr>
		<tr>
			<td>	</td>
			<td>制表符（tab键，或者四个空格）</td>
		</tr>
		<tr>
			<td>&rsquo;</td>
			<td>单引号</td>
		</tr>
		<tr>
			<td>&quot;</td>
			<td>双引号</td>
		</tr>
		<tr>
			<td>\</td>
			<td>反斜杠</td>
		</tr>
	</tbody>
</table>

<h4>切片操作</h4>

<pre>
<code>//切片操作
	s := &quot;I am a student.&quot;
	m, n := 2, 4

	fmt.Printf(&quot;s[m:n]: %v
&quot;, s[m:n]) //获取字符串s索引位置从m到n-1的值
	fmt.Printf(&quot;s[:n]: %v
&quot;, s[:n])   //获取字符串s索引位置从0到n-1的值
	fmt.Printf(&quot;s[m:]: %v
&quot;, s[m:])   //获取字符串s索引位置从m到len(s)-1的值
	fmt.Printf(&quot;s[:]: %v
&quot;, s[:])     //获取字符串s
	fmt.Printf(&quot;s[m]: %v
&quot;, s[m])     //获取字符串s索引位置m的字符的ascii值
</code></pre>

<h4>字符串的一些常用方法</h4>

<table>
	<thead>
		<tr>
			<th>方法</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>len(s)</td>
			<td>获取字符串s的长度</td>
		</tr>
		<tr>
			<td>+或者fmt.Sprintf</td>
			<td>拼接字符串</td>
		</tr>
		<tr>
			<td>strings.Split(s,seq)</td>
			<td>用分隔符seq分割字符s</td>
		</tr>
		<tr>
			<td>strings.Contains(s,subs)</td>
			<td>查询字符串s中是否包含子串subs</td>
		</tr>
		<tr>
			<td>strings.HasPrefix(s,prefix)/strings.HasSuffix(s,suffix)</td>
			<td>判断前/后缀是否是指定的字符串</td>
		</tr>
		<tr>
			<td>strings.Index(s,subs)/strings.LastIndex(s,subs)</td>
			<td>查询子串subs在s中第一次(最后一次)出现的索引位置，若没有则返回-1</td>
		</tr>
		<tr>
			<td>strings.join(s_arr,seq)</td>
			<td>将字符串数组用seq拼接成一个字符串</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//分割字符串
	fmt.Printf(&quot;strings.Split(s, &quot; &quot;): %v
&quot;, strings.Split(s, &quot; &quot;))

	//查询某个字符串是否包含指定的字符串
	fmt.Printf(&quot;strings.Contains(s, &quot;student&quot;): %v
&quot;, strings.Contains(s, &quot;student&quot;))

	//判断前缀是否是指定的字符串
	fmt.Printf(&quot;strings.HasPrefix(s, &quot;hello&quot;): %v
&quot;, strings.HasPrefix(s, &quot;hello&quot;))

	//判断后缀是否是指定的字符串
	fmt.Printf(&quot;strings.HasSuffix(s, &quot;student.&quot;): %v
&quot;, strings.HasSuffix(s, &quot;student.&quot;))

	//查找指定字符串第一次出现的索引位置
	fmt.Printf(&quot;strings.Index(s, &quot;a&quot;): %v
&quot;, strings.Index(s, &quot;aaa&quot;))

	//查找指定字符串最后一次出现的索引位置
	fmt.Printf(&quot;strings.LastIndex(s, &quot;a&quot;): %v
&quot;, strings.LastIndex(s, &quot;a&quot;))

	//拼接字符串数组
	fmt.Printf(&quot;strings.Join([]string{&quot;i&quot;, &quot;am&quot;, &quot;a&quot;, &quot;student.&quot;}, &quot; &quot;): %v
&quot;, strings.Join([]string{&quot;i&quot;, &quot;am&quot;, &quot;a&quot;, &quot;student.&quot;}, &quot; &quot;))
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>strings.Split(s, &quot; &quot;): [I am a student.]
strings.Contains(s, &quot;student&quot;): true
strings.HasPrefix(s, &quot;hello&quot;): false
strings.HasSuffix(s, &quot;student.&quot;): true
strings.Index(s, &quot;a&quot;): -1
strings.LastIndex(s, &quot;a&quot;): 5
strings.Join([]string{&quot;i&quot;, &quot;am&quot;, &quot;a&quot;, &quot;student.&quot;}, &quot; &quot;): i am a student.
</code></pre>

<h3>格式化输出</h3>

<h4>普通占位符</h4>

<table>
	<thead>
		<tr>
			<th>占位符</th>
			<th>说明</th>
			<th>举例</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>%v</td>
			<td>相应值的默认格式。</td>
			<td>fmt.Printf(&ldquo;a: %v
&rdquo;, 100) ----&gt; a:100</td>
		</tr>
		<tr>
			<td>%#v</td>
			<td>会打印出数据的完整格式。</td>
			<td>tom := studnet{&ldquo;Tom&rdquo;}fmt.Printf(&ldquo;tom: %#v
&rdquo;, tom) ----&gt;tom: main.studnet{Name:&ldquo;Tom&rdquo;}</td>
		</tr>
		<tr>
			<td>%T</td>
			<td>相应值的类型。</td>
			<td>fmt.Printf(&ldquo;a: %T
&rdquo;, 100) ----&gt; a:int</td>
		</tr>
		<tr>
			<td>%%</td>
			<td>输出%。</td>
			<td>fmt.Printf(&ldquo;%%&rdquo;) ----&gt;%</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//相应数据的默认格式
a := 10
fmt.Printf(&quot;a: %#v
&quot;, a)

tom := studnet{&quot;Tom&quot;}
//数据的完整格式
fmt.Printf(&quot;tom: %#v
&quot;, tom)

//%
fmt.Printf(&quot;%%
&quot;)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>a: 10
tom: main.studnet{Name:&quot;Tom&quot;}
%
</code></pre>

<h4>布尔占位符</h4>

<table>
	<thead>
		<tr>
			<th>占位符</th>
			<th>说明</th>
			<th>举例</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>%t</td>
			<td>输出true或false。</td>
			<td>fmt.Printf(&ldquo;flag: %t
&rdquo;, true) ----&gt;true</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//布尔占位符
flag := true
fmt.Printf(&quot;flag: %t
&quot;, flag)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>flag: true
</code></pre>

<h4>整数占位符</h4>

<table>
	<thead>
		<tr>
			<th>占位符</th>
			<th>说明</th>
			<th>举例</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>%b</td>
			<td>输出二进制表示</td>
			<td>fmt.Printf(&ldquo;%b
&rdquo;, 10) ----&gt;1010</td>
		</tr>
		<tr>
			<td>%c</td>
			<td>相应的Unicode码值所表示的码符</td>
			<td>fmt.Printf(&ldquo;%c
&rdquo;,97) ----&gt;a</td>
		</tr>
		<tr>
			<td>%d</td>
			<td>输出十进制表示</td>
			<td>fmt.Printf(&ldquo;%d
&rdquo;, 10) ----&gt;10</td>
		</tr>
		<tr>
			<td>%o</td>
			<td>输出八进制表示</td>
			<td>fmt.Printf(&ldquo;%o
&rdquo;, 10) ----&gt;12</td>
		</tr>
		<tr>
			<td>%x</td>
			<td>十六进制表示（小写字母）</td>
			<td>fmt.Printf(&ldquo;%x
&rdquo;, 10) ----&gt;a</td>
		</tr>
		<tr>
			<td>%X</td>
			<td>十六进制表示（大写字母）</td>
			<td>fmt.Printf(&ldquo;%X
&rdquo;, 10) ----&gt;A</td>
		</tr>
		<tr>
			<td>%q</td>
			<td>单引号围绕的字符字面值，由go语法安全的转义</td>
			<td>fmt.Printf(&ldquo;%q
&rdquo;, 10) ----&gt;&lsquo;
&rsquo;</td>
		</tr>
		<tr>
			<td>%U</td>
			<td>Unicode格式：U+1234等同于&ldquo;U+%04X&rdquo;</td>
			<td>fmt.Printf(&ldquo;%U
&rdquo;, 10) ----&gt;U+000A</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//二进制输出
fmt.Printf(&quot;%b
&quot;, 10)

//相应的Unicode码值对应的码符
fmt.Printf(&quot;%c
&quot;, 97)

//八进制
fmt.Printf(&quot;%o
&quot;, 10)

//十六进制 小写字母
fmt.Printf(&quot;%x
&quot;, 10)

//十六进制 大写字母
fmt.Printf(&quot;%X
&quot;, 10)

fmt.Printf(&quot;%q
&quot;, 10)
fmt.Printf(&quot;%U
&quot;, 10)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>1010
a
12
a
A
&#39;
&#39;
U+000A
</code></pre>

<h4>浮点数和复数占位符</h4>

<table>
	<thead>
		<tr>
			<th>占位符</th>
			<th>说明</th>
			<th>举例</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>%b</td>
			<td>无小数部分的，指数为二的幂的科学计数法，与strconv.FormatFloat的&rsquo;b&rsquo;转换格式一样</td>
			<td>fmt.Printf(&ldquo;%b
&rdquo;, 10.1) ----&gt;5685794529555251p-49</td>
		</tr>
		<tr>
			<td>%e</td>
			<td>科学计数法（小写字母）</td>
			<td>fmt.Printf(&ldquo;%e
&rdquo;, 10.1) ----&gt;1.010000e+01</td>
		</tr>
		<tr>
			<td>%E</td>
			<td>科学计数法（大写字母）</td>
			<td>fmt.Printf(&ldquo;%E
&rdquo;, 10.1) ----&gt;1.010000E+01</td>
		</tr>
		<tr>
			<td>%f</td>
			<td>有小数点而无指数</td>
			<td>fmt.Printf(&ldquo;%5.2f
&rdquo;, 10.1) ----&gt;10.10（总长度为5，小数点两位）</td>
		</tr>
		<tr>
			<td>%g</td>
			<td>根据情况选择%e或%f以产生更紧凑的输出（无末尾的0）</td>
			<td>fmt.Printf(&ldquo;%g
&rdquo;, 10.10000) ----&gt;10.1</td>
		</tr>
		<tr>
			<td>%G</td>
			<td>根据情况选择%E或%f以产生更紧凑的输出（无末尾的0）</td>
			<td>fmt.Printf(&ldquo;%G
&rdquo;, 10.000+2.0600i) ----&gt;(10+2.06i)</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//浮点数和复数
fmt.Printf(&quot;%b
&quot;, 10.1)
fmt.Printf(&quot;%e
&quot;, 10.1)
fmt.Printf(&quot;%E
&quot;, 10.1)
fmt.Printf(&quot;2%5.2f2
&quot;, 10.1)
fmt.Printf(&quot;%g
&quot;, 10.10000)
fmt.Printf(&quot;%G
&quot;, 10.000+2.0600i)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>5685794529555251p-49
1.010000e+01
1.010000E+01
210.102
10.1
(10+2.06i)
</code></pre>

<h4>字符串与字节切片占位符</h4>

<table>
	<thead>
		<tr>
			<th>占位符</th>
			<th>说明</th>
			<th>举例</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>%s</td>
			<td>输出字符串表示（string类型或[]byte类型）</td>
			<td>fmt.Printf(&ldquo;[]byte{&ldquo;hello&rdquo;, &ldquo;world&rdquo;}: %s
&rdquo;, []byte(&ldquo;hello&rdquo;)) ----&gt;[]byte{&ldquo;hello&rdquo;, &ldquo;world&rdquo;}: hello</td>
		</tr>
		<tr>
			<td>%q</td>
			<td>双引号围绕的字符串，由go语言安全地转义</td>
			<td>fmt.Printf(&ldquo;&ldquo;hello&rdquo;: %q
&rdquo;, &ldquo;hello&rdquo;) ----&gt;&ldquo;hello&rdquo;</td>
		</tr>
		<tr>
			<td>%x</td>
			<td>十六进制，小写字母，每字节两个字符</td>
			<td>fmt.Printf(&ldquo;&ldquo;hello&rdquo;: %x
&rdquo;, &ldquo;hello&rdquo;) ----&gt;&ldquo;hello&rdquo;: 68656c6c6f</td>
		</tr>
		<tr>
			<td>%X</td>
			<td>十六进制，大写字母，每字节两个字符</td>
			<td>fmt.Printf(&ldquo;&ldquo;hello&rdquo;: %X
&rdquo;, &ldquo;hello&rdquo;) ----&gt;&ldquo;hello&rdquo;: 68656C6C6F</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//字符串
fmt.Printf(&quot;[]byte{&quot;hello&quot;, &quot;world&quot;}: %s
&quot;, []byte(&quot;hello&quot;))
fmt.Printf(&quot;&quot;hello&quot;: %q
&quot;, &quot;hello&quot;)
fmt.Printf(&quot;&quot;hello&quot;: %x
&quot;, &quot;hello&quot;)
fmt.Printf(&quot;&quot;hello&quot;: %X
&quot;, &quot;hello&quot;)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>[]byte{&quot;hello&quot;, &quot;world&quot;}: hello
&quot;hello&quot;: &quot;hello&quot;
&quot;hello&quot;: 68656c6c6f
&quot;hello&quot;: 68656C6C6F
</code></pre>

<h4>指针占位符</h4>

<table>
	<thead>
		<tr>
			<th>占位符</th>
			<th>说明</th>
			<th>举例</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>%p</td>
			<td>十六进制表示，输出指针所指向的地址</td>
			<td>h := 100 p_h := &amp;h fmt.Printf(&ldquo;%p
&rdquo;, &amp;h) fmt.Printf(&ldquo;%p
&rdquo;, p_h) ----&gt;两个输出是一样的：0xc0000ba018，都是输出的h的地址</td>
		</tr>
	</tbody>
</table>

<pre>
<code>h := 100
p_h := &amp;h
fmt.Printf(&quot;h: %p
&quot;, &amp;h)
fmt.Printf(&quot;p_h: %p
&quot;, p_h)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>h: 0xc0000140f8
p_h: 0xc0000140f8
</code></pre>

<h3>golang运算符</h3>

<p>go语言内置的运算符有：</p>

<ul>
	<li>算术运算符</li>
	<li>关系运算符</li>
	<li>逻辑运算符</li>
	<li>位运算符</li>
	<li>赋值运算符</li>
</ul>

<h4>算术运算符</h4>

<table>
	<thead>
		<tr>
			<th>运算符</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>+</td>
			<td>相加</td>
		</tr>
		<tr>
			<td>-</td>
			<td>相减</td>
		</tr>
		<tr>
			<td>*</td>
			<td>相乘</td>
		</tr>
		<tr>
			<td>/</td>
			<td>相除</td>
		</tr>
		<tr>
			<td>%</td>
			<td>取模（求余）</td>
		</tr>
	</tbody>
</table>

<blockquote>
<p>注意：++（自增）和&ndash;（自减）在go语言中是单独的语句，并不是运算符。</p>
</blockquote>

<pre>
<code>a := 100
	b := 200
	//算术运算符
	res := a + b
	fmt.Printf(&quot;res: %v
&quot;, res)

	res = a - b
	fmt.Printf(&quot;res: %v
&quot;, res)

	res = a * b
	fmt.Printf(&quot;res: %v
&quot;, res)

	res = a / b
	fmt.Printf(&quot;res: %v
&quot;, res)

	res = a % b
	fmt.Printf(&quot;res: %v
&quot;, res)
	a++
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>res: 300
res: -100
res: 20000
res: 0
res: 100
</code></pre>

<h4>关系运算符</h4>

<table>
	<thead>
		<tr>
			<th>运算符</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>==</td>
			<td>检查两个值是否相等，返回true或false</td>
		</tr>
		<tr>
			<td>!=</td>
			<td>检查两个值是否不相等，返回true或false</td>
		</tr>
		<tr>
			<td>&gt;</td>
			<td>检查左边的值是否大于右边的值，返回true或false</td>
		</tr>
		<tr>
			<td>&gt;=</td>
			<td>检查左边的值是否大于等于右边的值，返回true或false</td>
		</tr>
		<tr>
			<td>&lt;</td>
			<td>检查左边的值是否小于右边的值，返回true或false</td>
		</tr>
		<tr>
			<td>&lt;=</td>
			<td>检查左边的值是否小于等于右边的值，返回true或false</td>
		</tr>
	</tbody>
</table>

<pre>
<code>// 关系运算符
	var res2 bool

	res2 = a == b
	fmt.Printf(&quot;res2: %v
&quot;, res2)

	res2 = a &gt; b
	fmt.Printf(&quot;res2: %v
&quot;, res2)

	res2 = a &gt;= b
	fmt.Printf(&quot;res2: %v
&quot;, res2)

	res2 = a &lt; b
	fmt.Printf(&quot;res2: %v
&quot;, res2)

	res2 = a &lt;= b
	fmt.Printf(&quot;res2: %v
&quot;, res2)

	res2 = a != b
	fmt.Printf(&quot;res2: %v
&quot;, res2)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>res2: false
res2: false
res2: false
res2: true
res2: true
res2: true
</code></pre>

<h4>逻辑运算符</h4>

<table>
	<thead>
		<tr>
			<th>运算符</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>&amp;&amp;</td>
			<td>逻辑and运算符。只有两边的操作数都为true才返回true，否则返回false。</td>
		</tr>
		<tr>
			<td>||</td>
			<td>逻辑or运算符。只要有一个操作数为true就返回true，否则返回false。</td>
		</tr>
		<tr>
			<td>!</td>
			<td>逻辑not运算符。取相反的结果。</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//逻辑运算
	var res3 bool
	res3 = true &amp;&amp; true
	fmt.Printf(&quot;res3: %v
&quot;, res3)
	res3 = true || false
	fmt.Printf(&quot;res3: %v
&quot;, res3)
	res3 = !res3
	fmt.Printf(&quot;res3: %v
&quot;, res3)
</code></pre>

<pre>
<code>res3: true
res3: true
res3: false
</code></pre>

<h4>位运算符</h4>

<p>位运算是对整数在内存中的二进制位进行操作。</p>

<table>
	<thead>
		<tr>
			<th>运算符</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>&amp;</td>
			<td>参与运算的两个数各对应的二进位相与。（两位均为1才为1）</td>
		</tr>
		<tr>
			<td>|</td>
			<td>参与运算的两个数各对应的二进位相或。（两位只要有一个为1就为1）</td>
		</tr>
		<tr>
			<td>^</td>
			<td>参与运算的两个数各对应的二进位异或。（当相对应的二进位相异时，结果才为1，否则为0）</td>
		</tr>
		<tr>
			<td>&lt;&lt;</td>
			<td>左移n位就是乘以2的n次方。a&lt;</td>
		</tr>
		<tr>
			<td>&lt;&lt;</td>
			<td>右移n位就是除以2的n次方。a&gt;&gt;b是把a的各二进位全部右移b位。</td>
		</tr>
	</tbody>
</table>

<pre>
<code>//位运算
	aa := 10
	bb := 11
	fmt.Printf(&quot;aa: %b
&quot;, aa)
	fmt.Printf(&quot;bb: %b
&quot;, bb)

	res4 := aa &amp; bb
	fmt.Printf(&quot;res4:%b  %v
&quot;, res4, res4)
	res4 = aa | bb
	fmt.Printf(&quot;res4:%b  %v
&quot;, res4, res4)
	res4 = aa ^ bb
	fmt.Printf(&quot;res4:%b  %v
&quot;, res4, res4)

	res4 = aa &lt;&lt; 2
	fmt.Printf(&quot;res4:%b  %v
&quot;, res4, res4)
	res4 = aa &gt;&gt; 1
	fmt.Printf(&quot;res4:%b  %v
&quot;, res4, res4)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>aa: 1010
bb: 1011
res4:1010  10
res4:1011  11
res4:1  1
res4:101000  40
res4:101  5
</code></pre>

<h4>赋值运算符</h4>

<table>
	<thead>
		<tr>
			<th>运算符</th>
			<th>描述</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>=</td>
			<td>简单的赋值运算符，将等号右边的结果赋值给左边的变量。</td>
		</tr>
		<tr>
			<td>+=</td>
			<td>相加后再赋值</td>
		</tr>
		<tr>
			<td>-=</td>
			<td>相减后再赋值</td>
		</tr>
		<tr>
			<td>*=</td>
			<td>相乘后再赋值</td>
		</tr>
		<tr>
			<td>/=</td>
			<td>相除后再赋值</td>
		</tr>
		<tr>
			<td>%=</td>
			<td>取模后再赋值</td>
		</tr>
		<tr>
			<td>&lt;&lt;=</td>
			<td>左移后再赋值</td>
		</tr>
		<tr>
			<td>&gt;&gt;=</td>
			<td>右移后再赋值</td>
		</tr>
		<tr>
			<td>&amp;=</td>
			<td>按位与后赋值</td>
		</tr>
		<tr>
			<td>|=</td>
			<td>按位或后赋值</td>
		</tr>
		<tr>
			<td>^=</td>
			<td>异或后赋值</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

