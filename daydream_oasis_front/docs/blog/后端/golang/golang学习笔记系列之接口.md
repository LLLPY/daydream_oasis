
<BlogInfo id="1222" title="golang学习笔记系列之接口" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=178 category="golang" tag_list="[]" create_time="2022.10.03 16:52:32.372359" update_time="2022.10.03 16:52:32" />

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

## 接口

go语言的接口，是一种新的类型定义，它把所有的具有共性的方法定义在一起，任何其他类型只要实现了这些方法就实现了这个接口。

接口就像一个公司里面的领导，它会定义一些通用规范，只是设计，而不实现规范。

**语法**


```golang
type interface_name interface{
    func_name(parma_li)(return_li)
}
```

  * interface_name：接口名
  * func_name：方法名
  * param_li：参数列表
  * return_li：返回值列表


```golang
package main

import "fmt"

// 定义一个USB的读写接口
type USB interface {
	read()
	write(string)
}

// 计算机
type Computer struct {
	name string
}

//手机
type Mobile struct {
	name string
}

// 计算机实现USB接口
func (c Computer) read() {
	fmt.Printf("%v is reading...\n", c.name)
}

func (c Computer) write() {
	fmt.Printf("%v is writing...\n", c.name)
}

func main() {

	c := Computer{name: "Mac"}
	c.read()
	c.write()

}
```


**运行结果**

```shell script
Mac is reading...
Mac is writing...
```

### 接口和类型的关系

  * 一个类型可以实现多个接口
  * 多个类型可以实现一个接口（多态：不同的类型调用同一个方法，具体实现细节不一样）


```golang
package main

import "fmt"

//一个类型实现多个接口
type Music interface {
	PlayMusic()
}

type Vide interface {
	PlayVideo()
}

type Mobile struct {
	name string
}

func (m Mobile) PlayMusic() {
	fmt.Printf("%v播放音乐...\n", m.name)
}

func (m Mobile) PlayVideo() {
	fmt.Printf("%v播放视频...\n", m.name)

}

// 多个类型实现一个接口
type Eat interface {
	eat()
}

type Dog struct {
	name string
}

type Cat struct {
	name string
}

func main() {

	m := Mobile{name: "Apple"}
	m.PlayMusic()
	m.PlayVideo()

	erha := Dog{name: "二哈"}
	fmt.Printf("%v is eating...\n", erha.name)
	tom := Cat{name: "Tom"}
	fmt.Printf("%v is eating...\n", tom.name)

}
```

**运行结果**

```shell script
Apple播放音乐...
Apple播放视频...
二哈 is eating...
Tom is eating...
```

### 接口嵌套

接口可以通过嵌套，创建新的接口。

```golang
package main

type Fly interface {
	fly()
}

type Swim interface {
	swim()
}

type FlyFish interface {
	Fly
	Swim
}

type Fish struct {
}

func (f Fish) fly() {
	print("flying...\n")
}

func (f Fish) swim() {
	print("swimming...\n")
}

func main() {

	f := Fish{}
	f.fly()

	var ff FlyFish
	ff = Fish{}
	ff.fly()	

}
```

**运行结果**

```shell script
flying...
flying...
```

### 通过接口实现开闭原则（OCP）

面向对象的可复用设计的第一块基石，便是所谓的"开闭"原则（Open-Close
Principle，常缩写为OCP，意为对扩展开放，对修改关闭）。虽然go语言不是面向对象语言，但是也可以模拟实现这个原则。

```golang
package main

//定义一个宠物接口
type Pet interface {
	eat()
	sleep()
}

//定义两个结构体，然后分别实现接口
type Dog struct{}
type Cat struct{}

func (d Dog) eat() {
	print("dog is eating...\n")
}

func (d Dog) sleep() {
	print("dog is sleeping...\n")
}

func (c Cat) eat() {
	print("cat is eating...\n")
}

func (cat Cat) sleep() {
	print("cat is sleeping...\n")
}

type Person struct {
	name string
}

func (p Person) care(pet Pet) {

	pet.eat()
	pet.sleep()

}

func main() {

	d := Dog{}
	c := Cat{}
	p := Person{name: "Tom"}
	p.care(d)
	p.care(c)

}
```

**运行结果**

```shell script
dog is eating...
dog is sleeping...
cat is eating...
cat is sleeping...
```

>
> 个人理解：为了方便理解，我觉得可以把它和面向对象语言里面的概念对比来理解，go语言中的接口有点类似于面向对象语言中的抽象基类，而实现了接口中所有方法的结构体可以看成是这个抽象基类的实现类，只有实现了接口中所有方法的实现类，才能把它看成是这个接口的一个子类，在参数类型是这个接口类型的地方，传入这个子类也是合法的。
>
>
> 在上面的例子中，可以看到，Pet这个接口有两个方法eat和sleep，在结构体Dog和Cat中都分别将它们实现了，因此可以将Dog和Cat看做是Pet的一个子类；而在后面的调用中也显示出了这个特性：当Person的care方法的参数是Pet类型时，传入是Dog或者Cat类型的参数也是正确的！
>
> 同时也可以举一个反例来看：
>
>
> 我将Cat结构体的sleep方法给注释掉，同时将p.sleep()的调用给注释掉，但是这样编译都不会通过。所以，很显然，因为Cat没有实现Pet中所有的方法，所以在使用Pet的地方是不能使用Cat的，而报错的提示也确实如此！


```golang
package main

//定义一个宠物接口
type Pet interface {
	eat()
	sleep()
}

//定义两个结构体，
type Dog struct{}
type Cat struct{}

func (d Dog) eat() {
	print("dog is eating...\n")
}

func (d Dog) sleep() {
	print("dog is sleeping...\n")
}

func (c Cat) eat() {
	print("cat is eating...\n")
}

// func (cat Cat) sleep() {
// 	print("cat is sleeping...\n")
// }

type Person struct {
	name string
}

func (p Person) care(pet Pet) {

	pet.eat()
	// pet.sleep()

}

func main() {

	d := Dog{}
	c := Cat{}
	p := Person{name: "Tom"}
	p.care(d)
	p.care(c)

}
```

**运行结果**

```shell script
# command-line-arguments
./lll06_通过接口实现OCP原则.go:46:9: cannot use c (variable of type Cat) as type Pet in argument to p.care:
        Cat does not implement Pet (missing sleep method)
```


## 继承

通过结构体嵌套来实现继承。


```golang
package main

import "fmt"

//"父类"
type Pet struct {
	name string
	age  int
}

func (p Pet) eat() {
	fmt.Printf("%v is eating\n", p.name)
}

func (p Pet) sleep() {
	fmt.Printf("%v is sleeping\n", p.name)
}

// “子类”
type Dog struct {
	Pet
}

func main() {

	erha := Dog{
		Pet{name: "二哈", age: 2},
	}

	// 子类可以直接调用父类中的方法
	erha.eat()
	erha.sleep()

}
```

**运行结果**


```shell script
二哈 is eating
二哈 is sleeping
```



