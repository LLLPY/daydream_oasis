
<BlogInfo id="1228" title="git的一些基本操作" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=27 category="git" tag_list="['git', '版本控制']" create_time="2022.09.22 16:08:22.615161" update_time="2023.03.25 20:17:27.589470" />

![下载.d9b9a679cb0611edaaebdcf505c52fb0.png](../../../media/image/2023/03/25/下载.d9b9a679cb0611edaaebdcf505c52fb0.png)

**Git初始化仓库的一般步骤**

#1.创建项目

```shell script
mkdir my_project
```
#2.切换到项目目录下

```shell script
cd my_project
```
#3.本地初始化

```shell script
git init
```
#4.创建README.md文件

```shell script
touch README.md
```
#5.添加文件

```shell script
git add .
```
#6.提交

```shell script
git commit -m 'first commit'
```
#7.添加到远程仓库（给远程仓库添加别名）

```shell script
Git remote add 别名 远程仓库地址
```
#8.查看别名列表

```shell script
git remote -v
```
**版本分支**

#1. 查看所有版本信息

```shell script
git branch -v
```
#1.创建分支

```shell script
git branch 版本名
```
#2.切换分支

```shell script
git checkout 版本名
```
#3.删除分支

```shell script
git branch -d 分支名
```
#4.合并分支

```shell script
git merge 分支名
```
**推送本地库到远程**

```shell script
Git push 别名/远程仓库地址 分支名
```
**克隆远程仓库**

```shell script
1.新建一个空的文件

2.切换到新建的目录中，并执行如下命令

git clone 远程仓库地址
```

**配置git忽略文件**

```shell script
1.cd到项目的根目录下

2.touch .gitignore

3.将要忽略的文件名加入其中即可
```


