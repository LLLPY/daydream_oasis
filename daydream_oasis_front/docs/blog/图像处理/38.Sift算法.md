---

next: false

---



<BlogInfo id="1033"/>

```python
import numpy as np
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
```



<ActionBox />
