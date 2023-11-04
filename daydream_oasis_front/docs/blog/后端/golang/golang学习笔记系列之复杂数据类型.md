
<BlogInfo id="396" title="golang学习笔记系列之复杂数据类型" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="211" category="golang" tag_list="['数据类型']" create_time="2022.09.18 22:40:24.602004" update_time="2022.09.18 22:40:24" />

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

## 复杂数据类型

### 数组

数组是 **相同数据类型** 的一组数据的集合，数组一旦定义长度不能修改，数组 可以通过索引来访问元素。

#### **数组的定义**


```golang
var array_name [SIZE]TYPE
```
  * array_name：数组名
  * SIZE：数组的大小
  * TYPE：数组中数据的类型

```golang
type Student struct {
	Name string
	num  int
}
// 数组的定义
var arr_int [10]int
fmt.Printf("arr_int: %v\n", arr_int)
var arr_str [10]Student
fmt.Printf("arr_str: %v\n", arr_str)
```

**运行结果**


```shell script
arr_int: [0 0 0 0 0 0 0 0 0 0]
arr_str: [{ 0} { 0} { 0} { 0} { 0} { 0} { 0} { 0} { 0} { 0}]
```

#### 数组的初始化

初始化就是给数组的元素赋初值，没有初始化的数组，默认元素都是 **零值** （数值型的默认值是0，布尔型的默认值所示false，字符串型的默认值是空字符）。

```golang
//给数组赋初始值
var arr_int_init = [10]int{1, 2, 3}
fmt.Printf("arr_int_init: %v\n", arr_int_init)

//给指定位置赋初始值
var arr_float_init = [10]float64{0: 100.0, 3: 200.0}
fmt.Printf("arr_float_init: %v\n", arr_float_init)

//使用...不指定数组的大小,根据初始值来判断数组的大小
var arr_string_init = [...]string{"hello", "world"}
fmt.Printf("arr_string_init: %v\n", arr_string_init)
```

**运行结果**

```shell script
arr_int_init: [1 2 3 0 0 0 0 0 0 0]
arr_float_init: [100 0 0 200 0 0 0 0 0 0]
arr_string_init: [hello world]
```


#### 数组的访问

可以通过索引的方式来访问数组。数组的最大下标为数组的长度减一，最小为0，大于这个值会发生数组越界。


```golang
package main

import "fmt"

func main() {

	var arr_int = [10]int{1, 2, 3, 4, 5, 6}

	//访问第一个元素
	fmt.Printf("arr_int[0]: %v\n", arr_int[0])

	//访问第3个元素
	fmt.Printf("arr_int[2]: %v\n", arr_int[2])

	//访问最后一个元素
	fmt.Printf("arr_int[len(arr_int)-1]: %v\n", arr_int[len(arr_int)-1])

	//for遍历数组
	for i := 0; i < len(arr_int); i++ {

		fmt.Printf("a[%v]=%v \n", i, arr_int[i])

	}
	print("#########################################\n")
	//for range遍历数组
	for i, v := range arr_int {
		fmt.Printf("a[%v]=%v \n", i, v)

	}
```

**运行结果**

```shell script
arr_int[0]: 1
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
```


### 切片

和数组类似，切片也是一组相同数据类型的数据的集合，但与数组不一样的是，切片的长度是可变的。对于数组来说，当我们对要保存的元素的个数不确定时，如果申请太小的数组，可能就不够用；如果申请太大的数组，可能就造成了不必要的浪费。鉴于这个原因，就有了切片，我们可以把切片理解为可变长度的数组，其实它底层就是使用数组实现的，只不过增加了一个自动扩容功能。

#### 切片的定义

语法 **1**

```golang
 var slice_name []TYPE `
```
  * slice_name：切片名
  * TYPE：切片类型

语法 **2**

```golang
//使用make函数定义切片时，会同时将切片初始化
slice_name := make([]TYPE,SIZE)
```
  * slice_name：切片名
  * TYPE：切片中元素的类型
  * SIZE：初始化切片的大小

```golang
package main

import "fmt"

func main() {

	//切片的定义
	var s1 []int
	s1 = append(s1, 1)
	fmt.Printf("s1: %v\n", s1)

	//make定义切片的同时会将其初始化
	s2 := make([]string, 10)
	fmt.Printf("s2: %v\n", s2)

	//访问切片中的元素
	fmt.Printf("s1[0]: %v\n", s1[0])

	//在切片的末尾添加元素
	s1 = append(s1, 2)
	fmt.Printf("s1: %v\n", s1)
	//修改切片中的元素
	s1[0] = 100
	fmt.Printf("s1: %v\n", s1)

	//获取切片的大小
	fmt.Printf("len(s1): %v\n", len(s1))

	fmt.Printf("cap(s1): %v\n", cap(s1))

}
```

**运行结果**

```shell script
s1: [1]
s2: [         ]
s1[0]: 1
s1: [1 2]
s1: [100 2]
len(s1): 2
cap(s1): 2
```

#### 切片的初始化

```golang
package main

import "fmt"

func main() {

	//切片的初始化
	//方法一
	var s1 = []int{1, 2, 3}
	fmt.Printf("s1: %v\n", s1)

	//方法二：make
	s2 := make([]int, 10)
	fmt.Printf("s2: %v\n", s2)

	//方法三：借助数组
	arr := [3]int{1, 2, 3}
	s3 := arr[:]
	fmt.Printf("s3: %v\n", s3)

	//切片/数组/字符串的切片操作： s[a:b] 左闭右开 于python不一样的是，go语言中不能修改步长，步长只能是1
	s4 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Printf("s4[1:9]: %v\n", s4[1:3])
    
    //访问操作和遍历操作同数组
}
```

**运行结果**
```shell script
s1: [1 2 3]
s2: [0 0 0 0 0 0 0 0 0 0]
s3: [1 2 3]
s4[1:9]: [2 3]
```

#### 切片的crud操作

```golang
package main

import (
	"fmt"
)

func main() {

	s := []int{1, 2, 3, 4, 5}

	//add
	s = append(s, 1)
	fmt.Printf("s: %v\n", s)

	//delete：删除索引为index的元素
	index := 2
	s = append(s[:index], s[index+1:]...)
	fmt.Printf("s: %v\n", s)

	//update
	s[4] = 6
	fmt.Printf("s: %v\n", s)

	//query
	target := 5
	for i, v := range s {
		if v == target {
			println("找到了！", i)
			break
		}

	}

}
```

**运行结果**
```shell script
s: [1 2 3 4 5 1]
s: [1 2 4 5 1]
s: [1 2 4 5 6]
找到了！ 3
```

### map

map是一种key:value键值对的数据结构。map内部实现是hash表。map最重要的一点是通过key能够快速的检索出数据。

#### map的定义

```golang
 var m[K_TYPE]V_TYPE `
```
  * m：map名
  * K_TYPE：key的类型
  * V_TYPE：value的类型

```golang
package main

import (
	"fmt"
)

func main() {

	//map的定义
	//方法一
	var m1 map[string]string
	fmt.Printf("m1: %v\n", m1)

	//方法二
	m2 := make(map[string]string)
	fmt.Printf("m2: %v\n", m2)

	//map的初始化
	var m3 = map[string]string{
		"name": "Tom",
		"age":  "18",
	}
	fmt.Printf("m3: %v\n", m3)

	//增加/修改map
	m3["num"] = "1234"
	m3["age"] = "20"
	fmt.Printf("m3: %v\n", m3)

	//根据k获取v
	fmt.Printf("m3[\"name\"]: %v\n", m3["name"])

	//判断某个k是否存在  v,ok=m[k]--->如果k存在，ok为true，否则为false
	v, ok := m3["name"]
	if ok {
		print(v)
	}

	//删除某个k
	delete(m3, "age")
	fmt.Printf("m3: %v\n", m3)
}
```

**运行结果**

```shell script
m1: map[]
m2: map[]
m3: map[age:18 name:TOm]
m3: map[age:20 name:TOm num:1234]
m3["name"]: TOm
TOmm3: map[name:TOm num:1234]
```

#### map的遍历

通过for range对map进行遍历。
```golang
package main

import "fmt"

func main() {

	var m = map[string]string{
		"name": "Tom",
		"age":  "18",
		"num":  "1234",
	}

	//for range遍历
	//1.只拿到key
	for k := range m {
		fmt.Printf("k: %v v: %v\n", k, m[k])
	}

	//2.同时拿到k和v
	for k, v := range m {
		fmt.Printf("k: %v v: %v\n", k, v)
	}

}
```

**运行结果**

```shell script
k: name v: Tom
k: age v: 18
k: num v: 1234
k: num v: 1234
k: name v: Tom
k: age v: 18
```



