
<BlogInfo title="golang学习笔记系列之标准库json的学习" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=89 category="golang" tag_list="[]" create_time="2022.11.23 22:47:10.959552" update_time="2022.11.23 22:47:10" />

^^^^^^^^^
<h3><img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&amp;refer=http%3A%2F%2Fp8.itc.cn&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1665661975&amp;t=37860c72d333426b69c936abcb7d5473" /></h3>

<h3>json</h3>

<p>这个包可以实现json的编码和解码，即实现json对象和struct之间相互转换。</p>

<p><strong>核心的两个函数</strong></p>

<pre>
<code>func Marshal(v interface{}) ([]byte ,error)  //将go语言中的struct编码成json,返回json字符串的字节切片和错误信息
</code></pre>

<pre>
<code>func Unmarshal(data []byte, v interface{}) error //将json解码成go语言中的struct，返回错误信息
</code></pre>

<pre>
<code>package main

import (
	&quot;encoding/json&quot;
	&quot;fmt&quot;
	&quot;os&quot;
)

type Person1 struct {
	Name   string
	Age    int
	PetDog Dog
}

type Dog struct {
	Name string
	Age  int
}

func main() {

	erha := Dog{Name: &quot;二哈&quot;, Age: 3}
	tom := Person1{Name: &quot;Tom&quot;, Age: 18, PetDog: erha}
	fmt.Printf(&quot;tom: %v
&quot;, tom)

	//1.将一个struct实例转换成一个json对象
	//Marshal接收一个任何类型的对象，然后会返回对应json字符串的字节切片
	b, _ := json.Marshal(tom)
	json_b := string(b)
	fmt.Printf(&quot;b: %v
&quot;, b)
	fmt.Printf(&quot;json_b: %v
&quot;, json_b)

	//2.将一个json字符串转成一个struct Unmarshal接收一个json字符串的字节切片和一个任意struct对象的地址
	//Unmarshal会将json字符串对象的值相应的赋给这个struct对象
	var tom2 Person1
	json.Unmarshal([]byte(json_b), &amp;tom2)
	fmt.Printf(&quot;tom2: %v
&quot;, tom2)

	//3.从io流中获取json字符串，然后转成struct
	f, _ := os.Open(&quot;demo.json&quot;)
	defer f.Close()
	json_decoder := json.NewDecoder(f)
	var tom3 map[string]interface{}
	json_decoder.Decode(&amp;tom3)
	for k, v := range tom3 {
		fmt.Printf(&quot;k:%v,v:%v
&quot;, k, v)
	}

	//4.将struct实例转成json后写入文件
	jerry := Person1{Name: &quot;Jerry&quot;, Age: 16, PetDog: erha}
	f2, _ := os.OpenFile(&quot;demo2.json&quot;, os.O_RDWR|os.O_CREATE, 0777)
	defer f2.Close()
	json_encoder := json.NewEncoder(f2)
	json_encoder.Encode(jerry)

	//从json文件中读取写入的内容
	res := make([]byte, 100)
	f3, _ := os.Open(&quot;demo2.json&quot;)
	f3.Read(res)
	defer f3.Close()
    fmt.Printf(&quot;res: %v
&quot;, res)


}

</code></pre>

<p><strong>运行结果</strong></p>

<pre>
<code>tom: {Tom 18 {二哈 3}}
b: [123 34 78 97 109 101 34 58 34 84 111 109 34 44 34 65 103 101 34 58 49 56 44 34 80 101 116 68 111 103 34 58 123 34 78 97 109 101 34 58 34 228 186 140 229 147 136 34 44 34 65 103 101 34 58 51 125 125]
json_b: {&quot;Name&quot;:&quot;Tom&quot;,&quot;Age&quot;:18,&quot;PetDog&quot;:{&quot;Name&quot;:&quot;二哈&quot;,&quot;Age&quot;:3}}
tom2: {Tom 18 {二哈 3}}
k:PetDog,v:map[Age:3 Name:二哈]
k:Name,v:Tom
k:Age,v:18
res: {&quot;Name&quot;:&quot;Jerry&quot;,&quot;Age&quot;:16,&quot;PetDog&quot;:{&quot;Name&quot;:&quot;二哈&quot;,&quot;Age&quot;:3}}</code></pre>

