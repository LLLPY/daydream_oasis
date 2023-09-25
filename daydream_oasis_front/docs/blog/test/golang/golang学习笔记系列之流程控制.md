
<BlogInfo title="golang学习笔记系列之流程控制" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=249 category="golang" tag_list="['golang', '流程控制']" create_time="2022.09.12 16:39:58.773835" update_time="2022.09.13 19:56:20" />

^^^^^^^^^
<h2>&nbsp;</h2>

<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" style="-webkit-user-select:none; background-color:hsl(0, 0%, 90%); display:block; margin:auto; transition:background-color 300ms" /></p>

<h2>流程控制</h2>

<h3>go语言中的条件</h3>

<p><strong>条件语句</strong>是用来判断给定的条件是否满足，并根据判断的结果决定执行的语句，go语言中的条件语句也是这样的。</p>

<h3>go语言中的条件语句</h3>

<ol>
	<li>if语句：if语句由一个布尔表达式后紧跟一个或多个语句组成。</li>
	<li>if&hellip;else语句：if语句后可以使用可选的else语句，else语句中的表达式在布尔表达式为false时执行。</li>
	<li>if嵌套语句</li>
	<li>switch语句：switch语句用于基于不同条件执行不同的动作。</li>
	<li>select语句：select语句类似于switch语句，但是select会随机执行一个可运行的case，如果没有case可运行，它将阻塞，直到有case可运行。</li>
</ol>

<h4>if语句</h4>

<p><strong>语法</strong></p>

<pre>
<code>if 布尔表达式{
    /*布尔表达式为true时要执行的语句*/
}
</code></pre>

<blockquote>
<p>注意：在go语言中，布尔表达式不需要使用括号。</p>
</blockquote>

<pre>
<code>//示例
a := 100
	if a &gt; 10 {
		fmt.Println(&quot;hello&quot;)
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>hello
</code></pre>

<blockquote>
<p><strong>初始变量可以声明在布尔表达式里面，但是这个变量的作用于只能用在当前条件语句中！</strong></p>

<pre>
<code>//示例
	if b := 100; b &gt; 10 {
		fmt.Println(&quot;if条件成立！&quot;)
		fmt.Printf(&quot;b: %v
&quot;, b)
	} else {
		fmt.Println(&quot;if条件不成立！&quot;)
		fmt.Printf(&quot;b: %v
&quot;, b)
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>if条件成立！
b: 100
</code></pre>

<pre>
<code>if b := 100; b &gt; 10 {
		fmt.Println(&quot;if条件成立！&quot;)
		fmt.Printf(&quot;b: %v
&quot;, b)
	} else {
		fmt.Println(&quot;if条件不成立！&quot;)
		fmt.Printf(&quot;b: %v
&quot;, b)
	}
	fmt.Printf(&quot;b: %v
&quot;, b)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>19:24: undefined: b
</code></pre>
</blockquote>

<p>go语言if语句使用提示：</p>

<ol>
	<li>不能使用布尔类型以外的其他值作为判断条件</li>
	<li>不能使用括号将条件语句括起来</li>
	<li>大括号必须存在，即使只有一行语句</li>
	<li>左括号必须于if，else同一行</li>
	<li>在if之后，条件语句之前，可以添加变量初始化语句，使用分号;分割</li>
</ol>

<h4>if else语句</h4>

<p><strong>语法</strong></p>

<pre>
<code>if 布尔表达式{
    /*布尔表达式为true时要执行的语句*/
}else{
    /*布尔表达式为false时要执行的语句*/
}
</code></pre>

<pre>
<code>//示例
if age := 18; age &gt; 18 {
		fmt.Println(&quot;你已经成年了！&quot;)
	} else {
		fmt.Println(&quot;你还未成年！&quot;)
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>你还未成年！
</code></pre>

<h4>if else if语句</h4>

<p><strong>语法</strong></p>

<pre>
<code>if 布尔表达式1{
    /*布尔表达式1为true时要执行的语句*/
}else if 布尔表达式2{
    /*布尔表达式2为true时要执行的语句*/
}else{
    /*以上所有布尔表达式都不成立时要执行的语句*/
}
</code></pre>

<pre>
<code>//示例
var aa int
	fmt.Println(&quot;请输入一个数：&quot;)
	fmt.Scan(&amp;aa)
	if aa == 100 {
		fmt.Printf(&quot;aa: %v
&quot;, aa)
	} else if aa &lt; 100 {
		fmt.Println(&quot;太小了！&quot;)
	} else {
		fmt.Println(&quot;太大了！&quot;)
	}

</code></pre>

<pre>
<code>请输入一个数：
10
太小了！
</code></pre>

<h4>switch语句</h4>

<h5>单值匹配</h5>

<p><strong>语法</strong></p>

<pre>
<code>//单值匹配
switch 条件表达式{
    case var1:
    	...
    case var2:
    	...
    case var3:
    	...
    default:
    	...
}

</code></pre>

<pre>
<code>//示例
	aaa := 1
	switch aaa {
	case 1:
		fmt.Println(&quot;唱歌！&quot;)
	case 2:
		fmt.Println(&quot;跳舞！&quot;)
	case 3:
		fmt.Println(&quot;唱歌+跳舞！&quot;)
	default:
		fmt.Println(&quot;才艺表演。&quot;)
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>唱歌！
</code></pre>

<h5>多值匹配</h5>

<p><strong>语法</strong></p>

<pre>
<code>//多值匹配
switch 条件表达式{
    case var1,var2,var3...:
    	...
    case var4,var5...:
    	...
    default:
    	...
}
</code></pre>

<pre>
<code>//示例
var day int
	fmt.Println(&quot;请输入一个数字：&quot;)
	fmt.Scan(&amp;day)
	switch day {
	case 1, 2, 3, 4, 5:
		fmt.Println(&quot;工作日！&quot;)
	case 6, 7:
		fmt.Println(&quot;假期！&quot;)
	default:
		fmt.Println(&quot;输入有误！&quot;)
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>请输入一个数字：
6
假期！
</code></pre>

<h5>case后接条件表达式</h5>

<p><strong>语法</strong></p>

<pre>
<code>//case后接条件表达式
switch{
    case 条件表达式1:
    	...
    case 条件表达式2:
    	...
    case 条件表达式3:
    	...
    default:
    	...
}
</code></pre>

<pre>
<code>//示例
	var n int
	fmt.Println(&quot;请输入一个数字：&quot;)
	fmt.Scan(&amp;n)
	switch {
	case n == 10:
		fmt.Println(&quot;猜对了！&quot;)
	case n &lt; 10:
		fmt.Println(&quot;太小了！&quot;)
	case n &gt; 10:
		fmt.Println(&quot;太大了！&quot;)
	default:
		fmt.Println(&quot;不可能执行到这条语句，除非上面的case都不成立。&quot;)
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>请输入一个数字：
23
太大了！
</code></pre>

<h5>fallthrough</h5>

<p><strong>语法</strong></p>

<pre>
<code>//fallthrough 可以执行满足条件的下一个case
switch 条件表达式{
    case var1:
    	...
    	fallthrough
    case var2:
    	...
    	fallthrough
    case var3:
    	...
    default:
    	...
}

</code></pre>

<pre>
<code>bb := 100
	switch bb {
	case 100:
		fmt.Printf(&quot;bb: %v
&quot;, bb)
		fallthrough
	case 200:
		fmt.Println(&quot;200&quot;)
		fallthrough
	case 300:
		fmt.Println(&quot;300&quot;)
	default:
		fmt.Println(&quot;case都不成立就执行这里。&quot;)
	}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>bb: 100
200
300
</code></pre>

<p>go语言switch使用注意事项：</p>

<ol>
	<li>支持多条件匹配</li>
	<li>不同的case之间不使用break分隔，默认只会执行一个case</li>
	<li>如果想执行多个case，需要使用fallthrough关键字，也可以用break终止</li>
	<li>case后还可以使用条件表达式</li>
</ol>

<h3>go语言中的循环语句</h3>

<p>go语言中的循环只有for循环，去除了while，do while循环，使用起来更加简洁。</p>

<ol>
	<li>for循环。</li>
	<li>for range循环。（类似于python中的for in）</li>
</ol>

<h4>for语句</h4>

<p><strong>语法</strong></p>

<pre>
<code>for 初始语句;条件表达式；结束语句{
    循环语句
}
</code></pre>

<pre>
<code>//for循环
	for i := 0; i &lt; 10; i++ {
		fmt.Printf(&quot;i: %v	&quot;, i)
	}
	fmt.Println(&quot;
&quot;)
	//初始条件写在外面
	j := 0
	for ; j &lt; 10; j++ {
		fmt.Printf(&quot;j: %v	&quot;, j)
	}

	fmt.Println(&quot;
&quot;)
	//结束语句写在循环体内
	for i := 0; i &lt; 10; {
		fmt.Printf(&quot;i: %v	&quot;, i)
		i++

	}
	fmt.Println(&quot;
&quot;)

	//永真循环
	k := 0
	for {
		fmt.Printf(&quot;k: %v &quot;, k)
		k++
		if k == 10 {
			break
		}
	}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>i: 0    i: 1    i: 2    i: 3    i: 4    i: 5    i: 6    i: 7    i: 8    i: 9

j: 0    j: 1    j: 2    j: 3    j: 4    j: 5    j: 6    j: 7    j: 8    j: 9

i: 0    i: 1    i: 2    i: 3    i: 4    i: 5    i: 6    i: 7    i: 8    i: 9

k: 0 k: 1 k: 2 k: 3 k: 4 k: 5 k: 6 k: 7 k: 8 k: 9 
</code></pre>

<h4>for range语句</h4>

<p>go语言中可以使用for range遍历数组，切片，字符串，map及通道（channel）。通过for range遍历的返回值有一下规律：</p>

<ol>
	<li>数组，切片，字符串返回索引和值</li>
	<li>map返回键和值</li>
	<li>通道只返回通道内的值</li>
</ol>

<pre>
<code>//for range
	//遍历数组
	var arr = [...]int{1, 2, 3, 4, 5, 6, 7}
	for i, v := range arr {
		fmt.Printf(&quot;%v:%v
&quot;, i, v)

	}

	//遍历map
	var m = make(map[string]string, 0)
	m[&quot;name&quot;] = &quot;Tom&quot;
	m[&quot;age&quot;] = &quot;18&quot;
	m[&quot;num&quot;] = &quot;1234&quot;
	for k, v := range m {
		fmt.Printf(&quot;%v:%v
&quot;, k, v)

	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>name:Tom
age:18
num:1234
</code></pre>

<h3>break关键字</h3>

<p>break关键字可以结束for，switch和select的代码块。</p>

<pre>
<code>//跳出for循环
k := 0
	for {
		fmt.Printf(&quot;k: %v &quot;, k)
		k++
		if k == 10 {
			break
		}
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>k: 0 k: 1 k: 2 k: 3 k: 4 k: 5 k: 6 k: 7 k: 8 k: 9 
</code></pre>

<pre>
<code>//配合标签使用
label:
	for i := 0; i &lt; 10; i++ {
		fmt.Printf(&quot;i: %v
&quot;, i)
		if i == 5 {
			break label
		}

	}
	fmt.Println(&quot;END...&quot;)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>i: 0
i: 1
i: 2
i: 3
i: 4
i: 5
END...
</code></pre>

<p>go语言中break的注意事项：</p>

<ol>
	<li>单独在select中使用break和不使用break没有啥区别。</li>
	<li>单独在switch中使用break，并且没有使用fallthrough，和不使用break没有啥区别。</li>
	<li>在switch中，配合fallthrough关键字，能够终止fallthrough后面case语句的执行。</li>
	<li>带标签的break，可以跳出多层select/select作用域。让break更加灵活，写法更加简单，不需要使用控制变量一层一层跳出循环，没有带break的只能跳出当前语句。</li>
</ol>

<h3>continue关键字</h3>

<p>continue只能用在循环中，在go中只能用在for循环中，它可以终止本次循环，进入下一轮循环。</p>

<p>continue也可以配合标签使用。</p>

<pre>
<code>//打印10以内的偶数
	for i := 0; i &lt; 11; i++ {
		if i%2 != 0 {
			continue
		}
		fmt.Printf(&quot;i: %v
&quot;, i)
	}
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>i: 0
i: 2
i: 4
i: 6
i: 8
i: 10
</code></pre>

<p><strong>配合标签使用</strong></p>

<pre>
<code>label:

	for i := 0; i &lt; 3; i++ {

		for j := 0; j &lt; 3; j++ {
			if i == 1 &amp;&amp; j == 1 {
				continue label //跳到label所在的地方
			}
			fmt.Printf(&quot;i: %v  j: %v
&quot;, i, j)
		}

	}
	fmt.Println(&quot;i=1,j=1时跳出了循环。&quot;)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>i: 0  j: 0
i: 0  j: 1
i: 0  j: 2
i: 1  j: 0
i: 2  j: 0
i: 2  j: 1
i: 2  j: 2
i=1,j=1时跳出了循环。
</code></pre>

<h3>goto关键字</h3>

<p>goto语句通过标签进行代码间的无条件跳转。goto语句可以在快速跳出循环，避免重复退出上有一定帮助。</p>

<h4>跳到指定标签</h4>

<pre>
<code>for i := 0; i &lt; 10; i++ {
		fmt.Printf(&quot;i: %v
&quot;, i)
		if i == 5 {
			goto label
		}

	}

label:
	fmt.Println(&quot;循环结束！&quot;)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>i: 0
i: 1
i: 2
i: 3
i: 4
i: 5
循环结束！
</code></pre>

<h4>跳出多重循环</h4>

<pre>
<code>//与break不一样的是，break只能跳出一层循环，而goto可以直接跳出所有循环
for i := 0; i &lt; 3; i++ {
		for j := 0; j &lt; 3; j++ {
			for k := 0; k &lt; 3; k++ {
				fmt.Printf(&quot;i=%v j=%v k=%v
&quot;, i, j, k)
				if i == 1 &amp;&amp; j == 1 &amp;&amp; k == 1 {
					goto mylabel
				}

			}

		}

	}
mylabel:
	fmt.Println(&quot;循环结束！&quot;)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>i=0 j=0 k=0
i=0 j=0 k=1
i=0 j=0 k=2
i=0 j=1 k=0
i=0 j=1 k=1
i=0 j=1 k=2
i=0 j=2 k=0
i=0 j=2 k=1
i=0 j=2 k=2
i=1 j=0 k=0
i=1 j=0 k=1
i=1 j=0 k=2
i=1 j=1 k=0
i=1 j=1 k=1
循环结束！</code></pre>

