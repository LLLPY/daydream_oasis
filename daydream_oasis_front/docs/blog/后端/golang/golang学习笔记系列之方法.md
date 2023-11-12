---

next: false

---



<BlogInfo id="400"/>

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

## 方法

go语言没有面向对象的特性，也没有类的概念。但是，可以使用结构体来模拟这些特性；在面向对象里面类有方法的概念，在go语言中，我们也可以为每一个结构体定义属于自己的方法。

### **语法**

go语言中的方法是一种特殊的函数，定义于struct之上（与struct绑定），被称为struct的接受者（receiver）。


```golang
func (recv recv_type) method_name (params_li)(return_type){
    
}
```

  * func：定义函数的关键字
  * recv recv_type：接受者和接受者的类型
  * method_name：方法名
  * params_li：[参数]和参数类型列表
  * return_type：返回值类型

> 方法和函数的定义基本上一模一样，只不过在func和函数名之间添加了一个接受者和接受者的类型。


```golang
package main

import "fmt"

type Dog struct {
	name string
	age  int
}

//为结构体Dog定义方法
func (dog Dog) say_hi() {
	fmt.Printf("我叫%v，我今年%v岁啦！\n", dog.name, dog.age) 
}

func (dog Dog) woof() {
	fmt.Printf("%v正在汪汪大叫~\n", dog.name)
}

func main() {

	wc := Dog{"旺财", 2}
	wc.say_hi()
	wc.woof()

}
```


**运行结果**

```shell script
我叫旺财，我今年2岁啦！
旺财正在汪汪大叫~
```

**方法的注意事项**

  * 方法的receiver type并非一定是struct类型，type定义的类型别名，slice，map，channel，func类型等都可以。
  * struct结合它的方法就等价于面向对象中的类。只不过struct可以和它的方法分开，并非一定要属于同一个文件，但必须属于同一个包。
  * 方法有两种接收类型：（T Type）和(T *Type)。
  * 方法就是函数，go语言中没有重载的说法，也就是同一个结构体中的所有方法都必须是唯一的。
  * 如果receiver是一个指针类型，则会自动解除引用。
  * 方法和type是分开的，意味着实例的行为和数据存储是分开的，但是它们通过receiver建立起关联关系。（个人感觉：只不过是多了一个必须参数receiver）

### 方法的接受者类型

和函数的传值方法一样，方法的接受者类型同样支持值传递和地址传递，通过地址传递的，在方法内部对接受者进行操作会影响到接受者。

```golang
package main

import "fmt"

type Person struct {
	name string
}

//传递值
func (p Person) fix_name(name string) {
	p.name = name

}

//传递指针
func (p *Person) fix_name2(name string) {
	p.name = name

}

func main() {

	tom := Person{name: "Tom"}
	jerry := &Person{name: "Jerry"}
	fmt.Printf("tom.name: %v\n", tom.name)
	tom.fix_name("Tooooom")
	fmt.Printf("tom.name: %v\n", tom.name)
	print("----------------------------\n")
	fmt.Printf("jerry.name: %v\n", jerry.name)
	jerry.fix_name2("Jeeeeery")
	fmt.Printf("jerry.name: %v\n", jerry.name)

}
```


**运行结果**

```shell script
tom.name: Tom
tom.name: Tom
----------------------------
jerry.name: Jerry
jerry.name: Jeeeeery
```

>
> 可以看到通过传递地址的fix_name2在内部修改结构体的属性后，该结构体的属性值会随之变化，而通过值传递的fix_name在内部修改结构体的属性值并不会对原结构体产生任何影响。





<ActionBox />
