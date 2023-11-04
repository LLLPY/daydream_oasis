
<BlogInfo id="390" title="golang学习笔记系列之go语言的环境搭建-linux系统" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="5" category="golang" tag_list="['golang', '              安装', '              环境搭建']" create_time="2022.07.28 12:38:00" update_time="2022.09.10 18:08:00" />

**目录**

1.下载golang

2.安装

2.1移除之前的安装残留，同时安装当前版本

2.2 添加环境变量

2.3检查是否安装成功

3.编写第一个go文件 ！

# 1.下载golang

下载地址：[golang](https://golang.google.cn/dl/ "golang")

如下图所示，找到golang的下载地址后，下载对应的linux版的最新版

![](https://img-blog.csdnimg.cn/de69d45f1c174e64a5009871286a6d64.png)

# 2.安装

我们按照官方给的提示安装：

![](https://img-blog.csdnimg.cn/e3cc07dee84745b0a405e8115cf53420.png)

## 2.1移除之前的安装残留，同时安装当前版本

执行命令(普通用户可能权限不够，所以加了sudo)：

## 2.2 添加环境变量

执行命令：

## 2.3检查是否安装成功

执行命令：

 如果提示了go语言的版本，就说明安装成功啦！

![](https://img-blog.csdnimg.cn/28ba454d83824328a6f615ca2228563f.png)

# 3.编写第一个go文件 ！

打开任一编辑器，输入如下代码(以hello.go命名文件)：

```golang
 package main import "fmt" func main() {
fmt.Println("hello,go!") } `
```

同目录下在终端中输入：
![](https://img-blog.csdnimg.cn/ce848144e51a43c8a4f31e4f99cdfe1e.png)
 如上，执行成功！
