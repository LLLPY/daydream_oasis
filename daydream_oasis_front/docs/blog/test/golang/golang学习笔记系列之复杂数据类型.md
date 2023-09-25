
<BlogInfo title="golang学习笔记系列之复杂数据类型" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=211 category="golang" tag_list="['数据类型']" create_time="2022.09.18 22:40:24.602004" update_time="2022.09.18 22:40:24" />

^^^^^^^^^
<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" style="-webkit-user-select:none; background-color:hsl(0, 0%, 90%); display:block; margin:auto; transition:background-color 300ms" /></p>

<h2>复杂数据类型</h2>

<h3>数组</h3>

<p>数组是<strong>相同数据类型</strong>的一组数据的集合，数组一旦定义长度不能修改，数组 可以通过索引来访问元素。</p>

<h4><strong>数组的定义</strong></h4>

<pre>
<code>var array_name [SIZE]TYPE
</code></pre>

<ul>
	<li>array_name：数组名</li>
	<li>SIZE：数组的大小</li>
	<li>TYPE：数组中数据的类型</li>
</ul>

<pre>
<code>type Student struct {
	Name string
	num  int
}
// 数组的定义
var arr_int [10]int
fmt.Printf(&quot;arr_int: %v
&quot;, arr_int)
var arr_str [10]Student
fmt.Printf(&quot;arr_str: %v
&quot;, arr_str)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>arr_int: [0 0 0 0 0 0 0 0 0 0]
arr_str: [{ 0} { 0} { 0} { 0} { 0} { 0} { 0} { 0} { 0} { 0}]
</code></pre>

<h4>数组的初始化</h4>

<p>初始化就是给数组的元素赋初值，没有初始化的数组，默认元素都是<strong>零值</strong>（数值型的默认值是0，布尔型的默认值所示false，字符串型的默认值是空字符）。</p>

<pre>
<code>//给数组赋初始值
	var arr_int_init = [10]int{1, 2, 3}
	fmt.Printf(&quot;arr_int_init: %v
&quot;, arr_int_init)

	//给指定位置赋初始值
	var arr_float_init = [10]float64{0: 100.0, 3: 200.0}
	fmt.Printf(&quot;arr_float_init: %v
&quot;, arr_float_init)

	//使用...不指定数组的大小,根据初始值来判断数组的大小
	var arr_string_init = [...]string{&quot;hello&quot;, &quot;world&quot;}
	fmt.Printf(&quot;arr_string_init: %v
&quot;, arr_string_init)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>arr_int_init: [1 2 3 0 0 0 0 0 0 0]
arr_float_init: [100 0 0 200 0 0 0 0 0 0]
arr_string_init: [hello world]
</code></pre>

<h4>数组的访问</h4>

<p>可以通过索引的方式来访问数组。数组的最大下标为数组的长度减一，最小为0，大于这个值会发生数组越界。</p>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	var arr_int = [10]int{1, 2, 3, 4, 5, 6}

	//访问第一个元素
	fmt.Printf(&quot;arr_int[0]: %v
&quot;, arr_int[0])

	//访问第3个元素
	fmt.Printf(&quot;arr_int[2]: %v
&quot;, arr_int[2])

	//访问最后一个元素
	fmt.Printf(&quot;arr_int[len(arr_int)-1]: %v
&quot;, arr_int[len(arr_int)-1])

	//for遍历数组
	for i := 0; i &lt; len(arr_int); i++ {

		fmt.Printf(&quot;a[%v]=%v 
&quot;, i, arr_int[i])

	}
	print(&quot;#########################################
&quot;)
	//for range遍历数组
	for i, v := range arr_int {
		fmt.Printf(&quot;a[%v]=%v 
&quot;, i, v)

	}
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>arr_int[0]: 1
arr_int[2]: 3
arr_int[len(arr_int)-1]: 0
a[0]=1 
a[1]=2 
a[2]=3 
a[3]=4 
a[4]=5 
a[5]=6 
a[6]=0 
a[7]=0 
a[8]=0 
a[9]=0 
#########################################
a[0]=1 
a[1]=2 
a[2]=3 
a[3]=4 
a[4]=5 
a[5]=6 
a[6]=0 
a[7]=0 
a[8]=0 
a[9]=0 
</code></pre>

<h3>切片</h3>

<p>和数组类似，切片也是一组相同数据类型的数据的集合，但与数组不一样的是，切片的长度是可变的。对于数组来说，当我们对要保存的元素的个数不确定时，如果申请太小的数组，可能就不够用；如果申请太大的数组，可能就造成了不必要的浪费。鉴于这个原因，就有了切片，我们可以把切片理解为可变长度的数组，其实它底层就是使用数组实现的，只不过增加了一个自动扩容功能。</p>

<h4>切片的定义</h4>

<p>语法<strong>1</strong></p>

<pre>
<code>var slice_name []TYPE
</code></pre>

<ul>
	<li>slice_name：切片名</li>
	<li>TYPE：切片类型</li>
</ul>

<p>语法<strong>2</strong></p>

<pre>
<code>//使用make函数定义切片时，会同时将切片初始化
slice_name := make([]TYPE,SIZE)
</code></pre>

<ul>
	<li>slice_name：切片名</li>
	<li>TYPE：切片中元素的类型</li>
	<li>SIZE：初始化切片的大小</li>
</ul>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//切片的定义
	var s1 []int
	s1 = append(s1, 1)
	fmt.Printf(&quot;s1: %v
&quot;, s1)

	//make定义切片的同时会将其初始化
	s2 := make([]string, 10)
	fmt.Printf(&quot;s2: %v
&quot;, s2)

	//访问切片中的元素
	fmt.Printf(&quot;s1[0]: %v
&quot;, s1[0])

	//在切片的末尾添加元素
	s1 = append(s1, 2)
	fmt.Printf(&quot;s1: %v
&quot;, s1)
	//修改切片中的元素
	s1[0] = 100
	fmt.Printf(&quot;s1: %v
&quot;, s1)

	//获取切片的大小
	fmt.Printf(&quot;len(s1): %v
&quot;, len(s1))

	fmt.Printf(&quot;cap(s1): %v
&quot;, cap(s1))

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>s1: [1]
s2: [         ]
s1[0]: 1
s1: [1 2]
s1: [100 2]
len(s1): 2
cap(s1): 2
</code></pre>

<h4>切片的初始化</h4>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//切片的初始化
	//方法一
	var s1 = []int{1, 2, 3}
	fmt.Printf(&quot;s1: %v
&quot;, s1)

	//方法二：make
	s2 := make([]int, 10)
	fmt.Printf(&quot;s2: %v
&quot;, s2)

	//方法三：借助数组
	arr := [3]int{1, 2, 3}
	s3 := arr[:]
	fmt.Printf(&quot;s3: %v
&quot;, s3)

	//切片/数组/字符串的切片操作： s[a:b] 左闭右开 于python不一样的是，go语言中不能修改步长，步长只能是1
	s4 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Printf(&quot;s4[1:9]: %v
&quot;, s4[1:3])
    
    //访问操作和遍历操作同数组
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>s1: [1 2 3]
s2: [0 0 0 0 0 0 0 0 0 0]
s3: [1 2 3]
s4[1:9]: [2 3]
</code></pre>

<h4>切片的crud操作</h4>

<pre>
<code>package main

import (
	&quot;fmt&quot;
)

func main() {

	s := []int{1, 2, 3, 4, 5}

	//add
	s = append(s, 1)
	fmt.Printf(&quot;s: %v
&quot;, s)

	//delete：删除索引为index的元素
	index := 2
	s = append(s[:index], s[index+1:]...)
	fmt.Printf(&quot;s: %v
&quot;, s)

	//update
	s[4] = 6
	fmt.Printf(&quot;s: %v
&quot;, s)

	//query
	target := 5
	for i, v := range s {
		if v == target {
			println(&quot;找到了！&quot;, i)
			break
		}

	}

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>s: [1 2 3 4 5 1]
s: [1 2 4 5 1]
s: [1 2 4 5 6]
找到了！ 3
</code></pre>

<h3>map</h3>

<p>map是一种key:value键值对的数据结构。map内部实现是hash表。map最重要的一点是通过key能够快速的检索出数据。</p>

<h4>map的定义</h4>

<pre>
<code>var m[K_TYPE]V_TYPE
</code></pre>

<ul>
	<li>m：map名</li>
	<li>K_TYPE：key的类型</li>
	<li>V_TYPE：value的类型</li>
</ul>

<pre>
<code>package main

import (
	&quot;fmt&quot;
)

func main() {

	//map的定义
	//方法一
	var m1 map[string]string
	fmt.Printf(&quot;m1: %v
&quot;, m1)

	//方法二
	m2 := make(map[string]string)
	fmt.Printf(&quot;m2: %v
&quot;, m2)

	//map的初始化
	var m3 = map[string]string{
		&quot;name&quot;: &quot;Tom&quot;,
		&quot;age&quot;:  &quot;18&quot;,
	}
	fmt.Printf(&quot;m3: %v
&quot;, m3)

	//增加/修改map
	m3[&quot;num&quot;] = &quot;1234&quot;
	m3[&quot;age&quot;] = &quot;20&quot;
	fmt.Printf(&quot;m3: %v
&quot;, m3)

	//根据k获取v
	fmt.Printf(&quot;m3[&quot;name&quot;]: %v
&quot;, m3[&quot;name&quot;])

	//判断某个k是否存在  v,ok=m[k]---&gt;如果k存在，ok为true，否则为false
	v, ok := m3[&quot;name&quot;]
	if ok {
		print(v)
	}

	//删除某个k
	delete(m3, &quot;age&quot;)
	fmt.Printf(&quot;m3: %v
&quot;, m3)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>m1: map[]
m2: map[]
m3: map[age:18 name:TOm]
m3: map[age:20 name:TOm num:1234]
m3[&quot;name&quot;]: TOm
TOmm3: map[name:TOm num:1234]
</code></pre>

<h4>map的遍历</h4>

<p>通过for range对map进行遍历。</p>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	var m = map[string]string{
		&quot;name&quot;: &quot;Tom&quot;,
		&quot;age&quot;:  &quot;18&quot;,
		&quot;num&quot;:  &quot;1234&quot;,
	}

	//for range遍历
	//1.只拿到key
	for k := range m {
		fmt.Printf(&quot;k: %v v: %v
&quot;, k, m[k])
	}

	//2.同时拿到k和v
	for k, v := range m {
		fmt.Printf(&quot;k: %v v: %v
&quot;, k, v)
	}

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>k: name v: Tom
k: age v: 18
k: num v: 1234
k: num v: 1234
k: name v: Tom
k: age v: 18</code></pre>

