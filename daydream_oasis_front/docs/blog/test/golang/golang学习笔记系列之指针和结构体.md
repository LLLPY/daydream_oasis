
<BlogInfo title="golang学习笔记系列之指针和结构体" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=293 category="golang" tag_list="[]" create_time="2022.09.24 22:09:33.034463" update_time="2022.09.24 22:09:33" />

^^^^^^^^^
<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" /></p>

<h2>defer语句</h2>

<p>go语言中的defer语句会将其后面紧跟随的语句延迟处理。在defer归属的函数即将返回时，将延迟处理的语句按照defer定义的顺序逆序执行，也就是说，先defer的语句后执行，后defer的语句先执行。</p>

<p><strong>defer特性</strong></p>

<ul>
	<li>关键字defer用于注册延迟调用。</li>
	<li>这些调用直到return前才执行。因此可以用来做资源清理。</li>
	<li>多个defer语句，按先进后出的执行顺序。</li>
	<li>defer语句中的变量，在defer声明时就决定了。</li>
</ul>

<pre>
<code>package main

func main() {
	print(&quot;start
&quot;)
	defer print(&quot;step 1
&quot;)
	defer print(&quot;step 2
&quot;)
	defer print(&quot;step 3
&quot;)
	print(&quot;end
&quot;)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>start
end
step 3
step 2
step 1
</code></pre>

<blockquote>
<p>如运行结果所示，defer后的语句都被<strong>延迟</strong>执行了，并且有多个defer语句存在时，后defer的语句先执行。</p>
</blockquote>

<h2>init函数</h2>

<p>golang有一个特殊的init函数，先于main函数执行，可以用于实现包级别的一些初始化工作。</p>

<p><strong>init函数的主要特点</strong></p>

<ul>
	<li>init函数先于main函数执行，不能被主动调用，它是<strong>自动执行</strong>的</li>
	<li>init函数即没有参数，也没有返回值</li>
	<li>每个包可以有多个init函数</li>
	<li>包的每个源文件也可以有多个init函数，这点比较特殊，就是可以在同一个文件下定义多个init函数</li>
	<li>同一个包的init执行顺序没有明确的定义，但是同一个文件下的init函数是按顺序执行的</li>
	<li>不同包的init函数按照包导入的依赖关系决定执行顺序。</li>
</ul>

<p><strong>golang初始化顺序</strong></p>

<p>顺序：变量初始化&gt;init函数&gt;main函数</p>

<pre>
<code>package main

func init_var() int {
	print(&quot;初始化变量...
&quot;)
	return 10
}

func init() {
	print(&quot;init函数1...
&quot;)
}

func init() {
	print(&quot;init函数2...
&quot;)
}

var i int = init_var()

func main() {
	print(&quot;main函数被执行了...
&quot;)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>初始化变量...
init函数1...
init函数2...
main函数被执行了...
</code></pre>

<h2>指针</h2>

<p>go语言中的函数传参都是值拷贝，当我们想修改某个变量的时候，我们可以创建一个指向该变量地址的指针变量。传递数据使用指针，而无需拷贝数据。</p>

<p>类型指针不能进行偏移和运算。</p>

<p>go语言中的指针操作非常简单，只需要记住两个符号：&amp;（取地址）和*（根据地址取值）。</p>

<h3>指针地址和指针类型</h3>

<p>每个变量在运行时都拥有一个地址，这个地址代表变量在内存中的位置。go语言中使用&amp;字符放在变量前面对变量进行取地址操作。go语言中的值类型（int，float，bool，string，array，struct）都有对应的指针类，如：*int，**string等。</p>

<h3>指针语法</h3>

<p>一个指针变量指向了一个值的内存地址。（也就是我们声明了一个指针之后，可以像变量赋值一样，把一个值的内存地址放入到指针当中。）</p>

<p><strong>语法</strong></p>

<pre>
<code>var var_name *var_type
</code></pre>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	var p *int
	var pp **int
	var ppp ***int
	a := 10
	p = &amp;a    //将指针p指向a的地址 即*p=a=10
	pp = &amp;p   //将指针pp指向p的地址 即*pp=p-&gt; *(*pp)=*p=a=10
	ppp = &amp;pp //将指针ppp指向pp的地址 即*ppp=pp-&gt; *(*ppp)=*pp -&gt; *(*(*ppp))=*(*pp)=*p=a=10

	fmt.Printf(&quot;p: %v
&quot;, p)
	fmt.Printf(&quot;p: %v
&quot;, &amp;p)
	fmt.Printf(&quot;pp: %v
&quot;, pp)
	fmt.Printf(&quot;ppp: %v
&quot;, ***ppp)
	fmt.Println(*p == a)
	fmt.Println(*(*pp) == a)
	fmt.Println(*(*(*ppp)) == a)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>p: 0xc0000ba000
p: 0xc0000b4018
pp: 0xc0000b4018
ppp: 10
true
true
true
</code></pre>

<h3>指向数组的指针</h3>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	var arr = [5]int{1, 2, 3, 4, 5}
	var arr_p [5]*int //数组类型的指针
	fmt.Printf(&quot;arr: %v
&quot;, arr)
	for i := 0; i &lt; len(arr); i++ {
		arr_p[i] = &amp;arr[i]
	}

	for i := 0; i &lt; len(arr_p); i++ {
		fmt.Printf(&quot;arr_p[i]=%v *arr_p[i]=%v arr[i]=%v
&quot;, arr_p[i], *arr_p[i], arr[i])

	}

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>arr: [1 2 3 4 5]
arr_p[i]=0xc0000b2030 *arr_p[i]=1 arr[i]=1
arr_p[i]=0xc0000b2038 *arr_p[i]=2 arr[i]=2
arr_p[i]=0xc0000b2040 *arr_p[i]=3 arr[i]=3
arr_p[i]=0xc0000b2048 *arr_p[i]=4 arr[i]=4
arr_p[i]=0xc0000b2050 *arr_p[i]=5 arr[i]=5
</code></pre>

<h2>结构体</h2>

<h3>golang类型定义和类型别名</h3>

<p><strong>类型定义语法</strong></p>

<pre>
<code>type my_type old_type
</code></pre>

<ul>
	<li>my_type：自己新定义的类型</li>
	<li>old_type：已经存在的类型</li>
</ul>

<p><strong>类型别名语法</strong></p>

<pre>
<code>type my_type = old_type //用已存在的类型赋值给新类型
</code></pre>

<p><strong>两者的区别</strong></p>

<ul>
	<li>类型定义相当于定义了一个全新的类型，与之前的类型不同；但是类型别名并没有定义新的类型，而是使用一个别名来代替之前的类型</li>
	<li>类型别名只会在代码中存在，在编译完成之后并不会存在该别名</li>
	<li>因为类型别名和原来的类型是一致的，所以原类型所拥有的方法，类型别名定义的变量也拥有；但是如果是重定义的一个类型，那么不可以调用之前的任何方法</li>
</ul>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//类型定义
	type my_string string

	var name my_string = &quot;Tom&quot;
	fmt.Printf(&quot;name: %T %v
&quot;, name, name) //类型为自己定义的新类型

	//类型别名
	type my_string2 = string
	var name2 my_string2 = &quot;Tom&quot;
	fmt.Printf(&quot;name2: %T %v
&quot;, name2, name2) //类型仍旧是string

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>name: main.my_string Tom
name2: string Tom
</code></pre>

<h3>golang结构体</h3>

<p>go语言没有面向对象的概念，但是可以使用结构体来实现面向对象编程的一些特性，你如：继承，组合等特性。</p>

<p><strong>结构体的定义</strong></p>

<pre>
<code>type struct_name struct{
    member1 type1
    member2 type2
    member3 type3
    ...
    
}
</code></pre>

<ul>
	<li>type：结构体定义关键字</li>
	<li>struct_name：结构体名</li>
	<li>struct：结构体定义关键字</li>
	<li>member type：成员定义</li>
</ul>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//一个结构体就相当于一个新的类型
	type Student struct {
		name  string
		num   int
		age   int
		email string
	}

	tom := Student{&quot;Tom&quot;, 1, 18, &quot;110@qq.com&quot;}
	fmt.Printf(&quot;tom: %v
&quot;, tom)
	fmt.Printf(&quot;tom.name: %v
&quot;, tom.name)
	fmt.Printf(&quot;tom.age: %v
&quot;, tom.age)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>tom: {Tom 1 18 110@qq.com}
tom.name: Tom
tom.age: 18
</code></pre>

<p><strong>匿名结构体</strong></p>

<p>对于临时需要使用结构体时，可以定义匿名结构体。</p>

<pre>
<code>// 匿名结构体
	var dog struct {
		name string
		age  int
	}

	dog.name = &quot;Jerry&quot;
	dog.age = 3
	fmt.Printf(&quot;dog: %v
&quot;, dog)
	fmt.Printf(&quot;dog.name: %v
&quot;, dog.name)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>dog: {Jerry 3}
dog.name: Jerry
</code></pre>

<h3>结构体的初始化</h3>

<p>对于通过结构体定义的一个变量来说，未初始化的变量的每个成员属性都是零值；go语言中提供了两种结构体初始化的方法，分别是&ldquo;k-v&rdquo;式和&ldquo;列表&rdquo;式。</p>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {
	type Student struct {
		name  string
		age   int
		email string
	}

	tom := Student{}
	fmt.Printf(&quot;tom: %v
&quot;, tom) //未初始化的结构体每个成员属性都是零值

	//&ldquo;k-v&rdquo;式初始化 可以对部分值进行初始化，也可以对全部值初始化
	jerry := Student{name: &quot;Jerry&quot;, age: 18}
	fmt.Printf(&quot;jerry: %v
&quot;, jerry)

	//&ldquo;列表&rdquo;式初始化 必须将所有值初始化
	autumn := Student{&quot;Autumn&quot;, 18, &quot;110@qq.com&quot;}
	fmt.Printf(&quot;autumn: %v
&quot;, autumn)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>tom: { 0 }
jerry: {Jerry 18 }
autumn: {Autumn 18 110@qq.com}
</code></pre>

<h3><strong>结构体指针</strong></h3>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	type Student struct {
		name string
		age  int
	}

	tom := Student{name: &quot;Tom&quot;, age: 18}

	//定义一个结构体指针
	var s_p *Student
	s_p = &amp;tom
	fmt.Printf(&quot;s_p: %v
&quot;, s_p)
	fmt.Printf(&quot;(*s_p): %v
&quot;, (*s_p))
	fmt.Printf(&quot;(*s_p).name: %v
&quot;, (*s_p).name)
	fmt.Printf(&quot;s_p.name: %v
&quot;, s_p.name) //在取成员变量的值的时候可以将*省略

	//使用new关键字创建结构体指针
	var jerry = new(Student)
	jerry.name = &quot;Jerry&quot;
	fmt.Printf(&quot;jerry: %v
&quot;, jerry)
	fmt.Printf(&quot;(*jerry): %v
&quot;, (*jerry)) //取值
	fmt.Printf(&quot;jerry.name: %v
&quot;, jerry.name)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>s_p: &amp;{Tom 18}
(*s_p): {Tom 18}
(*s_p).name: Tom
s_p.name: Tom
jerry: &amp;{Jerry 0}
(*jerry): {Jerry 0}
jerry.name: Jerry
</code></pre>

<h3>结构体作为函数参数</h3>

<p>go语言的结构体可以像普通变量一样，作为函数参数，参数的传递方式分为两种：</p>

<ol>
	<li>直接传结构体，在函数体内对结构体的操作不会影响原结构体（因为操作的只是原结构体的副本）</li>
	<li>传递结构体的地址，在函数体内对结构的任何操作都会对原结构体生效</li>
</ol>

<pre>
<code>package main

import &quot;fmt&quot;

type Student struct {
	name string
	age  int
}

//值传递
func show_student(s Student, name string, age int) {
	s.name = name
	s.age = age
	fmt.Printf(&quot;s: %v
&quot;, s)

}

//地址传递（引用传递）
func show_student2(s *Student, name string, age int) {
	s.name = name
	s.age = age
	fmt.Printf(&quot;s: %v
&quot;, s)
}

func main() {

	tom := Student{name: &quot;Tom&quot;, age: 18}
	jerry := Student{name: &quot;Jerry&quot;, age: 18}

	//tom直接传值
	fmt.Printf(&quot;tom: %v
&quot;, tom)
	show_student(tom, &quot;Tom2&quot;, 20)
	fmt.Printf(&quot;tom: %v
&quot;, tom)
	fmt.Println(&quot;-------------------&quot;)
	//jerry传递地址
	fmt.Printf(&quot;jerry: %v
&quot;, jerry)
	show_student2(&amp;jerry, &quot;Jerry2&quot;, 20)
	fmt.Printf(&quot;jerry: %v
&quot;, jerry)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>tom: {Tom 18}
s: {Tom2 20}
tom: {Tom 18}
-------------------
jerry: {Jerry 18}
s: &amp;{Jerry2 20}
jerry: {Jerry2 20}
</code></pre>

<h3>结构体的嵌套</h3>

<p>go语言的结构体中可以嵌套另一个结构体。</p>

<pre>
<code>package main

import &quot;fmt&quot;

type Person struct {
	name string
	age  int
	dog  Dog //宠物狗，另一个结构体
}

type Dog struct {
	name string
	age  int
}

func main() {

	var tom Person
	tom.name = &quot;Tom&quot;
	tom.age = 18

	var erha = Dog{name: &quot;二哈&quot;, age: 3}
	tom.dog = erha

	fmt.Printf(&quot;tom: %v
&quot;, tom)
	fmt.Printf(&quot;tom.name: %v
&quot;, tom.name)
	fmt.Printf(&quot;tom.dog.name: %v
&quot;, tom.dog.name)
	tom.dog.name = &quot;二哈哈哈&quot;
	fmt.Printf(&quot;tom.dog: %v
&quot;, tom.dog)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>tom: {Tom 18 {二哈 3}}
tom.name: Tom
tom.dog.name: 二哈
tom.dog: {二哈哈哈 3}</code></pre>

