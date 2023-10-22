
<BlogInfo id="1401" title="浅谈c++" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=815 category="c plus plus" tag_list="['c++', '类', '对象']" create_time="2021.06.25 20:02:38.318631" update_time="2022.08.28 16:39:23" />

浅谈C++1.类的定义2.类成员的访问控制3.对象3.1声明对象的一般格式3.2构造函数和析构函数3.2.1构造函数3.2.1.1默认构造函数3.2.2析构函数3.2.2.1默认析构函数3.3拷贝构造函数3.3.1默认拷贝构造函数3.4类的静态成员3.4.1静态数据成员3.4.2静态数据成员的初始化3.5类的友元3.5.1友元函数3.5.2友元类继承机制4.1继承和派生的基本概念4.1.1继承的种类4.1.2二义性4.1.3支配原则4.1.4虚基类4.2程序设计多态性和虚函数5.1.1静态联编(速度快)5.1.2动态联编5.1.3虚函数5.1.3.1纯虚函数5.1.3.2抽象类6.程序设计模板7.1模板的概念7.2解决强类型冲突的几种途径7.3函数模板7.4利用例7.3中的函数模板求两个数中的较大值运算符重载8.1运算符重载规则8.2用成员函数重载运算符8.3用友元函数重载运算符8.4用成员函数重载运算符"++"和"\--"

# 浅谈C++

## 1.类的定义

为了在程序中创建对象,必须首先定义类.c++语言用保留字class定义一个类,一般形式为:
```c++

    

    class 类名

    {

    •       public:

    •               <共有数据和函数>

    •       protected:

    •               <保护数据和函数>

    •       private:

    •               <私有数据和函数>

    ​

    };
```


值得注意的是,右花括号后的分号";"作为类声明的结束标志是不能漏掉的.类中定义的数据和函数分别称为数据成员和成员函数.



## 2.类成员的访问控制

关键字public,protected和private均用于控制类中的成员在程序中的可访问性,关键字public,protected和private以后的成员的访问权限分别是共有,保护和私有的.所有成员默认定义为private的,当为了提高程序的可读性,不主张使用这种默认定义方式。



## 3.对象

类是一种程序员自定义的数据类型,称为类类型,程序员可以使用这个新类型在程序中声明新的变量,具有类类型的变量称为对象.



### 3.1声明对象的一般格式
```c++

    

    <类名> <对象名表>;
```


其中,<类名>是所定义的对象所属类的名字.<对象名表>中可以是一般的对象名,也可以是指向对象的指针名或者引用名,还可以是对象数组名.指向对象的指针称为对象指针,对象的引用称为对象引用.

例如,声明类Point的对象如下所示:
```c++

    

    Point p1,p2,*pdate,p[3],&rp=p1;
```


其中,Point是类名,p1和p2是两个一般的对象名,pdate是指向类Point的对象指针名,p[3]是对象数组,该数组是具有3个元素的一维数组,每个数组元素是类Point的一个对象,rp是对象引用名,它被初始化后,rp是对象p1的引用.



### 3.2构造函数和析构函数

#### 3.2.1构造函数

构造函数是一种特殊的成员函数,对象的创建和初始化工作可以由它来完成.其格式如下:
```c++

    

    <类名>::<类名>(形参表)

    {

        <函数体>

    }
```


构造函数应该被声明为共有函数,因为它是在创建对象的时候被自动调用.构造函数有如下特点:

  * 它的函数名与类名相同

  * 它可以重载

  * 不能指定返回类型,即使是void类型也不可以

  * 它不能被显示调用,在创建对象的时候被自动调用



##### 3.2.1.1默认构造函数

默认构造函数就是无参数的构造函数.既可以是自己定义的,也可是是编译系统自动生成的.

当没有为一个类定义任何的构造函数的情况下,编译系统就会自动生成一个无参数,空函数体的默认构造函数.其格式如下:
```c++

    

    <类名>::<类名>(){}
```




#### 3.2.2析构函数

析构函数也是一种特殊的成员函数,它的作用是在对象消失时执行一项清理任务,例如,可以用来释放由构造函数分配的内存等.其格式如下:
```c++

    

    <类名>::~<类名>(){}
```


构造函数也只能被声明为共有函数,因为它是在释放对象的时候被自动调用.析构函数有如下特点:

  * 析构函数的名字同类名,与构造函数名的区别在于析构函数名的前面加"~",表明它的功能与构造函数的功能相反.

  * 析构函数没有参数,不能重置,一个类中只定义一个析构函数

  * 不能指定返回类型,即使是void类型也不可以

  * 析构函数在释放一个对象时候被自动调用,与构造函数 不同的是,它能被显示调用,当不提倡



##### 3.2.2.1默认析构函数

如果一个类中没有定义析构函数时,系统将自动生成一个默认构造函数,其格式如下:
```c++

    

    <类名>::~<类名>(){}
```




### 3.3拷贝构造函数

拷贝构造函数是一种特殊的构造函数,它的作用是用一个已经存在的对象去初始化另一个对象,为了保证,所引用的对象不被修改,通常把引用参数声明为const参数.其格式如下:
```c++

    

    <类名>::<类名>(const <类名>&<对象名>)

    {

        <函数体>

    }
```


拷贝构造函数具有一般构造函数的特性,特点如下:

  * 拷贝构造函数名字与类名相同,并且不能指定返回类型

  * 拷贝构造函数只有一个参数,并且该参数是该类的引用

  * 它不能被显示调用,在以下三种情况都会被自动调用

    1. 当用一个类的对象去初始化另一个对象时

    2. 当函数的形参是类的对象,进行形参和实参的结合时

    3. 当函数的返回值是类的对象,函数执行完成返回调用者时



#### 3.3.1默认拷贝构造函数

如果一个类中没有定义拷贝构造函数,则系统自动生成一个默认拷贝构造函数.该函数的功能是将已知对象的所有数据成员的值拷贝给对应的对象的所有数据成员.



### 3.4类的静态成员

每创建一个对象时,系统就为该对象分配一块内存单元来存放类中的所有数据的数据成员.这样各个对象的数据成员可以分别存放,互补相干.但在某些应用中,需要程序中属于某个类的所有对象共享某个数据.虽然可以将所要共享的数据说明为全局变量,但这种解决办法将破坏数据的封装性.较好的解决办法是将所要共享的数据说明为类的静态成员.
**静态成员是指声明为static的类成员** ,包括 **静态数据成员** 和 **静态成员函数** ,在类的范围内所有对象共享该数据.



#### 3.4.1静态数据成员

静态数据成员不属于任何对象,它不因对象的建立而产生,也不因对象的析构而删除,它是类定义的一部分,所以使用静态成员不会破坏类的隐蔽性.类中的静态数据成员布偶同与一般的静态变量,也不同于其他类的数据成员.它在程序开始运行时创建而不是在对象创建时创建.它所占空间的回收也不是在析构函数时进行而是在程序结束时进行.



#### 3.4.2静态数据成员的初始化

必须对静态数据成员进行初始化,因为只有这时编译器才会为静态成员分配一个具体的空间.静态数据成员的初始化与一般数据成员不同,它的初始化不能在构造函数中进行.静态数据成员初始化格式为:
```c++

    

    <数据类型><类名>::<静态数据成员名>=<初始值>;
```


这里的作用域运算符"::"用来说明静态数据成员所属类.



### 3.5类的友元

有时候,需要普通函数直接访问一个类的保护或私有数据成员.例如要求两点之间的距离,判断两个矩形的面积是否相等,这需要访问前面点类中的点的坐标X和Y,矩形类中的面积area.
**友元是c++提供给外部的类或函数访问类的私有成员和保护成员的另一种途径**
,它提供在不同类的成员之间,类的成员函数与一般函数之间进行数据共享的机制.友元可以是一个函数,称为友元函数,也可以是一个类,称为友元类.



#### 3.5.1友元函数

在类里声明一个普通函数,加上关键字friend,就成了该类的友元函数, **它可以访问该类的一切成员.** 其原型为:
```c++

    

    friend <类型><友元函数名>(<参数表>);
```


友元函数声明的位置可以在类的任何地方,既可以在共有区,也可以在保护区,意义完全相同.友元函数的实现则在类的外部,一般与类的成员函数定义放在一起.

例-利用友元函数求两个点之间的距离:
```c++

    

    #include<iostream>

    using namespace std;

    class Point {

    public:

        //构造函数

        Point(double x, double y);

        //析构函数

        ~Point();

        //计算距离的友元函数

        friend double distance(Point& a, Point& b);

    private: //私有成员变量

        double X, Y;

    };

    ​

    //构造函数的实现

    Point::Point(double x, double y) {

        X = x;

        Y = y;

    }

    ​

    //析构函数的实现

    Point::~Point() {

        cout << "析构函数被调用~";

    }

    ​

    //在类的外部对友元函数进行实现

    double distance(Point &a, Point &b) { //两个参数都是对Point类的对象的引用

        double len;

        len = sqrt(pow((a.X - b.X), 2) + pow((a.Y - b.Y), 2));

        cout << "两点之间的距离为:" << len << endl;

        return len;

    }

    ​

    int main() {

    ​

        //创建两个点对象

        Point A(0, 0), B(3, 4);

        distance(A, B); //调用友元函数,计算两个点之间的距离

    ​

        return 0;

    ​

    }

    ​
```


取的两个分别为(0,0)和(3,4),计算出两点之间的距离为5,运行结果如下:





#### 3.5.2友元类

除了函数之外,一个类也可以被声明为另一个类的友元,该类被称为友元类.假设有类A和类B,若在类B的定义中将类A声明为友元,那么,类A被称作类B的友元类,它所有的成员函数都可以访问类B中的任意成员.友元类的声明格式为:
```c++

    

    friend class<类名>;
```




# 继承机制



## 4.1继承和派生的基本概念

通过继承机制可以利用已有的数据类型来定义新的数据类型. **根据一个类创建一个新类的过程称为继承,也称派生**.



### 4.1.1继承的种类

在c++语言中,一个派生类既可以从一个基类派生,也可以从多个基类派生.从一个基类派生的继承被称为单继承,单继承形成的类层次是一个倒挂的树,从多个基类派生类的继承被称为多继承,多继承形成的类层次是一个有向无环图.



### 4.1.2二义性

一般地讲,在派生类中对基类成员的访问是唯一的.但是,在有多继承的情况下,可能会造成派生类对基类成员访问的不唯一性,即二义性.

1.调用不同基类的相同成员时可能出现二义性.

2.访问共同基类的成员时可能出现二义性.(如果一个派生类从多个基类派生而来,而这些基类又有一个共同的基类,则在这个派生类中访问这个共同基类中的成员时可能会产生二义性.)

例:
```c++

    

    #include<iostream>

    using namespace std;

    ​

    //基类1

    class Base1{ 

    public:

    void show(){

         cout<<"这是基类1的show函数"<<endl;

    }

    };

    ​

    //基类2

    class Base2{

        public:

        void show(){

            cout<<"这是基类2的show函数"<<endl;

        };

    };

    ​

    //派生类同时继承自基类1和基类2

    class Child public:Base1,public:Base2{

    }

    int main(){

        //创建一个派生类的对象

        Child demo;

        demo.show(); //派生类的子对象调用show方法

        return 0;

        

    }

    ​
```


程序运行结果如下:



由于同时继承的两个基类中都有show方法,因此派生类的子对象关于要调用哪个show方法的时候指向不明确,程序报错.

解决办法:

可以使用作用域运算符,指明要调用的show方法来自继承的哪一个类,例(调用Base1的show方法):
```c++

    

    demo.Base1::show();
```






### 4.1.3支配原则

类X中的名字N支配类Y中同名的名字N,是指类X以类Y为它的一个基类,这称为支配原则.如果一个名字支配另一个名字,则二者之间不存在二义性,当选择该名字时,使用支配者的名字即可.

例(利用支配原则解决上述的二义性问题):

如果在派生类中定义一个自己的show方法,那么就出现了与基类中同名的情况,那么派生类的对象在调用show方法试,会使用支配者的show方法(即派生类自己的show方法):
```c++

    

    class Child : public Base1, public Base2 {

    public:

        void show() {

            cout << "这是派生类的show方法" << endl;

        }

    };
```


程序同样正常运行:





### 4.1.4虚基类

引进虚基类的目的是为了解决二义性问题,使得公共基类在它的派生类对象中只产生一个基类子对象.虚基类说明的格式如下:
```c++

    

    virtual <继承方式> <基类名>
```


其中,virtual是说明虚基类的关键字.虚基类的说明是用在定义派生类时,写在派生类名的后面.

4.1.5多继承机制下构造函数的调用顺序

  1. 首先基类构造函数被调用

  2. 子对象所在类的构造函数次之

  3. 最后执行派生类构造函数

多继承机制下析构函数的调用顺序与之相反



## 4.2程序设计

定义一个点类(Point).矩形类(Rectangle)和立方体类(Cube)的层次结构.矩形包括长度和宽度两个新数据成员,矩形的位置从点类继承.立方体类由长度,宽度和高度构成.要求各类提供支持初始化的构造函数和显示自己成员的成员函数.编写主函数,测试这个层次结构,输出立方体类的相关信息.
```c++

    

    #include<iostream>

    using namespace std;

    //定义一个点类

    class Point {

    public:

        static int ObjNum; //定义一个静态成员变量 用于记录创建的对象的个数

        Point(double x, double y); //构造函数

        ~Point(); //析构函数

        void show(); //用于显示成员数据的函数

    private:

        double X, Y;//点的坐标x和y的值

    };

    ​

    //点类的成员函数的实现

    Point::Point(double x, double y) {

        cout << "点类的构造函数被调用" << endl;

        X = x;

        Y = y;

        ObjNum ++; //如果构造函数调用成功,说明对象创建成功,对象数量加1

        cout << "当前的对象数量为:" << Point::ObjNum << endl;

    ​

    }

    //点类的析构函数

    Point::~Point() {

        cout << "点类的析构函数被调用" << endl;

        ObjNum--; //如果析构函数调用成功,说明对象销毁成功,对象数量减1

        cout << "当前的对象数量为:" << Point::ObjNum << endl;

    ​

    }

    ​

    void Point::show() {

        cout << "我的坐标位置是:(" << X << "," << Y << ")" << endl;

    }

    ​

    //定义一个矩形类 继承自点类

    class Rectangle :public Point

    {

    public:

        //构造函数

        Rectangle(double x, double y, double length, double width);

        //析构函数

        ~Rectangle() {

            cout << "矩形类的析构函数被调用" << endl;

            cout << "当前的对象数量为:" << Point::ObjNum << endl;

    ​

        }

        //矩形类的show函数

        void show();

        double area;//(表)面积

    private:

        double Length, Width;//矩形的长度 宽度 

    ​

    ​

    };

    //矩形类构造函数的实现

    Rectangle::Rectangle(double x, double y, double length, double width) :Point(x,y) { //Point(x,y):点类的数据成员的初始化,同时也会调用点类的构造函数

        cout << "矩形类的构造函数被调用" << endl;

        Length = length;

        Width = width;

        area = length * width;

        cout << "当前的对象数量为:" << Point::ObjNum << endl;

    ​

    }

    ​

    //矩形类show方法的实现

    void Rectangle::show() {

        Point::show();

        cout << "我的长度和宽度分别是:" << Length << "," << Width << endl;

        cout << "我的(表)面积是:" << area << endl;

    }

    ​

    //定义一个立方体类 继承自矩形类

    class Cube :public Rectangle {

    public:

        //立方体类的构造函数

        Cube(double x, double y, double length, double width, double height);

        //立方体类的析构函数

        ~Cube() {

            cout << "立方体类的析构函数被调用" << endl;

        }

    ​

        //立方体类的show函数

        void show();

    private:

        double Height, V;

    };

    ​

    //立方体类构造函数的实现

    Cube::Cube(double x, double y, double length, double width, double height) :Rectangle( x,  y, length, width) {

        cout << "立方体类的构造函数被调用" << endl;

        Height = height;

        //因为在Rectangle中,area是共有成员变量,所以通过public的方式下来能够有权限访问到

        area = (length * width + length * height + width + height) * 2; //重写表面积的计算方法

        V = length * width * height; //体积

        cout << "当前的对象数量为:" << Point::ObjNum << endl;

    }

    ​

    //立方体类的show函数

    void Cube::show() {

        Rectangle::show(); //调用矩形类的show方法

        cout << "我的高度是" << Height << endl;

        cout << "我的体积是" << V << endl;

    }

    //初始化静态数据成员 (不能在main函数里面初始化)

    int Point::ObjNum = 0;

    int main() {

    ​

        //初始化以立方体类

        double x = 0, y = 0, length = 10, width = 10, height = 10;

        Cube demoCube(x, y, length, width, height);

        demoCube.show();

        //初始化一个点类

        Point demoPoint(x,y);

        return 0;

    }

    ​
```




# 多态性和虚函数



5.1静态联编和动态联编

多态性就是统一符号或者名字在不同情况下具有不同解释现象,即是指同一个函数的多种形态.c++可以支持两种多态性,编译时的多态性和运行时的多态性.



## 5.1.1静态联编(速度快)

静态联编是指在程序编译连接阶段进行的联编.编译器根据源代码调用固定的函数标识符,然后由连接器管这些标识符,并用物理地址代替它们.这种联编又被称为早起联编,因为这种联编工作是在程序运行之前完成的.静态联编所支持的多态性称为编译时的多态性.



## 5.1.2动态联编

动态联编是指在
**程序运行时进行编译**.只有向具有多态性的函数传递一个实际对象时,该函数才能与多种可能的函数中的一种联系起来.这种联编有称为晚期联编.动态联编所支持的多态性被称为运行时的多态性.



## 5.1.3虚函数

虚函数是一个成员函数, **该成员函数在基类内部声明**
并且被派生类重新定义,为了创建虚函数,应在基类中该函数声明前加上关键字virtual.虚函数的定义格式如下:
```c++

    

    virtual <返回值类型><函数名>(<形式参数表>)

    {

    <函数体>

    }
```


其中,virtual是关键字,被该关键字说明的函数为虚函数.



虚函数与一般重载函数的区别,主要有一下几点:

  * 重载函数只要求有相同的函数名,而且重载函数是在相同作用域中定义的名字相同的不同函数.而 **虚函数不仅要求函数名相同,而且要求函数的签名,返回类型也相同**.也就是说函数原型必须完全相同,而且虚函数特性必须是体现在基类和派生类的类层次结构中.

  * 重载函数可以是成员函数或友元函数,而虚函数子类是非静态成员函数.

  * 构造函数可以重载,析构函数不能重载.正好相反,构造函数不能定义为虚函数,析构函数能定义为虚函数.

  * 重载函数的调用是以所传递参数序列的差别作为调用不同函数的依据,而虚函数是根据对象的不同去调用不同类的虚函数.

  * 重载函数在编译时表现出多态性,是静态联编;而虚函数则在运行时表现出多态性,是动态联编,因此说明动态联编是c++的精髓.



### 5.1.3.1纯虚函数

如果不能在基类中给出有意义的纯虚函数的实现,但又必须让基类为派生类提供一个公共界面函数.这时可以将它说明为纯虚函数,它的实现留给派生类来做.说明纯序函数的一般形式为:
```c++

    

    virtual <返回值类型><函数名>(<形式参数表>)=0;
```




### 5.1.3.2抽象类

一个类可以说明多个纯虚函数,对于包含有纯虚函数的类被称为抽象类.一个抽象类只能作为基类来派生新类,不能说明抽象类的对象.因为抽象类中有一个或者多个函数没有定义.



## 6.程序设计

(1)使用虚函数编写程序求球体和圆柱体的体积及表面积.由于球体和圆柱体都可以看作由圆继承而来,所以可以定义圆类Circle作为基类.在Circle类中定义一个数据成员radius和两个虚函数area()和volume().由Circle类派生Sphere类和Column类.在派生类中对虚函数area()和volumn()重新定义,分别求球体和圆柱体的体积及表面积.
```c++

    

    #include<iostream>

    using namespace std;

    ​

    //定义基类Circle

    class Circle {

    ​

    public:

        //声明圆类的构造函数

        Circle(double r);

    ​

        //声明求面积的area虚函数

        virtual double area();

    ​

        //声明求体积的volumn纯虚函数

        virtual double volumn() = 0;

    //private:

        double radius;//半径

    ​

    };

    ​

    //圆类构造函数的实现 初始化半径

    Circle::Circle(double r) {

        radius = r;

    }

    ​

    //圆类面积函数的实现

    double Circle::area() {

        return 3.14 * radius * radius;

    }

    ​

    //定义球类 继承自Circle类

    class Sphere :public Circle {

    ​

    public:

        //声明球类的构造函数

        Sphere(double r);

    ​

        //声明球类的计算表面积的函数area

        double area();

    ​

        //声明球类的计算体积的函数volumn

        double volumn();

    ​

    ​

    //private:

        double V; //体积

    };

    ​

    //球类构造函数的实现

    Sphere::Sphere(double r) :Circle(r) {

        V = 4 * 3.14 * pow(radius, 3) / 3;

    }

    ​

    //球类area函数的实现

    double Sphere::area() {

    ​

        return 4 * 3.14 * pow(radius,2);

    ​

    }

    ​

    //球类volumn函数的实现

    double Sphere::volumn() {

        return 4 * 3.14 * pow(radius, 3) / 3;

    }

    ​

    //定义圆柱类 继承自圆类

    class Column :public Circle {

    ​

    public:

        //圆柱类的构造函数

        Column(double r, double h);

    ​

        //圆柱类的area函数

        double area();

    ​

        //圆柱类的volumn函数

        double volumn();

    ​

    private:

        double height; //圆柱体的高

    ​

    };

    ​

    ​

    //圆柱类构造函数的实现

    Column::Column(double r, double h) :Circle(r) {

        height = h;

    }

    ​

    //圆柱体的area函数的实现

    double Column::area() {

        return 3.14 * pow(radius, 2) * 2 + 2 * 3.14 * radius * height;

    }

    ​

    //圆柱体volumn函数的实现

    double Column::volumn() {

        return 3.14 * pow(radius, 2) * height;

    }

    ​

    int main() {

    ​

    ​

        //实例一个球体

        double r = 12;

        double h = 10;

        double area, volumn;

        Sphere demoSphere(r);

        area = demoSphere.area();

        volumn = demoSphere.volumn();

        cout << "半径为" << r << "的球的体积为:" << volumn << "表面积为:" << area << endl;

    ​

        //实例一个圆柱体

        Column demoColumn(r, h);

        volumn = demoColumn.volumn();

        area = demoColumn.area();

        cout << "半径为" << r <<"高度为:"<<h<<"的球的体积为:" << volumn << "表面积为:" << area << endl;

    ​

        return 0;

    ​

    }
```


程序运行结果如下:



值得注意的是:因为在Sphere类和Column类中,依然要用到成员函数radius,所以在基类中,radius应定为共有成员或者抱负成员,否则在派生类(共有继承方式)中为不可访问



(2)编写一个程序,用于计算正方形,三角形和圆的面积及计算各类形状的总面积.
```c++

    

    #include<iostream>

    using namespace std;

    ​

    //定义一个图形的基类

    class Fig {

    ​

    public:

        static double sumArea;  //定义为共有成员 使其可在派生类中被访问

        //声明计算面积的area函数

        virtual double area() = 0; //图形没有面积,声明诶纯虚函数

        double area_;

    };

    ​

    //定义正方形类 继承自Fig

    class Square :public Fig {

    ​

    public:

        //声明正方形类的构造函数

        Square(double w);

    ​

        //声明正方形类的area函数

        double area();

    ​

    ​

    private:

        double width;//边长

    ​

    };

    ​

    //正方形类构造函数的实现

    Square::Square(double w) {

        width = w;

    ​

    }

    ​

    //正方形类area函数的实现

    double Square::area() {

        area_ = pow(width, 2);

        Fig::sumArea += area_;

        return area_;

    }

    ​

    //三角形类 

    class Triangle :public Fig {

    public:

        //三角形类的构造函数

        Triangle(double r1, double r2, double r3);

    ​

        //三角形的area函数

        double area();

    private:

        double R1, R2, R3;

    ​

    };

    ​

    //三角形类构造函数的实现

    Triangle::Triangle(double r1, double r2, double r3) {

        R1 = r1;

        R2 = r2;

        R3 = r3;

    }

    ​

    //三角形类area函数的实现

    double Triangle::area() {

    ​

        //利用海伦公式求解三角形的面积 S=√p(p-a)(p-b)(p-c)

        double p = (R1 + R2 + R3) / 2;

        area_ = sqrt(p * (p - R1) * (p - R2) * (p - R3));

        Fig::sumArea += area_;

        return area_;

    }

    ​

    //定义圆类

    class Circle :public Fig {

    ​

    public:

        //圆类的构造函数

        Circle(double r);

        //圆类的area函数

        double area();

    ​

    private:

        double R; //圆的半径

    ​

    };

    ​

    //圆类构造函数的实现

    Circle::Circle(double r) {

        R = r;

    }

    ​

    //圆类area函数的实现

    double Circle::area() {

        area_ = 3.14 * pow(R, 2);

        Fig::sumArea += area_;

        return area_;

    }

    ​

    //初始化静态成员变量

    double Fig::sumArea = 0;

    ​

    int main() {

    ​

    ​

        //实例一个正方形

        double r = 10,area;

        Square demoSquare(r);

        area = demoSquare.area();

        cout << "边长为" << r << "的正方形的面积为:" << area << endl;

    ​

        cout << "总面积为:" << Fig::sumArea << endl;

    ​

        //实例一个三角形

        double r1 = 3, r2 = 4, r3 = 5;

        Triangle demoTriangle(r1, r2, r3);

        area = demoTriangle.area();

        cout << "三边长分别为:" << r1 << "," << r2 << "," << r3 << "的三角形的面积为:" << area << endl;

    ​

        cout << "总面积为:" << Fig::sumArea << endl;

    ​

        //实例一个圆

        double radius = 10;

        Circle demoCircle(radius);

        area = demoCircle.area();

        cout << "半径为:" << radius << "的圆的面积为:" << area << endl;

        cout << "总面积为:" << Fig::sumArea << endl;

        return 0;

    }

    ​
```




# 模板



## 7.1模板的概念

在强类型程序设计语言中,参与运算的所有对象的类型在编译时即可确定下来,并且编译程序将进行严格的类型检测,这样可以在程序未运行之前就检查出类型不兼容的错误,帮助程序员开发可靠性较高的程序.

但这种强类型语言在提高可靠性的同时又带来了一些副作用,例如,以下两个函数:
```c++

    

    int max(int a,int b){

        return a>b?a:b;

    }

    ​

    和

     float max(float a,float b){

        return a>b?a:b;

    }
```


一个是求两个整数中的较大值,另一个是求两个浮点数中的较大值.它们采用的算法基本基本完全一样,但由于参数类型不同,程序员只好写两段几乎完全相同的代码.



## 7.2解决强类型冲突的几种途径

  1. 利用红宏函数,众所周知,宏函数虽然方便,但是有时常常会引入一些意想不到的问题,从c++开始已经不提倡使用宏了;

  2. 为各种类型都重载这一函数,而为各种数据类型重载又显得有点麻烦

  3. 放松类型检测,在编译期间忽略这些类型匹配问题,而在运行期间进行类型匹配检测,但在程序运行时可能出现类型不兼容的问题

  4. **最理想的方法,是直接将数据类型作为参数,就像函数可以将数据作为参数一样,这种机制被称为类属.**

在c++语言中,程序员可以采用模板(template)机制实现类属.类属机制既提供了数据类型的灵活性,也支持在编译时做严格的类型检测,因而被认为是提高程序可重用性的有力工具.

模板是一种参数化的多态性工具,可以为逻辑功能相同而类型不同的程序提供代码共享机制.

由于c++程序结构主要构件是类和函数.所以在c++中,模板卑分为函数模板和类模板.模板并非一个实实在在的防暑或类,仅仅是函数或类的描述,模板运算对象的类型不是实际的数据类型,而是一种参数化的类型(又称为类属类型).类属参数的函数称为函数模板,类属参数的类称为模板类.程序员只需要面对抽象的类属类型编写逻辑操作代码,而无需关心实际运行时的数据类型.



## 7.3函数模板

函数模板的定义格式如下:
```c++

    

    template <模板参数表>

    <返回值类型><函数名>(<参数表>){

    <函数体>

    }
```


其中,关键字template说定义模板的关键字.<模板参数表>中包含一个或多个用逗号分开的模板参数项,每一项由保留字class或者typename开始,后跟用户命名的标识符,此标识符为模板参数,表示数据类型.函数模板中可以利用这些模板参数定义函数返回值类型,参数类型和函数体中的变量类型.它同基本数据类型一样,可以在函数中任何地方使用.



例7.3.定义函数模板求两个数中的较大值
```c++

    

    template <typename T>

    T max(T a,T b){    

        return a>b?a:b

    }
```


当程序中使用这个函数模板时,编译程序将根据函数调用时的实际数据类型产生相应的函数.如产生求两个整数中的较大值函数,或求两个浮点数中较大值函数.

<参数表>中可以使用模板参数,也可以使用一般类型参数.但<参数表>至少有一个形参的类型必须用<模板参数表>中的参数定义的, **并且在
<模板参数表>中的每个模板参数都必须在<参数表>中得到使用**,即作为形参的类型使用.



## 7.4利用例7.3中的函数模板求两个数中的较大值
```c++

    

    #include<oistream>

    using namespace std;

    ​

    template <typename T> //函数模板

    T max(T a,T b){

        return a>b?a:b;

    }

    ​

    int main(){

        

        int a=19,b=23,c;

        c=max(a,b);

        cout<<c<<endl;

        

        

        

        

        return 0;

    }
```




# 运算符重载



## 8.1运算符重载规则

运算符重载可以使程序更加简介,使表达式更加直观,从而增加可读性.但是重载运算符必须遵循以下规则:

  1. 重载运算符必须符合语言语法.

例如,不能在c++中这样写:
```c++

    

    float f;

    ​

    3.14=f;
```


  2. 不能重载对内部c++数据类型进行操作的运算符.

例如,不能重载二元浮点减法运算.

  3. 不能创建新的运算符

  4. 不能重载下面运算符

    * 类成员选择运算符

    * *成员指针运算符

    * ::作用域运算符

    * ?:条件表达式运算符

除此之外的运算符都可以被重载,并且只有"="的重载函数不能被继承.

  5. 重载运算符要保持原有的基本语义不变



## 8.2用成员函数重载运算符

用成员函数重载运算符的原型为:

<返回值类型>operator<运算符>(<形参表>);

其中<返回值类型>可以为任何有效类型,但通常是返回操作类的对象.<运算符>表示要重载的运算符,<形式参数表>中参数个数与重载的运算符操作数的个数有关.由于每个非静态成员函数都带有一个隐含的自引用参数this指针,对于一元运算符函数,不用显示声明形参,所需要的形参将由自引用参数提供,而对于二元运算符函数,只需要显示声明右操作数,左操作数则由引用参数提供.总之,用成员函数重载运算符需要的参数个数总比它的操作数少一个.

例.用成员函数重载运算符,实现复数的二元加法,乘法运算
```c++

    

    #include<iostream>

    using namespace std;

    ​

    class Complex {

    public:

        Complex(double r = 0.0, double i = 0.0);

        Complex operator +(Complex c); //重载二元加

        Complex operator -(Complex c);//重载二元减

        void display();

    private:

        double real, img;

    };

    ​

    Complex::Complex(double r, double i) {

        real = r;

        img = i;

    }

    ​

    Complex Complex::operator +(Complex c) { //重载加法

        Complex temp; //声明一个Complex的临时对象

        temp.real = real + c.real;

        temp.img = img + c.img;

        return temp;

    ​

    }

    ​

    Complex Complex::operator -(Complex c) { //重载减法

        Complex temp;

        temp.real = real - c.real;

        temp.img = img - c.img;

        return temp;

    ​

    }

    ​

    void Complex::display(){

        const char *strs;

        strs = (img < 0) ? "" : "+"; //如果虚部小于0就不需要添加"+"号 否则添加

        cout << real << strs << img << endl;

    }

    ​

    ​

    int main() {

    ​

        //实例两个复数对象

        double real1 = 10, real2 = 2, imag1 = 12, imag2 = 73.2;

        Complex demoComplex1(real1, imag1), demoComplex2(real2, imag2),c2,c3;

        c2 = demoComplex1 + demoComplex2;

        c3 = demoComplex1 - demoComplex2;

        c2.display();

        c3.display();

        return 0;

    ​

    }

    ​
```


程序运行结果如下:





## 8.3用友元函数重载运算符

用友元函数重载运算符的原型为:

friend <返回值类型>operator<运算符>(<形参表>);

其中,标识符的函数与成员函数重载运算符的格式中的同名标识符的含义相同.由于友元函数不是类的成员,没有this指针,所以参数的个数必须显示声明.即对于一元运算符函数,就需要声明一个形参,而对于二元运算符函数,则需要声明两个形参.总之,用友元函数重载运算符需要的参数个数与操作数的个数一样多.

例.用友元函数重载运算符,实现复数的二元加法,减法运算.
```c++

    

    #include<iostream>

    using namespace std;

    ​

    class Complex {

    ​

    public:

        friend Complex operator+(Complex c1, Complex c2); //返回类型和参数类型都是Complex

        friend Complex operator-(Complex c1, Complex c2); 

        //构造函数

        Complex(double r=0, double i=0);

        void display();

    ​

    private:

        double real, imag;

    };

    ​

    ​

    //构造函数的实现

    Complex::Complex(double r, double i) {

        real = r;

        imag = i;

    }

    ​

    ​

    //加法

    Complex operator+(Complex c1, Complex c2) {

        Complex temp;

        temp.real = c1.real + c2.real;

        temp.imag = c1.imag + c2.imag;

        return temp;

    }

    ​

    //减法

    Complex operator-(Complex c1, Complex c2) {

        Complex temp;

        temp.real = c1.real - c2.real;

        temp.imag = c1.imag - c2.imag;

        return temp;

    }

    ​

    void Complex::display() {

        const char* str;

        str = (imag > 0) ? "+" : "";

        cout << real << str << imag << endl;

    }

    ​

    int main() {

    ​

        //实例两个对象

        Complex c1(10, 10), c2(15, 21);

        Complex c;

        cout << "c1=";

        c1.display();

        cout << "c2=";

        c2.display();

        c = c1 + c2;

        cout << "c1+c2=";

        c.display();

        c = c1 - c2;

        cout << "c1-c2=";

        c.display();

        return 0;

    }

    ​
```


程序运行结果如下:





## 8.4用成员函数重载运算符"++"和"\--"
```c++

    

    #include<iostream>

    using namespace std;

    ​

    class Counter {

    public:

        Counter(double v=0) { value = v; }

        Counter operator++();//前缀++

        Counter operator++(int);//后缀++

        Counter operator--();//前缀--

        Counter operator--(int);//后缀--

        void display() {cout << value << endl;}

    private:

        unsigned value;

    };

    ​

    //前缀++

    Counter Counter::operator++() {

        value++;

        return *this;

    }

    ​

    //前缀--

    Counter Counter::operator--() {

        value--;

        return *this;

    }

    ​

    //后缀++

    Counter Counter::operator++(int) {

        Counter temp;

        temp.value = value++;

        return temp;

    }

    ​

    //后缀--

    Counter Counter::operator--(int) {

        Counter temp;

        temp.value = value--;

        return temp;

    }

    ​

    ​

    int main() {

    ​

        Counter n(10);  //n=10

        Counter c=++n; //c=11 n=11

        n.display();

        c.display();

        c = n++;  //c=11 n=12

        c.display();

        n.display();

        c = c--; //c=11

        c.display();

        n=--c; 

        n.display();//n=10

        c.display();//c=10

    ​

    ​

    ​

    }
```




**​附件**

[浅谈C.pdf](/media/file/2022/08/28/浅谈C.pdf)


