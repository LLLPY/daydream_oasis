---

next: false

---



<BlogInfo id="1040"/>

```python
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文


#camshift
'''
在meanshift算法中检测窗口的大小是固定的,而物体在移动的过程中,如果是由近及远或者
由远及近的移动,那么固定的窗口就不合适了.所以我们需要根据目标的大小和角度来对窗口
的大小和角度进行修正

camshaft算法的全称是"Continuously Adaptive Mean-Shift"(连续自适应meanshift算法),
是对meanshift算法的改进,可随着跟踪目标的大小变化实时调整搜索窗口的大小,具有较好的跟踪效果.

camshaft算法首先应用meanshift,一旦meanshift收敛,它就会更新窗口的大小,还计算最佳拟合
椭圆的方向,从而根据目标的位置和大小更新搜索窗口


camshaft在OpenCV中实现时,只需要将上述的meanshift函数改为camshaft函数即可

'''

#创建视频读取对象
cap=cv.VideoCapture()
cap.open('video/skip2.mp4')
# cap.open(0)

#获取第一帧图像并指定目标的位置
ret,frame=cap.read()
if ret:
    r, h, c, w = 190, 45, 410, 25
    win=(c,r,w,h)

    #指定感兴趣的区域
    roi=frame[r:r+h,c:c+w]
    cv.rectangle(frame,(c,r),(c+w,r+h),(0,255,0),2)
    cv.imshow('w',frame)
    cv.waitKey()


    #将目标区域转成HSV格式
    roi_hsv=cv.cvtColor(roi,cv.COLOR_BGR2HSV)
    #计算直方图
    mask = cv.inRange(roi_hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))  # 将低亮度的值忽略掉
    roi_hist=cv.calcHist([roi_hsv],[0],mask,[180],[0,180])
    #归一化
    cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

    #目标追踪
    #设置终止条件
    term=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)

    while True:
        #获取每一帧图像
        ret,frame=cap.read()
        if ret:
            #图像转成hsv格式
            frame_hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
            #计算直方图的反向投影
            dst=cv.calcBackProject([frame_hsv],[0],roi_hist,[0,180],1)
            #进行camshift跟踪
            ret,win=cv.CamShift(dst,win,term)
            # ret,win=cv.meanShift(dst,win,term)
            #将追踪的位置绘制在图像上
            print(ret)
            pts=cv.boxPoints(ret)
            pts=np.int0(pts)
            cv.polylines(frame,[pts],True,255,2)
            cv.imshow('frame',frame)

            keyword=cv.waitKey(25)
            if keyword==113: #按q键退出
                break
        else:
            break

```



<ActionBox />
