
<BlogInfo id="1327" title="java知识点（复习）" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=571 category="java" tag_list="['java基础']" create_time="2021.11.23 17:08:29.996735" update_time="2021.11.23 17:08:29" />

# java基础

主要知识点：掌握java程序基本结构，变量定义，基本数据类型，各种运算符，控制台输入输出  
  
输入中的小tips  
next()一定要读取到有效字符后才可以结束输入，对输入有效字符之前遇到的空格键，tab键或Enter键等结束符，next()方法会自动将其去掉，只有在输入输入有效字符后，next()方法才将其后输入的空格键，Tab键或Enter键视为分隔符或结束符。  
  
例如：键入： tom Tom  
  
使用next()方法获取到的仅仅是：tom  
![在这里插入图片描述](https://img-blog.csdnimg.cn/87b9bb3363234fd685ee2f7c40fe3a79.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)  
  
nextLine()的结束符只是Enter键，即nextLine()方法返回的是Enter键之前的所有字符  
  

  * 例如：输入： tom Tom 返回： tom Tom

![\[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传\(img-xNU51yzJ-1637657964352\)\(C:UsersLLL03Desktopschooljava复习java基础1637652752775.png\)\]](https://img-blog.csdnimg.cn/13e011adc70a4181a9d2e1fe2e262104.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)


  
  
同样对于nextInt()，nextDouble()等和next()一样一定要读取到有效字符后才可以结束输入。如果next()或者nextInt()等下面有nextLine()时，中间要再加一句nextLine()用来接收next()或者nextInt()等过滤的回车，tab，空格。这样才能让下面的nextLine()生效,否者它就收了enter，tab，空格等，导致用户没有输入就结束了。  
  

例如（错误的写法）：

![\[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传\(img-8uaO4Gpb-1637657964355\)\(C:UsersLLL03Desktopschooljava复习java基础1637653282701.png\)\]](https://img-blog.csdnimg.cn/90838ee87afe4c49a2896beabc58d76c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)

  
  
在输入编号之后，按enter键，发现name时空的，其实name存储的是被scan.nextInt()当作结束符的enter。  
  

  * 正确的写法：

![\[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传\(img-
UUbM2Jis-1637657964358\)\(C:UsersLLL03Desktopschooljava复习java基础1637653416829.png\)\]](https://img-blog.csdnimg.cn/a4bb226efb264032b4446cda8b7abb6e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)


# java流程控制 **​**

主要知识点：if分支，for，while，do while  
  
for循环一般适用于循环次数已知  
while循环一般适用于循环次数未知，但循环条件明确  
相比于while循环，区别在于：不管条件是否成立，循环语句至少会执行一次  
字符串比较不能使用==进行比较，应使用equal方法  
产生一个100以内的随机整数：(int) (Math.random() * 100)  
猜数小游戏  
需求：给定一个100以内的随机整数，提示用户进行猜测，如果用户猜测的数比真实的数大，就提示用户：太大了；如果用户猜测的数比真实的数小，就提示用户：太小了；否则提示用户：恭喜猜对了！  
  
```java
public class guessNum {  
public static void main(String[] args) {  
//定义变量  
int real_num = (int) (Math.random() * 100); //产生一个1-100内的随机证整数  
int num_from_custom = 0; //用户输入的数字  
Scanner scan = new Scanner(System.in);  
while (real_num != num_from_custom) {  
System.out.println("请输入您猜测的数：");  
num_from_custom = scan.nextInt();  
if (num_from_custom > real_num) {  
System.out.println("太大了！");  
} else {  
System.out.println("太小了！");  
}  
}  
System.out.println("恭喜猜对了！");  
}  
} 
``` 

![\[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传\(img-ifJA3MXk-1637657964361\)\(C:UsersLLL03Desktopschooljava复习java基础1637655020636.png\)\]](https://img-blog.csdnimg.cn/f0be60fc20a14491aa0cef38b2dc3efe.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)

# java模块化编程

知识点：创建自定义方法，方法调用，多重分支switch，数组  
  
方法  
方法就是一段可重复调用的代码段，你如：有某段长度约为100行的代码，要在多个地方使用此代码，如果在各个地方都重复编写此部分代码的话，则肯定会比较麻烦，而且此部分代码如果修改的话比较困难，所以此时可以将此部分代码定义成一个方法，以供程序反复调用。  
  
方法定义的格式：  
  
pubic [static] 返回值类型 方法名称(类型 参数1,类型 参数2…){  
  
​ 方法体  
  
​ [return 表达式]  
  
}  
  
在java的方法定义中，可以使用return语句直接结束方法  
  
一个java类有若干个方法组成，但是有且只能有一个main  
  
数组  
数组是一组相关数据的集合，一个数组实际上就是一连串的变量  
一维数组可以存放上千万个数据，并且这些数据的类型是完全相同的  
声明数组的方法：数据类型 数组名[]=new 数据类型[长度];  
可以利用索引来访问数组中的某一个值，下表从0开始  
一个int类型的数据占4个字节  
可以使用：数组.length来获取数组的长度  

# java面向对象基础​​

知识点：面向对象基本概念，类的定义，构造方法，方法重载，类的封装，类图，创建对象，对象的使用  
  
面向对象的三大特征  
封装：对外部不可见  
继承：扩展类的功能  
多态：方法的重载，对象的多态性  
类与对象  
类是对某一类事物的描述，是抽象的，概念上的定义；对象是实际存在的该类事物的每个个体，因而也称为实例  
  
类的定义：  
  
```java
class 类名{  
  
​ 访问权限 数据类型 属性; //定义属性  
  
​ 访问权限 返回值的数据类型 方法名称(类型 参数1,类型 参数2…){} //定义方法  
  
}
```  
  
构造方法的定义格式  
  
```java
class 类名称{  
  
​ 访问权限 类名称(类型 参数1,类型 参数2…){  
  
​ //构造方法没有返回值  
  
}  
  
}  
```
  
构造方法的名称必须与类名一致  
  
构造方法的声明处不能有任何返回值类型的声明  
  
不能在构造方法中使用return返回一个值  
  
//构造方法没有返回值  
}  
  
}  
  
构造方法的名称必须与类名一致  
构造方法的声明处不能有任何返回值类型的声明  
不能在构造方法中使用return返回一个值  

  

（后续继续更新...）

  

  

  


