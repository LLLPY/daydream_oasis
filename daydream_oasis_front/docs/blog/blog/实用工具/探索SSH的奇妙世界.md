
<BlogInfo title="探索SSH的奇妙世界" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=197 category="实用工具" tag_list="['ssh', '远程连接', '文件传输']" create_time="2023.09.10 23:55:11.780732" update_time="2023.09.10 23:57:58.874192" />

^^^^^^^^^
<blockquote>
<p>引言： 在现代互联网时代，安全远程管理和文件传输是许多企业和个人必备的技术需求。而SSH（Secure Shell）作为一种安全的网络协议，为我们提供了一种加密的远程访问和文件传输解决方案。本博客将深入介绍SSH的基本概念、工作原理、常见用法和安全性等方面，帮助读者更好地理解和应用SSH技术。</p>
</blockquote>
<p><img src="../../../media/image/2023/09/05/openssh.1076aac04bd211eea0c4d9fd74d8f392.gif" alt="openssh.1076aac04bd211eea0c4d9fd74d8f392.gif" /></p>
<h2 id="1-什么是SSH">1.什么是SSH</h2>
<p>SSH，全称为Secure Shell，是一种<strong>网络协议</strong>，<strong>用于在不安全的网络中安全地进行远程登录和文件传输</strong>。它通过加密通信和身份验证机制，确保数据的机密性和完整性。</p>
<p>SSH的工作原理：</p>
<ul>
<li class="vditor-task"><input disabled="" type="checkbox" /> 客户端与服务器建立连接</li>
<li class="vditor-task"><input disabled="" type="checkbox" /> 客户端和服务器进行身份验证</li>
<li class="vditor-task"><input disabled="" type="checkbox" /> 加密通信通道的建立</li>
<li class="vditor-task"><input disabled="" type="checkbox" /> 安全地传输数据</li>
</ul>
<h2 id="2-我们经常说的ssh连接是啥-">2.我们经常说的ssh连接是啥？</h2>
<p>在开发过程中，当我们需要将项目部署到服务器，或者使用vscode连接远程服务器进行编码，或者是使用scp进行文件传输......等等这些，都能见到ssh的身影，举一个更加直观的例子，比如我想使用ssh连接一台服务器，我会进行如下操作：</p>
<p><img src="../../../media/image/2023/09/05/image.917f98504bde11eea0c4d9fd74d8f392.png" alt="image.917f98504bde11eea0c4d9fd74d8f392.png" /></p>
<p>那么这里的“ssh”命令和上面说的ssh协议有什么关系呢？其实这里的“ssh”命令是基于ssh协议实现的一个远程连接工具，它是<a href="https://www.openssh.com/">openssh</a>工具下的一个子工具，openssh包含了ssh，scp和sftp三大工具，都是基于ssh协议实现的。</p>
<h2 id="3-SSH的基本用法">3.SSH的基本用法</h2>
<h3 id="3-1SSH的安装和配置">3.1SSH的安装和配置</h3>
<p>a.安装和配置SSH客户端（Debian系统，这里是ubuntu系统）</p>
<pre><code class="language-bash"># 安装服务端
sudo apt install openssh-server

# 安装客户端
sudo apt install openssh-server
</code></pre>
<p><img src="../../../media/image/2023/09/06/image.f4d5b1724ca711eea0c4d9fd74d8f392.png" alt="image.f4d5b1724ca711eea0c4d9fd74d8f392.png" /></p>
<p>在安装完openssh-server之后，它的默认的配置文件的地址是需要我们知道的，因为有一些功能是需要通过修改配置文件去实现的。</p>
<p>(ps:windows上安装openssh的方法：<a href="https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse#install-openssh-using-windows-settings">windows上安装openssh</a>)</p>
<pre><code class="language-bash"># linux系统的ssh配置文件地址
/etc/ssh/sshd_config

# windows上ssh配置文件地址
/C/ProgramData/ssh/sshd_config
</code></pre>
<p>b.使用SSH命令连接远程服务器</p>
<p>在远程安装完服务端，在本地安装客户端之后，就可以在本地通过客户端连接远程的服务端了。windows10及以上的终端中默认集成了openssh-client，因此就可以直接进行连接了。</p>
<p><img src="../../../media/image/2023/09/06/image.92a171ac4ca811eea0c4d9fd74d8f392.png" alt="image.92a171ac4ca811eea0c4d9fd74d8f392.png" /></p>
<h3 id="3-2SSH命令的基本用法">3.2SSH命令的基本用法</h3>
<p>a.登录远程服务器</p>
<pre><code class="language-bash">ssh [用户名]@[服务器地址]

# 例如：我这里要使用用户lll登录192.168.130.128这台服务器

ssh lll@192.168.130.128
</code></pre>
<p><img src="../../../media/image/2023/09/06/image.92a171ac4ca811eea0c4d9fd74d8f392.png" alt="image.92a171ac4ca811eea0c4d9fd74d8f392.png" /></p>
<p>指定端口登录</p>
<p>有时候我们可能为了安全起见，不会使用ssh的默认端口22，会改成其他端口，这样在一定程度上能够减少服务器受到攻击的概率，因此我们可以在登录的时候指定我们设置的端口（这里端口需要先在服务器上配置完成）。</p>
<pre><code class="language-bash">ssh -p 22 lll@192.168.130.128
</code></pre>
<p>b.退出SSH会话</p>
<pre><code class="language-bash">exit
</code></pre>
<p><img src="../../../media/image/2023/09/06/image.69c480fc4ca911eea0c4d9fd74d8f392.png" alt="image.69c480fc4ca911eea0c4d9fd74d8f392.png" /></p>
<p>c.执行远程命令：ssh [用户名]@[服务器地址] [命令]</p>
<p>有时候我们可能只是想远程执行一条命令，那么直接在命令末尾跟上我们要执行的命令即可，在连接成功后立即执行。</p>
<pre><code class="language-bash"># 例如：登录成功后，执行ls命令，查看一下当前目录下的文件信息
ssh lll@192.168.130.128 ls
</code></pre>
<p><img src="../../../media/image/2023/09/09/image.7e642e2a4ecc11eea0c5d9fd74d8f392.png" alt="image.7e642e2a4ecc11eea0c5d9fd74d8f392.png" /></p>
<h3 id="3-3SSH配置文件的常见选项和参数">3.3SSH配置文件的常见选项和参数</h3>
<p>以下罗列了几个比较常用的参数配置，了解了这几个常用的配置差不多能胜任平常80%的开发了。</p>
<p>-p[port]：指定ssh服务器的端口号，默认端口号是22，可以在服务端的ssh配置文件中配置。</p>
<pre><code class="language-bash"># 这里上面已经展示过就不展示了。
</code></pre>
<p>-l[login_name]：指定登录时的用户名（感觉用处不大，直接用username@host更方便）。</p>
<p><img src="../../../media/image/2023/09/10/image.32ab0f824fec11eea0c5d9fd74d8f392.png" alt="image.32ab0f824fec11eea0c5d9fd74d8f392.png" /></p>
<p>-C[compression]：压缩传输，连接时带上这个参数后，所有的传输（命令，数据等）都会进行压缩和解压缩以提高传输的效率，在传输量较小或者适中的情况下可以开启，如果要传输的文件较大，压缩和解压可能会更加耗时。</p>
<p><img src="../../../media/image/2023/09/10/image.9417fcda4fec11eea0c5d9fd74d8f392.png" alt="image.9417fcda4fec11eea0c5d9fd74d8f392.png" /></p>
<p>-E[log_file]：指定ssh的日志文件，指定后，ssh会话的内容日志回输出到该文件中，当遇到问题，可以通过它来排查。</p>
<p><img src="../../../media/image/2023/09/10/image.0d6199d44fed11eea0c5d9fd74d8f392.png" alt="image.0d6199d44fed11eea0c5d9fd74d8f392.png" /></p>
<p>-i[identify_file]：指定密钥文件的路径，可用于免密登录。</p>
<p><img src="../../../media/image/2023/09/10/image.ac5110604fed11eea0c5d9fd74d8f392.png" alt="image.ac5110604fed11eea0c5d9fd74d8f392.png" /></p>
<h2 id="4-SSH的高级用法">4.SSH的高级用法</h2>
<p>虽然上面的基本用法已经能够解决我们日常开发中80%的需求，但是在掌握下面的几个高级玩法之后，也许这就是你成为人群顶峰中那20%的理由，特别是第二种高级用法，当我看到本地端口转发服务时，我于是立马就兴奋了，因为它的功能是能把本地的服务转发到远程，于是我立马想到：这样的话，我岂不是能够实时修改本地的内容，实时将服务“发布”在远程？于是我立马在本地启了一个demo服务，然后通过本地端口转发到我的服务器，果不其然真的可以访问！然后在看到远程端口转发时，其实它和本地端口转发相比，就是发送者和接受者对调了一下，但是突然让我想到了：如果将这两个功能结合起来，是不是就可以实现任意两台电脑之间的互联？这不就是我们经常用的远程桌面那玩意吗（只是大胆猜测，但是实际还需要具体考究）？</p>
<h3 id="4-1SSH代理和跳板机的使用场景和配置方法">4.1SSH代理和跳板机的使用场景和配置方法</h3>
<p>使用SSH代理进行网络流量的安全转发和加密</p>
<p>使用SSH跳板机访问内网服务器</p>
<h3 id="未完待续---">未完待续...</h3>
<h3 id="4-2SSH端口转发的概念和用法">4.2SSH端口转发的概念和用法</h3>
<p>本地端口转发：将本地端口转发到远程服务器</p>
<p>远程端口转发：将远程端口转发到本地计算机</p>
<h3 id="4-3SSH的高级配置和定制化选项">4.3SSH的高级配置和定制化选项</h3>
<p>修改SSH服务器配置文件：/etc/ssh/sshd_config</p>
<p>修改SSH客户端配置文件：~/.ssh/config</p>
<h2 id="5-SSH文件传输">5.SSH文件传输</h2>
<h3 id="5-1SCP-Secure-Copy-的基本原理和使用方法">5.1SCP（Secure Copy）的基本原理和使用方法</h3>
<p>上传文件到远程服务器：scp [本地文件路径] [用户名]@[服务器地址]:[目标路径]</p>
<p>从远程服务器下载文件：scp [用户名]@[服务器地址]:[远程文件路径] [本地目标路径]</p>
<h3 id="5-2SFTP-SSH-File-Transfer-Protocol-的基本原理和使用方法">5.2SFTP（SSH File Transfer Protocol）的基本原理和使用方法</h3>
<p>连接远程服务器：sftp [用户名]@[服务器地址]</p>
<p>上传文件到远程服务器：put [本地文件路径] [远程目标路径]</p>
<p>从远程服务器下载文件：get [远程文件路径] [本地目标路径]</p>
<p>文件传输操作技巧和注意事项：</p>
<p>传输文件夹：使用-r选项</p>
<p>断点续传：使用-r选项和--partial选项</p>
<p>设置文件权限：使用-P选项</p>
<h2 id="6-SSH的安全性和最佳实践">6.SSH的安全性和最佳实践</h2>
<h3 id="6-1SSH的安全性特点和防护措施">6.1SSH的安全性特点和防护措施</h3>
<p>加密通信：确保数据的机密性</p>
<p>身份验证：保护服务器免受未经授权的访问</p>
<p>防止中间人攻击：使用公钥验证服务器身份</p>
<h3 id="6-2SSH安全性的最佳实践">6.2SSH安全性的最佳实践</h3>
<p>使用强密码和密钥对进行身份验证</p>
<p>限制SSH登录的IP范围</p>
<p>禁用SSH的root登录</p>
<p>定期更新SSH软件和密钥</p>
<h3 id="6-3常见的SSH安全漏洞和攻击类型">6.3常见的SSH安全漏洞和攻击类型</h3>
<h4 id="6-3-1暴力破解密码">6.3.1暴力破解密码</h4>
<h4 id="6-3-2中间人攻击">6.3.2中间人攻击</h4>
<h4 id="6-3-3Brute-Force攻击">6.3.3Brute-Force攻击</h4>
<h4 id="6-3-4SSH安全防御措施">6.3.4SSH安全防御措施</h4>
<h5 id="6-3-4-1使用防火墙限制SSH访问">6.3.4.1使用防火墙限制SSH访问</h5>
<h5 id="6-3-4-2使用Fail2Ban等工具防止暴力破解">6.3.4.2使用Fail2Ban等工具防止暴力破解</h5>
<h5 id="6-3-4-3使用公钥验证服务器身份">6.3.4.3使用公钥验证服务器身份</h5>

