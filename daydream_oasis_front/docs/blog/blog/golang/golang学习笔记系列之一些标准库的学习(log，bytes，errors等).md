
<BlogInfo title="golang学习笔记系列之一些标准库的学习(log，bytes，errors等)" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=215 category="golang" tag_list="[]" create_time="2022.11.06 16:45:45.426156" update_time="2022.11.06 16:48:45" />

^^^^^^^^^
<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" /></p>

<h3>log</h3>

<p>golang内置了log包，实现了简单的日志服务。通过调用log包的函数，可以实现简单的日志打印功能。</p>

<p>log包中有3个系列的日志打印函数，分别是print系列，panic系列和fatal系列。</p>

<table>
	<thead>
		<tr>
			<th>函数系列</th>
			<th>作用</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>print</td>
			<td>单纯打印日志</td>
		</tr>
		<tr>
			<td>panic</td>
			<td>打印日志，抛出panic异常</td>
		</tr>
		<tr>
			<td>fatal</td>
			<td>打印日志，强制结束程序（os.Exit(1)）,defer函数不会执行</td>
		</tr>
	</tbody>
</table>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;log&quot;
	&quot;os&quot;
)

func main() {

	//配置日志的输出前缀
	log.SetPrefix(&quot;Log:&quot;)

	//配置日志
	log.SetFlags(log.Ldate | log.Ltime | log.Lmicroseconds | log.Llongfile)

	//设置日志输出到文件
	f, _ := os.OpenFile(&quot;a.log&quot;, os.O_WRONLY|os.O_CREATE|os.O_APPEND, os.ModePerm)
	defer f.Close()
	log.SetOutput(f)

	//简单打印日志
	log.Print(&quot;hello golang...&quot;)
	defer fmt.Print(&quot;程序结束...&quot;)
	//panic日志
	// log.Panic(&quot;bye...&quot;) //defer会被执行

	//fatal日志
	// log.Fatal(&quot;致命错误...&quot;) //defer不会被执行

	//自定义logger
	my_logger := log.New(os.Stdout, &quot;My Log:&quot;, log.Ldate|log.Ltime|log.Lmicroseconds|log.Llongfile)
	my_logger.Print(&quot;这个是自己定义的logger，一次性配置所有，会方便许多!&quot;)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>My Log:2022/11/05 17:27:35.150644 /home/lll/Desktop/go/lll08_标准库/os/lll07_日志相关的操作.go:33: 这个是自己定义的logger，一次性配置所有，会方便许多!
</code></pre>

<h3>builtin</h3>

<p>这个包提供了一些类型声明，变量和常量声明，还有一些便利的函数，这个包不需要导入，这些变量和函数就可以直接使用。</p>

<h4>panic</h4>

<p>抛出一个panic异常。</p>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {

	//panic 抛出异常
	panic(&quot;抛出异常!!!&quot;)
	
}

</code></pre>

<h4>new和make</h4>

<p>new和make的区别：</p>

<ol>
	<li>make只能用来分配及初始化类型为slice，map和chan的数据；new可以分配任意类型的数据</li>
	<li>new分配返回的是指针，即类型为*T；make返回的是数据的值，即T</li>
	<li>make分配后会对数据进行初始化，而new不会</li>
</ol>

<pre>
<code>package main

import &quot;fmt&quot;

func main() {


	s := new(string)
	fmt.Printf(&quot;s: %T
&quot;, s) //*string
	fmt.Printf(&quot;s: %v
&quot;, *s)

	i2 := new([]int)
	fmt.Printf(&quot;i2: %T
&quot;, i2) //*[]int
	fmt.Printf(&quot;i2: %v
&quot;, *i2)

	i3 := make([]int, 10, 100) //初始化容量为100，长度为10
	fmt.Printf(&quot;i3: %T
&quot;, i3)
	fmt.Printf(&quot;i3: %v
&quot;, i3)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>s: *string
s: 
i2: *[]int
i2: []
i3: []int
i3: [0 0 0 0 0 0 0 0 0 0]
</code></pre>

<blockquote>
<p>内建函数make(T,args)与new(T)的用途不一样。它只用来创建slice，map和chan，并且返回一个初始化后的类型为T的数据。之所以不同，是因为这三个类型的背后引用了使用前必须初始化的数据结构。例如：slice是一个三元描述符，包含一个指向数据的指针，长度，以及容量，在这些项被初始化之前，slice都是nil。对于slice，map和chan，make初始化这些内部数据结构，并准备好可用的值。</p>
</blockquote>

<h3>bytes</h3>

<p>bytes提供了对字节切片进行读写操作的一系列函数，字节切片处理函数比较多分为基本处理函数，比较函数，后缀检查函数，索引函数，分割函数，大小写处理函数和子切片处理函数。</p>

<pre>
<code>package main

import (
	&quot;bytes&quot;
	&quot;fmt&quot;
)

func main() {

	s1 := &quot;hello world!&quot;
	b1 := []byte(&quot;你好，世界！&quot;)
	fmt.Printf(&quot;s1: %v
&quot;, s1)
	fmt.Printf(&quot;b1: %v
&quot;, b1)

	//bytes和string的相互转换
	//1.bytes转string
	fmt.Printf(&quot;string(b1): %v
&quot;, string(b1))
	//2.string转bytes
	fmt.Printf(&quot;[]byte(s1): %v
&quot;, []byte(s1))

	//contains：检查bytes中是否包含子bytes
	fmt.Printf(&quot;bytes.Contains(b1, []byte(&quot;世界&quot;)): %v
&quot;, bytes.Contains(b1, []byte(&quot;世界&quot;)))

	//count：统计某个bytes出现的次数
	fmt.Printf(&quot;bytes.Count([]byte(s1), []byte(&quot;l&quot;)): %v
&quot;, bytes.Count([]byte(s1), []byte(&quot;l&quot;)))

	//compare:比较两个bytes The result will be 0 if a == b, -1 if a &lt; b, and +1 if a &gt; b.
	fmt.Printf(&quot;bytes.Compare(b1, []byte(&quot;hello&quot;)): %v
&quot;, bytes.Compare(b1, []byte(&quot;hello&quot;)))

	//分割bytes
	before, after, _ := bytes.Cut(b1, []byte(&quot;，&quot;))
	fmt.Printf(&quot;before: %v
&quot;, string(before))
	fmt.Printf(&quot;after: %v
&quot;, string(after))

	//连接bytes
	b := bytes.Join([][]byte{b1, []byte(s1)}, []byte(&quot;===&quot;))
	fmt.Printf(&quot;b: %v
&quot;, string(b))

	//runes 转成utf8编码 这样能够正确计算中文长度
	r := bytes.Runes(b1)
	fmt.Printf(&quot;bytes.Runes(b1): %v
&quot;, r)
	fmt.Printf(&quot;len(r): %v
&quot;, len(r))

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>s1: hello world!

b1: [228 189 160 229 165 189 239 188 140 228 184 150 231 149 140 239 188 129]

string(b1): 你好，世界！

[]byte(s1): [104 101 108 108 111 32 119 111 114 108 100 33]

bytes.Contains(b1, []byte(&quot;世界&quot;)): true

bytes.Count([]byte(s1), []byte(&quot;l&quot;)): 3

bytes.Compare(b1, []byte(&quot;hello&quot;)): 1

before: 你好

after: 世界！

b: 你好，世界！===hello world!

bytes.Runes(b1): [20320 22909 65292 19990 30028 65281]

len(r): 6
</code></pre>

<h3>errors</h3>

<p>errors包实现了操作错误的函数。go语言使用error类型来返回函数执行过程中遇到的错误，如果返回的error值为nil，则表示未遇到错误，否则error会返回一个字符串，用于说明遇到了什么错误。</p>

<p>error的结构</p>

<pre>
<code>type error interface {
    Error() string
}
</code></pre>

<p><strong>你可以使用任何类型去实现它（只要添加一个Error()方法即可）</strong>，也就是说，error可以是任何类型，这意味着，函数返回的error值实际可以包含任意信息，不一定是字符串。</p>

<p>error不一定表示一个错误，它可以表示任何信息，比如io包中就用error类型的io.EOF表示数据读取结束，而不是遇到了什么错误。</p>

<p>errors包实现了一个最简单的error类型，只包含了一个字符串，它可以记录大多数情况下遇到的错误信息。errors包的用法很简单，只有一个New函数，用于生成一个简单的error对象：</p>

<pre>
<code>func New(text string) error
</code></pre>

<pre>
<code>package main

import (
	&quot;errors&quot;
	&quot;fmt&quot;
	&quot;time&quot;
)

//自定义errors
type MyError struct {
	When time.Time
	What string
}

/*
type error interface {
	Error() string
}


error是一个接口，只要实现了Error方法，就可以是一个error

*/

func (e MyError) Error() string {
	return fmt.Sprintf(&quot;%v : %v&quot;, e.When, e.What)
}

//检测字符串是否为空
func check_str(s string) (err error) {

	if s == &quot;&quot; {
		err = errors.New(&quot;字符串不能为空...&quot;)
	} else {
		err = MyError{
			When: time.Date(2022, 11, 11, 11, 11, 11, 11, time.UTC),
			What: fmt.Sprintf(&quot;%v 不是一个空字符串...&quot;, s),
		}
	}
	return

}
func main() {

	s := &quot;&quot;
	err := check_str(s)
	fmt.Printf(&quot;err: %v
&quot;, err)
	s2 := &quot;hello python&quot;
	err2 := check_str(s2)
	fmt.Printf(&quot;err2: %v
&quot;, err2)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>err: 字符串不能为空...
err2: 2022-11-11 11:11:11.000000011 +0000 UTC : hello python 不是一个空字符串...</code></pre>

