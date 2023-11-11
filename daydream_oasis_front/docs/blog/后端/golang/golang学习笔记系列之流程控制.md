---

next: false

---



<BlogInfo id="405" title="golang学习笔记系列之流程控制" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="249" category="golang" tag_list="['golang', '              流程控制']" create_time="2022.09.12 16:39:58.773835" update_time="2022.09.13 19:56:20" />


![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

## 流程控制

### go语言中的条件

**条件语句** 是用来判断给定的条件是否满足，并根据判断的结果决定执行的语句，go语言中的条件语句也是这样的。

### go语言中的条件语句

  1. if语句：if语句由一个布尔表达式后紧跟一个或多个语句组成。
  2. if…else语句：if语句后可以使用可选的else语句，else语句中的表达式在布尔表达式为false时执行。
  3. if嵌套语句
  4. switch语句：switch语句用于基于不同条件执行不同的动作。
  5. select语句：select语句类似于switch语句，但是select会随机执行一个可运行的case，如果没有case可运行，它将阻塞，直到有case可运行。

#### if语句

**语法**


```golang
if 布尔表达式{
    /*布尔表达式为true时要执行的语句*/
}
```


> 注意：在go语言中，布尔表达式不需要使用括号。


```golang
//示例
a := 100
	if a > 10 {
		fmt.Println("hello")
	}
```


**运行结果**


```shell script
hello
```

> **初始变量可以声明在布尔表达式里面，但是这个变量的作用于只能用在当前条件语句中！**
>

```golang
//示例
if b := 100; b > 10 {
    fmt.Println("if条件成立！")
    fmt.Printf("b: %v\n", b)
} else {
    fmt.Println("if条件不成立！")
    fmt.Printf("b: %v\n", b)
}
```

>
> **运行结果**
>

```shell script
if条件成立！
b: 100
```

```golang
if b := 100; b > 10 {
		fmt.Println("if条件成立！")
		fmt.Printf("b: %v\n", b)
	} else {
		fmt.Println("if条件不成立！")
		fmt.Printf("b: %v\n", b)
	}
	fmt.Printf("b: %v\n", b)
```

>
> **运行结果**
>

```shell script
19:24: undefined: b
```


go语言if语句使用提示：

  1. 不能使用布尔类型以外的其他值作为判断条件
  2. 不能使用括号将条件语句括起来
  3. 大括号必须存在，即使只有一行语句
  4. 左括号必须于if，else同一行
  5. 在if之后，条件语句之前，可以添加变量初始化语句，使用分号;分割

#### if else语句

**语法**

```golang
if 布尔表达式{
    /*布尔表达式为true时要执行的语句*/
}else{
    /*布尔表达式为false时要执行的语句*/
}
```

```golang
//示例
if age := 18; age > 18 {
		fmt.Println("你已经成年了！")
	} else {
		fmt.Println("你还未成年！")
	}
```

**运行结果**

```shell script
你还未成年！
```


#### if else if语句

**语法**


```golang
if 布尔表达式1{
    /*布尔表达式1为true时要执行的语句*/
}else if 布尔表达式2{
    /*布尔表达式2为true时要执行的语句*/
}else{
    /*以上所有布尔表达式都不成立时要执行的语句*/
}
```

```golang
//示例
var aa int
fmt.Println("请输入一个数：")
fmt.Scan(&aa)
if aa == 100 {
    fmt.Printf("aa: %v\n", aa)
} else if aa < 100 {
    fmt.Println("太小了！")
} else {
    fmt.Println("太大了！")
}
```

```shell script
请输入一个数：
10
太小了！
```


#### switch语句

##### 单值匹配

**语法**

```golang
//单值匹配
switch 条件表达式{
    case var1:
    	...
    case var2:
    	...
    case var3:
    	...
    default:
    	...
}
```

```golang
//示例
aaa := 1
switch aaa {
case 1:
    fmt.Println("唱歌！")
case 2:
    fmt.Println("跳舞！")
case 3:
    fmt.Println("唱歌+跳舞！")
default:
    fmt.Println("才艺表演。")
}
```


**运行结果**


```shell script
唱歌！
```


##### 多值匹配

**语法**


```golang
//多值匹配
switch 条件表达式{
    case var1,var2,var3...:
    	...
    case var4,var5...:
    	...
    default:
    	...
}
```

```golang
//示例
var day int
fmt.Println("请输入一个数字：")
fmt.Scan(&day)
switch day {
case 1, 2, 3, 4, 5:
    fmt.Println("工作日！")
case 6, 7:
    fmt.Println("假期！")
default:
    fmt.Println("输入有误！")
}
```


**运行结果**


```shell script
请输入一个数字：
6
假期！
```

##### case后接条件表达式

**语法**

```golang
//case后接条件表达式
switch{
    case 条件表达式1:
    	...
    case 条件表达式2:
    	...
    case 条件表达式3:
    	...
    default:
    	...
}
```


```golang
//示例
var n int
fmt.Println("请输入一个数字：")
fmt.Scan(&n)
switch {
case n == 10:
    fmt.Println("猜对了！")
case n < 10:
    fmt.Println("太小了！")
case n > 10:
    fmt.Println("太大了！")
default:
    fmt.Println("不可能执行到这条语句，除非上面的case都不成立。")
}
```


**运行结果**


```shell script
请输入一个数字：
23
太大了！
```


##### fallthrough

**语法**


```golang
//fallthrough 可以执行满足条件的下一个case
switch 条件表达式{
    case var1:
    	...
    	fallthrough
    case var2:
    	...
    	fallthrough
    case var3:
    	...
    default:
    	...
}
```

```golang
bb := 100
switch bb {
case 100:
    fmt.Printf("bb: %v\n", bb)
    fallthrough
case 200:
    fmt.Println("200")
    fallthrough
case 300:
    fmt.Println("300")
default:
    fmt.Println("case都不成立就执行这里。")
}
```


**运行结果**


```shell script
bb: 100
200
300
```


go语言switch使用注意事项：

  1. 支持多条件匹配
  2. 不同的case之间不使用break分隔，默认只会执行一个case
  3. 如果想执行多个case，需要使用fallthrough关键字，也可以用break终止
  4. case后还可以使用条件表达式

### go语言中的循环语句

go语言中的循环只有for循环，去除了while，do while循环，使用起来更加简洁。

  1. for循环。
  2. for range循环。（类似于golang中的for in）

#### for语句

**语法**


```golang
for 初始语句;条件表达式；结束语句{
    循环语句
}
```


```golang
//for循环
	for i := 0; i < 10; i++ {
		fmt.Printf("i: %v\t", i)
	}
	fmt.Println("\n")
	//初始条件写在外面
	j := 0
	for ; j < 10; j++ {
		fmt.Printf("j: %v\t", j)
	}

	fmt.Println("\n")
	//结束语句写在循环体内
	for i := 0; i < 10; {
		fmt.Printf("i: %v\t", i)
		i++

	}
	fmt.Println("\n")

	//永真循环
	k := 0
	for {
		fmt.Printf("k: %v ", k)
		k++
		if k == 10 {
			break
		}
	}
```


**运行结果**

```shell script
i: 0    i: 1    i: 2    i: 3    i: 4    i: 5    i: 6    i: 7    i: 8    i: 9

j: 0    j: 1    j: 2    j: 3    j: 4    j: 5    j: 6    j: 7    j: 8    j: 9

i: 0    i: 1    i: 2    i: 3    i: 4    i: 5    i: 6    i: 7    i: 8    i: 9

k: 0 k: 1 k: 2 k: 3 k: 4 k: 5 k: 6 k: 7 k: 8 k: 9 
```


#### for range语句

go语言中可以使用for range遍历数组，切片，字符串，map及通道（channel）。通过for range遍历的返回值有一下规律：

  1. 数组，切片，字符串返回索引和值
  2. map返回键和值
  3. 通道只返回通道内的值


```golang
//for range
//遍历数组
var arr = [...]int{1, 2, 3, 4, 5, 6, 7}
for i, v := range arr {
    fmt.Printf("%v:%v\n", i, v)

}

//遍历map
var m = make(map[string]string, 0)
m["name"] = "Tom"
m["age"] = "18"
m["num"] = "1234"
for k, v := range m {
    fmt.Printf("%v:%v\n", k, v)

}
```


**运行结果**


```shell script
name:Tom
age:18
num:1234
```


### break关键字

break关键字可以结束for，switch和select的代码块。


```golang
//跳出for循环
k := 0
for {
    fmt.Printf("k: %v ", k)
    k++
    if k == 10 {
        break
    }
}
```


**运行结果**

```shell script
k: 0 k: 1 k: 2 k: 3 k: 4 k: 5 k: 6 k: 7 k: 8 k: 9 
```

```golang
//配合标签使用
label:
	for i := 0; i < 10; i++ {
		fmt.Printf("i: %v\n", i)
		if i == 5 {
			break label
		}

	}
	fmt.Println("END...")
```


**运行结果**


```shell script
i: 0
i: 1
i: 2
i: 3
i: 4
i: 5
END...
```


go语言中break的注意事项：

  1. 单独在select中使用break和不使用break没有啥区别。
  2. 单独在switch中使用break，并且没有使用fallthrough，和不使用break没有啥区别。
  3. 在switch中，配合fallthrough关键字，能够终止fallthrough后面case语句的执行。
  4. 带标签的break，可以跳出多层select/select作用域。让break更加灵活，写法更加简单，不需要使用控制变量一层一层跳出循环，没有带break的只能跳出当前语句。

### continue关键字

continue只能用在循环中，在go中只能用在for循环中，它可以终止本次循环，进入下一轮循环。

continue也可以配合标签使用。


```golang
//打印10以内的偶数
for i := 0; i < 11; i++ {
    if i%2 != 0 {
        continue
    }
    fmt.Printf("i: %v\n", i)
}
```


**运行结果**


```shell script
i: 0
i: 2
i: 4
i: 6
i: 8
i: 10
```


**配合标签使用**


```golang
label:

	for i := 0; i < 3; i++ {

		for j := 0; j < 3; j++ {
			if i == 1 && j == 1 {
				continue label //跳到label所在的地方
			}
			fmt.Printf("i: %v  j: %v\n", i, j)
		}

	}
	fmt.Println("i=1,j=1时跳出了循环。")
```


**运行结果**

```shell script
i: 0  j: 0
i: 0  j: 1
i: 0  j: 2
i: 1  j: 0
i: 2  j: 0
i: 2  j: 1
i: 2  j: 2
i=1,j=1时跳出了循环。
```


### goto关键字

goto语句通过标签进行代码间的无条件跳转。goto语句可以在快速跳出循环，避免重复退出上有一定帮助。

#### 跳到指定标签


```golang
for i := 0; i < 10; i++ {
		fmt.Printf("i: %v\n", i)
		if i == 5 {
			goto label
		}

	}

label:
	fmt.Println("循环结束！")
```


**运行结果**


```golang
i: 0
i: 1
i: 2
i: 3
i: 4
i: 5
循环结束！
```


#### 跳出多重循环

```golang
//与break不一样的是，break只能跳出一层循环，而goto可以直接跳出所有循环
for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			for k := 0; k < 3; k++ {
				fmt.Printf("i=%v j=%v k=%v\n", i, j, k)
				if i == 1 && j == 1 && k == 1 {
					goto mylabel
				}

			}

		}

	}
mylabel:
	fmt.Println("循环结束！")
```


**运行结果**


```golang
i=0 j=0 k=0
i=0 j=0 k=1
i=0 j=0 k=2
i=0 j=1 k=0
i=0 j=1 k=1
i=0 j=1 k=2
i=0 j=2 k=0
i=0 j=2 k=1
i=0 j=2 k=2
i=1 j=0 k=0
i=1 j=0 k=1
i=1 j=0 k=2
i=1 j=1 k=0
i=1 j=1 k=1
循环结束！
```






<ActionBox />
