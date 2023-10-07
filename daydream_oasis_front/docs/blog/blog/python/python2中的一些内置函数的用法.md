
<BlogInfo title="python2中的一些内置函数的用法" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=950 category="python" tag_list="[]" create_time="2022.10.08 17:54:00.761892" update_time="2022.10.14 16:04:34" />

^^^^^^^^^
<p>&nbsp;</p>

<pre data-widget="codeSnippet">
<code class="language-python hljs"><span class="hljs-comment"># coding:utf8</span>

<span class="hljs-comment"># 1.abs(x) 求一个数的绝对值</span>
<span class="hljs-string">&quot;&quot;&quot;Return the absolute value of a number. The argument may be a plain or long integer or a floating point number. If the argument is a complex number, its magnitude is returned.&quot;&quot;&quot;</span>

<span class="hljs-keyword">from</span> ast <span class="hljs-keyword">import</span> operator
<span class="hljs-keyword">from</span> curses <span class="hljs-keyword">import</span> raw
<span class="hljs-keyword">from</span> filecmp <span class="hljs-keyword">import</span> cmp
<span class="hljs-keyword">from</span> imp <span class="hljs-keyword">import</span> reload
<span class="hljs-keyword">import</span> imp
<span class="hljs-keyword">from</span> re <span class="hljs-keyword">import</span> X
<span class="hljs-keyword">from</span> telnetlib <span class="hljs-keyword">import</span> DO
<span class="hljs-keyword">from</span> turtle <span class="hljs-keyword">import</span> setx


a = -<span class="hljs-number">10</span>**<span class="hljs-number">10</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">abs</span>(a))

<span class="hljs-comment"># 2.all(iterable)  只有全部为True才返回True，否则返回Flase</span>
<span class="hljs-string">&quot;&quot;&quot;
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
底层实现
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
&quot;&quot;&quot;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">all</span>([<span class="hljs-number">1</span>, <span class="hljs-number">0</span>, <span class="hljs-number">23</span>, <span class="hljs-number">233</span>, <span class="hljs-literal">False</span>]))  <span class="hljs-comment"># Flase</span>

<span class="hljs-comment"># 3.any(iterable)    只要有一个为True就返回Ture，否则返回False</span>
<span class="hljs-string">&quot;&quot;&quot;
Return True if any element of the iterable is true. If the iterable is empty, return False. 
底层实现
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
&quot;&quot;&quot;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">any</span>([<span class="hljs-number">12</span>, <span class="hljs-number">0</span>, <span class="hljs-number">23</span>, <span class="hljs-string">&#39;&#39;</span>, <span class="hljs-string">&#39;awefaw&#39;</span>]))  <span class="hljs-comment"># True</span>

<span class="hljs-comment"># 4.basestring() str和unicode的超类,是一个抽象类型，不能调用和实例化对象 可以用于检测</span>
<span class="hljs-comment"># 一个对象是不是str或者unicode的实例</span>
<span class="hljs-string">&quot;&quot;&quot;This abstract type is the superclass for str and unicode. It cannot be called or instantiated, but it can be used to test whether an object is an instance of str or unicode. isinstance(obj, basestring) is equivalent to isinstance(obj, (str, unicode)).&quot;&quot;&quot;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">isinstance</span>(<span class="hljs-string">&quot;hello world&quot;</span>, basestring))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">isinstance</span>(<span class="hljs-number">1111</span>, basestring))

<span class="hljs-comment"># 5.bin(x) 返回一个数的二进制 如果x不是一个int对象，那么它必须定义__index__()方法来返回一个整数</span>
<span class="hljs-string">&quot;&quot;&quot;Convert an integer number to a binary string. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer.&quot;&quot;&quot;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">bin</span>(<span class="hljs-number">10</span>))


<span class="hljs-keyword">class</span> <span class="class_ hljs-title">MyInt</span>:
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__index__</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">id</span>(self)


<span class="hljs-built_in">print</span>(<span class="hljs-built_in">bin</span>(MyInt()))

<span class="hljs-comment"># 6.bool() 返回一个值对应的布尔值 bool也是一个类，它是int的一个子类，但是它不能用来实例化对象，它的对象只有Ture和False</span>
<span class="hljs-string">&quot;&quot;&quot;Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise it returns True. bool is also a class, which is a subclass of int. Class bool cannot be subclassed further. Its only instances are False and True.&quot;&quot;&quot;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">bool</span>(<span class="hljs-string">&quot;123&quot;</span>))

<span class="hljs-comment"># 7.bytearray()  返回一个字节数组</span>
arr_li = <span class="hljs-built_in">bytearray</span>(<span class="hljs-string">&quot;hello world你好&quot;</span>)
<span class="hljs-built_in">print</span>(arr_li)
<span class="hljs-built_in">print</span>(arr_li[<span class="hljs-number">0</span>])
str_u = <span class="hljs-string">u&#39;你好，world&#39;</span>  <span class="hljs-comment"># unicode</span>
str_u_byte = <span class="hljs-built_in">bytearray</span>(str_u, encoding=<span class="hljs-string">&#39;utf8&#39;</span>)
<span class="hljs-built_in">print</span>(str_u.encode(<span class="hljs-string">&#39;utf8&#39;</span>))
<span class="hljs-built_in">print</span>(str_u_byte.decode(<span class="hljs-string">&#39;utf8&#39;</span>))
<span class="hljs-built_in">print</span>(str_u)

<span class="hljs-comment"># 8.callable(obj) 判断一个对象是否是可调用的</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">callable</span>(<span class="hljs-number">1</span>))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">callable</span>(<span class="hljs-string">&quot;123&quot;</span>))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">callable</span>(<span class="hljs-built_in">list</span>))

<span class="hljs-comment"># 9.chr(i) 将码值(0～255的ASCII码值)转成码符</span>
<span class="hljs-string">&quot;&quot;&quot;Return a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string &#39;a&#39;. This is the inverse of ord(). The argument must be in the range [0..255], inclusive; ValueError will be raised if i is outside that range. See also unichr().&quot;&quot;&quot;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">chr</span>(<span class="hljs-number">97</span>))

<span class="hljs-comment"># 10.classmethod(fuc)  将一个函数转成一个类方法</span>
<span class="hljs-string">&quot;&quot;&quot;Return a class method for function.
class C(object):
    @classmethod
    def f(cls, arg1, arg2, ...):
        ...
&quot;&quot;&quot;</span>


<span class="hljs-comment"># 10.cmp(x,y) 丢弃</span>

<span class="hljs-comment"># 11.compile 将一个字符串编译为字节代码</span>
<span class="hljs-string">&#39;&#39;&#39;
compile(source, filename, mode[, flags[, dont_inherit]])
    source -- 字符串或者AST（Abstract Syntax Trees）对象。。
    filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
    mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
    flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
    flags和dont_inherit是用来控制编译源码时的标志

&#39;&#39;&#39;</span>
c = <span class="hljs-built_in">compile</span>(<span class="hljs-string">&#39;for i in range(10):print(i)&#39;</span>, <span class="hljs-string">&#39;&#39;</span>, <span class="hljs-string">&#39;exec&#39;</span>)
<span class="hljs-built_in">print</span>(c)
<span class="hljs-built_in">exec</span>(c)
<span class="hljs-built_in">eval</span>(c)

<span class="hljs-comment"># 12.complex()  返回一个复数对象</span>
<span class="hljs-string">&#39;&#39;&#39;class complex([real[, imag]])
Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the function serves as a numeric conversion function like int(), long() and float(). If both arguments are omitted, returns 0j.&#39;&#39;&#39;</span>
c = <span class="hljs-built_in">complex</span>(<span class="hljs-string">&quot;10+1j&quot;</span>)
c = <span class="hljs-built_in">complex</span>(<span class="hljs-number">10</span>, <span class="hljs-number">5</span>)  <span class="hljs-comment"># real,imag</span>
<span class="hljs-built_in">print</span>(c, c.real, c.imag)

<span class="hljs-comment"># 13.delattr(obj,name) 删除对象obj的属性name 等价于 del obj.name</span>


<span class="hljs-keyword">class</span> <span class="class_ hljs-title">A</span>:
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self</span>):
        self.name = <span class="hljs-string">&quot;hello&quot;</span>


a = A()
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">getattr</span>(a, <span class="hljs-string">&#39;name&#39;</span>))
<span class="hljs-built_in">print</span>(a.__dict__)
<span class="hljs-built_in">delattr</span>(a, <span class="hljs-string">&#39;name&#39;</span>)
<span class="hljs-built_in">print</span>(a.__dict__)

<span class="hljs-comment"># 14.dict(**kwarg) 创建一个字典</span>
d = <span class="hljs-built_in">dict</span>(a=<span class="hljs-string">&quot;a&quot;</span>, b=<span class="hljs-string">&quot;b&quot;</span>, c=<span class="hljs-string">&quot;c&quot;</span>)
<span class="hljs-built_in">print</span>(d)


<span class="hljs-comment"># 15.dir([obj]) 不带参数返回本地作用域名称列表，如果有一个参数，尝试返回该对象的有效属性</span>
<span class="hljs-string">&#39;&#39;&#39;Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">dir</span>(a))


<span class="hljs-comment"># 16.divmod(a,b) 返回aheb的商和余数</span>
<span class="hljs-string">&#39;&#39;&#39;Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using long division. With mixed operand types, the rules for binary arithmetic operators apply. For plain and long integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 &lt;= abs(a % b) &lt; abs(b).&#39;&#39;&#39;</span>
res = <span class="hljs-built_in">divmod</span>(<span class="hljs-number">4.3</span>, <span class="hljs-number">2.32</span>)
<span class="hljs-built_in">print</span>(res)


<span class="hljs-comment"># 17.enumerate(sequence,start=0) 返回一个枚举对象</span>
<span class="hljs-string">&#39;&#39;&#39;Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration. The next() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over sequence:&#39;&#39;&#39;</span>
seq = [<span class="hljs-string">&#39;h&#39;</span>, <span class="hljs-string">&#39;e&#39;</span>, <span class="hljs-string">&#39;l&#39;</span>, <span class="hljs-string">&#39;l&#39;</span>, <span class="hljs-string">&#39;o&#39;</span>]
e = <span class="hljs-built_in">enumerate</span>(seq, start=<span class="hljs-number">1</span>)
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">list</span>(e))

<span class="hljs-comment"># 18.eval()传入一个表达式，返回表达式的值</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">eval</span>(<span class="hljs-string">&#39;1*6+3-2&#39;</span>))

<span class="hljs-comment"># 19.execfile(filename,[globals,[locals]])   python3已移除</span>
<span class="hljs-string">&#39;&#39;&#39;This function is similar to the exec statement, but parses a file instead of a string.&#39;&#39;&#39;</span>
<span class="hljs-comment"># execfile(&#39;lll01_内置函数.py&#39;)</span>
<span class="hljs-comment"># execfile(&#39;demo.py&#39;)</span>


<span class="hljs-comment"># 20.file 构造函数 已丢弃</span>


<span class="hljs-comment"># 21.filter(func,iterable) 过滤器，迭代iterable中的每一个值，将它们传给func，如果返回True就保留</span>
<span class="hljs-string">&#39;&#39;&#39;Construct a list from those elements of iterable for which function returns true.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">filter</span>(<span class="hljs-keyword">lambda</span> a: a % <span class="hljs-number">2</span>, <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>)))  <span class="hljs-comment"># 获取10以内的奇数</span>


<span class="hljs-comment"># 22.float(x) 将一个数或则字符串x转成一个浮点数</span>
<span class="hljs-string">&#39;&#39;&#39;Return a floating point number constructed from a number or string x.

If the argument is a string, it must contain a possibly signed decimal or floating point number, possibly embedded in whitespace. The argument may also be [+|-]nan or [+|-]inf. Otherwise, the argument may be a plain or long integer or a floating point number, and a floating point number with the same value (within Python&rsquo;s floating point precision) is returned. If no argument is given, returns 0.0.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">float</span>(<span class="hljs-number">1</span>))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">float</span>(<span class="hljs-string">&#39;1212&#39;</span>))


<span class="hljs-comment"># 23.format(value,[format_spec]) 字符串格式化</span>
s = <span class="hljs-string">&#39;hello,{}&#39;</span>.<span class="hljs-built_in">format</span>(<span class="hljs-string">&#39;Tom&#39;</span>)
<span class="hljs-built_in">print</span>(s)

<span class="hljs-comment"># 24.frozenset([iterable]) 返回一个frozenset（不可变集合）</span>
<span class="hljs-string">&#39;&#39;&#39;Return a new frozenset object, optionally with elements taken from iterable.&#39;&#39;&#39;</span>
fs = <span class="hljs-built_in">frozenset</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>))
<span class="hljs-built_in">print</span>(fs)
<span class="hljs-built_in">print</span>(<span class="hljs-number">1</span> <span class="hljs-keyword">in</span> fs)


<span class="hljs-comment"># 25.getattr(obj,name) 获取对象obj的属性name的值</span>
<span class="hljs-string">&#39;&#39;&#39;Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object&rsquo;s attributes, the result is the value of that attribute. For example, getattr(x, &#39;foobar&#39;) is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.&#39;&#39;&#39;</span>
a = A()
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">getattr</span>(a, <span class="hljs-string">&#39;name&#39;</span>))


<span class="hljs-comment"># 26.globals()  返回当前全局符号表</span>
<span class="hljs-string">&#39;&#39;&#39;Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">globals</span>())


<span class="hljs-comment"># 27.hasattr(obj,name) 判断对象obj是否有属性name</span>
<span class="hljs-string">&#39;&#39;&#39;The arguments are an object and a string. The result is True if the string is the name of one of the object&rsquo;s attributes, False if not.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">hasattr</span>(a, <span class="hljs-string">&#39;age&#39;</span>))


<span class="hljs-comment"># 28.hash(obj) 返回对象obj的hash值 数值（值相等，但类型不同）的hash值是相等的</span>
<span class="hljs-string">&#39;&#39;&#39;Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">hash</span>(a))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">hash</span>(<span class="hljs-number">111</span>) == <span class="hljs-built_in">hash</span>(<span class="hljs-number">111.000000</span>))

<span class="hljs-comment"># 29.help(obj)  交互式的返回obj的相关帮组文档</span>
<span class="hljs-string">&#39;&#39;&#39;If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. &#39;&#39;&#39;</span>
<span class="hljs-comment"># help(a)</span>


<span class="hljs-comment"># 30.hex(x) 将一个整数转成一个16进制的数</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">hex</span>(<span class="hljs-number">12</span>))


<span class="hljs-comment"># 31.id(obj) 返回对象obj的&rdquo;唯一标识&ldquo;</span>
<span class="hljs-string">&#39;&#39;&#39;Return the &ldquo;identity&rdquo; of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.&#39;&#39;&#39;</span>
<span class="hljs-comment"># CPython implementation detail: This is the address of the object in memory. --- 在cpython解释器中，这里对应的是对象的内存地址</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">id</span>(<span class="hljs-string">&quot;hello&quot;</span>))


<span class="hljs-comment"># 32.input(prompt) 输入</span>
<span class="hljs-comment"># input(&#39;请输入你的选择：&#39;)</span>


<span class="hljs-comment"># 33.int(x=0)  将x转成一个int对象</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">int</span>(<span class="hljs-number">1111</span>))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">int</span>(<span class="hljs-string">&#39;1111&#39;</span>))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">int</span>(<span class="hljs-number">123.45</span>))


<span class="hljs-comment"># 34.int(x,base=10) x必须为一个字符串或unicode对象 将base进制的数转成对应的10进制数</span>
<span class="hljs-string">&#39;&#39;&#39;The default base is 10. The allowed values are 0 and 2&ndash;36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O/0, or 0x/0X, as with integer literals in code. Base 0 means to interpret the string exactly as an integer literal, so that the actual base is 2, 8, 10, or 16.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">int</span>(<span class="hljs-string">&#39;1234&#39;</span>, base=<span class="hljs-number">8</span>))

<span class="hljs-comment"># 35.isinstance(obj,classinfo) 判断对象obj是不是classinfo的实例，或者子类的实例</span>
<span class="hljs-string">&#39;&#39;&#39;Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. Also return true if classinfo is a type object (new-style class) and object is an object of that type or of a (direct, indirect or virtual) subclass thereof. If object is not a class instance or an object of the given type, the function always returns false. If classinfo is a tuple of class or type objects (or recursively, other such tuples), return true if object is an instance of any of the classes or types. If classinfo is not a class, type, or tuple of classes, types, and such tuples, a TypeError exception is raised.&#39;&#39;&#39;</span>


<span class="hljs-keyword">class</span> <span class="class_ hljs-title">B</span>(<span class="class_ hljs-title inherited__">A</span>):
    <span class="hljs-keyword">pass</span>


b = B()
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">isinstance</span>(b, A))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">isinstance</span>(b, B))

<span class="hljs-comment"># 36.iter(o,[sentinel]) 如果没有第二个参数，o必须为可迭代对象； 如果有第二个参数，o必须是一个可调用的对象 通过o不断产出值，如果值等于sentinel就停止</span>
<span class="hljs-string">&#39;&#39;&#39;
Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, o must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then o must be a callable object. The iterator created in this case will call o with no arguments for each call to its next() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.

&#39;&#39;&#39;</span>

<span class="hljs-comment"># 一行一行的读取文件内容</span>
<span class="hljs-keyword">with</span> <span class="hljs-built_in">open</span>(<span class="hljs-string">&#39;demo.py&#39;</span>) <span class="hljs-keyword">as</span> fp:
    <span class="hljs-keyword">for</span> line <span class="hljs-keyword">in</span> <span class="hljs-built_in">iter</span>(fp.readline, <span class="hljs-string">&#39;&#39;</span>):  <span class="hljs-comment"># 遇到空字符串就说明读取完了</span>
        <span class="hljs-built_in">print</span>(line)


<span class="hljs-comment"># 37.len(obj) 返回对象obj的长度</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">len</span>(<span class="hljs-string">&quot;hello world!&quot;</span>))


<span class="hljs-comment"># 38.list(iterable) 将可迭代对象转成列表</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">list</span>(<span class="hljs-string">&#39;hello world!&#39;</span>))

<span class="hljs-comment"># 39.locals() 返回当当前局部标识符表 只能在函数中被调用 对它的修改是不起作用的</span>
<span class="hljs-string">&#39;&#39;&#39;Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks.  The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter.&#39;&#39;&#39;</span>


<span class="hljs-keyword">def</span> <span class="function_ hljs-title">fun</span>():
    a = <span class="hljs-number">1</span>
    b = <span class="hljs-string">&#39;2&#39;</span>
    <span class="hljs-built_in">print</span>(<span class="hljs-built_in">locals</span>())
    <span class="hljs-built_in">locals</span>()[<span class="hljs-string">&#39;a&#39;</span>] = <span class="hljs-number">111</span>  <span class="hljs-comment"># 修改无效</span>
    <span class="hljs-built_in">print</span>(<span class="hljs-built_in">locals</span>())


fun()


<span class="hljs-comment"># 40.long() python3丢弃</span>

<span class="hljs-comment"># 41.map(func,iterable,...) 将func作用到iterable的每一个元素中，并将返回结果以列表的形式返回</span>
<span class="hljs-string">&#39;&#39;&#39;Apply function to every item of iterable and return a list of the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. If one iterable is shorter than another it is assumed to be extended with None items. If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). The iterable arguments may be a sequence or any iterable object; the result is always a list.&#39;&#39;&#39;</span>
res = <span class="hljs-built_in">map</span>(<span class="hljs-keyword">lambda</span> *a: <span class="hljs-built_in">sum</span>(a), [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>])  <span class="hljs-comment"># 求序列对应位置的和</span>
<span class="hljs-built_in">print</span>(res)
res = <span class="hljs-built_in">map</span>(<span class="hljs-keyword">lambda</span> *a: <span class="hljs-built_in">sum</span>(a), [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>], [<span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>])
<span class="hljs-built_in">print</span>(res)


<span class="hljs-comment"># 42.max([*]iterable,[key])  返回最大值 key用于指定比较方法</span>
<span class="hljs-string">&#39;&#39;&#39;Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, iterable must be a non-empty iterable (such as a non-empty string, tuple or list). The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.

The optional key argument specifies a one-argument ordering function like that used for list.sort(). The key argument, if supplied, must be in keyword form (for example, max(a,b,c,key=func)).&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">max</span>({<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, -<span class="hljs-number">23</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">23</span>, <span class="hljs-number">343</span>, -<span class="hljs-number">999</span>}, key=<span class="hljs-built_in">abs</span>))  <span class="hljs-comment"># 按照绝对值比较，返回最大值</span>


<span class="hljs-comment"># 43.memoryview(obj) 将对象obj转成一个memory view对象</span>
s = <span class="hljs-string">&#39;hello world&#39;</span>
mv = <span class="hljs-built_in">memoryview</span>(s)
<span class="hljs-built_in">print</span>(mv)


<span class="hljs-comment"># 44.min([*]iterable,[key])  返回最小值 key用于指定比较方法</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">min</span>({<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, -<span class="hljs-number">23</span>, -<span class="hljs-number">1</span>, <span class="hljs-number">23</span>, <span class="hljs-number">343</span>, -<span class="hljs-number">999</span>}, key=<span class="hljs-built_in">abs</span>))  <span class="hljs-comment"># 按照绝对值比较，返回最小值</span>


<span class="hljs-comment"># 45.next(iterator,[default]) 返回迭代器的下一个值，如果没有就返回default</span>
<span class="hljs-string">&#39;&#39;&#39;Retrieve the next item from the iterator by calling its next() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.&#39;&#39;&#39;</span>
it = (i <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>))  <span class="hljs-comment"># 生成器也是迭代器</span>
<span class="hljs-keyword">while</span> <span class="hljs-literal">True</span>:
    s = <span class="hljs-built_in">next</span>(it, <span class="hljs-number">666</span>)
    <span class="hljs-built_in">print</span>(s)
    <span class="hljs-keyword">if</span> s == <span class="hljs-number">666</span>:
        <span class="hljs-keyword">break</span>


<span class="hljs-comment"># 46.oct(x) 将一个整数转成一个八进制数</span>
<span class="hljs-string">&#39;&#39;&#39;Convert an integer number (of any size) to an octal string. The result is a valid Python expression.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">oct</span>(<span class="hljs-number">100</span>))

<span class="hljs-comment"># 47.open(name[,mode,[buffering]]) 打开文件</span>
<span class="hljs-keyword">with</span> <span class="hljs-built_in">open</span>(<span class="hljs-string">&#39;lll01_内置函数.py&#39;</span>, <span class="hljs-string">&#39;r&#39;</span>) <span class="hljs-keyword">as</span> f:
    <span class="hljs-built_in">print</span>(f.read())


<span class="hljs-comment"># 48.ord(c) 返回一个字符对应的unicode码值</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">ord</span>(<span class="hljs-string">&#39;a&#39;</span>))

<span class="hljs-comment"># 49.pow(x,y[,z]) 返回x**y的值，如果z被传入，返回 (x**y)%z的值</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">pow</span>(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">6</span>))

<span class="hljs-comment"># 50.print(*object,sep=&#39;&#39;,end=&#39;
&#39;,file=sys.stdout) 打印输出</span>
<span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;#hello wolrd!&#39;</span>)


<span class="hljs-comment"># 51.property([fget[, fset[, fdel[, doc]]]]) 特性 常用于修饰限定某一个属性</span>
<span class="hljs-string">&#39;&#39;&#39;
如果没有fset，那么property所修饰的属性就是一个只读变量

&#39;&#39;&#39;</span>


<span class="hljs-keyword">class</span> <span class="class_ hljs-title">A</span>:

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__init__</span>(<span class="hljs-params">self</span>):
        self.x = <span class="hljs-literal">None</span>

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">setx</span>(<span class="hljs-params">self, x</span>):
        self.x = x

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">getx</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> self.x

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">delx</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">del</span> self.x

    x = <span class="hljs-built_in">property</span>(getx, setx, delx, <span class="hljs-string">&quot;this is a attribte of instance of A.&quot;</span>)


a = A()
a.x = <span class="hljs-number">6666</span>
<span class="hljs-built_in">print</span>(a.x)


<span class="hljs-comment"># 52.range(start,stop[,step]) 返回一个等差数列 start指定开始值，默认为0 stop指定结束值，step指定步长 左闭右开原则</span>
aaa = <span class="hljs-built_in">range</span>(<span class="hljs-number">1</span>, <span class="hljs-number">10</span>, <span class="hljs-number">2</span>)
<span class="hljs-built_in">print</span>(aaa)

<span class="hljs-comment"># 53.raw_input([prompt]) 读入一行内容</span>
<span class="hljs-comment"># s=raw_input(&#39;---&gt;&#39;)</span>
<span class="hljs-comment"># print(s)</span>


<span class="hljs-comment"># 54.reduce(function,iterable[,intializer]) 累积操作，将多个值最终变成一个值</span>
<span class="hljs-string">&#39;&#39;&#39;Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned. Roughly equivalent to:

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError(&#39;reduce() of empty sequence with no initial value&#39;)
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value&#39;&#39;&#39;</span>
<span class="hljs-comment"># 求1到100的和</span>
<span class="hljs-built_in">print</span>(reduce(<span class="hljs-keyword">lambda</span> a, b: a+b, <span class="hljs-built_in">range</span>(<span class="hljs-number">1</span>, <span class="hljs-number">101</span>)))


<span class="hljs-comment"># 55.reload(module) 重新加载一个模块 一般用于版本兼容</span>
<span class="hljs-string">&#39;&#39;&#39;Reload a previously imported module. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (the same as the module argument).&#39;&#39;&#39;</span>
<span class="hljs-keyword">try</span>:
    <span class="hljs-keyword">import</span> csv
<span class="hljs-keyword">except</span>:
    reload(csv)


<span class="hljs-comment"># 56.repr(object) 返回一个对象的&ldquo;描绘&rdquo;  可用于打印显示对象的相关信息</span>
<span class="hljs-string">&#39;&#39;&#39;Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">repr</span>(A()))

<span class="hljs-comment"># 57.reversed(seq) 翻转序列seq,并以迭代器的形式返回</span>
<span class="hljs-string">&#39;&#39;&#39;Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).&#39;&#39;&#39;</span>
a = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
b = <span class="hljs-built_in">reversed</span>(a)
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">id</span>(a), a)
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">id</span>(b), b)


<span class="hljs-comment"># 58.round(number[, ndigits]) 四舍五入 ndigits表示保留的小数位</span>
<span class="hljs-string">&#39;&#39;&#39;Return the floating point value number rounded to ndigits digits after the decimal point. If ndigits is omitted, it defaults to zero. The result is a floating point number. Values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done away from 0 (so, for example, round(0.5) is 1.0 and round(-0.5) is -1.0).&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">round</span>(<span class="hljs-number">10.2323434</span>, <span class="hljs-number">2</span>))
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">round</span>(-<span class="hljs-number">7.232323723223232</span>, <span class="hljs-number">5</span>))


<span class="hljs-comment"># 59.class set([iterable]) 从iterable中获取元素，将其转成一个集合</span>
<span class="hljs-string">&#39;&#39;&#39;Return a new set object, optionally with elements taken from iterable. set is a built-in class. See set and Set Types &mdash; set, frozenset for documentation about this class.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">set</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>)))


<span class="hljs-comment"># 60.setattr(object, name, value) 给对象object设置属性name的值为value（如果object本身没有这个属性，就是新增属性并赋值）</span>
<span class="hljs-string">&#39;&#39;&#39;This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, &#39;foobar&#39;, 123) is equivalent to x.foobar = 123.&#39;&#39;&#39;</span>
a = A()
<span class="hljs-built_in">setattr</span>(a, <span class="hljs-string">&#39;x&#39;</span>, <span class="hljs-number">6666</span>)
<span class="hljs-built_in">print</span>(a.x)


<span class="hljs-comment"># 61.class slice(start, stop[, step]) 返回一个切片对象</span>
<span class="hljs-string">&#39;&#39;&#39;Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.&#39;&#39;&#39;</span>
a = <span class="hljs-built_in">list</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>))
a_slice = <span class="hljs-built_in">slice</span>(<span class="hljs-number">0</span>, <span class="hljs-number">9</span>, <span class="hljs-number">3</span>)  <span class="hljs-comment"># 索引范围：[0,9) a步长为3进行取值</span>
<span class="hljs-built_in">print</span>(a[<span class="hljs-number">0</span>:<span class="hljs-number">9</span>:<span class="hljs-number">3</span>])
<span class="hljs-built_in">print</span>(a[a_slice])


<span class="hljs-comment"># 62.sorted(iterable[, cmp[, key[, reverse]]]) 对iterable中的元素进行排序，并以列表的形式返回 cmp指定排序规则，key指定排序的参考值，</span>

<span class="hljs-comment"># a=[1,-2,32,4,-999,888]</span>
<span class="hljs-comment"># print(sorted(a,cmp=lambda x,y:cmp(abs(x),abs(y))))</span>


<span class="hljs-comment"># 63.staticmethod(function) 对于不会用到类的属性但需要定义在类里面的方法可以使用它  能够被所属类直接调用，也可以被所属类的实例直接调用</span>
<span class="hljs-string">&#39;&#39;&#39;A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()).

Static methods in Python are similar to those found in Java or C++. Also see classmethod() for a variant that is useful for creating alternate class constructors.&#39;&#39;&#39;</span>


<span class="hljs-keyword">class</span> <span class="class_ hljs-title">B</span>:
<span class="hljs-meta">    @staticmethod</span>
    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">say</span>(): <span class="hljs-built_in">print</span>(<span class="hljs-string">&#39;hello&#39;</span>)

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__str__</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> <span class="hljs-string">&#39;helo str!&#39;</span>

    <span class="hljs-keyword">def</span> <span class="function_ hljs-title">__repr__</span>(<span class="hljs-params">self</span>):
        <span class="hljs-keyword">return</span> <span class="hljs-string">&#39;hello repr!&#39;</span>


B.say()
B().say()


<span class="hljs-comment"># 64.class str(object=&#39;&#39;) 返回调用对应的__str__方法，如果没有定义，就调用__repr__方法，如果都没有调用，就返回obj的描述</span>
<span class="hljs-string">&#39;&#39;&#39;Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable to eval(); its goal is to return a printable string. If no argument is given, returns the empty string, &#39;&#39;.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">str</span>(B()))


<span class="hljs-comment"># 65.sum(iterable[, start]) 求iterable中所有元素之和 start指定初始值，默认为0 即 result=sum(iterable)+start</span>
<span class="hljs-string">&#39;&#39;&#39;Sums start and the items of an iterable from left to right and returns the total. start defaults to 0. The iterable&rsquo;s items are normally numbers, and the start value is not allowed to be a string.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">sum</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>], <span class="hljs-number">1</span>))


<span class="hljs-comment"># 66.class super([type[, object-or-type]]) 用于调用超类中的方法 如果是多继承下，多个超类中有相同的方法名，具体调用哪一个要参考__mro__</span>
<span class="hljs-comment"># class Animal:</span>
<span class="hljs-comment">#     def __init__(self):</span>
<span class="hljs-comment">#         print(&#39;我是一个动物！&#39;)</span>

<span class="hljs-comment"># class Dog(Animal):</span>
<span class="hljs-comment">#     def __init__(self):</span>
<span class="hljs-comment">#         super().__init__(self)</span>
<span class="hljs-comment">#         print(&#39;我是一只狗?！&#39;)</span>

<span class="hljs-comment"># Dog()</span>


<span class="hljs-comment"># 67.tuple([iterable]) 将iterable转成一个元组并返回</span>
<span class="hljs-string">&#39;&#39;&#39;Return a tuple whose items are the same and in the same order as iterable&rsquo;s items. iterable may be a sequence, a container that supports iteration, or an iterator object. If iterable is already a tuple, it is returned unchanged. For instance, tuple(&#39;abc&#39;) returns (&#39;a&#39;, &#39;b&#39;, &#39;c&#39;) and tuple([1, 2, 3]) returns (1, 2, 3). If no argument is given, returns a new empty tuple, ().&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">tuple</span>(<span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>)))


<span class="hljs-comment"># 68.class type(object) 返回object对象的类型</span>
<span class="hljs-string">&#39;&#39;&#39;With one argument, return the type of an object.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">type</span>(<span class="hljs-string">&#39;hello&#39;</span>))


<span class="hljs-comment"># 69.unichr(i) f返回码值i对应的码符</span>
<span class="hljs-string">&#39;&#39;&#39;Return the Unicode string of one character whose Unicode code is the integer i. &#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">chr</span>(<span class="hljs-number">97</span>))


<span class="hljs-comment"># 70.unicode(object=&#39;&#39;) python3已丢弃</span>


<span class="hljs-comment"># 71.vars([object])  返回对象object的所有属性</span>
<span class="hljs-string">&#39;&#39;&#39;Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.&#39;&#39;&#39;</span>
<span class="hljs-built_in">print</span>(<span class="hljs-built_in">vars</span>())


<span class="hljs-comment"># 72.xrange python3已丢弃</span>


<span class="hljs-comment"># 73.zip([iterable, ...]) 并行访问多个iterable中相同位置的元素，并以一个元组的形式返回</span>
<span class="hljs-string">&#39;&#39;&#39;This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple arguments which are all of the same length, zip() is similar to map() with an initial argument of None. With a single sequence argument, it returns a list of 1-tuples. With no arguments, it returns an empty list.&#39;&#39;&#39;</span>
a = <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>)
b = <span class="hljs-built_in">range</span>(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>)
c = <span class="hljs-built_in">range</span>(<span class="hljs-number">20</span>, <span class="hljs-number">30</span>)
<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">zip</span>(a, b, c):
    <span class="hljs-built_in">print</span>(i)
</code></pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

