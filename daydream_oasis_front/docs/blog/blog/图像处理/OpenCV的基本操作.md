
<BlogInfo title="OpenCV的基本操作" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=181 category="图像处理" tag_list="['图像处理', 'OpenCV']" create_time="2021.08.09 11:44:04.449554" update_time="2023.08.29 13:50:54.382765" />

^^^^^^^^^
<h2 id="安装">安装</h2>
<pre><code class="language-python">#安装OpenCV之前需要安装numpy,matplotlib

#安装命令:pip install opencv-python

#如果我们要利用SIFT和SURF等进行特征提取时,还需要安装:
#pip install opencv-contrib-python
</code></pre>
<h2 id="主要模块">主要模块</h2>
<pre><code class="language-python">'''

core,highgui,imgproc是最基础的模块

core模块:实现了最核心的数据结构及其基本运算,如绘图函数,数组操作相关函数
highgui模块:实现了视频与图像的读取,显示,存储等接口
imgproc模块:实现了图像处理的基本方法,包括图像滤波,图像的几何变换,平滑,
阈值分割,形态学处理,边缘检测,目标检测,运动分析和对象跟踪等

'''
</code></pre>
<h2 id="IO操作">IO操作</h2>
<pre><code class="language-python">import cv2
import matplotlib.pyplot as plt
# 读取图像
# API:cv.imread()
'''
imread()
参数:
    .要读取的图像的路径
    .读取方式的标志
        .cv.IMREAD_COLOR:以彩色模式加载图像,任何图像的透明度都将被忽略.这个是默认参数值
        .cv.IMREAD_GRAYSCALE:以灰度模式加载图像
        .cv.IMREAD_UNCHANGED:包括alpha通道的加载图像模式
    注:可以使用1,0,-1来代替上面三个标志
'''

# 例:以灰度图的形式读取图像
imgObj = cv2.imread('image/demo.jpg', cv2.IMREAD_GRAYSCALE)
# imgObj = cv2.imread('image/demo.jpg', 1)
# 或者:  imgObj=cv2.imread('demo.jpg',0)

# 注:如果加载的路径有误,不会报错,会返回一个None

# 显示图像
# API:cv.imshow()
'''
imshow()
参数:
    .显示图像的窗口名称,以字符串类型表示
    .要加载的图像
  
    注:在调用显示图像的API后,要调用cv.waitKey()给图像绘制留下时间,否则窗口会出现
    无响应的情况,并且图像无法显示
'''

#例:显示刚刚读取的图像
cv2.imshow('demo',imgObj)
cv2.waitKey() #等待键盘的输入     cv2.waitKey(0) 表示永远的等待下去
cv2.destroyAllWindows() #销毁窗口
#同时也可以使用matplotlib进行图像的显示
# plt.imshow(imgObj[:,:,::-1]) #彩色图
plt.imshow(imgObj,cmap=plt.cm.gray) #灰度图
plt.show()

#保存图像
'''
cv.imwrite()
参数:
    .文件名,要保存在哪里
    .要保存的图像
'''

#例:保存刚刚读取的灰度图像
cv2.imwrite('image/demo_gray.jpg',imgObj)
</code></pre>
<h2 id="绘制图形-直线-圆-长方形-文字-">绘制图形(直线,圆,长方形,文字)</h2>
<pre><code class="language-python">import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#绘制直线
#API:cv.line(img,start,end,color,thickness)
'''
参数:
    .img:要绘制直线的图像
    .start,end:直线的起点和终点
    .color:线条的颜色
    .thickness:线条的宽度
'''

#绘制圆形
#API:cv.circle(img,centerpoint,r,color,thcikness)
'''
参数:
    .img:要绘制圆形的图像
    .centerpoint,r:圆心和半径
    .color:线条的颜色
    .thickness:线条的宽度 #如果取值为-1.会生成一个闭合的圆形

'''

#绘制矩形
#API:cv.rectangle(img,leftupper,rightdown,color,thickness)
'''
参数:
    .img:要绘制矩形的图像
    .leftupper,rightdown:矩形的左上角和右下角坐标
    .color:线条的颜色
    .thickness:线条的宽度
'''

#向图像中添加文字
#API:cv.putText(img,text,station,font,fontsize,color,thickness,cv.LINE_AA)
'''
参数:
    .img:图像
    .text:文本内容
    .station:文本的放置位置
    .font:字体
    .fontsize:字体大小
    .color:字体颜色
    .thickness:线条宽度
'''

#例 在空白图像中绘制各种图像和文字

#创建一个空白的图像 512x512
img=np.zeros((512,512,3),np.uint8)

#绘制一条直线
cv.line(img,(0,0),(511,511),(0,255,0),5)

#绘制一个矩形
cv.rectangle(img,(100,100),(400,400),(255,0,0),5)

#绘制一个圆
cv.circle(img,(255,255),150,(0,0,255),-1)

#写入文本
font=cv.FONT_HERSHEY_COMPLEX
cv.putText(img,'hello world~',(100,255),font,1.5,(255,255,255),5)

plt.imshow(img[:,:,::-1])
plt.show()
</code></pre>
<h2 id="像素的操作">像素的操作</h2>
<pre><code class="language-python">import cv2 as cvimport numpy as npimport matplotlib.pyplot as plt
'''
我们可以通过行和列的坐标值获取该像素点的像素值.对于BGR图像,它返回一个蓝,绿,红的数组.
对于灰度图像,仅返回相应的强度值.使用相同的方法对像素值进行修改.
'''

#创建图像
img=np.zeros((256,256,3),np.uint8)

#获取某一点的像素值
px=img[100,100]
print(px)

#仅获取蓝色通道的强度值
blue=img[100,100,0] 

#第三个参数0,1,2对应蓝,绿,红通道
print(blue)

#修改某一像素点的像素值
img[100,100]=[0,255,0]plt.imshow(img[:,:,::-1]) #通道翻转
plt.show()

</code></pre>
<h2 id="图像的属性">图像的属性</h2>
<pre><code class="language-python">import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 以彩色模式读取图片
img = cv.imread('image/demo.jpg', 1)

# 图像属性包括行数,列数和通道数,图像数据类型,像素数等
'''
    属性               API
    形状               img.shape
    图像大小            img.size
    数据类型            img.dtype
'''

# 获取图像的形状
shape = img.shape
print(shape)

# 获取图像的大小(像素的个数)
size = img.size
print(size)

# 数据类型
dtype = img.dtype
print(dtype)

plt.imshow(img[:, :, ::-1])
plt.show()
</code></pre>
<h2 id="通道的拆分与合并">通道的拆分与合并</h2>
<pre><code class="language-python">import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


'''
有时需要在B,G,R通道单独工作.在这种情况下,需要将BGR图像分割为单个的通道,或者
在其他情况下,可能需要将这些单独的通道合并成BGR图像.
'''

img=cv.imread('image/demo.jpg')


#通道拆分
b,g,r=cv.split(img)
# print(b,g,r)

for i in (b,g,r):
    plt.imshow(i,cmap=plt.cm.gray)
    plt.show()


#通道合并
img_merge=cv.merge((b,g,r))
# print(img_merge)
plt.imshow(img_merge[:,:,::-1])
plt.show()
</code></pre>
<h2 id="色彩空间的转换">色彩空间的转换</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


'''
opencv中有150多种颜色空间的转换方法.最广泛使用的转换方法有两种,
BGR-&gt;Gray和BGR-&gt;HSV

API:
    cv.cvtColor(input_image,flag)

参数:
    input_image:进行颜色空间转换的图像
    flag:转换类型
        cv.COLOR_BGR2GRAY:BGR-&gt;Gray
        cv.COLOR_BGR2HSV:BGR-&gt;HSV
'''

img=cv.imread('image/demo.jpg')

#彩色图像转灰度图像
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#彩色图像转HSV
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
plt.imshow(img_gray,cmap=plt.cm.gray)
plt.show()

plt.imshow(img_hsv)
plt.show()
</code></pre>

