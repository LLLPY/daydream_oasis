
<BlogInfo title="使用OpenCV实现人脸检测的案例" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=147 category="图像处理" tag_list="['OpenCV', '人脸检测', 'Haar特征']" create_time="2021.08.17 13:23:15.361350" update_time="2023.08.29 13:13:09.335822" />

^^^^^^^^^
<h2 id="1-图像中的人脸检测">1.图像中的人脸检测</h2>
<pre><code class="language-python">import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文

#基础
'''
我们使用机器学习的方法完成人脸检测,首先需要大量的正样本图像(面部图像)和负样本图像(不含面部的图像)来
训练分类器.我们需要从其中提取特征.其中Haar特征会被使用到,就像卷积核一样,每一个特征是一个值,这个值
等于黑色矩形中的像素值之和减去白色矩形中的像素值之和.


Haar特征值反映了图像的灰度变化情况.例如:脸部的一些特征能由矩形特征简单的描述,眼睛要比脸颊颜色要深,
鼻梁两侧比鼻梁颜色要深,嘴巴比周围颜色要深

Haar特征可用于图像任意位置,大小也可以任意改变,所以矩形特征值是矩形模板类别,矩形位置和矩形大小这三个
因数的函数.故类别,大小和位置的变化,使得很小的检测窗口含有非常多的矩形特征

得到图像的特征后,训练一个决策树构建的adaboost级联决策器来识别是否为人脸

'''



# 检测流程

# 1.读取图片,并转换成灰度图

# 2.实例化人脸和眼睛检测的分类器对象
#OpenCV中自带已训练好的检测器,包括面部,眼睛,猫脸等,都保存在xml文件中,我们可以通过已下过程找到他们:
'''
import cv2
print(cv2.__file__)
#保存在cv2的data目录下

'''
# classifier=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# 加载分类器
# classifier.load('haarcascade_frontalface_default.xml')

# 3.进行人脸和眼睛的检测
'''
API:
    rect=classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize,maxSize)
    参数:
        gray:要进行检测的人脸图像
        scaleFactor:前后两次扫描中,扫描窗口的比例系数
        minNeighbors:目标至少被检测到minNeighbors次才会被认为是目标
        minSize,maxSize:目标最小尺寸和最大尺寸
'''
# 4.将检测结果绘制出来


# 1.读取图片并将其转化成灰度图
img = cv.imread('image/family.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2.实例化OpenCV人脸和眼睛识别的分类器(使用OpenCV中已训练好的分类器)
face_cas = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cas.load('haarcascade_frontalface_default.xml')


eyes_cas = cv.CascadeClassifier('haarcascade_eye.xml')
eyes_cas.load('haarcascade_eye.xml')

# 3.调用人脸识别
faceRects = face_cas.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(200, 200))
for faceRect in faceRects:
    x, y, w, h = faceRect
    # 框出人脸
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
    # 4.在识别出的人脸中进行眼睛检测
    roi_color = img[y:y + h, x:x + w]
    roi_gray = img_gray[y:y + h, x:x + w]
    eyes = eyes_cas.detectMultiScale(roi_gray,scaleFactor=1.1,minNeighbors=9)
    for (ex, ey, ew, eh) in eyes: #有两只眼睛
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

plt.imshow(img[:, :, ::-1])
plt.savefig('image/人脸检测.jpg')
plt.show()

</code></pre>
<p><img src="https://img-blog.csdnimg.cn/65eaf49d8ad44e5fbbef6171963ff1b4.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="2-视频中的人脸检测">2.视频中的人脸检测</h2>
<pre><code class="language-python">import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正确显示中文

# 1.读取视频
cap = cv.VideoCapture()
cap.open(0)
# cap.open('video/party.mp4')

# 2.在每一帧数据中进行人脸检测
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 3.实例化忍人脸识别分类器
        face_cas = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        face_cas.load('haarcascade_frontalface_default.xml')

        #戴眼镜的
        eyes_cas = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
        eyes_cas.load('haarcascade_eye_tree_eyeglasses.xml')

        # 4.调用人脸识别(参数可以根据实际情况进行调试和修改)
        faceRects = face_cas.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(50, 50))
        for faceRect in faceRects:
            x, y, w, h = faceRect
            # 框出人脸
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # 5.在识别出的人脸中进行眼睛检测
            roi_color = frame[y:y + h, x:x + w]
            roi_gray = frame_gray[y:y + h, x:x + w]
            eyes = eyes_cas.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=9)
            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv.imshow('frame', frame)
        key = cv.waitKey(25)
        if key == 113:
            break

# 释放资源
cap.release()
cv.destroyAllWindows()
</code></pre>

