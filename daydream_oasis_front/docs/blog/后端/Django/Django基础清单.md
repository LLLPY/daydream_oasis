---

next: false

---



<BlogInfo id="381"/>

接着python基础清单，开始刷django基础清单。

## **问题1：如何理解设计模式中的MVC模式，你平时怎么使用这种模式？**

答：首先得清楚，MVC意思就是把项目分成三层，model层，view层，controller层，分别对应django中的model，templates和逻辑控制层（views和urls）。M层主要用于和数据库交互，V层就是展示层，显示给用户看，C层用于逻辑的控制，将一个项目这样分层后更加便于管理和迭代升级。我一般在django中使用这种开发模式（在django中也可以叫做mtv模式，m-m-
model，t-v-templates，v-c-views）。



## **问题2：如何理解django中的mtv模型？**

答：问题一中已经基本回答了。



## **问题3：介绍一下django中你熟悉的模块及其作用。**

**答：感觉还挺多的，我按照mtv的结构分层介绍一下吧!**

M层中：
```shell
AbstractUser：这个是django中提供的一个用户类，该类基本上定义好了用户常用的属性和方法，一般在自己定义用类的时候就直接继承它就行了！
Model：这个是django中提供的默认model类，没有特殊需求，一般都继承自这个类
Q：Q查询
F：F查询
```


V层中：
```shell
load：加载文件包，比如load static：加载静态文件 load my_tags：加载自定义的标签文件 load cache：加载缓存文件

extends：继承自某个文件

block："挖坑"和"填坑"

for：for循环

cache：使用缓存，缓存页面的某个部分或整体

safe：修饰需要渲染的html文件时安全的
```



C层中：
```shell script


make_password：用于生成加密后的密码

check_passwrd：检查加密后的密码和当前密码是否一致

Pageinator：分页器

JsonResposne：返回jjson格式的响应

render：渲染html

redirect：重定向

reverse：将namespace和name解析成对应的url地址

cache_page：修饰器，缓存整个页面内容

cache：缓存
get_redis_connection：django自带的链接redis的接口
MiddlewareMixin：中间件的使用，一般自定义中间件，继承自这个类
FileSystemStorage：django中文件存储的类，自定义文件保存时继承自它
```


## **问题4：如何看待django自带的admin，并说说你的使用经验。**

答：django自带的admin太赞了！有了它基本上不用再自己写crud的逻辑了，只需要简单的写一些配置，就基本上能实现增删改查的功能了，如果再配合simpleui或者xadmin等皮肤，简直就是一个完美的管理系统！对于使用经验，我感觉上手非常容易，非常的好用！



## **问题5：如何理解wsgi的作用？**

**答：WSGI,全称是web server gateway interface（web服务器网关接口）。这是python中定义的一个网关协议，规定了web
server如何跟应用程序交互。web
server可以理解为一个web应用的容器，通过它可以启动应用，进而提供HTTP服务。而应用程序是指我们基于框架开发的系统。这个协议最主要的目的就是保证在python中所有web
server程序或者说gateway程序，能够通过统一的协议跟web框架或者说web应用进行交互。这对于部署web程序来说很重要。如果没有这个协议，那么每个程序，每个web
server可能都会实现各自的接口，实现各自的
"轮子"，最终的结果会是一团乱。使用统一协议的另外一个好处就是，web应用框架只需要实现wsgi，就可以跟外部请求进行交互了，不用去针对某个web
server来独立开发交互逻辑，开发者可以把精力放在框架本身。（书上的解释，相当于又复习了一边）**



## **问题6：如何自己实现wsgi协议？**

答：在把流程复习一边吧，具体代码就略过吧

wsgi服务的流程：

首先，该协议分为两部分，其中一部分是web server或者gateway，它监听在某个端口上接受外部的请求；另一部分是web application。

1.web server接受请求之后，会通过wsgi协议规定的方式把数据传递给web applicable，在web
application中处理完之后，设置对应的状态和header，之后返回body部分。

2.web server拿到web application返回ide数据后，再进行HTTP协议的封装，最终返回完整的HTTPResponse数据。



## **问题7：为什么正式部署时不要开启DEBUG=True配置？**

**答：在debug=True时，django会在每一次请求中都会后台自动统计数据，关掉后就不会自动统计了，可以大大提高性能，减少消耗。**





## **问题8：如何理解django migrations的作用？**

答：每一次在model层中新建了模型或者修改的模型都会进行迁移，将django中的模型映射到数据库中，所以migrations的作用就是映射，将模型中的属性映射到数据库中的字段，将模型中属性的参数映射到数据库中的字段约束，将模型本身映射成数据库中的表。



## **问题9：是否有过手动编辑migrations文件的经历？原因是什么？**

答：有过一两次应该，原因就是数据库和django中的模型映射不一致，原因可能是同一个项目我本地有一个，服务器上有一个，在本地进行了模型修改和迁移，但是没有将最新的项目更新到服务器上，在服务器上进行迁移时就失败了。



## **问题10：介绍一下orm的概念。**

答：orm的全称是：object relation
mapping，即对象关系映射，在django的model层中，就是将model中的模型映射成数据库中的表，数据库中的字段和字段约束同模型的属性和属性参数一一对应。



## **问题11：如何理解orm在django框架中的作用？**

答：大大提高了开发效率，不用为编写额外的sql语句而苦恼！



## **问题12：介绍一下orm下的N+1问题，发生的原因以及解决方案。**

**答：n+1问题就是在一次查询中附带额外的n次查询。例如：有学生公寓dept和学生student两个表，需要查询某一个公寓下所有学生的姓名，查询dept是一次查询，查询dept对应的stu是n次查询，所以是n+1问题。发生原因是因为存在外键约束。在django中，对于一对一的模型可以使用select_related接口解决；对于多对多模型，可以使用prefetch_related接口解决。**





## **问题13：介绍一下django中Model的作用。**

答：我感觉就是程序和数据库交互懂得翻译的"中间人"，可以将编程语言的逻辑翻译成sql，进而操作数据库。



## **问题14：Model的Meta属性类有哪些可配置项？其作用是什么？日常怎么使用它？**

答：我先介绍一下我自己经常使用的：
```python

    

    db_table：配置数据库中对应的表名
```

```python

    

    verbose_name_plural，verbose_name：admin后台显示的数据库的名称
```

```python

    

    ordering：指定排序方式（值的类型是列表）
```




百度得：（参考：[Django--(2)模型(Model)属性与参数整理](https://blog.csdn.net/Mikowoo007/article/details/98203653?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164379161816780264080571%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164379161816780264080571&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-3-98203653.pc_search_insert_ulrmf&utm_term=Model%E7%9A%84Meta%E5%B1%9E%E6%80%A7%E7%B1%BB%E6%9C%89%E5%93%AA%E4%BA%9B%E5%8F%AF%E9%85%8D%E7%BD%AE%E9%A1%B9&spm=1018.2226.3001.4187)）

属性 | 描述  
---|---  
abstract | 标识本类是否为抽象基类  
app_label | 定义本类所属的应用  
db_table | 映射的数据库表名，例如： db_table='moments' 如果在Meta中不提供 db_table 字段，则Django 会为模型自动生成数据表名，生成的格式为"应用名_模型名",例如：应用app的模型Comment 的默认数据表名为 app_comment  
db_tablespace | 映射的表空间名称  表空间的概念只在某些数据库如 Oracle 中存在，不存在表空间的概念的数据库将忽略此字段  

## **问题15：介绍一下queryset的作用以及你常用的queryset优化措施。**

答：queryset是查询结果集，是一个懒加载对象，只有等你真正需要使用查询的结果时，它才会真正执行查询操作，同时它也支持链式调用，之所以queryset支持链式操作，所以才会有懒查询，这样减少了数据库的查询，对性能有一定的优化作用。

我常用的优化措施：尽量避免外键查询，减少对大字段的查询，按照索引进行查询等等



## **问题16：介绍一下Pagination的用法。**

**答：看看本站的paginator的用法：**

![](http://www.lll.plus/media/image/2022/02/02/image-20220202171724-1.png)

首先得确定对谁进行切分操作，所以这里先获取了所有博客，然后传入到Paginator中生成分页对象，Paginator中的第二个参数是每页的数据量，page_num是从请求中获取的页码，通过生成的分页器对象调用page方法，传入页码即可获取当前页码对应的所有数据。操作就这样完成了！



## **问题17：介绍一下Model中Field的作用。**

答：ModelField控制着属性的类型，于数据库中的数据类型一一对应。



## **问题18：如何定制manager？什么场景下需要定制？**

**答：定义自己的** AdminSite即可。

操作如下：

1.定义自己的site，继承自AdminSite

![](http://www.lll.plus/media/image/2022/02/02/image-20220202172810-2.png)

2.添加到路由

![](http://www.lll.plus/media/image/2022/02/02/image-20220202173027-3.png)

3.注册时指定site为自己定义的

![](http://www.lll.plus/media/image/2022/02/02/image-20220202173156-4.png)

这样定制的manager就实现了！

使用场景的话：一般针对访问权限的不同，但都需要内容管理的项目，这时需要定制不同的admin后台。



## **问题19：原生SQL的效率跟ORM的效率是否进行过对比？结果如何？如何理解这种差异？**

答：我个人未进行过比较额。。。不过效率的话我感觉毫无疑问肯定是原生的高，毕竟orm在最终还是得转成sql，这就需要额外的消耗；其次相对于复杂的查询，orm可能实现不了。。



## **问题20：Django内置提供的权限逻辑以及其粒度。**

答：[Django内置的用户权限](https://blog.csdn.net/h18208975507/article/details/111476773)
之前没有接触过，感觉这篇文章讲的还不错。

















































<ActionBox />
