
<BlogInfo title="OpenCV中的几种图像变换操作" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=266 category="图像处理" tag_list="['图像处理', 'OpenCV', '几何变换']" create_time="2021.08.11 13:55:27.553064" update_time="2023.08.29 13:57:26.451008" />

^^^^^^^^^
<h2 id="1-图像的缩放">1.图像的缩放</h2>
<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
plt.rcParams[‘font.sans-serif’] = [‘SimHei’] #用来正确显示中文

#图像的缩放
'''
缩放是对图像的大小进行调整,即图像的放大或者缩小
API:
cv.resize(src,dsize,fx=0,fy=0,interpolation=cv.INTER_LINEAR)
参数:
src:输入图像
dsize:绝对尺寸,直接指定调整后的图像的大小
fx,fy:相对尺寸,将dsize设置为None,然后将fx和fy设置为比例因子即可
interpolation:插值方法
插值 含义
cv.INTER_LINEAR 双线性插值法
cv.INTER_NEAREST 最近邻插值
cv.INTER_AREA 像素区域重采集(默认)
cv.INTER_CUBIC 双三次插值
'''

taylor=cv.imread(‘image/Taylor.jpg’,1)

#绝对缩放 双三次插值法 放大10倍
res1_absolute=cv.resize(taylor,(19200,10800),fx=None,fy=None,interpolation=cv.INTER_CUBIC)

#相对缩放 缩小到原来的0.5倍
fx,fy=taylor.shape[:2]
print(fx,fy)
res2_relative=cv.resize(taylor,None,fx=0.5,fy=0.5)

plt.subplot(2,2,1)
plt.imshow(taylor[:,:,::-1])
plt.title(‘原图’)

plt.subplot(2,2,2)
plt.imshow(res1_absolute[:,:,::-1])
plt.title(‘放大10倍’)

plt.subplot(2,2,3)
plt.imshow(res2_relative[:,:,::-1])
plt.title(‘缩小1倍’)

plt.savefig(‘image/图像缩放.jpg’)
plt.show()


</code></pre>
<p><img src="https://img-blog.csdnimg.cn/ec42c21f89024ff0ba40b122aa6ed688.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="2-图像的平移">2.图像的平移</h2>
<pre><code class="language-python">import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams[‘font.sans-serif’] = [‘SimHei’] #用来正确显示中文

#图像平移
'''
图像平移将图像按照指定方向和距离,移动到相应的位置

API:
cv.warpAffine(img,M,dsize)
参数:
img:输入图像
M:2*3移动矩阵
对于(x,y)处的像素点,要把它移动到(x+t_x,y+t_y)处时,M矩阵应如下设置:
M= |1 0 t_x|
|0 1 t_y|
注意:将M设置为np.float32类型的numpy数组
dsize:输出图像的大小
注意:输出图像的大小,它应该是(宽度,高度)的形式,请记住,width=列数(col),height=行数(row)
'''

#例:将图像朝x正方向移动50,y正方向移动100(图像大小不变)

img=cv.imread(‘image/demo.jpg’,1)
rows,cols=img.shape[:2]

#平移矩阵

#[1,0,50]:指定x的移动方向和距离(前两个值固定,第三个值的正负决定移动方向,绝对值大小决定移动距离)
#[0,1,100]:指定y的移动方向和距离
M=np.float32([[1,0,50],[0,1,-100]])

#平移
img2=cv.warpAffine(img,M,(cols,rows)) #cols=width rows=height

plt.subplot(2,1,1)
plt.imshow(img[:,:,::-1])
plt.title(‘原图’)

plt.subplot(2,1,2)
plt.imshow(img2[:,:,::-1])
plt.title(‘平移后的图像’)

plt.savefig(‘image/图像的平移.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/bf0a989fb8094e2f94c67e23cc41ffbf.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="3-图像的旋转">3.图像的旋转</h2>
<pre><code class="language-python">import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
plt.rcParams[‘font.sans-serif’] = [‘SimHei’] #用来正确显示中文

#图像旋转
'''
图像旋转是指图像按照某个位置转动一定角度的过程,旋转中图像仍保持这个尺寸.
图像旋转后图像的水平对称轴,垂直对称轴及中心坐标原点都可能发生变换,因此需
要对图像旋转中的坐标进行相应的变换

在OpenCV中图像旋转首先根据旋转角度和旋转中心获取旋转矩阵,然后根据旋转矩阵进行变换,即
可实现任意角度和任意中心的旋转效果
API:
cv.getRotationMatrix2D(center,angle,scale)
参数:
center:旋转中心
angle:旋转角度
scale:缩放比例
返回值:
M:旋转矩阵
调用cv.warpAffine完成图像的旋转

'''

img=cv.imread(‘image/Taylor.jpg’)

#获取图像的尺寸
rows,cols=img.shape[:2]

#获取旋转矩阵 中心旋转90度,图像缩小一倍
M=cv.getRotationMatrix2D((cols/2,rows/2),90,0.5)

#旋转
img_rotate=cv.warpAffine(img,M,(cols,rows))

plt.subplot(2,2,1)
plt.imshow(img[:,:,::-1])
plt.title(‘原图’)

plt.subplot(2,2,2)
plt.imshow(img_rotate[:,:,::-1])
plt.title(‘中心逆时针旋转90度并缩小1倍后’)

plt.savefig(‘image/图像的旋转.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/4354c8cb1e094a779d144c2326d63a04.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="4-图像的仿射变换">4.图像的仿射变换</h2>
<pre><code class="language-python">import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

# 仿射变换
'''
图像的仿射变换涉及到图像形状位置角度变换,是深度学习预处理中常用到的功能,仿射变换
主要对图像的缩放,旋转和平移等操作的组合.

在仿射变换中,原图中所有的平行线在结果图像中同样平行.为了创建这个矩阵我们需要从原图
中找到三个点以及他们在输出图像中的位置,然后cv.getAffineTransform会创建一个2x3
的矩阵,最后这个矩阵会被传给cv.warpAffine.

'''

# 读取图像
img = cv.imread(‘image/demo.jpg’)

# 创建变换矩阵
pts1 = np.float32([[50, 50], [200, 50], [50, 200]]) # 3个点在原始图像中的位置
pts2 = np.float32([[100, 100], [200, 50], [100, 250]]) # 3个点在变换后的图像中的位置
M = cv.getAffineTransform(pts1, pts2) # 变换矩阵
rows, cols = img.shape[:2]

img_transform = cv.warpAffine(img, M, (cols, rows))

plt.subplot(2, 2, 1)
plt.imshow(img[:, :, ::-1])
plt.title(‘原图’)

plt.subplot(2, 2, 2)
plt.imshow(img_transform[:, :, ::-1])
plt.title(‘仿射变换后的图像’)

plt.savefig(‘image/仿射变换.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/b5474b45320e4950aebe16cb0b1e3854.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="5-图像的透射变换">5.图像的透射变换</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

#透射变换
'''
透射变换是视角变化的结果,是指利用透视中心,像点,目标点三点共线的条件,按透视旋转
定律使承影面(透视面)绕迹线(透视轴)旋转某一角度,破坏原有的投影光线束,仍能保持承
影面上投影几何图形不变的变换

在OpenCV中,我们要找到四个点,其中任意三个不共线,然后获取变换矩阵M,再进行变换,
通过cv.getPerspectiveTransform扎到变换矩阵,将cv.warPerspective应用于
此3x3变换矩阵

'''

#读取图像
img=cv.imread(‘image/demo.jpg’,1)

#获取变换矩阵
pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2=np.float32([[100,145],[300,100],[80,290],[310,300]])
M=cv.getPerspectiveTransform(pts1,pts2)

rows,cols=img.shape[:2]

#透射变换
img_transform=cv.warpPerspective(img,M,(cols,rows))

#显示图像
plt.subplot(2,2,1)
plt.imshow(img[:,:,::-1])
plt.title(‘原图’)

plt.subplot(2,2,2)
plt.imshow(img_transform[:,:,::-1])
plt.title(‘透射变换后’)

plt.savefig(‘image/图像的透射变换.jpg’)
plt.show()


</code></pre>
<p><img src="https://img-blog.csdnimg.cn/d22e17a62df742668303a347029554ad.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="6-图像金字塔">6.图像金字塔</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

#图像金字塔
'''
图像金字塔是图像多尺度表达的一种,最主要用于图像的分割,是一种以多分辨率来解释图像的有效但
概念简单的结构.
图像金字塔用于机器视觉和图像压缩,一副图像的金字塔是一系列以金字塔形状排列的分辨率逐步下降,
且来源于同一张原始图的图像集合.其通过梯次向下采样获得,直到达到某个终止条件才停止采样.
金字塔的底部是待处理图像的高分辨率表示,而顶部是低分辨率的近似,层级越高,图像越小,分辨率越低.

API:
cv.pyrUp(img) #对图像进行上采样
cv.pyrDown(img) #对图像进行下采样
'''

img=cv.imread(‘image/demo.jpg’)

#上采样
img_up=cv.pyrUp(img)

#下采样
img_down=cv.pyrDown(img)
img_down2=cv.pyrDown(img_down)

plt.subplot(2,2,1)
plt.imshow(img[:,:,::-1])
plt.title(‘原图’)

plt.subplot(2,2,2)
plt.imshow(img_up[:,:,::-1])
plt.title(‘上采样’)

plt.subplot(2,2,3)
plt.imshow(img_down[:,:,::-1])
plt.title(‘下采样’)

plt.subplot(2,2,4)
plt.imshow(img_down2[:,:,::-1])
plt.title(‘下采样2’)

plt.savefig(‘image/图像金字塔.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/ea6500b75a6346febd8024ed2618877f.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>

