
<BlogInfo id="1235" title="golang学习笔记系列之标识符，关键字以及命名规则" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=96 category="golang" tag_list="['golang']" create_time="2022.09.10 17:48:20.288849" update_time="2022.09.13 19:58:21" />


![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

### 标识符

标识符的英文是 **identifier** ，通俗地讲，就是给变量，常量，函数，结构体，数组，切片，接口起名字。

#### 标识符的规范要求

  * 由数字，字母，下划线组成
  * 不能以数字开头
  * 区分大小写
  * 尽量做到见名知意

```golang
//正确的标识符
var abc string
var a12 int
var _123 int[]

//错误的标识符
var 123abc int //不能以数字开头
var abc&afa string //出现了未知的字符
```

### 关键字

Go 共有 25
个保留关键字，各有其作用，不能用作[标识符](https://so.csdn.net/so/search?q=%E6%A0%87%E8%AF%86%E7%AC%A6&spm=1001.2101.3001.7020)。Go
的 25 个关键字按照作用可以分为 3 类，分别为包管理、程序实体声明与定义与程序流程控制。


```golang
包管理（2个）：
	import	package

程序实体声明与定义（8个）：
	chan	const	func	interface	map	struct	type	var

程序流程控制（15个）：
	break	case	continue	default	defer	else	fallthrough	
	for		go		goto		if		range	return	select		switch
```


除了上面的保留关键字，go语言还有36个预定义标识符，其中包含了基本类型名称和一些基本的内置函数，如下表：

append | bool | byte | cap | close | complex  
---|---|---|---|---|---  
complex64 | complex128 | uint16 | copy | false | float32  
float64 | imag | int | int8 | int16 | uint32  
int32 | int64 | iota | len | make | new  
nil | panic | unit64 | print | println | real  
recover | string | true | uint | uint8 | uintprt  
  
### 命名规则

#### 区分大小写

命名规则涉及变量，常量，全局函数，结构，接口，方法等的命名。go语言从语法层面进行了以下限定：任何需要对外暴露的名字必须以大写字母开头，不需要对外暴露的则应该以小写字母开头。

当命名以一个大写字母开头，如：Hello，那么使用这种形式的标识符的对象就 **可以被外部包的代码所使用**
（前提是导入了这个包），这被称为导出（类似于java中的public）；命名如果以小写字母开头，则 **对包外是不可见的**
，但是它们在整个包的内部是可见并可用的（类似于java中的private）。

![在这里插入图片描述](https://img-blog.csdnimg.cn/323ed093cd0d48509e4e920bff1a6e49.png#pic_center)

#### 包名称

保持package的名称和目录一致，尽量采取有意义的包名，简洁明了，尽量不要和标准库冲突。包名应该为 **小写** 单词，不要使用下划线或者混合大小写。

#### 文件名

尽量采取简洁明了的文件名，简短，有意义，应该为 **小写** 单词，使用 **下划线** 分割各个单词。

#### 结构体命名

一般采用驼峰命名法，首字母根据访问控制来规定大小写。


```golang
//客户订单
type CustomerOrder struct {
    Name string
    Address string 
}

order := CustomerOrder{"tom", "上海"}
```


#### 接口命名

命名规则同结构体。

单个函数的结构名以"er"作为后缀，例如：Reader，Writer。


```golang
type Reader interface {
    Read(p []byte) (n int, err error) 
    
}
```


#### 变量命名

基本命名规则同结构体，但遇到特有名词时，需要遵循以下规则：

  * 如果变量为私有，且特有名词为首个单词，则使用小写，如appService若变量类型为bool，则名称应以Has，Is，Can或Allow开头
```golang
var isExist bool
var hasConflict bool
var canManage bool
var allowGitHook bool
```
 
#### 常量命名

常量均使用大写字母组成，并且使用下划线分割单词。


```golang
 const APP_URL = "http://www.lll.plus" 
```


如果是枚举类型的常量，需要首先创建相应的类型


```golang
type Scheme string

const (
	HTTP Scheme = "http"
    HTTPS Scheme = "https"
)
```
