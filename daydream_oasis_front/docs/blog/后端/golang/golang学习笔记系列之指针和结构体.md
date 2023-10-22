
<BlogInfo id="1226" title="golang学习笔记系列之指针和结构体" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=293 category="golang" tag_list="[]" create_time="2022.09.24 22:09:33.034463" update_time="2022.09.24 22:09:33" />

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

## defer语句

go语言中的defer语句会将其后面紧跟随的语句延迟处理。在defer归属的函数即将返回时，将延迟处理的语句按照defer定义的顺序逆序执行，也就是说，先defer的语句后执行，后defer的语句先执行。

**defer特性**

  * 关键字defer用于注册延迟调用。
  * 这些调用直到return前才执行。因此可以用来做资源清理。
  * 多个defer语句，按先进后出的执行顺序。
  * defer语句中的变量，在defer声明时就决定了。

```golang
package main

func main() {
	print("start\n")
	defer print("step 1\n")
	defer print("step 2\n")
	defer print("step 3\n")
	print("end\n")
}
```

**运行结果**

```shell script
start
end
step 3
step 2
step 1
```

> 如运行结果所示，defer后的语句都被 **延迟** 执行了，并且有多个defer语句存在时，后defer的语句先执行。

## init函数

golang有一个特殊的init函数，先于main函数执行，可以用于实现包级别的一些初始化工作。

**init函数的主要特点**

  * init函数先于main函数执行，不能被主动调用，它是 **自动执行** 的
  * init函数即没有参数，也没有返回值
  * 每个包可以有多个init函数
  * 包的每个源文件也可以有多个init函数，这点比较特殊，就是可以在同一个文件下定义多个init函数
  * 同一个包的init执行顺序没有明确的定义，但是同一个文件下的init函数是按顺序执行的
  * 不同包的init函数按照包导入的依赖关系决定执行顺序。

**golang初始化顺序**

顺序：变量初始化>init函数>main函数

```golang
package main

func init_var() int {
	print("初始化变量...\n")
	return 10
}

func init() {
	print("init函数1...\n")
}

func init() {
	print("init函数2...\n")
}

var i int = init_var()

func main() {
	print("main函数被执行了...\n")

}
```

**运行结果**


```shell script
初始化变量...
init函数1...
init函数2...
main函数被执行了...
```


## 指针

go语言中的函数传参都是值拷贝，当我们想修改某个变量的时候，我们可以创建一个指向该变量地址的指针变量。传递数据使用指针，而无需拷贝数据。

类型指针不能进行偏移和运算。

go语言中的指针操作非常简单，只需要记住两个符号：&（取地址）和*（根据地址取值）。

### 指针地址和指针类型

每个变量在运行时都拥有一个地址，这个地址代表变量在内存中的位置。go语言中使用&字符放在变量前面对变量进行取地址操作。go语言中的值类型（int，float，bool，string，array，struct）都有对应的指针类，如：*int，**string等。

### 指针语法

一个指针变量指向了一个值的内存地址。（也就是我们声明了一个指针之后，可以像变量赋值一样，把一个值的内存地址放入到指针当中。）

**语法**

```golang
 var var_name *var_type `
```

```golang
package main

import "fmt"

func main() {

	var p *int
	var pp **int
	var ppp ***int
	a := 10
	p = &a    //将指针p指向a的地址 即*p=a=10
	pp = &p   //将指针pp指向p的地址 即*pp=p-> *(*pp)=*p=a=10
	ppp = &pp //将指针ppp指向pp的地址 即*ppp=pp-> *(*ppp)=*pp -> *(*(*ppp))=*(*pp)=*p=a=10

	fmt.Printf("p: %v\n", p)
	fmt.Printf("p: %v\n", &p)
	fmt.Printf("pp: %v\n", pp)
	fmt.Printf("ppp: %v\n", ***ppp)
	fmt.Println(*p == a)
	fmt.Println(*(*pp) == a)
	fmt.Println(*(*(*ppp)) == a)

}
```


**运行结果**


```shell script
p: 0xc0000ba000
p: 0xc0000b4018
pp: 0xc0000b4018
ppp: 10
true
true
true
```


### 指向数组的指针

```golang
package main

import "fmt"

func main() {

	var arr = [5]int{1, 2, 3, 4, 5}
	var arr_p [5]*int //数组类型的指针
	fmt.Printf("arr: %v\n", arr)
	for i := 0; i < len(arr); i++ {
		arr_p[i] = &arr[i]
	}

	for i := 0; i < len(arr_p); i++ {
		fmt.Printf("arr_p[i]=%v *arr_p[i]=%v arr[i]=%v\n", arr_p[i], *arr_p[i], arr[i])

	}

}
```


**运行结果**


```shell script
arr: [1 2 3 4 5]
arr_p[i]=0xc0000b2030 *arr_p[i]=1 arr[i]=1
arr_p[i]=0xc0000b2038 *arr_p[i]=2 arr[i]=2
arr_p[i]=0xc0000b2040 *arr_p[i]=3 arr[i]=3
arr_p[i]=0xc0000b2048 *arr_p[i]=4 arr[i]=4
arr_p[i]=0xc0000b2050 *arr_p[i]=5 arr[i]=5
```


## 结构体

### golang类型定义和类型别名

**类型定义语法**


```golang
 type my_type old_type `
```

  * my_type：自己新定义的类型
  * old_type：已经存在的类型

**类型别名语法**


```golang
 type my_type = old_type //用已存在的类型赋值给新类型 `
```

**两者的区别**

  * 类型定义相当于定义了一个全新的类型，与之前的类型不同；但是类型别名并没有定义新的类型，而是使用一个别名来代替之前的类型
  * 类型别名只会在代码中存在，在编译完成之后并不会存在该别名
  * 因为类型别名和原来的类型是一致的，所以原类型所拥有的方法，类型别名定义的变量也拥有；但是如果是重定义的一个类型，那么不可以调用之前的任何方法

```golang
package main

import "fmt"

func main() {

	//类型定义
	type my_string string

	var name my_string = "Tom"
	fmt.Printf("name: %T %v\n", name, name) //类型为自己定义的新类型

	//类型别名
	type my_string2 = string
	var name2 my_string2 = "Tom"
	fmt.Printf("name2: %T %v\n", name2, name2) //类型仍旧是string

}
```

**运行结果**

```shell script
name: main.my_string Tom
name2: string Tom
```

### golang结构体

go语言没有面向对象的概念，但是可以使用结构体来实现面向对象编程的一些特性，你如：继承，组合等特性。

**结构体的定义**

```golang
type struct_name struct{
    member1 type1
    member2 type2
    member3 type3
    ...
    
}
```


  * type：结构体定义关键字
  * struct_name：结构体名
  * struct：结构体定义关键字
  * member type：成员定义

```golang
package main

import "fmt"

func main() {

	//一个结构体就相当于一个新的类型
	type Student struct {
		name  string
		num   int
		age   int
		email string
	}

	tom := Student{"Tom", 1, 18, "110@qq.com"}
	fmt.Printf("tom: %v\n", tom)
	fmt.Printf("tom.name: %v\n", tom.name)
	fmt.Printf("tom.age: %v\n", tom.age)

}
```


**运行结果**

```shell script
tom: {Tom 1 18 110@qq.com}
tom.name: Tom
tom.age: 18
```


**匿名结构体**

对于临时需要使用结构体时，可以定义匿名结构体。

```golang
// 匿名结构体
	var dog struct {
		name string
		age  int
	}

	dog.name = "Jerry"
	dog.age = 3
	fmt.Printf("dog: %v\n", dog)
	fmt.Printf("dog.name: %v\n", dog.name)
```

**运行结果**

```shell script
dog: {Jerry 3}
dog.name: Jerry
```

### 结构体的初始化

对于通过结构体定义的一个变量来说，未初始化的变量的每个成员属性都是零值；go语言中提供了两种结构体初始化的方法，分别是"k-v"式和"列表"式。

```golang
package main

import "fmt"

func main() {
	type Student struct {
		name  string
		age   int
		email string
	}

	tom := Student{}
	fmt.Printf("tom: %v\n", tom) //未初始化的结构体每个成员属性都是零值

	//“k-v”式初始化 可以对部分值进行初始化，也可以对全部值初始化
	jerry := Student{name: "Jerry", age: 18}
	fmt.Printf("jerry: %v\n", jerry)

	//“列表”式初始化 必须将所有值初始化
	autumn := Student{"Autumn", 18, "110@qq.com"}
	fmt.Printf("autumn: %v\n", autumn)
}
```


**运行结果**


```shell script
tom: { 0 }
jerry: {Jerry 18 }
autumn: {Autumn 18 110@qq.com}
```


### **结构体指针**

```golang
package main

import "fmt"

func main() {

	type Student struct {
		name string
		age  int
	}

	tom := Student{name: "Tom", age: 18}

	//定义一个结构体指针
	var s_p *Student
	s_p = &tom
	fmt.Printf("s_p: %v\n", s_p)
	fmt.Printf("(*s_p): %v\n", (*s_p))
	fmt.Printf("(*s_p).name: %v\n", (*s_p).name)
	fmt.Printf("s_p.name: %v\n", s_p.name) //在取成员变量的值的时候可以将*省略

	//使用new关键字创建结构体指针
	var jerry = new(Student)
	jerry.name = "Jerry"
	fmt.Printf("jerry: %v\n", jerry)
	fmt.Printf("(*jerry): %v\n", (*jerry)) //取值
	fmt.Printf("jerry.name: %v\n", jerry.name)

}
```

**运行结果**

```shell script
s_p: &{Tom 18}
(*s_p): {Tom 18}
(*s_p).name: Tom
s_p.name: Tom
jerry: &{Jerry 0}
(*jerry): {Jerry 0}
jerry.name: Jerry
```


### 结构体作为函数参数

go语言的结构体可以像普通变量一样，作为函数参数，参数的传递方式分为两种：

  1. 直接传结构体，在函数体内对结构体的操作不会影响原结构体（因为操作的只是原结构体的副本）
  2. 传递结构体的地址，在函数体内对结构的任何操作都会对原结构体生效


```golang
package main

import "fmt"

type Student struct {
	name string
	age  int
}

//值传递
func show_student(s Student, name string, age int) {
	s.name = name
	s.age = age
	fmt.Printf("s: %v\n", s)

}

//地址传递（引用传递）
func show_student2(s *Student, name string, age int) {
	s.name = name
	s.age = age
	fmt.Printf("s: %v\n", s)
}

func main() {

	tom := Student{name: "Tom", age: 18}
	jerry := Student{name: "Jerry", age: 18}

	//tom直接传值
	fmt.Printf("tom: %v\n", tom)
	show_student(tom, "Tom2", 20)
	fmt.Printf("tom: %v\n", tom)
	fmt.Println("-------------------")
	//jerry传递地址
	fmt.Printf("jerry: %v\n", jerry)
	show_student2(&jerry, "Jerry2", 20)
	fmt.Printf("jerry: %v\n", jerry)

}
```


**运行结果**

```shell script
tom: {Tom 18}
s: {Tom2 20}
tom: {Tom 18}
-------------------
jerry: {Jerry 18}
s: &{Jerry2 20}
jerry: {Jerry2 20}
```


### 结构体的嵌套

go语言的结构体中可以嵌套另一个结构体。

```golang
package main

import "fmt"

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
	tom.name = "Tom"
	tom.age = 18

	var erha = Dog{name: "二哈", age: 3}
	tom.dog = erha

	fmt.Printf("tom: %v\n", tom)
	fmt.Printf("tom.name: %v\n", tom.name)
	fmt.Printf("tom.dog.name: %v\n", tom.dog.name)
	tom.dog.name = "二哈哈哈"
	fmt.Printf("tom.dog: %v\n", tom.dog)
}
```


**运行结果**


```shell script
tom: {Tom 18 {二哈 3}}
tom.name: Tom
tom.dog.name: 二哈
tom.dog: {二哈哈哈 3}                                                     
```



