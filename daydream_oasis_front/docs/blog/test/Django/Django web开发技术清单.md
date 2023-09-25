
<BlogInfo title="Django web开发技术清单" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=415 category="Django" tag_list="['清单', 'Django', 'python基础']" create_time="2022.01.28 17:59:57.543854" update_time="2022.07.11 10:56:58" />

^^^^^^^^^
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;前几天在学完《Django企业开发实战》一书后，发现在书的最后一章有一个技术栈清单，上面罗列了完成该书项目所需要的所有技术栈，从基础一直到高阶，通过提问的方式罗列出来，我感觉这种方式挺好的，带着问题去总结，总是会使人印象深刻的，所以今天打算来总结一下第一小块的内容---python基础。</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题1：基础语法是否熟悉？介绍一下</strong></h2>

<p>答：我感觉我对python的基础语法还算比较属性吧，if，else，for，while，with，open，import等等基本的语法还是经常使用的，前不久也在python3.10的官方文档中看到了3.10版本新增的switch语法，和c语言里面的用法很类似，但是灵活度更高！</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题2：有哪些关键字？解释其作用。</strong></h2>

<p><strong>答：额，这个的话我感觉我脑袋里对这个东西可能不是很清楚，<span style="color:#e74c3c">在我的脑海里，它和保留字差不多我认为，只不过保留字官方还没有投入使用而已，关键字则是已经在使用的保留字</span>。基本上的话，我认为只要是python内置的语法中出现了的单词应该都是关键字，比如：if，else，break，return，with，while，for，continue，set，list，str等等都属于关键字。这个是我个人的理解不知道对不对???</strong></p>

<p><strong>百度了一下，python中总共有33个关键字，所以我的想法还是正确的！但是我后面的话就被打脸了，百度上说保留字也属于关键字，所以我的说话可能有点欠妥；</strong></p>

<p><span style="color:#e74c3c"><strong>保留字也称为关键字</strong></span>，指被编程语言内部定义并保留使用的标识符，程序员编写程序时<span style="color:#c0392b">不能定义与保留字相同的标识符</span>。每种程序设计语言都有一套保留字，保留字一般用来构成程序整体框架、表达关键值和具有结构性的复杂语义等。掌握一门编程语言首先要熟记其所对应的保留字。</p>

<p><img src="../media/image/2022/01/28/image-20220128160557-1.png" style="height:450px; width:900px" /></p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题3：有哪些内置方法？解释其作用。</strong></h2>

<p>答：</p>

<p>list() ：将一个可迭代的对象转成一个数组，或者用于一个数组的定义。</p>

<p>tuple()：同list，但是类型是元组</p>

<p>set()：转成一个集合或者定义一个集合</p>

<p>str()：转成一个字符，或者定义一个字符</p>

<p>sorted(iterable,key,reverse)：将可迭代对象iterable按照key进行排序，reverse是否翻转</p>

<p>zip()：将可迭代对象进行并列拼接，所有可迭代对象包含的元素个数必须一致，否则在迭代的是否会报错</p>

<p>print()：输出打印到控制台</p>

<p>open()：打开文件</p>

<p>close()：关闭文件</p>

<p>filter(func,iterable)：过滤器，func设置过滤条件，iterable为过滤对象</p>

<p>eval()：不知道怎么描述。。。功能挺强大的</p>

<p>range(a,b,step)：根据步长，生成a到b的一个等差数列(a，b，step均为整数)</p>

<p>quit()：强行终止程序并退出</p>

<p>len()：返回传入对象的长度(元素个数)</p>

<p>我经常使用的应该就这些吧!</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题4：解释一下什么是动态语言？动态强类型是指什么？</strong></h2>

<p>答：这个问题确实难道我了???，但是我记得python好像是动态语言，且是弱指向类型的，对比一下就很明显了，比如在c，c++，java里面，比如一开始定义了一个int a;那么这个a就是int型的，在后面的对a进行赋值的是否只能赋int型的数值给它；而在python里面就不一样了，首先在声明a变量的时候就不用指定类型，你赋什么类型的值给它，它就是什么类型的，所以类型要求不是很严格，用官方的话就是弱类型。不知道这个弱类型和这里的动态强类型说的是不是同一个东西？</p>

<p>csdn上看了一下，好像和我说的这个就是一个东西：<a href="https://blog.csdn.net/bbc955625132551/article/details/75863434?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164335984516780271988343%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=164335984516780271988343&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-75863434.pc_search_insert_ulrmf&amp;utm_term=%E4%BB%80%E4%B9%88%E6%98%AF%E5%8A%A8%E6%80%81%E8%AF%AD%E8%A8%80&amp;spm=1018.2226.3001.4187">什么是动态语言/静态语言</a>，看了几篇，大概都是这个意思。</p>

<p>动态语言是在使用变量的时候才会去为它分配地址空间（不过首先还是确定其类型），而静态语言在使用之前就已经为其分配好地址空间了，所以这也是为什么在执行效率上静态语言更有优势的原因吧！</p>

<p>动态强类型：动态的解释如上，强弱的话：弱/强类型指的是语言类型系统的类型检查的严格程度。参考：<a href="https://www.cnblogs.com/vvsq/p/11351468.html" id="cb_post_title_url">Python是动态强类型语言</a>&nbsp;其实我看了还有一点糊，里面说：弱类型相对于强类型来说类型检查更不严格，比如说允许变量类型的隐式转换。强类型语言一般不允许这么做。</p>

<p>但是看了这篇文章之后，<a href="https://blog.csdn.net/chinesehuazhou2/article/details/108332447?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164336092216780271915521%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=164336092216780271915521&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_ulrmf~default-2-108332447.pc_search_insert_ulrmf&amp;utm_term=python%E6%98%AF%E5%BC%BA%E7%B1%BB%E5%9E%8B%E8%AF%AD%E8%A8%80%E5%90%97&amp;spm=1018.2226.3001.4187">Python到底是强类型语言，还是弱类型语言？</a>&nbsp;也许不那么迷茫了哈哈哈</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题5：是否有编码规范的概念？采用的是哪种编码规范？</strong></h2>

<p>答：额。。。感觉又是一个不好回答的问题，对我来说???，可能还是基础不扎实的缘故。我在很多地方都看到过PEP8规范，也许就是这个东西，比如定义变量的格式采用大驼峰，小驼峰等形式，其他的话我可能不好描述，但是我感觉代码时间写长了，都会有自己一定的风格。然后立马打开书看了下，作者从1.代码布局，2.字符串引号等等都讲了一定的规范格式，总结一句话就是：这样做的目的是，让你写的代码你自己很容易读懂，让别人在看的时候也很容易读懂，所以养成良好的编码格式还是非常重要的！</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题6：解释一下深拷贝和浅拷贝。</strong></h2>

<p>答：我就一句话概括一下：<strong>浅拷贝得到的和原有的同根同源,而深拷贝则是另一个新个体!（引入的是我之前的一句话），参考我在csdn的博客：</strong><a href="https://blog.csdn.net/max_LLL/article/details/119807873?spm=1001.2014.3001.5502">从numpy中学习深度拷贝和浅拷贝</a></p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题7：lambda的用法及使用场景。</strong></h2>

<p><strong>相对来说，这个函数的使用频率还是较高的，它的功能实在是太强大了！比如常在排序函数sorted()中使用，用来指定排序的key，或者在调用一个参数是函数的的方法时，如果被传入的函数没有参数还好说，如果传入的函数是有参数的话</strong></p>

<p>举个栗子康康：</p>

<p><img src="../media/image/2022/01/28/image-20220128175206-5.png" style="height:706px; width:936px" /></p>

<p>使用lambda函数成功执行：</p>

<p><img src="../media/image/2022/01/28/image-20220128175258-6.png" style="height:614px; width:808px" /></p>

<p>所以这个函数的功能是真的很强大的，使用场景也较多！</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题8：解释一下闭包及其作用。</strong></h2>

<p><strong>答：在看到闭包后，我想到的第一句话就是：在不修改原函数代码的基础上，为原函数增加新的功能。我想这句话应该是完美的概括的闭包的功能。闭包的话，说白了也是一个函数，一个方法，其有一个&ldquo;默认的参数&rdquo;，类型为函数，在其内部会调用这个函数，这也就是为什么在不改变原函数代码的基础上能够新增功能的原因，因为在闭包函数的内部，除了有原函数本身之外，还有其他的代码实现的其他功能。</strong></p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题9：实现一个简单的装饰器，用来对某个函数的结果进行缓存。</strong></h2>

<p><strong>答：源码如下：</strong></p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff">from time import sleep, time


# 修饰器函数，用于缓存某一个函数的返回结果
def my_cache(func):
    &#39;&#39;&#39;
    :param func:function
    :return: 如果某函数第一次被调用需要执行该函数并将其结果保存起来，非第一次调用直接从缓存中获取结果，最后都将结果返回
    &#39;&#39;&#39;
    cache_dic = {}  # 定义一个缓存字典

    # 1.首先从缓存中获取函数的结果
    def funcin(word):
        res = cache_dic.get(func.__name__, &#39;&#39;)
        if not res:  # 2.如果缓存中没有当前函数的结果，就调用函数，获取函数的返回值，并将结果存入缓存中
            res = func(word)
            cache_dic[func.__name__] = res
            sleep(3)  # 模拟调用函数会执行一段时间
        return res

    return funcin


@my_cache
def fun(word):  # 功能函数
    return f&#39;hello {word}&#39;


if __name__ == &#39;__main__&#39;:
    time1 = time()
    print(fun(&#39;world&#39;))
    time2 = time()
    print(fun(&#39;python&#39;))  # 即便输入的参数是python，这个函数的打印结果为world，原因是因为其结果已保存在缓存中，
    # 直接使用的是缓存的结果，未调用函数本身
    print(f&#39;第一次执行耗时：{time2 - time1}
第二次执行耗时：{time() - time2}&#39;)</span></pre>
</div>

<p>执行结果也是合理的：</p>

<p><img src="../media/image/2022/01/30/image-20220130205211-2.png" style="height:664px; width:900px" /></p>

<h2 style="font-style:italic"><strong>问题10：python中几种容器类型的差别及使用场景有哪些？</strong></h2>

<p>答：说实话，我在看到这个问题的时候，我都不知道python的容器是什么???，但是我可能用过，而且非常常用，于是c站上一搜，我自己都要笑了?</p>

<p><img src="../media/image/2022/01/30/image-20220130205753-3.png" style="height:468px; width:700px" /></p>

<p>大致看到了几个关键词，我就知道了，不就是经常使用的列表list，元组tuple，字典dict，集合set吗?看来还是自己脑回路有点长，转不过弯来，虽然之前没有见过容器的定义，但是顾名思义：容器不就是可以容纳东西的器具吗？在想想list，tuple，dict，set它们的功能不就是来容纳东西/数据的吗？？我真是醉鸟哈哈哈哈</p>

<p>言归正传：</p>

<p>所以python中有4中容器，分别是list，tuple，dict，set</p>

<table align="left" border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<tbody>
		<tr>
			<td>容器</td>
			<td>使用场景</td>
			<td>差别</td>
		</tr>
		<tr>
			<td>list</td>
			<td>一般用于具有相同属性的元素的存储和修改</td>
			<td>可任意修改容器中的元素</td>
		</tr>
		<tr>
			<td>tuple</td>
			<td>一般用于具有相同属性的元素的存储（仅能存储）</td>
			<td>值存入后不能修改</td>
		</tr>
		<tr>
			<td>dict</td>
			<td>一般高效访问和存储</td>
			<td>key-value存储</td>
		</tr>
		<tr>
			<td>set</td>
			<td>一般用于去重</td>
			<td>取值是随机的</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>上面的使用场景和用法是根据我个人经验写的，或多或少可能会有出入，更多用法参考：<a href="https://blog.csdn.net/nicejw/article/details/100811422?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164354728816780265479933%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=164354728816780265479933&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-100811422.pc_search_insert_ulrmf&amp;utm_term=python%E4%B8%AD%E7%9A%84%E5%AE%B9%E5%99%A8&amp;spm=1018.2226.3001.4187">python中的四种容器</a>&nbsp;，他总结的还挺详细的???&nbsp;</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题11：列表推导式的使用和场景有哪些？</strong></h2>

<p>答：首先看一下列表推导式有哪些吧：我抠破了投，好像只想到了一个：[i for i in range(100)]，这种格式的?</p>

<p>然后查看了我之前总结的一篇：<a href="http://www.lll.plus/learningPlanet/459">python中的一些进阶语法</a>&nbsp;，好像确实也只有这一个，其他的是配合if，else使用的</p>

<p>使用场景的话，我感觉就是在一个列表中进行循环，没有复杂的逻辑，只是对列表中的元素进行简单的操作，这时候可以使用列表推导式（或者在需要生成一个列表的时候，列表中的元素有一定的顾虑也可以使用），使用列表推导式的考出就是可以节省代码空间！</p>

<p><img src="../media/image/2022/01/30/image-20220130213330-5.png" style="height:427px; width:1356px" /></p>

<h2 style="font-style:italic"><strong>问题12：介绍一下yield的用法。</strong></h2>

<p>答：说实话，这个东西我好像没怎么用过，除了在学习的时候了解过一下，在上一个问题提到的一篇博客我中记录了一些关于它的用法的，如下总结：</p>

<p><img src="../media/image/2022/01/30/image-20220130213211-4.png" style="height:717px; width:789px" /></p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题13：常用的内置库有哪些？举例说明它们的用法。</strong></h2>

<p><strong>答：内置库的话，我清一清：os，csv，queue，time，threading，re，额，我常用的好像就这些?</strong></p>

<table border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<tbody>
		<tr>
			<td>内置库</td>
			<td>用法</td>
		</tr>
		<tr>
			<td>os</td>
			<td>这个库我一般用于文件操作，os.path,os.system用的还比较多</td>
		</tr>
		<tr>
			<td>csv</td>
			<td>操作csv文件，特别好用</td>
		</tr>
		<tr>
			<td>queue</td>
			<td>队列</td>
		</tr>
		<tr>
			<td>time</td>
			<td>和时间有关的操作</td>
		</tr>
		<tr>
			<td>threading</td>
			<td>多线程，一般结合爬虫使用</td>
		</tr>
		<tr>
			<td>re</td>
			<td>正则，用于匹配，使用场景感觉还是非常广泛的</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题14：介绍一下你了解的magic method（魔法方法）及其作用。</strong></h2>

<p>答：这个东东在我脑海里好像已经一点印象都没有了，不知道是不是压根没有学过的缘故?，我唯一有点印象的好像就是那个<a href="https://baike.baidu.com/item/%E9%AD%94%E6%96%B9%E7%9F%A9%E9%98%B5/6532651?fr=aladdin">魔方矩阵</a>，在matlab里见过，不过应该和这个半点关系都没有，只是都有一个&lsquo;魔&rsquo;字而已。</p>

<p>问问度娘吧：首先得知道什么是<a href="https://blog.csdn.net/weixin_37972723/article/details/80725738?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164355067116780357297248%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=164355067116780357297248&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_ulrmf~default-2-80725738.pc_search_insert_ulrmf&amp;utm_term=%E9%AD%94%E6%B3%95%E6%96%B9%E6%B3%95&amp;spm=1018.2226.3001.4187">魔法方法</a>&nbsp;</p>

<p><img src="../media/image/2022/01/30/image-20220130215706-6.png" style="height:331px; width:964px" /></p>

<p>哦哦，原来这个东东就是魔法方法，为啥这么多东西我都用过，但是不知其名?<img src="../media/image/2022/01/30/image-20220130220042-8.gif" style="height:300px; width:300px" /></p>

<p>我经常使用的也好像不多，好像就只有__init__用于初始化，其他在学习中可能用到过，但现在基本都忘记了，唉?看来还是得多巩固巩固基础！</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题15：解释一下面向对象的概念及其在编程中的作用。</strong></h2>

<p>答：python中的一个概念就是：一切皆对象。<a href="https://blog.csdn.net/zzd864582451/article/details/85335748?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164370437316780261955902%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=164370437316780261955902&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-85335748.pc_search_insert_ulrmf&amp;utm_term=%E4%BB%80%E4%B9%88%E6%98%AF%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1&amp;spm=1018.2226.3001.4187">面向对象</a>的概念就是把具有相同属性或者方法的函数/功能归为一类。（个人理解是这样的）它是一种编程思想，相比于过程化编程，它显得结构更加清晰，逻辑更加分明，最明显的作用就是可以通过继承减少代码重写，同时也可以通过多态丰富功能，对于实现复杂的功能，它能将功能模块化，将复杂的功能拆分成一小块的，使开发变得更加轻松！</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题16：如何实现单例模式？</strong></h2>

<p>答：首先得搞清楚什么是单例模式？百度得：<strong>单例模式是指确保一个类在任何情况下都绝对只有一个实例，并提供一个全局访问点。参考：</strong><a href="https://blog.csdn.net/xiaofeng10330111/article/details/105652399?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164370474816780269871803%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=164370474816780269871803&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_ulrmf~default-15-105652399.pc_search_insert_ulrmf&amp;utm_term=%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F&amp;spm=1018.2226.3001.4187">单例模式的使用总结</a></p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff"># 单例模式
&#39;&#39;&#39;
要点：
1.该类只能有一个实例
2.它必须自行创建这个实例
3.它必须自行向整个系统提供整个实例

&#39;&#39;&#39;
import threading


class SingleSimple:
    lock_ = threading.Lock()

    def __new__(cls, *args, **kwargs):

        if not hasattr(SingleSimple, &#39;instance_&#39;):
            with SingleSimple.lock_:  # 开锁--关锁
                if not hasattr(SingleSimple, &#39;instance_&#39;):
                    SingleSimple.instance_ = super(SingleSimple, cls).__new__(cls, *args, **kwargs)

        return SingleSimple.instance_

def test(number):
    s = SingleSimple()
    print(f&#39;{number}:{id(s)}&#39;)


if __name__ == &#39;__main__&#39;:
    for i in range(10):
        t = threading.Thread(target=test, args=(i,))
        t.start()</span>
</pre>
</div>

<p><img src="../media/image/2022/02/01/image-20220201173758-3.png" style="height:708px; width:900px" /></p>

<h2 style="font-style:italic"><strong>问题17：如何对python对象进行<a href="https://blog.csdn.net/tree_ifconfig/article/details/82766587?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164370812016781683973771%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=164370812016781683973771&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_ulrmf~default-2-82766587.pc_search_insert_ulrmf&amp;utm_term=%E5%BA%8F%E5%88%97%E5%8C%96&amp;spm=1018.2226.3001.4187">序列化</a>？</strong></h2>

<p>答：使用内置库pickle进行对象序列化和反序列化。</p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff">import pickle</span>

<span style="color:#ffffff">class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#序列化
with open(&#39;demo&#39;, &#39;wb&#39;) as f:
    
    #name:Tom age:1
    cat = Cat(&#39;Tom&#39;, 1)
    pickle.dump(cat, f)

with open(&#39;demo&#39;, &#39;rb&#39;) as f:

    #反序列化 将数据从文件中读取出来 并还原到其原本的数据类型
    while True:
        try:
            cat=pickle.load(f)
            print(f&#39;name:{cat.name} age:{cat.age}&#39;)
        except:
            break
</span></pre>
</div>

<p><img src="../media/image/2022/02/01/image-20220201173657-1.png" style="height:380px; width:900px" /></p>

<h2 style="font-style:italic"><strong>问题18：是否熟练编写多线程和多进程程序？</strong></h2>

<p>答：还行，对线程比较属性，一般没有用到过进程，不过两个的用法都大致差不多。</p>

<p><img src="../media/image/2022/02/01/image-20220201184008-4.png" style="height:703px; width:880px" /></p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题19：使用socket编写一个简单的http服务器，成功返回success即可。</strong></h2>

<p>答：</p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff">from socket import AF_INET, SOCK_STREAM, socket

HOST = &#39;127.0.0.1&#39;  # HSOT变量是空白的，这是对bind()方法的标识，标识它可以使用任何可用的地址
PORT = 80
BUFSIZ = 1024  # 将缓冲区的大小设置为1kb
ADDR = (HOST, PORT)  # 服务器地址

# 创建TCP服务器套接字
tcpserSocket = socket(AF_INET, SOCK_STREAM)
tcpserSocket.bind(ADDR)  # 绑定服务器地址
tcpserSocket.listen(5)  # 开启监听 listen()方法的参数是在连接被被转接或拒绝之前，传入请求的最大数
while True:
    print(&#39;waiting for connect....&#39;)
    tcpCliSock, addr = tcpserSocket.accept() #接受客户端的连接(若连接成功，返回客户端对象和其地址)
    print(&#39;...connected from:&#39;, addr) #客户端的地址信息
    while True:
        data = tcpCliSock.recv(BUFSIZ) #最大接收1kb大小的数据
        # if not data: #如果客户端发送过来的数据为空着退出循环，关闭连接(在这之前已经与客户端连接成功,但服务器未关闭，任处于服务状态)
        #     break
        print(&#39;(客户端):&#39;,(data.decode(&#39;utf-8&#39;))) #打印来自客户端的消息
        data=&#39;success&#39;
        tcpCliSock.send(&#39;{}&#39;.format(data).encode(&#39;utf-8&#39;))
    tcpCliSock.close()
tcpserSocket.close()</span>
</pre>
</div>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题20：如何理解python中的GIL？这对我们的日常开发有什么影响？</strong></h2>

<p><strong>答：</strong><a href="http://cenalulu.github.io/python/gil-in-python/">Python的GIL是什么鬼，多线程性能究竟如何</a>&nbsp;我好像是第一次接触到这个词，看了一下这篇博客，GIL是一把全局排他锁，主要就是为了解决多线程的问题。</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>问题21：解释一下协程，线程和进程之间的差别。</strong></h2>

<p>答：进程：&emsp;进程，直观点说，保存在硬盘上的程序运行以后，会在内存空间里形成一个独立的内存体，这个内存体有自己独立的地址空间，有自己的堆，上级挂靠单位是操作系统。操作系统会以进程为单位，分配系统资源（CPU时间片、内存等资源），进程是资源分配的最小单位。&emsp;进程，直观点说，保存在硬盘上的程序运行以后，会在内存空间里形成一个独立的内存体，这个内存体有自己独立的地址空间，有自己的堆，上级挂靠单位是操作系统。操作系统会以进程为单位，分配系统资源（CPU时间片、内存等资源），进程是资源分配的最小单位。</p>

<p>线程：线程，有时被称为轻量级进程(Lightweight Process，LWP），是操作系统调度（CPU调度）执行的最小单位。</p>

<p>协程：&emsp;协程，是一种比线程更加轻量级的存在，协程不是被操作系统内核所管理，而完全是由程序所控制（也就是在用户态执行）。这样带来的好处就是性能得到了很大的提升，不会像线程切换那样消耗资源。</p>

<p>参考：<a href="https://blog.csdn.net/daaikuaichuan/article/details/82951084?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164371608916780274160080%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&amp;request_id=164371608916780274160080&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-82951084.pc_search_insert_ulrmf&amp;utm_term=%E5%8D%8F%E7%A8%8B%EF%BC%8C%E7%BA%BF%E7%A8%8B%E5%92%8C%E8%BF%9B%E7%A8%8B%E4%B9%8B%E9%97%B4%E7%9A%84%E5%B7%AE%E5%88%AB&amp;spm=1018.2226.3001.4187">进程、线程和协程之间的区别和联系</a></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>python基础的清单算是完成了，大部分的都有所了解，但是有一些偏于底层的可能不是很清楚，但通过查阅一些博客，文章参考等之后都有所收获！</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

