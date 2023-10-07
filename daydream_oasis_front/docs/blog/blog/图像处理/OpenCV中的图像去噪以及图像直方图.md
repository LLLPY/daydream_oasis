
<BlogInfo title="OpenCV中的图像去噪以及图像直方图" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=324 category="图像处理" tag_list="['OpenCV', '图像去噪', '图像直方图']" create_time="2021.08.13 16:45:46.260151" update_time="2023.08.29 13:35:37.595289" />

^^^^^^^^^
<h2 id="1-图像噪声">1.图像噪声</h2>
<pre><code class="language-python"># 图像噪声
'''
由于图像采集,处理,传输,过程中不可避免的会受到噪声的污染,妨碍人们对图像理解及分析处理.
常见的图像噪声有高斯噪声,椒盐噪声等
'''

# 椒盐噪声
'''
椒盐噪声也称为脉冲噪声,是图像中经常见到的一种噪声,它是一种随机出现的白点或者黑点,
可能是亮的区域有黑色像素,或在白色区域有黑色像素(或者两者皆有).椒盐噪声的成因可能
是影像讯号受到突如其来的强烈干扰而产生,类比数位转换器或者位元素传输错误.例如失效
的感应器导致像素值为最小值,饱和的感应器导致像素值为最大值
'''

# 高斯噪声
'''
高斯噪声是指噪声密度函数服从高斯分布的一类噪声.由于高斯噪声在空间和频域中数学上的
易处理性,这种噪声(也称为正态噪声)模型经常被用于实践中.
'''
</code></pre>
<h2 id="2-图像平滑">2.图像平滑</h2>
<pre><code class="language-python"># 图像平滑
'''
图像平滑从信号处理的角度看就是去除其中的高频信息,保留低频信息.因此我们可以对
图像实施低通滤波,低通滤波可以去除图像中的噪声,对图像进行平滑.

根据滤波器的不同可分为均值滤波,高斯滤波,中值滤波,双边滤波
'''
</code></pre>
<h2 id="3-均值滤波">3.均值滤波</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 均值滤波
'''
采用均值滤波模板对图像噪声进行滤除.令Sxy表示中心在(x,y)点,尺寸为mxn的矩形图像窗口
的坐标组.均值滤波器可表示为:
fxy=1/mn
由一个归一化卷积框完成.它只是用卷积框覆盖区域所有像素的平均值来代替中心元素
例如,3x3标准化的平均过滤器如下:
|1 1 1|
K=1/9|1 1 1|
|1 1 1|
均值滤波的特点是算法简单,计算速度快,缺点是在去噪的同时去除了很多细节部分,将图像变得模糊

API:
cv.blur(src,ksize,anchor,borderType)
参数:
src:要处理的图像
ksize:卷积核的大小
anchor:默认值(-1,-1),表示核中心
borderType:边界类型
'''

img=cv.imread(‘image/dog.jpg’)

img_blur=cv.blur(img,(10,10))

plt.subplot(2,2,1)
plt.imshow(img[:,:,::-1])
plt.title(‘原图(椒盐噪声)’)

plt.subplot(2,2,2)
plt.imshow(img_blur[:,:,::-1])
plt.title(‘均值滤波’)

plt.savefig(‘image/均值滤波.jpg’)

plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/e5bec30d83e448bbb2a676c1cddbbadf.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="4-高斯滤波">4.高斯滤波</h2>
<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 正态分布
'''
正态分布是一种钟形曲线,越接近中心,取值越大,越远离中心,取值越小.计算平滑结果时,
只需要将&quot;中心点&quot;作为原点,其他点按照其在正态曲线上的位置,分配权重,就可以得到一个
加权平均值.高斯平滑在从图像中去除高斯噪声非常有效

API:
:cv.GaussianBlur(src,ksize,sigmaX,sigmaY,borderType)
参数:
src:要处理的图像
ksize:高斯卷积核的大小 注:卷积核的宽度和高度都应为奇数,且可以不同
sigmaX:水平方向的标准差
sigmaY:垂直方向的标准差,默认值为0,表示与sigmaX相同
borderType:填充边界类型

'''

img=cv.imread(‘image/dog2.jpg’)

img_GaussianBlur=cv.GaussianBlur(img,(3,3),1)

plt.subplot(2,2,1)
plt.imshow(img[:,:,::-1])
plt.title(‘原图(高斯噪声)’)

plt.subplot(2,2,2)
plt.imshow(img_GaussianBlur[:,:,::-1])
plt.title(‘高斯滤波’)

plt.savefig(‘image/高斯滤波.jpg’)

plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/7cba3d028c6d4ecc8ad234bd7c3070cf.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="5-中值滤波">5.中值滤波</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

#中值滤波
'''
中值滤波是一种典型的非线性滤波技术,基本思想是用像素领域灰度值的中值来代替
该像素点的灰度值.中值滤波对椒盐噪声来说尤其有用,因为它不依赖与领域内那些
与典型值差别很大的值.

API:
cv.medianBlur(src,ksize)
参数:
src:输入图像
ksize:卷积核的大小

'''

img=cv.imread(‘image/dog.jpg’)

#中值滤波
img_medianBlur=cv.medianBlur(img,5)

plt.subplot(2,2,1)
plt.imshow(img[:,:,::-1])
plt.title(‘原图(椒盐噪声)’)

plt.subplot(2,2,2)
plt.imshow(img_medianBlur[:,:,::-1])
plt.title(‘中值滤波’)

plt.savefig(‘image/中值滤波.jpg’)

plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/bce6b9acfe554d41b2e2289cdc831aef.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="6-直方图">6.直方图</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 直方图
'''
直方图是对数据进行统计的一种方法,并且将统计值组织到一系列实现定义好的bin中.
其中,bin为直方图中经常用到的一个概念,可以译为&quot;直条&quot;或者&quot;组距&quot;,其数值是从
数据中计算出的特征统计量,这些数据可以是诸如梯度,方向,色彩或者任何特征.

图像直方图是用以表示数字图像中亮度分布的直方图,标绘了图像中每个亮度值的像素
个数.这种直方图中,横坐标的左侧为较暗区域,而右侧为较亮区域.因此一张较暗图片
的直方图中数据多集中在左侧和中间部分,而整体明亮,只有少量阴影的图像则相反.

直方图的一些术语和细节:
dims:需要统计的特征数目.(例:仅统计灰度值,则dims=1)
bins:每个特征空间子区段的数目
range:要统计特征的取值范围

直方图的意义:
.直方图是图像中像素强度分布的图形表达方式
.它统计了每一个强度值所具有的像素个数
.不同的图像的直方图可能是相同的
'''

# API
'''
cv.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
参数:
images:原图像.当传入参数时应该用中括号括起来,例如:[img]
channels:如果输入图像是灰度图,它的值就是[0],如果是彩色图像的话,传入的参数可以是[0]
[1],[2],他们分别对应着通道B,G,R
mask:掩模图像.要统计整幅图像的直方图就把它设置为None.但是如果你只想统计图像某一部分
的直方图,你就需要制作一个掩模图像,并使用它.
hsitSize:bins的数目.也应该用中括号括起来,例如:[256]
ranges:像素值的范围,通常为:[0,256]

'''

# 按照灰度图的方式读取
img=cv.imread(‘image/demo.jpg’,0)

hist=cv.calcHist([img],[0],None,[256],[0,256])
print(hist)

plt.subplot(2,1,1)
plt.imshow(img,cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(2,1,2)
plt.plot(hist)
plt.title(‘图像直方图’)

plt.savefig(‘image/图像直方图.jpg’)
plt.show()


</code></pre>
<p><img src="https://img-blog.csdnimg.cn/5ca6401cbb1f412eb85ed19014fe2d1c.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="7-掩膜的应用">7.掩膜的应用</h2>
<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 掩膜的作用
'''
掩膜是用选定的图像,图形或物体,对要处理的图像进行遮挡,来控制,图像处理的区域.
在数字图像处理中,我们通常使用二维矩阵数组进行掩膜.掩膜是由0和1组成一个二进制
图像,利用该掩膜图像对要处理的图像进行掩膜,其中1值的区域被处理,0值的区域被屏蔽,
不会处理.

掩膜的主要用途:
.提取感兴趣的区域:用预先制作的感兴趣区掩膜与待处理图像进行&quot;与&quot;操作,得到感兴趣
图像,感兴趣区内图像保持不变,而区外图像值都是0.
.屏蔽作用:用掩膜对图像上某些某些区域做屏蔽,使其不参加处理参数的计算,或仅对屏蔽区
做处理或统计.
.结构特征提取:用相似性变量或图像匹配方法检测和提取图像中与掩膜相似的结构特征.
.特殊形状图像制作

'''

img=cv.imread(‘image/demo.jpg’,0)

#创建掩膜图像
mask=np.zeros(img.shape[:2],np.uint8)

#划定感兴趣的区域
mask[400:1000,550:1150]=1

mask_img=cv.bitwise_and(img,img,mask=mask)

#掩膜操作
hist=cv.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(2,2,1)
plt.imshow(img,cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(2,2,2)
plt.imshow(mask,cmap=plt.cm.gray)
plt.title(‘蒙版图’)

plt.subplot(2,2,3)
plt.imshow(mask_img,cmap=plt.cm.gray)
plt.title(‘掩膜之后的图像’)

plt.subplot(2,2,4)
plt.plot(hist)
plt.title(‘掩膜部分的图像直方图’)

plt.savefig(‘image/掩膜的应用.jpg’)
plt.show()


</code></pre>
<p><img src="https://img-blog.csdnimg.cn/1a262b4e44a04387b307cce43d3f881b.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="8-直方图均衡化">8.直方图均衡化</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 直方图均衡化
'''
直方图均衡化是把原始图像的灰度直方图从比较集中的某个灰度区间变成在更广泛灰度范围
内的分布.直方图均衡化就是对图像进行非线性拉伸,重新分配图像的像素值,使一定范围内
的像素数量大致相同.

这种方法提高图像的整体对比度,特别是有用数据的像素值分布比较接近时,在X光图像中使用
广泛,可以提高骨架结构的显示,另外在曝光过渡或不足的图像中可以更好突出细节.

API:
dist=cv.equalizeHist(img)
参数:
img:灰度图像
dist:均衡后的结果

'''

img=cv.imread(‘image/erha.jpg’,0)

#可以看到 均衡化之后,图像的整体对比度有所提高
dist=cv.equalizeHist(img)

plt.subplot(2,1,1)
plt.imshow(img,cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(2,1,2)
plt.imshow(dist,cmap=plt.cm.gray)
plt.title(‘均衡化之后的’)

plt.savefig(‘image/直方图均衡化.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/217f8e5b4bec43728a1f864caea098ea.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="9-自适应的直方图均衡化">9.自适应的直方图均衡化</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 自适应直方图均衡化
'''
在直方图均衡化中,我们考虑的图像是全局对比度.虽然在进行操作之后,全局的对比度有所提高,
但是在许多情况下会丢失很多信息,这样做的效果并不是很好.

为了解决这个问题,需要使用自适应的直方均衡化.此时,整幅图片会被分成很多小块,这些小块被称为
“tiles”(在OpenCV中tiles的大小默认是8*8),绕后对每一个小块分别进行直方土均衡化.所以在
每一个区域中,直方图会集中在某一个小区域中.如果有噪声的话,噪声会被放大,为了避免这种情况的
出现,要使用对比度限制.对于每一个小块来说,如果直方图中的bin超过对比度的上限的话,就把其中的
像素点均匀分散到其他bins中,然后再进行直方图均衡化.

最后,为了去除每一个小块之间的边界,再利用双线性差值,对每一小块进行拼接.

API:
cv.createCLAHE(clipLimit,tileGridSize)
参数:
clipLimit:对比度限制,默认值为40
tileGridSize:分块的大小,默认为8*8

'''

img = cv.imread(‘image/erha.jpg’, 0)

# 创建一个自适应均衡化对象,并应用于图像
clahe = cv.createCLAHE(10, (8, 8))

dist = cv.equalizeHist(img)
cla = clahe.apply(img)

plt.subplot(3, 1, 1)
plt.imshow(img, cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(3, 1, 2)
plt.imshow(dist, cmap=plt.cm.gray)
plt.title(‘均衡化’)

plt.subplot(3, 1, 3)
plt.imshow(cla, cmap=plt.cm.gray)
plt.title(‘自适应均衡化’)

plt.savefig(‘image/自适应直方图均衡化.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/7a45064f23694e20bce4ef61c0e5b69b.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>

