
<BlogInfo id="386" title="gitee 上传代码的步骤" author="夏哲哲" pv=0 read_times=0 pre_cost_time="36" category="git" tag_list="['']" create_time="2023.09.18 10:23:46.400145" update_time="2023.09.18 10:23:46.400151" />

230918
夏哲

# [添加ssh公匙](https://help.gitee.com/base/account/SSH%E5%85%AC%E9%92%A5%E8%AE%BE%E7%BD%AE)

_为自己的电脑添加访问gitee的条件_

> Windows 用户建议使用 **Windows PowerShell** 或者 **Git Bash** ，在 **命令提示符** 下无
> cat和ls命令。
1.生成ssh
```shell script
ssh-keygen **-t** ed25519 **-C** **"Gitee SSH Key"
```
_中间通过三次 **回车键** 确定_
2.查看生成的 SSH 公钥和私钥
```shell script
ls ~/.ssh/
```
私钥文件 id_ed25519
公钥文件  id_ed25519.pu

3.读取公钥文件
```shell script
cat ~/.ssh/id_ed25519.pub
```
输出： 
```shell script
ssh-ed25519 AAAA***5B Gitee SSH Key
```
4. **gitte - >「个人设置」->「安全设置」->「SSH 公钥」->「[添加公钥](https://gitee.com/profile/sshkeys)」**

5..通过 ssh -T 测试，输出 SSH Key 绑定的用户名，证明添加成功 
# 添加本地代码到test仓库
1.新建test仓库
![image.6e2e84f255c911eea0c5d9fd74d8f392.png](../../../media/image/2023/09/18/image.6e2e84f255c911eea0c5d9fd74d8f392.png)
2.提交代码
```shell script
# Git 全局设置
git config --global user.name "夏哲"
git config --global user.email "1446326370@qq.com"

# 进入本地代码路径，上传代码 
cd test 
git init  
git add .  # 添加所有文件 
git commit -m "first commit"  # 为该次提交添加评论 
git remote add origin git@gitee.com:xia-zhe-zhe/test.git   # 链接到指定仓库 
git push -u origin "master"  # 提交
```



