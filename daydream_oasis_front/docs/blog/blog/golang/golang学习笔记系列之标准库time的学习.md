
<BlogInfo title="golang学习笔记系列之标准库time的学习" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=150 category="golang" tag_list="[]" create_time="2022.11.14 23:05:38.202807" update_time="2022.11.14 23:05:38" />

^^^^^^^^^
<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" /></p>

<h3>time</h3>

<p>Package time provides functionality for measuring and displaying time.（用于时间的测量和显示）</p>

<h4>基本使用</h4>

<pre>
<code>//获取当前时间
	now := time.Now()
	fmt.Printf(&quot;now: %v
&quot;, now)
	year := now.Year()          //年
	month := now.Month()        //月
	day := now.Day()            //日
	hour := now.Hour()          //时
	minute := now.Minute()      //分
	second := now.Second()      //秒
	nsecond := now.Nanosecond() //纳秒
	fmt.Printf(&quot;%v-%v-%v:%v:%v:%v:%v
&quot;, year, month, day, hour, minute, second, nsecond)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>now: 2022-11-14 21:53:00.435701792 +0800 CST m=+0.000115447
2022-November-14:21:53:0:435701792
</code></pre>

<h4>时间戳</h4>

<p>时间戳是自1970年1月1日（08:00:00GMT）至当前时间的总秒数。它也被称为Unix时间戳。</p>

<pre>
<code>//时间戳
fmt.Printf(&quot;now.Unix(): %v
&quot;, now.Unix())           //秒数
fmt.Printf(&quot;now.UnixMicro(): %v
&quot;, now.UnixMicro()) //毫秒
fmt.Printf(&quot;now.UnixNano(): %v
&quot;, now.UnixNano())   //纳秒

//时间戳转成时间
fmt.Printf(&quot;time.Unix(now.Unix(), 0): %v
&quot;, time.Unix(now.Unix(), 0))
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>now.Unix(): 1668434792
now.UnixMicro(): 1668434792741556
now.UnixNano(): 1668434792741556203
time.Unix(now.Unix(), 0): 2022-11-14 22:06:32 +0800 CST
</code></pre>

<h4>时间的&quot;运算&quot;</h4>

<pre>
<code>//时间的运算
	today := now
	tomorrow := today.Add(time.Hour * 24) //在当前时间上增加24小时
	fmt.Printf(&quot;today: %v
&quot;, today)
	fmt.Printf(&quot;tomorrow: %v
&quot;, tomorrow)

	dif := today.Sub(tomorrow) //今天与昨天相差的时间
	fmt.Printf(&quot;dif: %v
&quot;, dif)

	//比较两个时间是否相同
	fmt.Printf(&quot;today.Equal(tomorrow): %v
&quot;, today.Equal(tomorrow))

	//判断当前时间是否在目标时间之前
	fmt.Printf(&quot;today.Before(tomorrow): %v
&quot;, today.Before(tomorrow))

	//判断当前时间是否在目标时间之后
	fmt.Printf(&quot;today.After(tomorrow): %v
&quot;, today.After(tomorrow))
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>today: 2022-11-14 22:16:35.620284622 +0800 CST m=+0.000048094
tomorrow: 2022-11-15 22:16:35.620284622 +0800 CST m=+86400.000048094
dif: -24h0m0s
today.Equal(tomorrow): false
today.Before(tomorrow): true
today.After(tomorrow): false
</code></pre>

<h4>Ticker和Timer</h4>

<pre>
<code>//定时器Ticker
	c := time.Tick(time.Second) //设置一个间隔一秒的定时器
	for i := range c {
		fmt.Printf(&quot;now: %v
&quot;, i)             //每隔一秒打印一下当前时间
		if i.After(now.Add(time.Second * 3)) { //3秒后停止
			break
		}
	}

	//Timer
	t := time.NewTimer(time.Second * 2)
	fmt.Printf(&quot;now2: %v
&quot;, time.Now())
	&lt;-t.C
	fmt.Printf(&quot;now2 after 2 seconds: %v
&quot;, time.Now()) //两秒后执行到这里
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>now: 2022-11-14 22:34:08.697290905 +0800 CST m=+1.000982288
now: 2022-11-14 22:34:09.697399128 +0800 CST m=+2.001090512
now: 2022-11-14 22:34:10.697623176 +0800 CST m=+3.001314560
now2: 2022-11-14 22:34:10.697739262 +0800 CST m=+3.001430647
now2 after 2 seconds: 2022-11-14 22:34:12.698702444 +0800 CST m=+5.002393830
</code></pre>

<h4>时间格式化</h4>

<p>时间类型有一个自带的Format方法，需要注意的是Go语言中格式化的模板不是常见的Y-m-d H:M:S，而是使用Go的诞生时间2006年1月2号15点04分（记忆口诀为：2006 1 2 3 4）。</p>

<pre>
<code>//时间格式化
fmt.Printf(&quot;now.Format(&quot;2006-01-02 15:04:05.000 Mon Jan&quot;): %v
&quot;, now.Format(&quot;2006/01/02 15:04:05.000 Mon Jan&quot;)) //24小时制
fmt.Printf(&quot;now.Format(&quot;Mon Jan 2006-01-02 3:4:4 PM&quot;): %v
&quot;, now.Format(&quot;Mon Jan 2006-01-02 3:4:4.000 PM&quot;))     //12小时制
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>now.Format(&quot;2006-01-02 15:04:05.000 Mon Jan&quot;): 2022/11/14 22:44:56.882 Mon Nov
now.Format(&quot;Mon Jan 2006-01-02 3:4:4 PM&quot;): Mon Nov 2022-11-14 10:44:44.882 PM
</code></pre>

<h4>解析字符串格式的时间</h4>

<pre>
<code>//解析字符串格式的时间
loc, _ := time.LoadLocation(&quot;Asia/Shanghai&quot;)

//第一个参数指定格式，第二参数为字符串格式的时间，第三个参数指定时区
t2, _ := time.ParseInLocation(&quot;2006/01/02 15:04:05.000 Mon Jan&quot;, &quot;2022/11/11 22:44:56.882 Mon Nov&quot;, loc)
fmt.Printf(&quot;t2: %T
&quot;, t2)
fmt.Printf(&quot;t2: %v
&quot;, t2)
</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>t2: time.Time
t2: 2022-11-11 22:44:56.882 +0800 CST
</code>
</pre>

<p>&nbsp;</p>

