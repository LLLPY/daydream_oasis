
<BlogInfo title="python中的property，以及属性和特性之间的优先权" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=354 category="《流畅的python》" tag_list="['特性', '属性']" create_time="2022.07.14 17:49:21.173992" update_time="2022.07.14 17:49:21" />

^^^^^^^^^
<p>&nbsp;</p>

<h1><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/087b5e8c794841d7b48a6951f33ac3a7.png" style="height:48px; width:48px" />前言<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/7f562ffa99d34ee19c800721a0e370ac.png" style="height:48px; width:48px" /></h1>

<p>&nbsp;</p>

<blockquote>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这几天又回过头来看《流畅的python》这本书了，在一个示例中又看到了property作为装饰器在使用，因为很久没有用这个东西了，对它的一些特性和使用方法等都不是很熟悉，所以又专门在搜了几篇博客和在官方文档中学习了它的相关用法。再者又刚好学到了python中的属性(attribute)，所以刚好这两者可以两相对比，也许更好理解！</p>
</blockquote>

<p>&nbsp;</p>

<h1><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/8b9460b815b3429db78714d93ba43a93.png" style="height:48px; width:48px" />属性(attribute)<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a6cb81ef4d6447a5baf2b4ecbe0d6dfd.png" style="height:48px; width:48px" /></h1>

<p>&nbsp;</p>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" />属性的定义<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" /></h2>

<blockquote>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在python中，<strong>属性其实是(对象的)属性和(对象的)方法的集合。</strong></p>

<p>一开始我以为就是：属性就是属性，方法就是方法，一个是&ldquo;属性&rdquo;，一个是行为，但是在打开IDE写了一个测试案例后，我就信服了：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># python中数据的属性和处理数据的方法统称为属性</span>
<span class="hljs-keyword">class</span> <span class="class_ hljs-title">Cat</span>:

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self, name</span>):
        self.name = name

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">run</span>(<span class="hljs-params">self</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;小碎步...&#39;</span>)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    tom = Cat(<span class="hljs-string">&#39;Tom&#39;</span>)
    <span class="hljs-built_in">print</span>(tom.__getattribute__(<span class="hljs-string">&#39;name&#39;</span>))  <span class="hljs-comment"># 对象的属性</span>
    <span class="hljs-built_in">print</span>(tom.__getattribute__(<span class="hljs-string">&#39;run&#39;</span>))  <span class="hljs-comment"># 对象的方法</span></code></pre>

<p>在这里我定义了一个类，同时在初始化方法中为它添加了一个属性name，然后定义了一个run方法，之后在main方法里创建了tom这个实例，使用__getattribute__()方法来获取它的name属性和run属性，果不其然，居然真的都获取到了！</p>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/9ddc3c2746494073a5bd96599bd6df6d.png" style="height:694px; width:864px" /></p>

<p>&nbsp;所以，以后再也不要说属性只是单纯的&ldquo;属性&rdquo;了！<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/71832c5698ee4d4483823c4a1bff683f.png" style="height:24px; width:24px" /></p>

<p>&nbsp;</p>
</blockquote>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" />属性的用法<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" /></h2>

<blockquote>
<p>属性用法很简单，不管是对象的属性还是方法，都是用.来获取或者调用。</p>

<h3>1.设置或修改对象的属性</h3>

<pre data-widget="codeSnippet">
<code class="hljs language-python">tom.name=<span class="hljs-string">&#39;Tom&#39;</span> <span class="hljs-comment">#设置(修改)对象tom的name属性值为Tom</span></code></pre>

<h3>2.删除对象的属性</h3>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">del</span> tom.name <span class="hljs-comment">#使用del关键字删除对象的属性</span></code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/be5940fbd2314eb7854a0b6cd3594036.png" style="height:404px; width:821px" /></p>

<p>&nbsp;可以看到，属性删除后就不能再获取了。</p>

<h3>3.调用对象的方法(属性)</h3>

<pre data-widget="codeSnippet">
<code class="hljs language-python">tom.run() <span class="hljs-comment">#直接用.调用即可</span></code></pre>

<p>4.对象的方法置None</p>

<p>对象的方法我们无法删除，但是我们可以将其置为None。</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python">tom.run=<span class="hljs-literal">None</span></code></pre>
</blockquote>

<h1><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a6cb81ef4d6447a5baf2b4ecbe0d6dfd.png" style="height:48px; width:48px" />特性(property)<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a6cb81ef4d6447a5baf2b4ecbe0d6dfd.png" style="height:48px; width:48px" /></h1>

<p>&nbsp;</p>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" />特性的定义<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" /></h2>

<blockquote>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;个人理解：特性就是属性的特例，因为预先知道某些属性的一些特定条件，比如取值范围，类型等等，所以在对这些属性进行操作的时候，为了在操作前后，保持一些特定条件不变（就是不准越界操作），所以就有了特性来约束它。</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 来看一下官方文档给的例子：</p>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/5658c66eee524cf887bebdc1fcfdb1bc.png" style="height:743px; width:1087px" /></p>

<p>官方文档中提到：一个典型的例子就是托管x(这里的x是一个类的属性)，&nbsp;使用方法也特别的直接明了：如果&nbsp;<em>c</em>&nbsp;为&nbsp;<em>C</em>&nbsp;的实例，<code>c.x</code>&nbsp;将调用 getter，<code>c.x&nbsp;=&nbsp;value</code>&nbsp;将调用 setter，&nbsp;<code>del&nbsp;c.x</code>&nbsp;将调用 deleter。就是在对c.x这个属性进行操作时，可以通过getter，setter，delx来控制它的修改和删除。</p>
</blockquote>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" />特性的用法<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" /></h2>

<blockquote>
<p>因为它是一个修饰器，所以调用方法有两种：</p>

<h3>1.直接使用@符号调用</h3>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">class</span> <span class="class_ hljs-title">Dog</span>:

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self</span>):
        self.__name = <span class="hljs-literal">None</span>

<span class="hljs-meta">    @property</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">name</span>(<span class="hljs-params">self</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;调用了get_name方法...&#39;</span>)
        <span class="hljs-keyword">return</span> self.__name

<span class="hljs-meta">    @name.setter</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">name</span>(<span class="hljs-params">self, val</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;调用了set_name方法...&#39;</span>)
        self.__name = val

<span class="hljs-meta">    @name.deleter</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">name</span>(<span class="hljs-params">self</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;调用了del_name方法...&#39;</span>)
        <span class="hljs-keyword">del</span> self.__name


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    tom = Dog()
    tom.name = <span class="hljs-string">&#39;Tom&#39;</span>
    <span class="hljs-built_in">print</span>(tom.name)
    <span class="hljs-keyword">del</span> tom.name</code></pre>

<h3><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/1b940ff196a347debd0beea883481b66.png" style="height:842px; width:1027px" />2.当做一个正常的函数使用</h3>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">class</span> <span class="class_ hljs-title">Cat</span>:

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self</span>):
        self.__name = <span class="hljs-literal">None</span>

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">set_name</span>(<span class="hljs-params">self, name</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;调用了set_name方法...&#39;</span>)
        self.__name = name

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">get_name</span>(<span class="hljs-params">self</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;调用了get_name方法...&#39;</span>)

        <span class="hljs-keyword">return</span> self.__name

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">del_name</span>(<span class="hljs-params">self</span>):
        <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;调用了del_name方法...&#39;</span>)

        <span class="hljs-keyword">del</span> self.__name

    name = <span class="hljs-built_in">property</span>(get_name, set_name, del_name, <span class="hljs-string">&#39;this is a property name.&#39;</span>)


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    tom = Cat()
    tom.name = <span class="hljs-string">&#39;Tom&#39;</span>
    <span class="hljs-built_in">print</span>(tom.name)
    <span class="hljs-keyword">del</span> tom.name</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/15d6a64e0c27406794a65f6b733619e3.png" style="height:761px; width:1100px" /></p>

<p>&nbsp;</p>

<p>&nbsp;可以看到两种方法使用的效果都是一样的！</p>
</blockquote>

<h2><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" />特性的使用场景<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/44f166fb97ee4ef1b0d0f5715e475e8f.png" style="height:35px; width:35px" /><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/c74daebf808247f0ae3f41f757b90bfb.png" style="height:48px; width:48px" /></h2>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;重点讲一下这个，正是因为有一些特定场景的存在，才会出现property这个特性的，正如之前在《Django企业开发实战》一书中所说的那样：若无必要，勿增实体。而python向来以简洁优雅著称，因为这些特定场景，所以是有必要增加property这个实体的。</p>

<p>主要使用场景有两个：</p>

<h3>1.限制一些属性为只读</h3>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 在只使用@property修饰某个方法后，将其变成特定的属性，如果不添加setter和deleter方法，那么它就变成了只读属性。比如：用户名设置后就不允许修改：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">class</span> <span class="class_ hljs-title">User</span>:

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self, username, password</span>):
        self.__username = username
        self.password = password

    <span class="hljs-comment"># 将username属性限定为只读</span>
<span class="hljs-meta">    @property</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">username</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> self.__username


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    tom=User(<span class="hljs-string">&#39;tom&#39;</span>,<span class="hljs-string">&#39;1234&#39;</span>)
    <span class="hljs-built_in">print</span>(tom.username)
    tom.username=<span class="hljs-string">&#39;Tom&#39;</span></code></pre>

<h3><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/65fffbbdb37a4733a28550e8feaa68bd.png" style="height:584px; width:900px" /></h3>

<p>可以看到在只读状态下，修改和删除属性都会失败！</p>

<h3>2.限定属性的操作范围</h3>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;生活中，你可能会遇到这样的情况，有一天你告诉你妈你想吃鱼，并且是红烧鱼而不是清蒸鱼，然后你妈命令你爸去买鱼，同时你妈嘱咐你爸说：买新鲜一点的啊，价格贵一点没关系！然后你爸心想：这个月工资还没发呢，能省省就省省吧，于是你爸在心中就大概确定了买一条鱼的开销区间(比如30到100)。可以看到在一条鱼上餐桌之前，你和你爸妈是对它进行了精挑细选，才得以上到你的餐桌，其实就是对鱼这个属性增加了一些条件限定：类型的限定：要红烧的而不是清蒸的；取值范围的限定：不能太贵也不能太便宜，30到100之前刚刚好。</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 接下来用代码实现一下这个栗子：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-keyword">class</span> <span class="class_ hljs-title">Fish</span>:

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self</span>):
        self.__price = <span class="hljs-literal">None</span>
        self.__cook = <span class="hljs-literal">None</span>

<span class="hljs-meta">    @property</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">price</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> self.__price

<span class="hljs-meta">    @price.setter</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">price</span>(<span class="hljs-params">self, pri</span>):

        <span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> <span class="hljs-built_in">isinstance</span>(pri, <span class="hljs-built_in">int</span>):
            <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">&#39;价格有误！&#39;</span>)
        <span class="hljs-keyword">if</span> pri &lt; <span class="hljs-number">30</span>:
            <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">&#39;太便宜了，不要！&#39;</span>)
        <span class="hljs-keyword">elif</span> pri &gt; <span class="hljs-number">100</span>:
            <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">&#39;太贵了，不要！&#39;</span>)
        <span class="hljs-keyword">else</span>:
            self.__price = pri
            <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;价格刚刚好!&#39;</span>)

<span class="hljs-meta">    @property</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">cook</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> self.__price

<span class="hljs-meta">    @cook.setter</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">cook</span>(<span class="hljs-params">self,method</span>):

        <span class="hljs-keyword">if</span> method!=<span class="hljs-string">&#39;红烧&#39;</span>:
            <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">&#39;我只要红烧鱼！&#39;</span>)
        <span class="hljs-keyword">else</span>:
            <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;耶，我最爱的红烧鱼！&#39;</span>)



<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    luck_fish=Fish()
    luck_fish.price=<span class="hljs-number">60</span>
    <span class="hljs-comment"># luck_fish.cook=&#39;清蒸&#39;</span>
    luck_fish.cook=<span class="hljs-string">&#39;红烧&#39;</span></code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/265d1fac1f9143e78d233541387ef07c.png" style="height:503px; width:900px" /></p>

<p>可以看到，只有当属性的取值返回和类型是规定的范围之内的时候，程序才会正常执行，而生活中类似这样的栗子很多，所以这也是特性存在的意义。&nbsp;</p>
</blockquote>

<h1><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a6cb81ef4d6447a5baf2b4ecbe0d6dfd.png" style="height:48px; width:48px" />属性和特性之间的差别和联系<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a6cb81ef4d6447a5baf2b4ecbe0d6dfd.png" style="height:48px; width:48px" /></h1>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; 直观的看，特性的目的好像是把方法&ldquo;属性化&rdquo;，但这样做一点意义也没有，如果我可以定义一个属性，何必再额外定义一个方法，然后将其转化成属性呢？所以，更重要的目的就是应对一些特定场景。</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; 从特性表现出来的性质和行为来看，它其实就是一种特定的&ldquo;属性&rdquo;。只不过特性的权利提升了一点点，就好像你可以去修改这个属性，但是能不能修改成功，就看你的上一级允不允许你修改（有没有给你这个属性添加限定条件），而特性的权利就扩展到了这个&ldquo;上一级&rdquo;。</p>
</blockquote>

<h1><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a6cb81ef4d6447a5baf2b4ecbe0d6dfd.png" style="height:48px; width:48px" />属性和特性之间的优先权<img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/a6cb81ef4d6447a5baf2b4ecbe0d6dfd.png" style="height:48px; width:48px" /></h1>

<blockquote>
<p>&nbsp; &nbsp; &nbsp; &nbsp; 在写程序的时候，也不乏会出现这样的例子：属性和特性之间重名了！那么这个时候在使用这个重名的属性(特性)时，程序是会报错？还是会使用属性的值？还是会使用特性的值？也许根据它们的名称就可以猜出来，特性嘛，肯定就特别一些嘛，<strong>所以会优先使用特性的值！</strong>下面这个栗子完美说明：</p>

<pre data-widget="codeSnippet">
<code class="hljs language-python"><span class="hljs-comment"># 关系：在同名的情况下,实例属性会覆盖类属性，特性会覆盖实例属性</span>

<span class="hljs-keyword">class</span> <span class="class_ hljs-title">Cat</span>:
<span class="hljs-meta">    @property</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">wow</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> <span class="hljs-string">&#39;property---喵~&#39;</span>


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">&#39;__main__&#39;</span>:
    <span class="hljs-comment"># 实例属性会覆盖类属性</span>
    jerry = Cat()

    <span class="hljs-comment"># 特性会覆盖实例属性</span>
    <span class="hljs-built_in">print</span>(jerry.__dict__)  <span class="hljs-comment"># 查看对象的属性字典</span>
    jerry.__dict__[<span class="hljs-string">&#39;wow&#39;</span>] = <span class="hljs-string">&#39;normal---喵~&#39;</span>
    <span class="hljs-built_in">print</span>(jerry.__dict__)
    <span class="hljs-built_in">print</span>(jerry.wow)  <span class="hljs-comment"># 虽然修改了jerry的wow的值，但是依旧返回的是其特性的值</span>
    <span class="hljs-built_in">print</span>(jerry.__dict__[<span class="hljs-string">&#39;wow&#39;</span>])
    <span class="hljs-keyword">del</span> Cat.wow  <span class="hljs-comment"># 删除类特性后，返回的就是正常的属性值</span>
    <span class="hljs-comment"># del Cat.wow  # 删除特性</span>
    <span class="hljs-built_in">print</span>(jerry.wow)
    Cat.wow = <span class="hljs-built_in">property</span>(<span class="hljs-keyword">lambda</span> self: <span class="hljs-string">&#39;add a property---喵~&#39;</span>)  <span class="hljs-comment"># 为类新增和属性同名的特性</span>
    <span class="hljs-built_in">print</span>(jerry.wow)  <span class="hljs-comment"># 之后还是优先访问特性的值</span>
</code></pre>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/ec5d183d9be4486ca869ee4edf7b2784.png" style="height:534px; width:900px" /></p>

<p>&nbsp;</p>
</blockquote>

<p>&nbsp;</p>

