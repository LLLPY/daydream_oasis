
<BlogInfo title="git的一些基本操作" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=27 category="git" tag_list="['git', '版本控制']" create_time="2022.09.22 16:08:22.615161" update_time="2023.03.25 20:17:27.589470" />

^^^^^^^^^
<p><img src="../../../media/image/2023/03/25/下载.d9b9a679cb0611edaaebdcf505c52fb0.png" alt="下载.d9b9a679cb0611edaaebdcf505c52fb0.png" /></p>
<p><strong>Git初始化仓库的一般步骤</strong></p>
<p> </p>
<p>#1.创建项目</p>
<p>mkdir my_project</p>
<p> </p>
<p>#2.切换到项目目录下</p>
<p>cd my_project</p>
<p> </p>
<p>#3.本地初始化</p>
<p>git init</p>
<p> </p>
<p>#4.创建README.md文件</p>
<p>touch README.md</p>
<p> </p>
<p>#5.添加文件</p>
<p>git add .</p>
<p> </p>
<p>#6.提交</p>
<p>git commit -m ‘first commit’</p>
<p> </p>
<p>#7.添加到远程仓库（给远程仓库添加别名）</p>
<p>Git remote  add  别名  远程仓库地址</p>
<p> </p>
<p>#8.查看别名列表</p>
<p>git remote -v</p>
<p> </p>
<p> </p>
<p><strong>版本分支</strong></p>
<p> </p>
<p>#1. 查看所有版本信息</p>
<p>git branch -v</p>
<p> </p>
<p>#1.创建分支</p>
<p>git branch 版本名</p>
<p> </p>
<p>#2.切换分支</p>
<p>git checkout 版本名</p>
<p> </p>
<p>#3.删除分支</p>
<p>git branch -d 分支名</p>
<p> </p>
<p>#4.合并分支</p>
<p>git merge 分支名</p>
<p> </p>
<p><strong>推送本地库到远程</strong></p>
<p> </p>
<p>Git push 别名/远程仓库地址 分支名</p>
<p> </p>
<p> </p>
<p><strong>克隆远程仓库</strong></p>
<p> </p>
<p>1.新建一个空的文件</p>
<p>2.切换到新建的目录中，并执行如下命令</p>
<p>git clone 远程仓库地址</p>
<p> </p>
<p> </p>
<p><strong>配置git忽略文件</strong></p>
<p> </p>
<p>1.cd到项目的根目录下</p>
<p>2.touch .gitignore</p>
<p>3.将要忽略的文件名加入其中即可</p>
<p> </p>

