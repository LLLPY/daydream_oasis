
<BlogInfo title="golang学习笔记系列之并发编程" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=568 category="golang" tag_list="[]" create_time="2022.10.05 16:17:09.592346" update_time="2022.10.05 16:17:09" />

^^^^^^^^^
<h2><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" /></h2>

<h2>并发编程</h2>

<p>golang中的并发，是函数相互独立运行的能力，goroutines是并发运行的函数。golang提供了goroutines作为并发处理的一种方式。</p>

<p>创建一个协程非常简单，就是在一个任务函数前面添加一个go关键字：</p>

<pre>
<code>go task()
</code></pre>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;time&quot;
)

func show(name string) {
	for i := 0; i &lt; 5; i++ {
		fmt.Printf(&quot;name: %v
&quot;, name)
		time.Sleep(time.Millisecond * 100)
	}
}

func main() {

	go show(&quot;Python&quot;) //开启一个go协程
	go show(&quot;Golang&quot;) //开启另外一个go协程
	time.Sleep(time.Millisecond * 2000)
	print(&quot;hello world!
&quot;) //默认情况下：主线程结束后其他线程也会结束
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>name: Golang
name: Python
name: Python
name: Golang
name: Golang
name: Python
name: Python
name: Golang
name: Python
name: Golang
hello world!
</code></pre>

<h3>并发编程之channel通道</h3>

<p>go提供了一种称为通道的机制，用于在goroutine之间共享数据。当goroutine执行并发活动时，需要在goroutine之间共享数据资源，channel通道充当goroutine之间的管道并提供一种机制来保证同步交换。</p>

<p>需要在声明通道时指定数据类型，我们可以共享内置，命名，结构和引用类型的值和指针。数据在通道上传递：<strong>在任何给定的时间只有一个goroutine可以访问数据项，因此按照设计不会发生数据竞争。</strong></p>

<p>根据数据交换的行为，有两种通道类型：<strong>无缓冲通道</strong>和<strong>缓冲通道</strong>。无缓存通道用于执行goroutine之间的同步信号，而缓冲通道用于执行异步信号。无缓冲通道保证在发送和接收发生的瞬间执行两个goroutine之间的交换。缓冲通道没有这样的保证。</p>

<p>通道由make函数创建，该函数指定chan关键字和通道的元素类型。</p>

<p><strong>语法</strong></p>

<pre>
<code>chan_ubuffered:=make(chan int) //整型无缓冲通道
chan_buffered:=make(chan int, 10) //整型有缓冲通道
</code></pre>

<p><strong>将值发送给通道使用==&lt;-==运算符</strong></p>

<pre>
<code>c:=make(chan string)
c &lt;- &quot;hello&quot;
</code></pre>

<p><strong>从通道中取值</strong></p>

<pre>
<code>var name string
name &lt;- c
</code></pre>

<p><strong>无缓冲通道</strong></p>

<p>在无缓冲通道中，在接收到任何值之前没有能力保存它。在这种类型的通道中，发送和接收的goroutine在任何发送或接收操作完成之前的同一时刻都是准备就绪的。如果两个goroutine没有在同一时刻准备好，则通道会让其中已准备好的一方等待另一方，直到两个都准备就绪。同步是通道上发送和接收之间交互的基础。没有另一个就不可能发生。</p>

<p><strong>缓冲通道</strong></p>

<p>在缓冲通道中，有能力在接收到一个或多个值之前保存它们。在这种类型的通道中，不强制goroutine在同一时刻准备好执行发送和接收。当发送或接收阻塞时也有不同的条件。<strong>只有当通道中没有要接收的值时，接收才会阻塞</strong>；<strong>仅当没有可用缓冲区来放置正在发送的值时，发送才会阻塞。</strong></p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;time&quot;
)

// 将值传入通道
func send(c *chan string, val string) {
	*c &lt;- val
}

// 将值从通道中取出
func get(c *chan string) *string {
	val := &lt;-*c
	fmt.Printf(&quot;val: %v
&quot;, val)
	return &amp;val
}

func main() {

	c := make(chan string) //无缓冲通道
	defer close(c)

	go send(&amp;c, &quot;hello&quot;)
	go get(&amp;c)
	go send(&amp;c, &quot;world&quot;)
	go get(&amp;c)

	time.Sleep(time.Millisecond * 1000)
	fmt.Printf(&quot;main end...&quot;)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>val: hello
val: world
main end...
</code></pre>

<h3>WaitGroup实现同步</h3>

<p>在golang中，如果除了主协程以外还有其他的协程，当主协程结束的时候其他协程也会一起结束，不管它们有没有执行完毕，即默认是协程守护的。使用WaitGroup可以使用协程之间的同步，（个人感觉类似于python中的join方法）。</p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
)

func show_msg(msg int) {
	fmt.Printf(&quot;msg: %d
&quot;, msg)
}

func main() {
	for i := 0; i &lt; 10; i++ {
		go show_msg(i)
	}

	print(&quot;end main...&quot;)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>end main...msg: 3
msg: 0
msg: 1
msg: 2
msg: 6
msg: 4
msg: 9
</code></pre>

<blockquote>
<p>可以看到上面的代码的每次运行结果都可能不一样，因为每一个show_msg都用一个协程来启动，它们和主协程一样，但是只要主协程执行结束，不管它们有没有被执行，都会被结束。</p>
</blockquote>

<p><strong>使用WaitGroup后</strong></p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;sync&quot;
)

var mg sync.WaitGroup

func show_msg(msg int) {
	fmt.Printf(&quot;msg: %d
&quot;, msg)
	defer mg.Add(-1) //任务完成就减一
}

func main() {

	for i := 0; i &lt; 10; i++ {
		mg.Add(1) //添加任务就加一
		go show_msg(i)
	}
	// Counter is 0, no need to wait.
	mg.Wait() //如果WaitGroup的计数为0就停止等待
	print(&quot;end main...&quot;)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>msg: 9
msg: 0
msg: 1
msg: 2
msg: 3
msg: 4
msg: 5
msg: 6
msg: 7
msg: 8
end main...
</code></pre>

<blockquote>
<p>在使用WaitGroup后，通过WaitGroup来进行计数，每添加一个协程，计数加一（Add(1)）；每完成一个协程，计数减一(Add(-1))，只有当计数为0时Wait才不会等待。</p>
</blockquote>

<h3>并发编程之runtime包</h3>

<p>runtime包中包含了一些协程管理相关的API。</p>

<h4>runtime.Gosched()</h4>

<p>功能：让出处理机，给其他的协程去使用。</p>

<blockquote>
<p>// Gosched yields the processor, allowing other goroutines to run. It does not</p>

<p>// suspend the current goroutine, so execution resumes automatically.</p>
</blockquote>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;runtime&quot;
)

func show_msg(msg int) {
	fmt.Printf(&quot;msg: %v
&quot;, msg)

}

func main() {
	go show_msg(100)

	runtime.Gosched() //在主协程中使用的

	print(&quot;main end...&quot;)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>msg: 100
main end...
</code></pre>

<blockquote>
<p>在上面的代码中，我们可以看到在主协程中调用了Gosched方法，因此当主协程和show_msg协程抢占处理机时，如果show_msg协程先抢到执行，则执行结果如上；如果主协程先抢到处理机，则它会主动让出处理机，此时show_msg会拿到处理机，因此执行结果还是如上。</p>
</blockquote>

<h4>runtime.Goexit()</h4>

<p>功能：退出协程</p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;runtime&quot;
)

func show_msg(msg int) {
	for i := 0; i &lt; 5; i++ {
		if i == 3 { //i等于3时直接结束协程
			runtime.Goexit()
		}
		fmt.Printf(&quot;msg: %v-%v
&quot;, msg, i)

	}

}

func main() {
	go show_msg(100)
	runtime.Gosched()
	print(&quot;main end...&quot;)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>msg: 100-0
msg: 100-1
msg: 100-2
main end...
</code></pre>

<h3>Mutex实现同步</h3>

<p>除了channel实现同步之外，还可以使用Mutex互斥锁实现同步。</p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;sync&quot;
)

var n int = 100
var lock sync.Mutex
var wg sync.WaitGroup

func add() {
	lock.Lock() //加锁
	n += 1
	lock.Unlock() //解锁
	wg.Add(-1)
}

func sub() {
	lock.Lock()
	n -= 1
	lock.Unlock()
	wg.Add(-1) //完成协程任务，计数减一
}

func main() {

	//当多个协程共同处理某一个数据时，如果不进行加锁，就会出现数据混乱的情况，例如：多个协程对一个数值进行加一和减一的操作
	//因此在多协程中，我们可以对数据进行的操作加锁，让同一时刻只能有一个协程对数据进行操作
	for i := 0; i &lt; 100000; i++ {
		wg.Add(1) //新增协程任务，计数加一
		go add()
		wg.Add(1)
		go sub()
	}
	wg.Wait() //主协程等待子协程执行完毕
	fmt.Printf(&quot;n: %v
&quot;, n)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>n: 100
</code></pre>

<h3>并发编程之select</h3>

<ol>
	<li>
	<p>select是go中的一个控制结构，类似于switch语句，用于处理异步IO操作。select会监听case语句中的channel的读写操作，当case中channel读写操作为非阻塞状态时，会触发相应的动作。</p>

	<blockquote>
	<p>select中case语句必须是一个channel操作（读或者写）</p>

	<p>select中default子句总是可以运行的</p>
	</blockquote>
	</li>
	<li>
	<p>如果有多个case都可运行，select会随机公平地选出一个执行，其他不会执行。</p>
	</li>
	<li>
	<p>如果没有可运行的case语句，且有default语句，那么就会执行default语句。</p>
	</li>
	<li>
	<p>如果没有可运行的case语句，且没有default语句，select将会阻塞。</p>
	</li>
</ol>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;time&quot;
)

var chanName = make(chan string, 0)
var chanAge = make(chan int, 0)

func main() {

	go func() {
		for i := 0; i &lt; 5; i++ {
			name := &quot;Tom&quot;
			chanName &lt;- name
			chanAge &lt;- i
		}
	}()

	for {
		select {
		case name := &lt;-chanName: //读chanName
			fmt.Printf(&quot;name: %v
&quot;, name)
		case age := &lt;-chanAge:
			fmt.Printf(&quot;age: %v
&quot;, age)

		default:
			print(&quot;default...
&quot;)

		}
		time.Sleep(time.Second)
	}

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>default...
name: Tom
age: 0
name: Tom
age: 1
name: Tom
age: 2
name: Tom
age: 3
name: Tom
age: 4
default...
default...
default...
default...
</code></pre>

<h3>并发编程是Timer</h3>

<p>Timer顾名思义，就是计时器的意思，可以实现一些定时操作，内部也是通过channel实现的。</p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;time&quot;
)

func main() {

	t1 := time.NewTimer(time.Second) //等待1秒钟
	fmt.Printf(&quot;time.Now(): %v
&quot;, time.Now())
	res := &lt;-t1.C //一直处于阻塞状态，直到到达等待时间
	fmt.Printf(&quot;res: %v
&quot;, res)
	fmt.Printf(&quot;time.Now(): %v
&quot;, time.Now())

	time.After(time.Second) //一秒后，After其实对NewTimer进行了一次封装
	fmt.Printf(&quot;time.Now(): %v
&quot;, time.Now())

	//停止计时器
	t2 := time.NewTimer(time.Second * 2)

	go func() {
		print(&quot;执行到了这里...
&quot;)
		&lt;-t2.C
		print(&quot;匿名函数被执行...
&quot;)
	}()

	t2.Stop() //如果调用了stop，上面的协程&lt;-t2.C以后的语句都不会被执行
	time.Sleep(time.Second * 3)

	//修改计时时间
	t3 := time.NewTimer(time.Second)
	fmt.Printf(&quot;time.Now(): %v
&quot;, time.Now())
	t3.Reset(time.Second * 2) //修改计时为2两秒
	&lt;-t3.C
	fmt.Printf(&quot;time.Now(): %v
&quot;, time.Now())

	fmt.Printf(&quot;main end...
&quot;)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>time.Now(): 2022-10-05 15:04:46.380136682 +0800 CST m=+0.000102410
res: 2022-10-05 15:04:47.380331775 +0800 CST m=+1.000297497
time.Now(): 2022-10-05 15:04:47.380414771 +0800 CST m=+1.000380500
time.Now(): 2022-10-05 15:04:47.380453944 +0800 CST m=+1.000419671
执行到了这里...
time.Now(): 2022-10-05 15:04:50.381683725 +0800 CST m=+4.001649449
time.Now(): 2022-10-05 15:04:52.38280595 +0800 CST m=+6.002771675
main end...
</code></pre>

<h3>并发编程之Ticker</h3>

<p>Timer是到达时间后执行一次，而Ticker是周期性的执行，是一个定时器。</p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;time&quot;
)

func main() {

	// 每隔一秒打印一次当前时间
	t1 := time.NewTicker(time.Second)
	n := 0
	for _ = range t1.C {
		fmt.Printf(&quot;time.Now(): %v
&quot;, time.Now())
		n += 1
		if n &gt; 5 {
			t1.Stop()
			break
		}
	}

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>time.Now(): 2022-10-05 15:20:32.53228156 +0800 CST m=+8.000943370
time.Now(): 2022-10-05 15:20:33.532483936 +0800 CST m=+9.001145744
time.Now(): 2022-10-05 15:20:34.531494225 +0800 CST m=+10.000156042
time.Now(): 2022-10-05 15:20:35.532310152 +0800 CST m=+11.000971959
time.Now(): 2022-10-05 15:20:36.532446657 +0800 CST m=+12.001108468
time.Now(): 2022-10-05 15:20:37.531670839 +0800 CST m=+13.000332645
</code></pre>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;time&quot;
)

func main() {


	t2 := time.NewTicker(time.Second)
	chanInt := make(chan int)
	go func() {
		//每秒钟向chanInt随机写一个数据
		for _ = range t2.C {
			select {
			case chanInt &lt;- 1:
			case chanInt &lt;- 2:
			case chanInt &lt;- 3:
			case chanInt &lt;- 4:
			case chanInt &lt;- 5:

			}
		}

	}()
	sum := 0
	for v := range chanInt {
		sum += v
		fmt.Printf(&quot;v: %v
&quot;, v)
		if sum &gt;= 10 {
			close(chanInt)
			break
		}
	}

	print(&quot;main end...
&quot;)

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>v: 1
v: 4
v: 1
v: 5
main end...
</code></pre>

<h3>并发编程之原子操作</h3>

<p>当多个协程操作同一个数据时，如果不加锁就可能会出现数据混乱的情况，除了使用mutex锁来解决这个问题外，golang还提供了原子操作这一概念来解决这个问题。</p>

<p>atomic提供的原子操作能够确保任一时刻只有一个goroutine对变量进行操作，善用atomic能够避程序中出现大量的锁操作。</p>

<p>atomic常见的操作有：</p>

<ul>
	<li>增减：Add</li>
	<li>加载（读）：Load</li>
	<li>存储（写）：Store</li>
	<li>比较和交换：cas</li>
	<li>交换：swap</li>
</ul>

<p><strong>增减操作</strong></p>

<pre>
<code>// AddInt32 atomically adds delta to *addr and returns the new value.
func AddInt32(addr *int32, delta int32) (new int32)

// AddUint32 atomically adds delta to *addr and returns the new value.
// To subtract a signed positive constant value c from x, do AddUint32(&amp;x, ^uint32(c-1)).
// In particular, to decrement x, do AddUint32(&amp;x, ^uint32(0)).
func AddUint32(addr *uint32, delta uint32) (new uint32)

// AddInt64 atomically adds delta to *addr and returns the new value.
func AddInt64(addr *int64, delta int64) (new int64)

// AddUint64 atomically adds delta to *addr and returns the new value.
// To subtract a signed positive constant value c from x, do AddUint64(&amp;x, ^uint64(c-1)).
// In particular, to decrement x, do AddUint64(&amp;x, ^uint64(0)).
func AddUint64(addr *uint64, delta uint64) (new uint64)

// AddUintptr atomically adds delta to *addr and returns the new value.
func AddUintptr(addr *uintptr, delta uintptr) (new uintptr)
</code></pre>

<p><strong>加载操作</strong></p>

<pre>
<code>// LoadInt32 atomically loads *addr.
func LoadInt32(addr *int32) (val int32)

// LoadInt64 atomically loads *addr.
func LoadInt64(addr *int64) (val int64)

// LoadUint32 atomically loads *addr.
func LoadUint32(addr *uint32) (val uint32)

// LoadUint64 atomically loads *addr.
func LoadUint64(addr *uint64) (val uint64)

// LoadUintptr atomically loads *addr.
func LoadUintptr(addr *uintptr) (val uintptr)

// LoadPointer atomically loads *addr.
func LoadPointer(addr *unsafe.Pointer) (val unsafe.Pointer)
</code></pre>

<p><strong>存储操作</strong></p>

<pre>
<code>// StoreInt32 atomically stores val into *addr.
func StoreInt32(addr *int32, val int32)

// StoreInt64 atomically stores val into *addr.
func StoreInt64(addr *int64, val int64)

// StoreUint32 atomically stores val into *addr.
func StoreUint32(addr *uint32, val uint32)

// StoreUint64 atomically stores val into *addr.
func StoreUint64(addr *uint64, val uint64)

// StoreUintptr atomically stores val into *addr.
func StoreUintptr(addr *uintptr, val uintptr)

// StorePointer atomically stores val into *addr.
func StorePointer(addr *unsafe.Pointer, val unsafe.Pointer)
</code></pre>

<p><strong>比较和交换操作</strong></p>

<pre>
<code>// CompareAndSwapInt32 executes the compare-and-swap operation for an int32 value.
func CompareAndSwapInt32(addr *int32, old, new int32) (swapped bool)

// CompareAndSwapInt64 executes the compare-and-swap operation for an int64 value.
func CompareAndSwapInt64(addr *int64, old, new int64) (swapped bool)

// CompareAndSwapUint32 executes the compare-and-swap operation for a uint32 value.
func CompareAndSwapUint32(addr *uint32, old, new uint32) (swapped bool)

// CompareAndSwapUint64 executes the compare-and-swap operation for a uint64 value.
func CompareAndSwapUint64(addr *uint64, old, new uint64) (swapped bool)

// CompareAndSwapUintptr executes the compare-and-swap operation for a uintptr value.
func CompareAndSwapUintptr(addr *uintptr, old, new uintptr) (swapped bool)

// CompareAndSwapPointer executes the compare-and-swap operation for a unsafe.Pointer value.
func CompareAndSwapPointer(addr *unsafe.Pointer, old, new unsafe.Pointer) (swapped bool)
</code></pre>

<p><strong>交换操作</strong></p>

<pre>
<code>// SwapInt32 atomically stores new into *addr and returns the previous *addr value.
func SwapInt32(addr *int32, new int32) (old int32)

// SwapInt64 atomically stores new into *addr and returns the previous *addr value.
func SwapInt64(addr *int64, new int64) (old int64)

// SwapUint32 atomically stores new into *addr and returns the previous *addr value.
func SwapUint32(addr *uint32, new uint32) (old uint32)

// SwapUint64 atomically stores new into *addr and returns the previous *addr value.
func SwapUint64(addr *uint64, new uint64) (old uint64)

// SwapUintptr atomically stores new into *addr and returns the previous *addr value.
func SwapUintptr(addr *uintptr, new uintptr) (old uintptr)

// SwapPointer atomically stores new into *addr and returns the previous *addr value.
func SwapPointer(addr *unsafe.Pointer, new unsafe.Pointer) (old unsafe.Pointer)
</code></pre>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;sync&quot;
	&quot;sync/atomic&quot;
)

var N int32 = 100
var wg sync.WaitGroup

func add() {
	atomic.AddInt32(&amp;N, 1) //加一操作
	defer wg.Add(-1)
}

func sub() {
	atomic.AddInt32(&amp;N, -1) //减一操作
	defer wg.Add(-1)
}
func main() {
	for i := 0; i &lt; 100000; i++ {
		go add()
		wg.Add(1)
		go sub()
		wg.Add(1)
	}

	wg.Wait()
	fmt.Printf(&quot;N: %v
&quot;, N)
}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>N: 100
</code></pre>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;sync/atomic&quot;
)

func main() {

	var i int32 = 100
	fmt.Printf(&quot;i: %v
&quot;, i)
	atomic.AddInt32(&amp;i, 100) //加100
	fmt.Printf(&quot;i: %v
&quot;, i)
	atomic.AddInt32(&amp;i, -50) //减50
	fmt.Printf(&quot;i: %v
&quot;, i)

	fmt.Printf(&quot;atomic.LoadInt32(&amp;i): %v
&quot;, atomic.LoadInt32(&amp;i)) //读取i的值
	atomic.StoreInt32(&amp;i, 1000)                                    //修改i的值为1000
	fmt.Printf(&quot;i: %v
&quot;, i)

	//cas 其他操作的根基
	success := atomic.CompareAndSwapInt32(&amp;i, i, 666) //修改i为666
	if success {

		fmt.Printf(&quot;修改成功！i: %v
&quot;, i)
	}

	//swap 直接交换 比较暴力
	b := atomic.CompareAndSwapInt32(&amp;i, i, 888)
	if b {
		fmt.Printf(&quot;修改成功！i: %v
&quot;, i)
	}

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>i: 100
i: 200
i: 150
atomic.LoadInt32(&amp;i): 150
i: 1000
修改成功！i: 666
修改成功！i: 888</code></pre>

