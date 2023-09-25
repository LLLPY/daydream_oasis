
<BlogInfo title="golang学习笔记系列之变量和常量" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=79 category="golang" tag_list="['golang']" create_time="2022.09.10 17:54:03.363674" update_time="2022.09.13 19:57:41" />

^^^^^^^^^
<h3>&nbsp;</h3>

<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" style="-webkit-user-select:none; background-color:hsl(0, 0%, 90%); display:block; margin:auto; transition:background-color 300ms" /></p>

<h3>变量</h3>

<p>变量是计算机语言中能存储计算结果或能表示值的抽象概念，不同的的变量保存的数据类型可能不一样。</p>

<h4>声明变量</h4>

<p>go语言中的变量需要声明后才能使用，同一作用域内不支持重复声明。并且go语言的变量声明后<strong>必须使用</strong>，否者会报错。</p>

<h4>默认语法</h4>

<pre>
<code>var indertifer type

//例：
var age int    //int类型的变量不赋值，默认值是0
var price float64 //默认值是0
var flag bool  //默认值是false 
</code></pre>

<h4>类型推断</h4>

<p>不需要为变量指定类型，根据变量的值来自动推断变量的类型。</p>

<pre>
<code>var name = &ldquo;TOm&rdquo;
var num = 10
</code></pre>

<h4>同时声明多个变量</h4>

<pre>
<code>var name,age,gender = &quot;Tom&quot;,18,true
</code></pre>

<h4>短变量声明</h4>

<p>短变量只能在<strong>函数内部</strong>进行声明，使用**:=**运算符对变量进行声明和初始化。</p>

<pre>
<code>identifer := &quot;&quot;

//例：注意，一定是在函数内部声明，否则会报错！

func fun(){
    age:=18
	name:=tom
}

</code></pre>

<h4>匿名变量</h4>

<p>如果我们接收到多个变量，有一些变量使用不到，可以使用下划线，便是变量名，这种变量叫做匿名变量。</p>

<pre>
<code>func Fun() (string, int) {
	return &quot;Tom&quot;, 18
}
//匿名变量 匿名变量不使用也不会报错
tom_name, _ := Fun()
fmt.Printf(&quot;tom_name: %v
&quot;, tom_name)
</code></pre>

<h3>常量</h3>

<p>常量，就是在程序编译阶段就确定下来的值，二程序在运行时则无法改变该值。在go语言中，常量可以是数值类型，布尔类型，字符串类型等等。</p>

<h4>常量声明</h4>

<p>定义一个常量使用const关键字，语法格式如下：</p>

<pre>
<code>const constantName [type] = value
</code></pre>

<ul>
	<li>const：定义常量的关键字</li>
	<li>constantName：常量名</li>
	<li>type：常量的类型，可选</li>
	<li>value：常量的值</li>
</ul>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//常规语法
	const PI float32 = 3.14
	const H = 100

	//定义多个
	const (
		NAME = &quot;Tom&quot;
		AGE  = 18
	)

	//注意：声明多个变量时，如果省略了赋值，则表示和上面的一行值相同
	const (
		a = 1
		b //b=a=1
		c = 100
		d //d=c=100
	)

	fmt.Printf(&quot;a: %v
&quot;, a)
	fmt.Printf(&quot;b: %v
&quot;, b)
	fmt.Printf(&quot;c: %v
&quot;, c)
	fmt.Printf(&quot;d: %v
&quot;, d)

	//同时定义
	const X, Y, Z = 2, 3, 4
	fmt.Printf(&quot;X: %v
&quot;, X)
	fmt.Printf(&quot;Y: %v
&quot;, Y)

}

</code></pre>

<h4>iota</h4>

<p>iota比较特殊，可以被认为是一个可被编译器修改的常量，它的默认值是0，每调用一次值就加一，遇到const关键字时被重置为0。</p>

<pre>
<code>//iota
	const (
		A = iota //0 
		B = iota //1
		C = iota //2

	)
	fmt.Printf(&quot;A: %v
&quot;, A)
	fmt.Printf(&quot;B: %v
&quot;, B)
	fmt.Printf(&quot;C: %v
&quot;, C)

	//iota中间截断
	const (
		aa = iota //0
		_         //1
		cc = iota //2
	)

	fmt.Printf(&quot;aa: %v
&quot;, aa)
	fmt.Printf(&quot;cc: %v
&quot;, cc)


	const(
		aaa=iota  //0
		bbb=1000  //1000 [1]
		ccc=iota  //2
	)

	fmt.Printf(&quot;aaa: %v
&quot;, aaa)
	fmt.Printf(&quot;ccc: %v
&quot;, ccc)</code></pre>

