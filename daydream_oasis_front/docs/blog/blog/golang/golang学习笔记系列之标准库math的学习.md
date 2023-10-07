
<BlogInfo title="golang学习笔记系列之标准库math的学习" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=103 category="golang" tag_list="[]" create_time="2022.12.25 17:59:52.866779" update_time="2022.12.25 17:59:52" />

^^^^^^^^^
<p><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" /></p>

<h3>math</h3>

<p>math包包含了一些基本的常量和数学函数。</p>

<pre>
<code>package main

import (
	&quot;fmt&quot;
	&quot;math&quot;
	&quot;math/rand&quot;
	&quot;time&quot;
)

func main() {

	//常量
	fmt.Printf(&quot;math.MaxFloat64: %v
&quot;, math.MaxFloat64)
	fmt.Printf(&quot;math.MaxFloat32: %v
&quot;, math.MaxFloat32)
	fmt.Printf(&quot;math.MaxInt64: %v
&quot;, math.MaxInt64)
	fmt.Printf(&quot;math.MaxInt32: %v
&quot;, math.MaxInt32)
	fmt.Printf(&quot;math.MaxInt16: %v
&quot;, math.MaxInt16)
	fmt.Printf(&quot;math.MaxInt8: %v
&quot;, math.MaxInt8)
	fmt.Printf(&quot;math.MaxInt: %v
&quot;, math.MaxInt)
	fmt.Printf(&quot;math.Pi: %.20f
&quot;, math.Pi)

	//数学函数

	//绝对值
	fmt.Printf(&quot;math.Abs(-100): %v
&quot;, math.Abs(-100))

	//幂函数
	fmt.Printf(&quot;math.Pow(2, 3): %v
&quot;, math.Pow(2, 3)) //2^3

	//开平方
	fmt.Printf(&quot;math.Sqrt(4): %v
&quot;, math.Sqrt(4))

	//开立方
	fmt.Printf(&quot;math.Cbrt(8): %v
&quot;, math.Cbrt(8))

	//向上取整
	fmt.Printf(&quot;math.Ceil(10.2): %v
&quot;, math.Ceil(10.2))
	//向下取整
	fmt.Printf(&quot;math.Floor(10.8): %v
&quot;, math.Floor(10.8))
	//四舍五入
	fmt.Printf(&quot;math.Round(10.4): %v
&quot;, math.Round(10.4))

	//取余
	fmt.Printf(&quot;math.Mod(10, 3): %v
&quot;, math.Mod(10, 3))

	//三角函数
	angle := math.Pi / 180 //1度
	fmt.Printf(&quot;math.Sin(90): %v
&quot;, math.Sin(90*angle))
	fmt.Printf(&quot;math.Cos(60): %v
&quot;, math.Cos(60*angle))
	fmt.Printf(&quot;math.Tan(90): %v
&quot;, math.Tan(45*angle))

	//随机数
	rand.Seed(time.Now().UnixMicro()) //设置随机数种子
	for i := 0; i &lt; 5; i++ {
		fmt.Printf(&quot;rand.Intn(100): %v
&quot;, rand.Intn(100)) //100以内的随机整数
		fmt.Printf(&quot;rand.Float64(): %v
&quot;, rand.Float64()) //0到1的随机小数

	}

}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>math.MaxFloat64: 1.7976931348623157e+308
math.MaxFloat32: 3.4028234663852886e+38
math.MaxInt64: 9223372036854775807
math.MaxInt32: 2147483647
math.MaxInt16: 32767
math.MaxInt8: 127
math.MaxInt: 9223372036854775807
math.Pi: 3.14159265358979311600
math.Abs(-100): 100
math.Pow(2, 3): 8
math.Sqrt(4): 2
math.Cbrt(8): 2
math.Ceil(10.2): 11
math.Floor(10.8): 10
math.Round(10.4): 10
math.Mod(10, 3): 1
math.Sin(90): 1
math.Cos(60): 0.5000000000000001
math.Tan(90): 1
rand.Intn(100): 12
rand.Float64(): 0.9683545409741706
rand.Intn(100): 36
rand.Float64(): 0.8207458891921628
rand.Intn(100): 52
rand.Float64(): 0.5214102032604347
rand.Intn(100): 6
rand.Float64(): 0.537895866071663
rand.Intn(100): 99
rand.Float64(): 0.7215569611912539</code></pre>

