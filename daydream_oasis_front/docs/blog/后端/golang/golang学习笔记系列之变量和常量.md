
<BlogInfo id="1234" title="golang学习笔记系列之变量和常量" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=79 category="golang" tag_list="['golang']" create_time="2022.09.10 17:54:03.363674" update_time="2022.09.13 19:57:41" />

###  

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

### 变量

变量是计算机语言中能存储计算结果或能表示值的抽象概念，不同的的变量保存的数据类型可能不一样。

#### 声明变量

go语言中的变量需要声明后才能使用，同一作用域内不支持重复声明。并且go语言的变量声明后 **必须使用** ，否者会报错。

#### 默认语法


```golang
var indertifer type

//例：
var age int    //int类型的变量不赋值，默认值是0
var price float64 //默认值是0
var flag bool  //默认值是false 
```


#### 类型推断

不需要为变量指定类型，根据变量的值来自动推断变量的类型。

```golang
var name = “TOm”
var num = 10```

```
#### 同时声明多个变量

```golang
 var name,age,gender = "Tom",18,true `
```

#### 短变量声明

短变量只能在 **函数内部** 进行声明，使用**:=**运算符对变量进行声明和初始化。

```golang
identifer := ""

//例：注意，一定是在函数内部声明，否则会报错！

func fun(){
    age:=18
	name:=tom
}
```

#### 匿名变量

如果我们接收到多个变量，有一些变量使用不到，可以使用下划线，便是变量名，这种变量叫做匿名变量。


```golang
func Fun() (string, int) {
	return "Tom", 18
}
//匿名变量 匿名变量不使用也不会报错
tom_name, _ := Fun()
fmt.Printf("tom_name: %v
", tom_name)
```


### 常量

常量，就是在程序编译阶段就确定下来的值，二程序在运行时则无法改变该值。在go语言中，常量可以是数值类型，布尔类型，字符串类型等等。

#### 常量声明

定义一个常量使用const关键字，语法格式如下：

```golang
 const constantName [type] = value `
```
  * const：定义常量的关键字
  * constantName：常量名
  * type：常量的类型，可选
  * value：常量的值

```golang
package main

import "fmt"

func main() {

	//常规语法
	const PI float32 = 3.14
	const H = 100

	//定义多个
	const (
		NAME = "Tom"
		AGE  = 18
	)

	//注意：声明多个变量时，如果省略了赋值，则表示和上面的一行值相同
	const (
		a = 1
		b //b=a=1
		c = 100
		d //d=c=100
	)

	fmt.Printf("a: %v
", a)
	fmt.Printf("b: %v
", b)
	fmt.Printf("c: %v
", c)
	fmt.Printf("d: %v
", d)

	//同时定义
	const X, Y, Z = 2, 3, 4
	fmt.Printf("X: %v
", X)
	fmt.Printf("Y: %v
", Y)

}
```

#### iota

iota比较特殊，可以被认为是一个可被编译器修改的常量，它的默认值是0，每调用一次值就加一，遇到const关键字时被重置为0。

```golang
//iota
	const (
		A = iota //0 
		B = iota //1
		C = iota //2

	)
	fmt.Printf("A: %v
", A)
	fmt.Printf("B: %v
", B)
	fmt.Printf("C: %v
", C)

	//iota中间截断
	const (
		aa = iota //0
		_         //1
		cc = iota //2
	)

	fmt.Printf("aa: %v
", aa)
	fmt.Printf("cc: %v
", cc)


	const(
		aaa=iota  //0
		bbb=1000  //1000 [1]
		ccc=iota  //2
	)

	fmt.Printf("aaa: %v
", aaa)
	fmt.Printf("ccc: %v
", ccc)
```



