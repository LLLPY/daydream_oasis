---

next: false

---



<BlogInfo id="473"/>

```python
#1.导入模块
from flask import Flask,render_template

#2.创建Flask实例对象
demo = Flask(__name__)
#__name__用来确定资源所v

#1.如何返回一个网页（模板）
#2.如何给模板填充数据
#3.定义路由和视图函数
#路由通过修饰器的修饰来实现
@demo.route('/')
def hello():
    #假设需要访问一个网址
    url_str =  "www.baidu.com"
    return render_template('index.html',url_str=url_str)

#4.启动程序
if __name__ == '__main__':

    demo.run(debug=True)


```



<ActionBox />
