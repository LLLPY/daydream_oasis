---

next: false

---



<BlogInfo id="395" title="golang学习笔记系列之基本数据类型" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="543" category="golang" tag_list="['golang']" create_time="2022.09.10 17:57:57.594559" update_time="2022.09.13 19:56:52" />

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

## 基本数据类型

在go语言中，数据类型用于声明函数和变量。

数据类型的出现是为了把数据分成所需内存大小不同的数据，编程的时候需要用大数据的时候才去申请大内存，需要小数据的时候就去申请小的内存，就可以充分利用空间。

go语言按类别有以下几种数据：

类型 | 描述  
---|---  
布尔类型 | 布尔类型的值只可以是常量true或false。一个简单的例子：var flag=true  
数字类型 | 数字类型包括整型int，浮点型float32和浮点型float64；同时支持复数。（注意： **不能用0或者非0表示条件判断** ）  
字符串类型 |字符串就是一串固定长度的字符连接起来的字符序列。go语言的字符串是由单个字节连接起来的，go语言的字符串的字节使用utf8编码标识unicode文本。  
派生类型 | 派生类型包括：指针类型，数组类型，切片类型，结构体类型，channel类型，接口类型，map类型等等  
  
### 整数类型

go语言也有基于架构的类型，例如：int，uint和uintptr。

类型 | 描述  
---|---  
uint8 | 无符号8位整型（0到255）  
uint16 | 无符号16位整数（0到65535）  
uint32 | 无符号32位整数（0到4294967295）  
uint64 | 无符号64位整数（0到18446744073709551616）  
int8 | 有符号8位整数（-128到127）  
int16 | 有符号16位整数（-32768到32767）  
int32 | 有符号32位整数（-2147483648到2147483647）  
int64 | 有符号64位整数（-9223372036854775808到9223372036854775807）  

```golang
package main

import (
	"fmt"
	"math"
	"unsafe"
)

func main() {

	var a uint8
	var b uint16
	var c uint32
	var d uint64

	fmt.Printf("a: %v %T %dB  %v~%v
", a, a, unsafe.Sizeof(a), 0, math.MaxUint8)
	fmt.Printf("b: %v %T %dB  %v~%v
", b, b, unsafe.Sizeof(b), 0, math.MaxUint16)
	fmt.Printf("c: %v %T %dB  %v~%v
", c, c, unsafe.Sizeof(c), 0, math.MaxUint32)
	fmt.Printf("d: %v %T %dB  %v~%v
", d, d, unsafe.Sizeof(d), 0, math.MaxInt64)

	var e int8
	var f int16
	var g int32
	var h int64
	fmt.Printf("e: %v %T %dB  %v~%v
", e, e, unsafe.Sizeof(e), math.MinInt8, math.MaxInt8)
	fmt.Printf("f: %v %T %dB  %v~%v
", f, f, unsafe.Sizeof(f), math.MinInt16, math.MaxInt16)
	fmt.Printf("g: %v %T %dB  %v~%v
", g, g, unsafe.Sizeof(g), math.MinInt32, math.MaxInt32)
	fmt.Printf("h: %v %T %dB  %v~%v
", h, h, unsafe.Sizeof(h), math.MinInt64, math.MaxInt64)

	var i float32
	var j float64
	fmt.Printf("i: %v %T %dB  %v~%v
", i, i, unsafe.Sizeof(i), -math.MaxFloat32, math.MaxFloat32)
	fmt.Printf("j: %v %T %dB  %v~%v
", j, j, unsafe.Sizeof(j), -math.MaxFloat64, math.MaxFloat64)

	var k complex64
	var l complex128
	fmt.Printf("k: %v %T %dB  
", k, k, unsafe.Sizeof(k))
	fmt.Printf("l: %v %T %dB  
", l, l, unsafe.Sizeof(l))

}

/*
a: 0 uint8 1B  0~255
b: 0 uint16 2B  0~65535
c: 0 uint32 4B  0~4294967295
d: 0 uint64 8B  0~9223372036854775807
e: 0 int8 1B  -128~127
f: 0 int16 2B  -32768~32767
g: 0 int32 4B  -2147483648~2147483647
h: 0 int64 8B  -9223372036854775808~9223372036854775807
i: 0 float32 4B  -3.4028234663852886e+38~3.4028234663852886e+38
j: 0 float64 8B  -1.7976931348623157e+308~1.7976931348623157e+308
k: (0+0i) complex64 8B  
l: (0+0i) complex128 16B 
*/

```

### 进制的相互转换

```golang
package main

import "fmt"

func main() {

	//十进制的数
	a := 10

	fmt.Printf("a的十进制表示a: %d
", a)
	fmt.Printf("a的二进制表示a: %b
", a)
	fmt.Printf("a的八进制表示a: %o
", a)
	fmt.Printf("a的十六进制表示a: %x
", a)

	//定义一个八进制的数 以0开头
	b := 077

	fmt.Printf("b的十进制表示a: %d
", b)
	fmt.Printf("b的二进制表示a: %b
", b)
	fmt.Printf("b的八进制表示a: %o
", b)
	fmt.Printf("b的十六进制表示a: %x
", b)

	//定义一个十六进制的数 以0x开头
	c := 0x111

	fmt.Printf("c的十进制表示a: %d
", c)
	fmt.Printf("c的二进制表示a: %b
", c)
	fmt.Printf("c的八进制表示a: %o
", c)
	fmt.Printf("c的十六进制表示a: %x
", c)

}
```


### 浮点类型

类型 | 描述  
---|---  
float32 | IEEE-754 32位浮点型数  
float64 | IEEE-754 64位浮点型数  
complex64 | 32位实数和虚数  
complex128 | 64位实数和虚数  
  
### 其他数字类型

类型 | 描述  
---|---  
byte | 类似uint8  
rune | 类似int32  
  
### 字符串类型

在go语言中，字符串使用双引号""或者反引号来创建。双引号用来创建可解析的字符串，支持转义，但不能用来引用多行；反引号用来创建原生的字符串，可由多行组成，但不支持转义，并且可以包含除了反引号外其他所有字符。双引号创建可解析的字符串应用最广泛，反引号用来创建原生的字符串多用于书写多行消息，HTML以及正则表达式。

#### 字符串的拼接

```golang
package main

import (
	"bytes"
	"fmt"
	"strings"
)

func main() {

	//单行字符串 支持转义
	a := "hello world"

	//多行字符串 不支持转义
	b := `
			<div>
			<p>hello</p>
			</div>
		`
	fmt.Printf("a: %v\n", a)
	fmt.Printf("b: %v\n", b)

	//字符串的拼接
	s1 := "hello"
	s2 := "world"
	//1.加号拼接
	res1 := s1 + " " + s2
	fmt.Printf("s: %v\n", res1)

	//2.字符串格式化 Sprintf
	res2 := fmt.Sprintf("%s %s", s1, s2)
	fmt.Printf("res2: %v\n", res2)

	//3.strings.join()
	/*
		join会根据字符串数组得到内容，计算出一个拼接之后的字符串的长度，然后申请对应大小的内存，一个一个字符填入，
		在已有一个数组的情况下，这种效率会很高，但是本来没有，去构造这个数组的代价也很高
	*/
	res3 := strings.Join([]string{s1, s2}, " ") //第一个参数是字符串数组，第二个参数是连接符
	fmt.Printf("res3: %v\n", res3)

	//4.buffer.WriteString()
	/*
		这个比较理想，可以当成可变字符串使用，对内存的增长也有优化，如果能预估字符串的长度，还可以使用buffer.Grow()接口来设置capacity
		同时这是直接写到缓冲区，因此效率比较高
	*/
	var buffer bytes.Buffer
	buffer.WriteString(s1)
	buffer.WriteString(s2)
	fmt.Printf("buffer.String(): %v\n", buffer.String())


}
```

#### 转义字符

go语言的字符串常见的转义字符包含回车，换行，单双引号，制表符等

转义符 | 含义  
---|---  
| 回车符号  
| 换行符  
| 制表符（tab键，或者四个空格）  
' | 单引号  
" | 双引号  
\ | 反斜杠  
  
#### 切片操作

```golang
//切片操作
	s := "I am a student."
	m, n := 2, 4

	fmt.Printf("s[m:n]: %v\n", s[m:n]) //获取字符串s索引位置从m到n-1的值
	fmt.Printf("s[:n]: %v\n", s[:n])   //获取字符串s索引位置从0到n-1的值
	fmt.Printf("s[m:]: %v\n", s[m:])   //获取字符串s索引位置从m到len(s)-1的值
	fmt.Printf("s[:]: %v\n", s[:])     //获取字符串s
	fmt.Printf("s[m]: %v\n", s[m])     //获取字符串s索引位置m的字符的ascii值
```


#### 字符串的一些常用方法

方法 | 描述  
---|---  
len(s) | 获取字符串s的长度  
+或者fmt.Sprintf | 拼接字符串  
strings.Split(s,seq) | 用分隔符seq分割字符s  
strings.Contains(s,subs) | 查询字符串s中是否包含子串subs  
strings.HasPrefix(s,prefix)/strings.HasSuffix(s,suffix) | 判断前/后缀是否是指定的字符串  
strings.Index(s,subs)/strings.LastIndex(s,subs) |
查询子串subs在s中第一次(最后一次)出现的索引位置，若没有则返回-1  
strings.join(s_arr,seq) | 将字符串数组用seq拼接成一个字符串  
`

```golang
//分割字符串
	fmt.Printf("strings.Split(s, \" \"): %v\n", strings.Split(s, " "))

	//查询某个字符串是否包含指定的字符串
	fmt.Printf("strings.Contains(s, \"student\"): %v\n", strings.Contains(s, "student"))

	//判断前缀是否是指定的字符串
	fmt.Printf("strings.HasPrefix(s, \"hello\"): %v\n", strings.HasPrefix(s, "hello"))

	//判断后缀是否是指定的字符串
	fmt.Printf("strings.HasSuffix(s, \"student.\"): %v\n", strings.HasSuffix(s, "student."))

	//查找指定字符串第一次出现的索引位置
	fmt.Printf("strings.Index(s, \"a\"): %v\n", strings.Index(s, "aaa"))

	//查找指定字符串最后一次出现的索引位置
	fmt.Printf("strings.LastIndex(s, \"a\"): %v\n", strings.LastIndex(s, "a"))

	//拼接字符串数组
	fmt.Printf("strings.Join([]string{\"i\", \"am\", \"a\", \"student.\"}, \" \"): %v\n", strings.Join([]string{"i", "am", "a", "student."}, " "))
```

**运行结果**


```shell script
strings.Split(s, " "): [I am a student.]
strings.Contains(s, "student"): true
strings.HasPrefix(s, "hello"): false
strings.HasSuffix(s, "student."): true
strings.Index(s, "a"): -1
strings.LastIndex(s, "a"): 5
strings.Join([]string{"i", "am", "a", "student."}, " "): i am a student.
```


### 格式化输出

#### 普通占位符

占位符 | 说明 | 举例  
---|---|---  
%v | 相应值的默认格式。 | fmt.Printf("a: %v ", 100) ----> a:100  
%#v | 会打印出数据的完整格式。 | tom := studnet{"Tom"}fmt.Printf("tom: %#v ", tom)
---->tom: main.studnet{Name:"Tom"}  
%T | 相应值的类型。 | fmt.Printf("a: %T ", 100) ----> a:int  
%% | 输出%。 | fmt.Printf("%%") ---->%  

```golang
//相应数据的默认格式
a := 10
fmt.Printf("a: %#v\n", a)

tom := studnet{"Tom"}
//数据的完整格式
fmt.Printf("tom: %#v\n", tom)

//%
fmt.Printf("%%\n")
```


**运行结果**


```shell script
a: 10
tom: main.studnet{Name:"Tom"}
%
```


#### 布尔占位符

占位符 | 说明 | 举例  
---|---|---  
%t | 输出true或false。 | fmt.Printf("flag: %t ", true) ---->true  

```golang
//布尔占位符
flag := true
fmt.Printf("flag: %t\n", flag)
```

**运行结果**

```shell script
 flag: true 
```

#### 整数占位符

占位符 | 说明 | 举例  
---|---|---  
%b | 输出二进制表示 | fmt.Printf("%b ", 10) ---->1010  
%c | 相应的Unicode码值所表示的码符 | fmt.Printf("%c ",97) ---->a  
%d | 输出十进制表示 | fmt.Printf("%d ", 10) ---->10  
%o | 输出八进制表示 | fmt.Printf("%o ", 10) ---->12  
%x | 十六进制表示（小写字母） | fmt.Printf("%x ", 10) ---->a  
%X | 十六进制表示（大写字母） | fmt.Printf("%X ", 10) ---->A  
%q | 单引号围绕的字符字面值，由go语法安全的转义 | fmt.Printf("%q ", 10) ---->' '  
%U | Unicode格式：U+1234等同于"U+%04X" | fmt.Printf("%U ", 10) ---->U+000A  

```golang
//二进制输出
fmt.Printf("%b\n", 10)

//相应的Unicode码值对应的码符
fmt.Printf("%c\n", 97)

//八进制
fmt.Printf("%o\n", 10)

//十六进制 小写字母
fmt.Printf("%x\n", 10)

//十六进制 大写字母
fmt.Printf("%X\n", 10)

fmt.Printf("%q\n", 10)
fmt.Printf("%U\n", 10)
```


**运行结果**

```shell script
1010
a
12
a
A
'\n'
U+000A
```

#### 浮点数和复数占位符

占位符 | 说明 | 举例  
---|---|---  
%b | 无小数部分的，指数为二的幂的科学计数法，与strconv.FormatFloat的'b'转换格式一样 | fmt.Printf("%b ",10.1) ---->5685794529555251p-49  
%e | 科学计数法（小写字母） | fmt.Printf("%e ", 10.1) ---->1.010000e+01  
%E | 科学计数法（大写字母） | fmt.Printf("%E ", 10.1) ---->1.010000E+01  
%f | 有小数点而无指数 | fmt.Printf("%5.2f ", 10.1) ---->10.10（总长度为5，小数点两位）  
%g | 根据情况选择%e或%f以产生更紧凑的输出（无末尾的0） | fmt.Printf("%g ", 10.10000) ---->10.1  
%G | 根据情况选择%E或%f以产生更紧凑的输出（无末尾的0） | fmt.Printf("%G ", 10.000+2.0600i)---->(10+2.06i)  

```golang
//浮点数和复数
fmt.Printf("%b\n", 10.1)
fmt.Printf("%e\n", 10.1)
fmt.Printf("%E\n", 10.1)
fmt.Printf("2%5.2f2\n", 10.1)
fmt.Printf("%g\n", 10.10000)
fmt.Printf("%G\n", 10.000+2.0600i)
```


**运行结果**


```shell script
5685794529555251p-49
1.010000e+01
1.010000E+01
210.102
10.1
(10+2.06i)
```

#### 字符串与字节切片占位符

占位符 | 说明 | 举例  
---|---|---  
%s | 输出字符串表示（string类型或[]byte类型） | fmt.Printf("[]byte{"hello", "world"}: %s ",
[]byte("hello")) ---->[]byte{"hello", "world"}: hello  
%q | 双引号围绕的字符串，由go语言安全地转义 | fmt.Printf(""hello": %q ", "hello") ---->"hello"  
%x | 十六进制，小写字母，每字节两个字符 | fmt.Printf(""hello": %x ", "hello") ---->"hello":68656c6c6f  
%X | 十六进制，大写字母，每字节两个字符 | fmt.Printf(""hello": %X ", "hello") ---->"hello":68656C6C6F  

```golang
//字符串
fmt.Printf("[]byte{\"hello\", \"world\"}: %s\n", []byte("hello"))
fmt.Printf("\"hello\": %q\n", "hello")
fmt.Printf("\"hello\": %x\n", "hello")
fmt.Printf("\"hello\": %X\n", "hello")
```

**运行结果**


```shell script
[]byte{"hello", "world"}: hello
"hello": "hello"
"hello": 68656c6c6f
"hello": 68656C6C6F
```

#### 指针占位符

占位符 | 说明 | 举例  
---|---|---  
%p | 十六进制表示，输出指针所指向的地址 | h := 100 p_h := &h fmt.Printf("%p ", &h)fmt.Printf("%p ", p_h) ---->两个输出是一样的：0xc0000ba018，都是输出的h的地址  

```golang
h := 100
p_h := &h
fmt.Printf("h: %p\n", &h)
fmt.Printf("p_h: %p\n", p_h)
```

**运行结果**


```shell script
h: 0xc0000140f8
p_h: 0xc0000140f8
```

### golang运算符

go语言内置的运算符有：

  * 算术运算符
  * 关系运算符
  * 逻辑运算符
  * 位运算符
  * 赋值运算符

#### 算术运算符

运算符 | 描述  
---|---  
+ | 相加  
- | 相减  
* | 相乘  
/ | 相除  
% | 取模（求余）  
  
> 注意：++（自增）和-（自减）在go语言中是单独的语句，并不是运算符。


```golang
a := 100
b := 200
//算术运算符
res := a + b
fmt.Printf("res: %v\n", res)

res = a - b
fmt.Printf("res: %v\n", res)

res = a * b
fmt.Printf("res: %v\n", res)

res = a / b
fmt.Printf("res: %v\n", res)

res = a % b
fmt.Printf("res: %v\n", res)
a++
```
**运行结果**

```shell script
res: 300
res: -100
res: 20000
res: 0
res: 100
```

#### 关系运算符

运算符 | 描述  
---|---  
== | 检查两个值是否相等，返回true或false  
!= | 检查两个值是否不相等，返回true或false  
> | 检查左边的值是否大于右边的值，返回true或false  
>= | 检查左边的值是否大于等于右边的值，返回true或false  
< | 检查左边的值是否小于右边的值，返回true或false  
<= | 检查左边的值是否小于等于右边的值，返回true或false  

```golang
// 关系运算符
var res2 bool

res2 = a == b
fmt.Printf("res2: %v\n", res2)

res2 = a > b
fmt.Printf("res2: %v\n", res2)

res2 = a >= b
fmt.Printf("res2: %v\n", res2)

res2 = a < b
fmt.Printf("res2: %v\n", res2)

res2 = a <= b
fmt.Printf("res2: %v\n", res2)

res2 = a != b
fmt.Printf("res2: %v\n", res2)
```

**运行结果**

```shell script
res2: false
res2: false
res2: false
res2: true
res2: true
res2: true
```

#### 逻辑运算符

运算符 | 描述  
---|---  
&& | 逻辑and运算符。只有两边的操作数都为true才返回true，否则返回false。  
|| | 逻辑or运算符。只要有一个操作数为true就返回true，否则返回false。  
! | 逻辑not运算符。取相反的结果。  

```golang
//逻辑运算
var res3 bool
res3 = true && true
fmt.Printf("res3: %v\n", res3)
res3 = true || false
fmt.Printf("res3: %v\n", res3)
res3 = !res3
fmt.Printf("res3: %v\n", res3)
```

```shell script
res3: true
res3: true
res3: false
```

#### 位运算符

位运算是对整数在内存中的二进制位进行操作。

运算符 | 描述  
---|---  
& | 参与运算的两个数各对应的二进位相与。（两位均为1才为1）  
| | 参与运算的两个数各对应的二进位相或。（两位只要有一个为1就为1）  
^ | 参与运算的两个数各对应的二进位异或。（当相对应的二进位相异时，结果才为1，否则为0）  
<< | 左移n位就是乘以2的n次方。a<  
<< | 右移n位就是除以2的n次方。a>>b是把a的各二进位全部右移b位。  

```golang
//位运算
aa := 10
bb := 11
fmt.Printf("aa: %b\n", aa)
fmt.Printf("bb: %b\n", bb)

res4 := aa & bb
fmt.Printf("res4:%b  %v\n", res4, res4)
res4 = aa | bb
fmt.Printf("res4:%b  %v\n", res4, res4)
res4 = aa ^ bb
fmt.Printf("res4:%b  %v\n", res4, res4)

res4 = aa << 2
fmt.Printf("res4:%b  %v\n", res4, res4)
res4 = aa >> 1
fmt.Printf("res4:%b  %v\n", res4, res4)
```

**运行结果**

```shell script
aa: 1010
bb: 1011
res4:1010  10
res4:1011  11
res4:1  1
res4:101000  40
res4:101  5
```


#### 赋值运算符

运算符 | 描述  
---|---  
= | 简单的赋值运算符，将等号右边的结果赋值给左边的变量。  
+= | 相加后再赋值  
-= | 相减后再赋值  
*= | 相乘后再赋值  
/= | 相除后再赋值  
%= | 取模后再赋值  
<<= | 左移后再赋值  
\>>= | 右移后再赋值
&= | 按位与后赋值  
|= | 按位或后赋值  
^= | 异或后赋值  



<ActionBox />
