
<BlogInfo title="gitee 上传代码的步骤" author="夏哲哲" pv=0 read_times=0 pre_cost_time=36 category="git" tag_list="[]" create_time="2023.09.18 10:23:46.400145" update_time="2023.09.18 10:23:46.400151" />

^^^^^^^^^
<p>230918</p>
<p>230918</p>
<p>夏哲</p>
<h1 id="添加ssh公匙"><a href="https://help.gitee.com/base/account/SSH%E5%85%AC%E9%92%A5%E8%AE%BE%E7%BD%AE">添加ssh公匙</a></h1>
<p><em>为自己的电脑添加访问gitee的条件</em></p>
<blockquote>
<p>Windows 用户建议使用 <strong>Windows PowerShell</strong> 或者 <strong>Git Bash</strong>，在 <strong>命令提示符</strong> 下无 <code>cat</code> 和 <code>ls</code> 命令。</p>
</blockquote>
<p>1.生成ssh</p>
<p><code>ssh-keygen **-t** ed25519 **-C** **&quot;Gitee SSH Key&quot;</code></p>
<p><em>中间通过三次<strong>回车键</strong>确定</em></p>
<p>2.查看生成的 SSH 公钥和私钥</p>
<p><code>ls ~/.ssh/</code></p>
<ul>
<li>私钥文件 <code>id_ed25519</code></li>
<li>公钥文件 <code>id_ed25519.pub</code></li>
<li></li>
<li></li>
<li></li>
</ul>
<p>3.读取公钥文件</p>
<p><code>cat ~/.ssh/id_ed25519.pub</code></p>
<p>输出：<code>ssh-ed25519 AAAA***5B Gitee SSH Key</code></p>
<p>4.<strong>gitte -&gt;「个人设置」-&gt;「安全设置」-&gt;「SSH 公钥」-&gt;「<a href="https://gitee.com/profile/sshkeys">添加公钥</a>」</strong></p>
<p>5.通过 <code>ssh -T</code> 测试，输出 SSH Key 绑定的<strong>用户名</strong>，证明添加成功</p>
<h1 id="添加本地代码到test仓库">添加本地代码到test仓库</h1>
<p>1.新建test仓库</p>
<p><img src="../../../media/image/2023/09/18/image.6e2e84f255c911eea0c5d9fd74d8f392.png" alt="image.6e2e84f255c911eea0c5d9fd74d8f392.png" /></p>
<p>2.提交代码</p>
<pre><code class="language-cmd"># Git 全局设置
git config --global user.name &quot;夏哲&quot;
git config --global user.email &quot;1446326370@qq.com&quot;

# 进入本地代码路径，上传代码 
cd test 
git init  
git add .  # 添加所有文件 
git commit -m &quot;first commit&quot;  # 为该次提交添加评论 
git remote add origin git@gitee.com:xia-zhe-zhe/test.git   # 链接到指定仓库 
git push -u origin &quot;master&quot;  # 提交
</code></pre>

