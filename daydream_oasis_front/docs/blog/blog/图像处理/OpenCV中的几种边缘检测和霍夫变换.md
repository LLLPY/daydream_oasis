
<BlogInfo title="OpenCV中的几种边缘检测和霍夫变换" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=452 category="图像处理" tag_list="['OpenCV', '霍夫变换', '边缘检测']" create_time="2021.08.14 16:41:49.835558" update_time="2023.08.29 12:55:47.224414" />

^^^^^^^^^
<h2 id="1-Sobel边缘检测">1.Sobel边缘检测</h2>
<pre><code class="language-python">import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# Sobel检测算子
'''
Sobel边缘检测算法比较简单,实际应用中效率比canny边缘检测效率要高,但是边缘检测
不如Canny检测的准确,但是很多实际应用的场合,sobel边缘却是首选,Sobel算子是高斯
平滑微分操作的结合体,所以其抗噪能力很强,用途较多.

API:
cv.Sobel(src,ddepth,dx,dy,dst,ksize,scale,delta,borderType)
参数:
src:输入图像
ddepth:图像的深度
dx,dy:指求导的阶数,0表示这个方向没有求导,取值为0,1
ksize:是Sobel算子的大小,即卷积核的大小,必须为奇数,默认值为3
注意:如果ksize=-1,就演变成为3x3的Scharr算子
scale:缩导数的比例常数,默认情况下没有缩放系数
borderType:图像边界的模式,默认值为cv.BORDER_DEFAULT

Sobel函数求完导数后会有负值,还会有大于255的值,而原图像是uitn8,即8位无符号数,所以Sobel建立的图像位数不够,会有截断.因此要使用16位有符号的类型,即cv.CV_16S,处理完图像后,再使用cv.convertScaleAbs()函数将其转回原来的uint8格式,否则图像无法显示Sobel算子在两个方向计算的,最后还需要使用cv.addWeighted()函数将其组合起来
'''

img=cv.imread(‘image/erha.jpg’,0)

#计算sobel卷积结果(sobel算子)
sobel_x=cv.Sobel(img,cv.CV_16S,1,0)
sobel_y=cv.Sobel(img,cv.CV_16S,0,1)

#scharr算子 ksize=-1时就是scharr算子
scharr_x=cv.Sobel(img,cv.CV_16S,1,0,ksize=-1)
scharr_y=cv.Sobel(img,cv.CV_16S,0,1,ksize=-1)

#将数据格式进行转换 cv.CV_16s–&gt;uint8
scale_absX=cv.convertScaleAbs(sobel_x)
scale_absY=cv.convertScaleAbs(sobel_y)

scale_absX_scharr=cv.convertScaleAbs(scharr_x)
scale_absY_scharr=cv.convertScaleAbs(scharr_y)

#将x方向和y方向的计算结果求和
img_result=cv.addWeighted(scale_absX,0.5,scale_absY,0.5,0)
img_result_scharr=cv.addWeighted(scale_absX_scharr,0.5,scale_absY_scharr,0.5,0)

plt.subplot(1,3,1)
plt.imshow(img,cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(1,3,2)
plt.imshow(img_result,cmap=plt.cm.gray)
plt.title(‘sobel边缘检测结果’)

plt.subplot(1,3,3)
plt.imshow(img_result,cmap=plt.cm.gray)
plt.title(‘scharr边缘检测结果’)

plt.savefig(‘image/sobel和scharr边缘检测结果.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/7dfeee0b93e34f59b68f743e6563daf1.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="2-Laplacian边缘检测">2.Laplacian边缘检测</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# Laplacian算子
'''
Laplacian是利用二阶导数来检测边缘

使用的卷积核为: |0 1 0|
kernel=|1 -4 1|
|0 1 0|

API:
cv.Laplacian(src,ddepth[,dst[,ksize[,scale[,delta[,borderType]]]]])
参数:
src:输入的图像
ddepth:图像的深度,-1表示采用的是原图像相同的深度,目标图像的深度必须大于原图像
的深度
ksize:算子的大小,即卷积核的大小,必须为奇数

'''

img = cv.imread(‘image/erha.jpg’, 0)

# 计算sobel卷积结果(sobel算子)
sobel_x = cv.Sobel(img, cv.CV_16S, 1, 0)
sobel_y = cv.Sobel(img, cv.CV_16S, 0, 1)

scharr算子 ksize=-1时就是scharr算子
scharr_x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
scharr_y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)

# Laplacian算子
laplacian_img = cv.Laplacian(img, cv.CV_16S)

# 将数据格式进行转换 cv.CV_16s–&gt;uint8
scale_absX = cv.convertScaleAbs(sobel_x)
scale_absY = cv.convertScaleAbs(sobel_y)

scale_absX_scharr = cv.convertScaleAbs(scharr_x)
scale_absY_scharr = cv.convertScaleAbs(scharr_y)

laplacian_result = cv.convertScaleAbs(laplacian_img)

# 将x方向和y方向的计算结果求和
img_result = cv.addWeighted(scale_absX, 0.5, scale_absY, 0.5, 0)
img_result_scharr = cv.addWeighted(scale_absX_scharr, 0.5, scale_absY_scharr, 0.5, 0)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(2, 2, 2)
plt.imshow(img_result, cmap=plt.cm.gray)
plt.title(‘sobel边缘检测结果’)

plt.subplot(2, 2, 3)
plt.imshow(img_result, cmap=plt.cm.gray)
plt.title(‘scharr边缘检测结果’)

plt.subplot(2, 2, 4)
plt.imshow(laplacian_result, cmap=plt.cm.gray)
plt.title(‘laplacian边缘检测结果’)

plt.savefig(‘image/sobel,scharr,laplacian边缘检测结果.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/f0840e948a004f86a26889f407c6a438.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="3-canny边缘检测">3.canny边缘检测</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# canny边缘检测
'''
canny边缘检测算法是一种非常流行的边缘监测算法,是John F,Canny于1986年提出的,
被认为是最优的边缘检测算法

原理(canny边缘检测算法由4步构成):
第一步:噪声去除
由于边缘检测很容易受到噪声影响,所以首先使用55高斯滤波器去除噪声
第二步:计算图像梯度
对平滑后的图像使用Sobel算子计算水平方向和垂直方向的一阶导数(Gx和Gy),
根据得到的这两副梯度图(Gx和Gy)找到边界的梯度和方向,公式如下:
Edge_Gradient(G)=sqrt(GxGx+Gy*Gy)
Angle=1/tan(Gy/Gx)
如果某个像素点是边缘,则其梯度方向总是与边缘垂直.梯度方向被归为4类:垂直,水平,
和两个对角线方向
第三步:非极大值抑制
在获得梯度的方向和大小之后,对整幅图像进行扫描,去除那些非边界上的点,对每一个像素
进行检测,看这个点的梯度是不是周围具有相同梯度方向的点总最大的
第四步:滞后阈值
现在要确定真正的边界.我们设置两个阈值.minVal和maxVal,当图像的灰度梯度高于maxVal
时被认为是真的边界,低于minVal就被抛弃,如果介于两者之间的话,就要看这个点是否与某个
被确定为真正边界的点相连,如果是就认为它也是边界,否则就抛弃.

API:
cv.Canny(image,threshold1,threshold2)
参数:
image:灰度图
threshold1:minval,较小的阈值将间断的边缘连接起来
threshold2:maxval,较大的阈值检测图像中明显的边缘

'''

img = cv.imread(‘image/erha.jpg’, 0)

# 设置较小阈值和较大阈值
min_threshold = 0
max_threshold = 100
canny_img = cv.Canny(img, min_threshold, max_threshold)

plt.subplot(2, 1, 1)
plt.imshow(img, cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(2, 1, 2)
plt.imshow(canny_img, cmap=plt.cm.gray)
plt.title(‘canny检测结果’)

plt.savefig(‘image/canny边缘检测.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/9d6bb2e6f6c94be29fd20f5fc321f5b9.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="4-模板匹配">4.模板匹配</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# matchTemplate
'''
所谓模板匹配,就是在给定的图片中查找和模板最相似的区域,该算法的输入包括模板和图片,
整个任务的思路就是按照滑窗的思路不断的移动模板图片,计算其与图像中对应区域的匹配度,
最终将匹配度最高的区域选择为最终结果.

API:
cv.matchTemplate(img,template,method)
参数:
img:要进行模板匹配的图像
template:模板
method:实现模板匹配的算法
1.平方差匹配(cv.TM_SQDIFF):利用模板与图像之间的平方差进行匹配,最好的匹配是0,
匹配越差,匹配的值越大
2.相关匹配(cv.TM_CCORR):利用模板与图像间的乘法进行匹配,数值越大表示匹配度越高,
越小表示匹配效果差
3.利用相关系数匹配(cv.TM_CCOEFF):利用模板与图像间的相关系数匹配,1表示完美匹配,
-1表示最差匹配
完成匹配后,使用cv.minMaxLoc()方法查找最大值所在的位置即可,如果使用平方差作为比较法,则最小值
位置是最佳匹配位置

'''

#要检测的图像
img = cv.imread(‘image/demo.jpg’)
img2 =cv.imread(‘image/demo.jpg’)

#模板
template = cv.imread(‘image/template.jpg’)

#模板的宽高
h, w = template.shape[:2]

res = cv.matchTemplate(img, template, cv.TM_CCOEFF) #相关系数匹配算法

res2=cv.matchTemplate(img,template,cv.TM_SQDIFF) #平方差匹配算法

#返回图像中最匹配的位置,确定左上角坐标,并将匹配位置绘制在图像上
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
min_val2, max_val2, min_loc2, max_loc2 = cv.minMaxLoc(res2)

# 确定矩形的位置
top_left = max_loc
top_left2 = min_loc2 #因为使用的是平方差匹配,所以最佳位置为最小值的位置

bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 20)

bottom_right2 = (top_left2[0] + w, top_left2[1] + h)
cv.rectangle(img2, top_left2, bottom_right2, (0, 255, 0), 20)

plt.subplot(2, 2, 1)
plt.imshow(cv.imread(‘image/demo.jpg’)[:, :, ::-1])
plt.title(‘要匹配的图像’)

plt.subplot(2, 2, 2)
plt.imshow(template[:, :, ::-1])
plt.title(‘模板’)

plt.subplot(2, 2, 3)
plt.imshow(img[:, :, ::-1])
plt.title(‘相关系数匹配匹配结果’)

plt.subplot(2, 2, 4)
plt.imshow(img2[:, :, ::-1])
plt.title(‘平方差匹配匹配结果’)

plt.savefig(‘image/matchTemplate/匹配结果.jpg’)
plt.show()

#拓展
'''
模板匹配不适用于尺度变换,视角变换后的图像,这时我们就要使用关键点匹配算法,比较经典的
关键点检测算法包括SIFT和SURF等,主要的思路是首先通过关键点检测算法获取模板和测试图像
中的关键点,然后使用关键点匹配算法即可,这些关键点可以很好的处理尺度变化,视角变化,旋转
变化,光照变化等,具有很好的不变性.
'''


</code></pre>
<p><img src="https://img-blog.csdnimg.cn/0fd25eb1b1094c988e4f4fc8344f5224.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="5-霍夫线形检测">5.霍夫线形检测</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# API
'''
cv.HoughLines(img,rho,theta,threshold)
参数:
img:检测的图像,要求二值化后的图像,所以在霍夫变换之前要进行二值化,或者进行canny
边缘检测
th,theta:ρ和θ的精确度
threshold:阈值,只有累加器中的值高于该阈值时才被认为是直线

'''

img = cv.imread(‘image/car.jpg’)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# canny边缘检测
edges = cv.Canny(gray, 50, 150)

# 霍夫变换 ρ的精度设为0.8 θ的精度设为1度 阈值设为150 只有大于150的才认为是直线
lines = cv.HoughLines(edges, 0.8, np.pi / 180, 150)

# 将检测到的线绘制在图像上(注意是极坐标)
for line in lines:
rho, theta = line[0] # rho=r theta=θ
a = np.cos(theta)
b = np.sin(theta)
x0 = a * rho # x=rsinθ
y0 = b * rho # y=rcosθ

# 在该直线上找两个距离较远的点x1 = int(x0 + 1000 * (-b))  # 图像的值为整型 所以要用inty1 = int(y0 + 1000 * (a))  # (x1,y1)距(x0,y0)正的1000x2 = int(x0 - 1000 * (-b))y2 = int(y0 - 1000 * (a))  # (x2,y2)距(x0,y0)负的1000cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
plt.subplot(2, 2, 1)
plt.imshow(img[:, :, ::-1])
plt.title(‘原图’)

plt.subplot(2, 2, 2)
plt.imshow(gray, cmap=plt.cm.gray)
plt.title(‘二值化后’)

plt.subplot(2, 2, 3)
plt.imshow(edges, cmap=plt.cm.gray)
plt.title(‘canny边缘检测后’)

plt.subplot(2, 2, 4)
plt.imshow(img[:, :, ::-1])
plt.title(‘霍夫变换直线检测结果’)

plt.savefig(‘image/霍夫变换直线检测.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/a6879ae8d8b34150b4de2713a8a1d970.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="6-霍夫圆检测">6.霍夫圆检测</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 霍夫圆检测
'''
圆的表达式:
(x-a)2+(y-b)2=r

其中a和b表示圆心坐标,r表示半径,因此标准的霍夫圆检测就是在这三个参数组成的三维空间累加器
上进行圆检测,此时效率就会很低,所以OpenCV中使用霍夫梯度法进行圆检测.

霍夫梯度法将霍夫圆检测分为两个阶段,第一阶段检测圆心,第二阶段利用圆心推到出圆半径
.圆心检测原理:圆心是圆周围法线的交汇处,设置一阈值,找某点的相交的直线条数大于这个阈值
就认为该汇点为圆心
.圆半径确定原理:圆心到圆周上的距离是相同的,确定一个阈值,只要相同距离的数量大于该阈值
,就认为该距离为该圆心的半径

原则上霍夫变换可以检测任何形状,但复杂的形状需要的参数就多,霍夫空间的维数就多,因此在程序实现
上所需的内存空间以及运算效率上都不利于把标准霍夫变换应用于实际复杂图形检测中,霍夫变换法是霍夫变换
的改进,它的目的是减少霍夫空间的维度,提高效率.

API:
cv.HoughCircle(image,method,dp,minDist,param1=100,param2=100,minRadius=0,maxRadius=0)
参数:
image:输入的灰度图像
method:使用霍夫变换圆检测的算法,cv.HOUGH_GRADIENT
dp:霍夫空间的分辨率,dp=1时代表霍夫空间与输入图像空间的大小一致,dp=2时霍夫空间是
输入图像空间的一半,以此类推
minDist:圆心之间的最小距离,如果检测到的两个圆心之间的距离小于该值,则认为他们是同一个
圆心
param1:边缘检测时使用Canny算子的高阈值,低阈值是高阈值的一半
param2:检测圆心和确定半径时所共有的阈值
minRadius,maxRadius:所检测到圆半径的最小值和最大值
返回值:
circles:输出圆向量,包括三个浮点型的元素–圆心横坐标,圆心纵坐标和圆半径

'''

img = cv.imread(‘image/car.jpg’)

#获取灰度图像

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#进行中值滤波 去噪

media_gray = cv.medianBlur(gray, 9)

#霍夫圆检测

circles = cv.HoughCircles(media_gray, cv.HOUGH_GRADIENT, 1, 200, param1=100, param2=50, minRadius=0, maxRadius=500)

#在图像上绘制圆

for circle in circles[0, :]:
x, y, r = [int(i) for i in circle]
cv.circle(img, (x, y), r, (0, 255, 0), 5) # 绘制圆
cv.circle(img, (x, y), 5, (0, 0, 255), -1) # 绘制圆心

plt.subplot(2, 2, 1)
plt.imshow(cv.imread(‘image/car.jpg’)[:, :, ::-1])
plt.title(‘原图’)

plt.subplot(2, 2, 2)
plt.imshow(gray, cmap=plt.cm.gray)
plt.title(‘灰度图’)

plt.subplot(2, 2, 3)
plt.imshow(media_gray, cmap=plt.cm.gray)
plt.title(‘去噪后’)

plt.subplot(2, 2, 4)
plt.imshow(img[:, :, ::-1])
plt.title(‘检测结果图’)

plt.savefig(‘image/或富源检测.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/4a01d6ad3ebd4927bd43facce763e419.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>

