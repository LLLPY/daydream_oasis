---

next: false

---



<BlogInfo id="1065" title="从numpy中学习深度拷贝和浅拷贝" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="102" category="杂谈" tag_list="['浅拷贝', '              深拷贝', '              numpy']" create_time="2021.08.19 18:48:35.508160" update_time="2021.08.19 19:56:19" />

前言:
今天在复习numpy的时候,在看那个array和asarray,深拷贝和浅拷贝的时候,总是感觉听得迷迷糊糊的,于是还是自己进行了测试,虽然这个知识点很小,但是用处还是挺多的,就总感觉自己知道这一块的内容,但是如果真在的让我理清这之间的关系,我感觉我可能还是一头雾水,只知其一,不知其二的那种感觉,不过在亲自动手后总算是云雾顿开了!!!

首先看一下百度对深拷贝和浅拷贝的释义:

###  **深拷贝**

深拷贝是指源对象与拷贝对象互相独立，其中任何一个对象的改动都不会对另外一个对象造成影响。

###  **浅拷贝**

拷贝出来的目标对象的指针和源对象的指针指向的内存空间是同一块空间，浅拷贝只是一种简单的拷贝，让几个对象公用一个内存，然而当内存销毁的时候，指向这个内存空间的所有指针需要重新定义，不然会造成野指针错误。**

**简单来说就是:浅拷贝得到的和原有的同根同源,而深拷贝则是另一个新个体!**

下面通过代码进行测试:  
```python
# #1.首先创建一个原始数组a
a = np.array([1, 2, 3, 4, 5, 6])

# 2.分别通过array和asarray拷贝a数组
print('未修改a[0]=10之前:')
b = np.array(a)
c = np.asarray(a)
print('数组a:', a)
print('数组b:', b)
print('数组c:', c)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/faf1d7e989bf431fb1929c23e9c3d673.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70)  
可以看到,在未修改原始数组a之前,数组a,b,c的值是一模一样的

```python
## 3.通过修改原数组a来看数组b和c的变化,以及通过修改数组b和c来看原数组a的变化

# 3.1.修改原数组(将数组a的第一个值由1改为10)
a[0] = 10
print('在修改a[0]=10后:')
print('原数组a:', a)
print('通过array拷贝数组a得到的数组b:', b)
print('通过asarray拷贝数组a得到的数组c:', c)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e9e98286163d4dfc9a8eaaf9f8ffc7cb.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70)  
在修改数组a[0]=1之后,通过array拷贝得到的数组b的b[0]值未发生变化,而通过asarray拷贝得到的数组c的c[0]值随之变化了

```python
# 3.2修改数组b观察数组a和c的变化情况
#修改通过array拷贝的数组b
b[1]=1
print('在修改b[0]=1后:')
print('原数组a:', a)
print('通过array拷贝数组a得到的数组b:', b)
print('通过asarray拷贝数组a得到的数组c:', c)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/d539aac4cc0445ab9ccf9827fdec5443.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70)  
在数组b中的b[1]修改为1之后,数组a和c中的对应的数值都未发生变化!,其中原数组a和通过asarray拷贝的数组c一模一样  
```python
# 3.3修改数组c观察数组a和b的变化情况
c[2]=1
print('原数组a:', a)
print('通过array拷贝数组a得到的数组b:', b)
print('通过asarray拷贝数组a得到的数组c:', c)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/7b8cd532ad334db3beef5dbedb290115.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70)  
在完成数组c中的c[2]的修改后,数组b中b[2]的值仍未发生变化,而原数组a的a[2]随之变化了,且原数组a和通过asarray拷贝得到的数组c任然保持一致!至此,整个测试完毕!

通过观察,我得到一下结论:  
通过拷贝得到两个完全同原数组a一模一样的数组后,无论对原数组a做什么修改,通过array拷贝的数组b都不会因其的改变而改变;而通过asarray拷贝的数组始终与原数组a保持一致.同时,无论对数组b进行怎样的改变,原数组a和通过asarray拷贝的数组c都不会发生改变.最后,无论对数组c进行怎样的操作,数组b都不会有改变,而原数组a会随之改变,且始终与其保持一致!

从拷贝层面来讲,通过asarray拷贝得到的数组c始终与原数组保持一致,“同根同源,相依为命”,可谓是生死之交,按照拷贝的定义,这种应该称为浅拷贝,而array使用的是深拷贝,因为数组c是通过浅拷贝得到的,所以数组和原数组a是共用一块内存的,数组c可以说是一种对原数组a的引用,数组c只是数组a的一个别名,其本质还是数组a;而通过深拷贝得到的数组b,则是另辟蹊径,开辟出属于其独有的内存,与原数组a再无瓜葛!

以上为我个人理解,希望对小伙伴们有所帮助~





<ActionBox />
