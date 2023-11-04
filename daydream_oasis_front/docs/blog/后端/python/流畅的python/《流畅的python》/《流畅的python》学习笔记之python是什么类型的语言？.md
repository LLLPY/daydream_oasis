
<BlogInfo id="770" title="《流畅的python》学习笔记之python是什么类型的语言？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="40" category="《流畅的python》" tag_list="['动态', '              强类型', '              解析性']" create_time="2022.04.03 16:32:08.172840" update_time="2022.10.15 20:58:33" />

#  讨论类型时，最好考虑两条不同的坐标线！

## 强类型和弱类型

如果一门语言很少隐式转换类型，说明它是强类型语言。如果经常这么做，说明它是弱类型语言。其中，java，c++和python是强类型语言，php，JavaScript和Perl是弱类型语言。

弱类型JavaScript会进行隐式的类型转换：


```javascript
 console.log(''=='0');
 console.log(0==''); //true
 console.log(0=='0'); //ture
```

![](https://img-blog.csdnimg.cn/7510f2bfbd30421c838e9045c71ddc48.png)

强类型python在相同的比较中则不会进行隐式转换：

```python
print(''=='0')
print(0=='')
print('0'==0)
```

![](..image/2022/04/03/image-20220403163156-1.png)

 因为python不会自动在字符串和数字之间强制转换，所以上述三个比较都是False。

## 静态类型和动态类型

在编译时检查类型的语言是静态类型语言，在运行时检查类型的语言是动态语言。静态语言需要声明类型。因此python是动态语言。


看到这里，小伙伴可能还会想到另一个分类：

### 解释性语言和编译性语言

解释性语言是写的代码不能直接编译成机器码，需要解释器将其翻译成机器语言，并且是一边翻译一边执行。而编译性语言是写的代码可以直接编译成机器语言，相当于直接有现成的。而作为解释性语言的python性能的慢的原因也是如此。


所以，最后总结一下： **Python是强类型动态的解析性语言！**



参考：[php是静态还是动态语言,什么是静态语言和动态语言。史上秒懂的大白话翻译。](https://blog.csdn.net/weixin_42510060/article/details/115758489?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164897391616781685314952%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164897391616781685314952&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-115758489.142^v5^pc_search_insert_es_download,157^v4^control&utm_term=%E9%9D%99%E6%80%81%E8%AF%AD%E8%A8%80%E5%BF%AB%E5%8A%A8%E6%80%81%E8%AF%AD%E8%A8%80%E6%85%A2&spm=1018.2226.3001.4187
"php是静态还是动态语言,什么是静态语言和动态语言。史上秒懂的大白话翻译。")


