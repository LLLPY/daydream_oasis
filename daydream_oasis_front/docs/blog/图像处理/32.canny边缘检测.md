---

next: false

---



<BlogInfo id="1027"/>

```python
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文

# canny边缘检测
'''
canny边缘检测算法是一种非常流行的边缘监测算法,是John F,Canny于1986年提出的,
被认为是最优的边缘检测算法

原理(canny边缘检测算法由4步构成):
    第一步:噪声去除
        由于边缘检测很容易受到噪声影响,所以首先使用5*5高斯滤波器去除噪声
    第二步:计算图像梯度
        对平滑后的图像使用Sobel算子计算水平方向和垂直方向的一阶导数(Gx和Gy),
        根据得到的这两副梯度图(Gx和Gy)找到边界的梯度和方向,公式如下:
            Edge_Gradient(G)=sqrt(Gx*Gx+Gy*Gy)
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

img = cv.imread('image/erha.jpg', 0)

# 设置较小阈值和较大阈值
min_threshold = 0
max_threshold = 100
canny_img = cv.Canny(img, min_threshold, max_threshold)

plt.subplot(2, 1, 1)
plt.imshow(img, cmap=plt.cm.gray)
plt.title('原图')

plt.subplot(2, 1, 2)
plt.imshow(canny_img, cmap=plt.cm.gray)
plt.title('canny检测结果')

plt.savefig('image/canny边缘检测.jpg')
plt.show()

```



<ActionBox />
