
<BlogInfo title="OpenCV中的几种角点检测方法" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=396 category="图像处理" tag_list="['图像处理', 'OpenCV', '角点检测', 'penCV']" create_time="2021.08.16 11:09:10.465584" update_time="2023.08.29 13:26:37.961455" />

^^^^^^^^^
<h2 id="1-Harris角点检测">1.Harris角点检测</h2>
<pre><code class="language-python">import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文

# Harris角点检测
'''
Harris角点检测的思想是通过图像的局部小窗口观察图像,角点的特征是窗口沿任意方向移动都会导致
图像灰度的明显变化

将上述思想转化为数学表达式,即将局部窗口向各个方向移动(u,v)并计算所有灰度差异的总和,表达式
如下:
    E(u,v)=∑w(x,y)[I(x+u,y+v)-I(x,y)]²
其中I(x,y)是局部窗口的灰度图,I(x+u,y+v)是平移后的灰度图像,w(x,y)是窗口函数,其可以是矩形
窗口,也可以是对每一个像素赋予不同权重的高斯窗口
角点检测中使E(u,v)的值最大.利用一阶泰勒展开有:
    I(x+u,y+v)=I(x,y)+Ix*u+Iy*v
    其中:Ix和Iy是沿x和y方向的导数,可用sobel算子计算.
  
    E(u,v)=∑w(x,y)[I(x+u,y+v)-I(x,y)]²
          =∑w(x,y)[Ix²u²+2Ix*Iy*u*v+Iy²*v²]
                       |Ix² Ix*Iy|
          =∑w(x,y)[u,v]|Ix*Iy Iy²|
        
          =[u v]M|u|
                 |v|
               
    M矩阵决定了E(u,v)的取值,M是Ix和Iy的二次函数,可以表示成椭圆的形状,椭圆的长短半轴由M的特征
    值a1和a2决定,方向由特征矢量决定
  
 
 共可分为三种情况:
    .图像中的直线.一个特征值大,另一个特征值小,a1&gt;&gt;a2或者a2&gt;&gt;a1.椭圆函数值在某一个方向上大,
    在其他方向小
    .图像中的平面.两个特征值都小,且近似相等,椭圆函数值再各个方向都有
    .图像中的角点.两个特征值都大,且近似相等,椭圆函数在所有方向都增大.

 Harris给出的角点计算方法并不需要计算具体的特征值,而是计算一个角点响应值R来判断角点.R的计算公式
 为:
    R=detM-α(traceM)²
    式中,detM为矩阵M的行列式,traceM为矩阵M的迹,α为常数取值范围为0.04~0.06.事实上,特征是隐含
    在detM和traceM中,因为:
        detM=a1a2
        traceM=a1+a2

    那么认为:
    .当R为大数时的正数是角点
    .当R为大数时的负数为边界
    .当R为小数认为是平坦区域
  

API:
    cv.cornerHarris(src,blockSize,ksize,k)
    参数:
        img:数据类型为float32的输入图像
        blockSize:角点检测中要考虑的领域大小
        ksize:sobel算子求导使用的核大小
        k:角点检测中的自由参数取值范围为[0.04,0.06]
   
'''

# 读取图片
img = cv.imread('image/house.jpg')

# 转换成灰度图
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 数据类型转换成float32
gray_float32 = np.float32(gray)

# 角点检测
dst = cv.cornerHarris(gray_float32, 2, 3, 0.04)

#设置阈值,将角点绘制出来,阈值根据图像进行选择
R=dst.max() * 0.01
#这里将阈值设为dst.max()*0.01 只有大于这个值的数才认为数角点
img[dst &gt; R] = [0, 0, 255]


plt.subplot(2,2,1)
plt.imshow(cv.imread('image/house.jpg')[:,:,::-1])
plt.title('原图')

plt.subplot(2,2,2)
plt.imshow(gray,cmap=plt.cm.gray)
plt.title('灰度图(uint8型)')

plt.subplot(2,2,3)
plt.imshow(gray_float32,cmap=plt.cm.gray)
plt.title('灰度图(float32型)')



plt.subplot(2,2,4)
plt.imshow(img[:,:,::-1])
plt.title('检测结果')

plt.savefig('image/角点检测(Harris).jpg')
plt.show()

</code></pre>
<p><img src="https://img-blog.csdnimg.cn/417dea974d0c4d16b99701174b6e55ab.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="2-Shi-Tomas算法">2.Shi-Tomas算法</h2>
<pre><code class="language-python">import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文

#shi-Tomas算法
'''
shi-Tomas算法是对Harris角点检测算法的改进,一般会比Harris算法得到更好的角点.
Harris算法的角点响应函数是将矩阵M的行列式值与M的迹相减,利用差值判断是否为角点,
后来shi和Tomas提出改进的方法是,若矩阵M的两个特征值中较小的一个大于阈值,则认为
他是角点,即:
    R=min(a1,a2)

API:
    corners=cv.goodFeaturesToTrack(image,maxcorners,qualityLevel,minDistance)
    参数:
        image:输入的灰度图像
        maxCorners:获取角点数的数目
        qualityLevel:该参数指出最低可接受的角点质量水平,在0~1之间
        minDistance:角点之间的最小欧氏距离,避免得到相邻特征点
    返回:
        corners:搜索到的角点,在这里所有低于质量水平的角点被排除,然后把合格的角点按照质量排序,
        然后将质量较好的角点附近(小于最小欧氏距离)的角点删除,最后找到maxCorners个角点返回

'''

#读取图片
img=cv.imread('image/house.jpg')

#转成灰度图
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#shi-Tomas角点检测
corners=cv.goodFeaturesToTrack(gray,1000,0.05,10)

#绘制角点
for corner in corners:
    x,y=corner.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,0,255),-1)




plt.subplot(2,1,1)
plt.imshow(cv.imread('image/house.jpg')[:,:,::-1])
plt.title('原图')


plt.subplot(2,1,2)
plt.imshow(img[:,:,::-1])
plt.title('检测结果')

plt.savefig('image/角点检测(shi-Tomas).jpg')
plt.show()

</code></pre>
<p><img src="https://img-blog.csdnimg.cn/bbe04849157d47b9898f2125894040a0.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="3-sift算法">3.sift算法</h2>
<pre><code class="language-python">import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文

# Sift算法
'''
Harris和shi-Tomas角点检测算法,这两种算法具有旋转不变性,但不具有尺度不变性,在原本能检测
到角点的位置,当图像放大后,就检测不到角点了.

尺度不变特征转换即SIFT(Scale-invariant feature transform).它用来侦测与描述影响中
局部性特征,它在空间尺度中寻找极值点,并提取出其位置,尺度,旋转不变量,此算法由David Lowe
在1999年所发表,2004年完善总结.应用范围包含物体识别,机器人地图感知与导航,影像缝合,3D模型
建立,手势识别,影像追踪和动作对比等领域.


SIFT算法实质是在不同的尺度空间上寻找关键点(特征点),并计算出关键点的方向.SIFT所查找到的关键点
是一些十分突出,不会因为光照,仿射变换和噪音等因素影响而变化的点,如角点,边缘点,暗区的亮点及亮区
的暗点.

'''

# 实现SIFT检测关键点的步骤

# 1.实例化sift
# sift = cv.SIFT_create()

# 2.利用sift.detectAndCompute()检测关键点并计算
'''
kp,des=sift.detectAndCompute(gray,None)
参数:
    gray:进行关键点检测的图像(灰度图)
返回:
    kp:关键点信息,包括位置,尺度,方向信息
    des:关键点描述,每个关键点对应128个梯度信息的特征向量
'''

#3.将关键点检测结果绘制在图像上
'''
cv.drawKeyPoints(image,keypoints,outputimage,color,flags)
参数:
    image:原始图像
    keypoints:关键点信息
    outputimage:输出图片,可以是原始图
    color:颜色设置,通过(b,g,r)修改颜色
    flags:绘图功能的标识设置
        1.cv.DRAW_MATCHES_FLAGS_DEFAULT:创建输出图像矩阵,使用现存的输出图像绘制匹配
        对和特征点,对每一个特征点只绘制中间点
        2.cv.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTING:不创建输出图像矩阵,而是在输出图像
        上绘制匹配对
        3.cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS:对每一个特征点绘制带大小和方向
        的关键点图形
        4.cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS:单点的特征点不被绘制
'''

#读取图像
img=cv.imread('image/house.jpg')

#转换成灰度图像
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#实例化sift
sift=cv.SIFT_create()


#检测关键点并计算
kp,des=sift.detectAndCompute(gray,None)

#绘制关键点
# cv.drawKeypoints(img,kp,img,(0,255,0),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.drawKeypoints(img,kp,img,(0,255,0),cv.DRAW_MATCHES_FLAGS_DEFAULT)


plt.subplot(2,1,1)
plt.imshow(cv.imread('image/house.jpg')[:,:,::-1])
plt.title('原图')


plt.subplot(2,1,2)
plt.imshow(img[:,:,::-1])
plt.title('检测结果')

plt.savefig('image/角点检测(sift).jpg')
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/73f48cce8d2a481695e3f8d3ffe56422.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="4-fast算法">4.fast算法</h2>
<pre><code class="language-python">import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文

# fast算法
'''
Fast(全称Features from accelerated segment test)是一种用于角点检测的算法,
该算法的原理是取图像中检测点,以改点为圆心的周围邻域内像素点判断检测点是否为角点,
通俗的讲就是若一个像素周围有一定数量的像素与该点像素不同,则认为其为角点.

基本流程:
    1.在图像中选取一个像素点p,来判断它是不是关键点.Ip等于点p的灰度值.
    2.以r为半径,覆盖p点周围M个像素,通常情况下,设置r=3,则M=16
    3.设置一个阈值t,如果在这16个像素点中存在n个连续像素点的灰度值都高于Ip+t,或者低于
      Ip-t,那么像素点p就被认为是一个角点,n一般取值为12
    4.由于检测特征点时是需要对所有的像素点进行监测,然而图像中绝大多数点都不是特征点,如
      果对每个像素点都进行上述的检测过程,那显然浪费许多时间,因此采用一种进行非特征点判别
      的方法:首先对候选点的周围每个90度的点:1,9,5,13进行测试(先测1和9,如果他们符合阈值
      要求,再测5和13).如果p是角点,那么这是个点中至少有3个要符合阈值要求,否则直接剔除,
      对保留下来的点再继续进行测试


虽然这个检测器的效率很高,但它有一下几个缺点:
    .获得的候选点比较多
    .特征点的选取不是最优的,因为它的效果取决于与要解决的问题的角点的分布情况
    .进行非特征点判别时大量的点被丢弃
    .检测到的很多特征点都是相邻的
前3个问题可以通过机器学习的方法解决,最后一个问题可以使用非最大值抑制的方法解决


'''

# 机器学习的角点检测
'''
1.选择一组训练图片(最好是跟最后应用相关的图片)
2.使用Fast算法找出每幅图像的特征点,对图像中每一个特征点,将其周围的16个像素存储构成
  一个向量p
3.每一个特征点的16个像素点都属于下列三类中的一种:
          | d Ip-&gt;x≤Ip-t (darker)
    Sp-&gt;x=| s Ip-t≤Ip-&gt;x≤Ip+t (similar)
          | b Ip-&gt;x≥Ip+t (brighter)
4.根据这些像素点的分类,特征向量P也被分为3个子集:Pd,Ps,Pb
5.定义一个新的布尔变量Kp,如果p是角点就设置为True,否则为False
6.利用特征向量p,目标值Kp,训练ID3树
7.将构建好的决策树运用于其他图像的快速检测

'''

# 非极大值抑制
'''
在筛选出来的候选点中有很多是紧挨在一起的,需要通过非极大值抑制来消除这种影响.
为所有的候选点后确定一个打分函数V,V的值可以这样计算:先分别计算Ip与圆上16个
点的像素值差值,取绝对值,再将这16个绝对值相加,就得到了V值
        V=∑|Ip-Ii| (i=1,2...16)

最后比较毗邻候选点的V值,把V值较小的候选点pass掉
Fast算法的思想与我们对角点的直观认识非常接近,化繁为简.Fast算法比其他角点的检测
算法快,但是在噪声比较高时不够稳定,这需要设置合适的阈值.
'''

#Fast算法的实现


'''
1.实例化fast
    fast=cv.FastFeatureDetector_create(threshold,nonmaxSuppression)
    参数:
        threshold:阈值t,默认值为10(特征点与周围像素值差值的阈值)
        nonmaxSuppression:是否进行非极大值抑制,默认为True
    返回:
        fast:创建的FastFeatureDetector对象

2.利用fast.detect检测关键点
    kp=fast.detect(grayImg,None)
    参数:
        grayImg:输入的灰度图片(彩色图像也可以)
    返回:
        kp:关键点信息,包括位置,尺度,方向信息

3.将关键点监测结果绘制在图像上,与sift中的一样
cv.drawKeypoints(image,keypoints,outputimage,color,flags)

'''

img=cv.imread('image/house.jpg')
img2=cv.imread('image/house.jpg')

#阈值设为20 进行非极大值抑制
fast=cv.FastFeatureDetector_create(threshold=30,nonmaxSuppression=True)
fast_not_nonmaxSuppression=cv.FastFeatureDetector_create(threshold=30,nonmaxSuppression=False)


#检测出关键点
kp=fast.detect(img,None)
kp_not_nonmaxSuppression=fast_not_nonmaxSuppression.detect(img2,None)

#将关键点绘制在图像上
cv.drawKeypoints(img,kp,img,(0,255,0),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.drawKeypoints(img2,kp_not_nonmaxSuppression,img2,(0,255,0),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


plt.subplot(2,1,1)
plt.imshow(img2[:,:,::-1])
plt.title('未进行非极大值抑制')

plt.subplot(2,1,2)
plt.imshow(img[:,:,::-1])
plt.title('进行了非极大值抑制')

plt.savefig('image/fast算法.jpg')
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/f81c6305d66642e4a3a6a32cf4360be4.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="5-ORM算法">5.ORM算法</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文


#ORB算法
'''
1.实例化ORB
    orb=cv.ORB_create(nfeatures)
    参数:
        nfeatures:特征点的最大数量
    返回值:
        orb:实例的ORB对象

2.利用orb.detectAndCompute()检测关键点并计算
    kp,des=orb.detectAndCompute(gray,None)
    参数:
        gray:输入的灰度图像
    返回值:
        kp:关键点的信息,包括位置,尺度,方向
        des:关键点描述符,每个关键点BRIEF特征向量,二进制字符

3.将关键点绘制在图像上
    cv.drawKeypoints(image,keypoints,outputimage,flags)

'''

img=cv.imread('image/house.jpg')

#实例化orb
orb=cv.ORB_create(5000)

#检测关键点
kp,des=orb.detectAndCompute(img,None)

print(des.shape)

#将特征点绘制在图像上
cv.drawKeypoints(img,kp,img,(0,255,0),cv.DRAW_MATCHES_FLAGS_DEFAULT)


plt.imshow(img[:,:,::-1])
plt.title('ORB检测结果')


plt.savefig('image/ORB算法.jpg')
plt.show()

</code></pre>
<p><img src="https://img-blog.csdnimg.cn/a371fc402a9a48a48a4d1ec5783990e3.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>

