
<BlogInfo title="golang学习笔记系列之函数" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=238 category="golang" tag_list="[]" create_time="2022.09.24 15:57:01.525162" update_time="2022.09.24 15:57:01" />

^^^^^^^^^
<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" /></p>

<h2>函数</h2>

<h3>golang函数简介</h3>

<p>函数是go语言中的<strong>一级公民</strong>，我们把所有的功能单元都定义在函数中，可以重复使用。函数包含函数的名称，参数列表和返回值类型，这些构成了函数的签名。</p>

<h3>golang中函数的特性</h3>

<ul>
	<li>go语言中有3种函数：普通函数，匿名函数，方法（定义在struct上的函数）。</li>
	<li>go语言中不允许函数重载（overload），也就是说不允许函数同名。</li>
	<li><strong>go语言中的函数不能嵌套函数</strong>，但可以嵌套匿名函数。</li>
	<li>函数是一个值，可以将函数赋值给变量，使得这个变量也成为函数。</li>
	<li>函数可以作为参数传递给另一个函数。</li>
	<li>函数的返回值可以是一个函数。</li>
	<li>函数调用的时候，如果有参数传递给函数，则先拷贝参数的副本，再将副本传递给函数。（值传递）</li>
	<li>函数参数可以没有名称。</li>
</ul>

<h3>golang中函数的定义和调用</h3>

<p>函数在使用之前必须先定义，可以调用函数来完成某个任务。函数可以重复使用，从而达到代码重用。</p>

<p><strong>语法</strong></p>

<pre>
<code>func function_name([parameter list])(return_types){
    //函数体
}
</code></pre>

<ul>
	<li>func：声明函数</li>
	<li>function_name：函数名</li>
	<li>[parameter list]：参数列表，参数就像一个占位符，当函数被调用时，你可以将值传递给函数，这个值被称为实际参数。参数列表指定的是参数类型，顺序及参数个数。参数是可选的，也就是说函数也可以不包含参数。</li>
	<li>return_types：函数返回值的类型。</li>
	<li>函数体：函数的逻辑代码部分</li>
</ul>

<pre>
<code>//定义一个两数之和
func sum(a int,b int)(res int){
    res=a+b
    return res
}
</code></pre>

<h3>golang函数的返回值</h3>

<p>函数可以有0个或多个返回值，返回值需要指定数据类型，返回值通过return关键字来指定。</p>

<p>return可以有参数，也可以没有参数，这些返回值可以有名称，也可以没有名称。go中的函数可以有多个返回值。</p>

<ul>
	<li>return关键字中指定了参数时，返回值可以不用名称。如果return省略参数，则返回值部分必须带名称。</li>
	<li>当返回值有名称时，必须使用括号包围，逗号分隔，即使只有一个返回值。</li>
	<li>但即使返回值命名了，return中也可以强制指定其他返回值名称，也就是说return的优先级更高。</li>
	<li>命名的返回值是预先声明好的，在函数内部可以直接使用，无需再次声明。命名返回值的名称不能和函数参数名称相同，否则报错提示变量重复声明。</li>
	<li>return中可以有表达式，但不能出现赋值表达式，这其他语言可能有所不同。例如可以：return a+b，但是不能：return a=b+c</li>
</ul>

<pre>
<code>package main

import &quot;fmt&quot;

//没有返回值
func foo1() {
	print(&quot;没有参数，也没有返回值！
&quot;)
}

//有参数，没有返回值
func foo2(name string) {
	print(&quot;有一个参数：&quot;)
	fmt.Printf(&quot;name: %v
&quot;, name)
}

//有参数，有返回值 且给返回值命名了
func foo3(name string, age int) (name2 string, age2 int) {
	name2 = name
	age2 = age
	return name2, age2
	// return    如果return不指定返回值，则默认返回上面定义的返回值
}

// 有参数，有返回值，但没有给返回值命名 这个时候就必须需要return来指定返回值
func foo4(name string, age int) (string, int) {
	return name, age

}

func main() {

	foo1()
	foo2(&quot;Tom&quot;)
	name2, age2 := foo3(&quot;Tom&quot;, 18)
	fmt.Printf(&quot;name2: %v
&quot;, name2)
	fmt.Printf(&quot;age2: %v
&quot;, age2)
	name, _ := foo4(&quot;Tom&quot;, 18)  //丢弃age
	fmt.Printf(&quot;name: %v
&quot;, name)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>没有参数，也没有返回值！
有一个参数：name: Tom
name2: Tom
age2: 18
name: Tom
</code></pre>

<blockquote>
<p>tips：</p>

<ul>
	<li>go中经常会使用其中一个返回值作为函数是否执行成功，是否有错误信息的判断条件。例如return value,exists；return value,ok（map中就是这样使用的）；return value,err等</li>
	<li>当函数的返回值过多时，例如有4个以上的返回值，应该将这些返回值收集到容器中，然后以返回容器的方式去返回。</li>
	<li>当函数有多个返回值时，如果其中某个或几个返回值不想使用，可以通过下划线_来丢弃这些返回值。</li>
</ul>
</blockquote>

<h3>golang函数的参数</h3>

<p>go语言函数可以有0个或多个参数，参数需要指定数据类型。</p>

<p>声明函数时的参数列表叫做形参，调用时传递的参数叫做实参。</p>

<p>go语言是通过<strong>传值的方式传参</strong>的，意味着传递给函数的是拷贝后的副本，所以函数内部访问，修改的也是这个副本。(但是map，slice，interface，channel这些数据类型本身就是指针类型，所以就算是拷贝传值也是拷贝的指针，拷贝后的参数任然指向底层数据结构，所以修改它们可能会影响外部数据结构的值。)</p>

<p>go语言可以使用变长参数，有时候不能确定参数的个数时，可以使用变长参数，可以在函数定义语句的参数部分使用<strong>args&hellip;type</strong>的方式。这时会将&hellip;代表的参数全部保存到一个名为args的slice中，并且这些参数的数据类型都是type。</p>

<pre>
<code>package main

import &quot;fmt&quot;

func test(a int) {
	a = 200
	fmt.Printf(&quot;里面的a: %v
&quot;, a)
}

//两数之和
func sum(a int, b int) (c int) {
	c = a + b
	return
}

//...接收无数个参数
func foo(name string, age int, args ...string) {
	fmt.Printf(&quot;name: %v
&quot;, name)
	fmt.Printf(&quot;age: %v
&quot;, age)
	for _, v := range args {
		fmt.Printf(&quot;v: %v
&quot;, v)
	}
}
func main() {

	a := 100
	test(a)
	fmt.Printf(&quot;外面的a=%v
&quot;, a)

	res := sum(1, 2)
	fmt.Printf(&quot;res: %v
&quot;, res)
	foo(&quot;Tom&quot;, 18, &quot;Hello&quot;, &quot;My&quot;, &quot;name&quot;, &quot;is&quot;, &quot;Tom&quot;)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>里面的a: 200
外面的a=100
res: 3
name: Tom
age: 18
v: Hello
v: My
v: name
v: is
v: Tom
</code></pre>

<h3>golang函数类型与函数变量</h3>

<p>可以使用type关键字来定义一个函数类型，语法如下：</p>

<pre>
<code>type fun func(par_type1,par_type2...) res_type1...
</code></pre>

<ul>
	<li>fun：自己定义的函数类型名</li>
	<li>par_type1，par_type2&hellip;：表示各个参数的类型</li>
	<li>res_type1&hellip;：表示各个返回值的类型</li>
</ul>

<pre>
<code>package main

import &quot;fmt&quot;

func sum(a int, b int) (c int) {
	c = a + b
	return
}

func main() {

	//自己声明函数的类型，然后再将函数赋值给一个变量
	type my_func func(int, int) int
	var my_sum my_func
	my_sum = sum
	res := my_sum(1, 2)
	fmt.Printf(&quot;res: %v
&quot;, res)

	//直接通过短变量的形式将一个函数赋值给一个变量
	c := sum
	res2 := c(1, 2)
	fmt.Printf(&quot;res2: %v
&quot;, res2)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>res: 3
res2: 3
</code></pre>

<h3>高阶函数</h3>

<p>go语言的函数，可以作为函数的参数，传递给另外一个函数，同时也可以作为函数的返回值返回。</p>

<h4>函数作为参数和返回值</h4>

<pre>
<code>package main

import &quot;fmt&quot;

func sum(a int, b int) (c int) {
	c = a + b
	return
}

func sub(a int, b int) (c int) {
	c = a - b
	return
}

func test(a int, b int, f func(int, int) int) {
	res := f(a, b)
	fmt.Printf(&quot;%v+%v=res: %v
&quot;, a, b, res)
}

func cal(flag string) func(int, int) int {
	switch flag {
	case &quot;+&quot;:
		return sum
	case &quot;-&quot;:
		return sub
	default:
		return sum
	}

}

func main() {

	//函数作为参数传给函数
	test(10, 20, sum)

	//函数作为返回值
	f_sum := cal(&quot;+&quot;)
	res := f_sum(1, 2)
	fmt.Printf(&quot;res: %v
&quot;, res)

	f_sub := cal(&quot;-&quot;)
	res2 := f_sub(1, 2)
	fmt.Printf(&quot;res2: %v
&quot;, res2)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>10+20=res: 30
res: 3
res2: -1
</code></pre>

<h3>匿名函数</h3>

<p>go语言函数不能嵌套，但是在函数内部可以定义匿名函数，实现一些简单的功能。所谓匿名函数，就是没有名称的函数。</p>

<p><strong>语法</strong></p>

<pre>
<code>func ([参数列表])([返回值列表]){
    //函数体
}
</code></pre>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//将匿名函数赋值给一个变量
	say_hello := func(name string, age int) {
		fmt.Printf(&quot;My name is  %v,And i&#39;,m %v old.
&quot;, name, age)
	}
	say_hello(&quot;Tom&quot;, 18)

	//直接调用匿名函数
	func(words string) {
		fmt.Printf(&quot;words: %v
&quot;, words)
	}(&quot;Hi,我是一个匿名函数！&quot;)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>My name is  Tom,And i&#39;,m 18 old.
words: Hi,我是一个匿名函数！
</code></pre>

<h3>闭包</h3>

<p>闭包就是延伸了函数作用于的函数，使得函数可以访问到函数体外的非全局变量。</p>

<pre>
<code>package main

import &quot;fmt&quot;

//求平均值的闭包
func make_avger() func(int) float64 {

	s := make([]int, 0) 
    //对于下面的匿名函数来说，切片s就相当于函数体外的非全局变量
    //并且调用make_avager方法后，在全局中是访问不到切片s的
  

	return func(num int) float64 {
		s = append(s, num)
		sum := 0
		for _, v := range s {
			sum += v
		}
		return float64(sum / len(s))
	}

}
func main() {

	avg := make_avger()
	for i := 0; i &lt; 10; i++ {
		fmt.Printf(&quot;%.2f
&quot;, avg(i))

	}
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>0.00
0.00
1.00
1.00
2.00
2.00
3.00
3.00
4.00
4.00
</code></pre>

<h3>递归</h3>

<p>函数内部调用函数自己的函数称为递归函数（同闭包一样，递归不是go语言特有的，而是go语言具备实现递归的条件）。</p>

<pre>
<code>package main

//使用递归实现斐波那契数列
func fib(n int) int {
	if n == 1 || n == 2 {
		return 1
	} else {
		return fib(n-1) + fib(n-2)
	}
}

func main() {
	res := fib(10)
	print(res)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>102334155</code></pre>

