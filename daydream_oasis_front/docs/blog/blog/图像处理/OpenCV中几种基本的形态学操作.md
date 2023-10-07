
<BlogInfo title="OpenCV中几种基本的形态学操作" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=203 category="图像处理" tag_list="['图像处理', '形态学操作', 'OpenCV']" create_time="2021.08.12 11:11:13.736007" update_time="2023.08.29 13:42:44.339505" />

^^^^^^^^^
<h2 id="1-连通性">1.连通性</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

#连通性
'''
连通性是描述区域和边界的重要概念,两个像素连通的两个必要条件是:
1.两个像素的位置是否相邻
2.两个像素的灰度值是否满足特定的相似准则

根据连通性的定义,有4连通,8连通和m连通三种
4连通:对于具有值V的像素p和q,如果q在集合N4§中,则称这两个像素是4连通
8连通:对于具有值V的像素p和q,如果q在集合N8§中,则称这两个像素是8连通
m连通:对于具有值V的像素p和q,如果:
1.q在集合N4§中,或者
2.q在集合ND§中,并且N4§与N4(q)的交集为空(没有值V的像素)
则称这两个像素是m连通,即4连通和D连通的混合连通.

'''
</code></pre>
<h2 id="2-腐蚀和膨胀">2.腐蚀和膨胀</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

#形态学操作
'''
形态学操作是基于图像形状的一些简单操作.它通常在二进制图像上进行.腐蚀和膨胀是
两个基本的形态学运算符.然后它的变形体如开运算,闭运算,礼帽黑帽等
'''

#腐蚀和膨胀
'''
腐蚀和膨胀是最基本的形态学操作,腐蚀和膨胀都是针对白色部分(高亮部分)而言的.
膨胀就是使图像中高亮的部分扩张,效果图拥有比原图更大的高亮区域;腐蚀是原图中的高亮
区域被蚕食,效果图拥有比原图更小的高亮区域.膨胀是求局部最大值的操作,腐蚀是求局部最
小值的操作.
'''

#腐蚀
'''
集体操作是:用一个结构元素扫描图中每一个像素,用结构元素中的每一个像素与其覆盖的像素
做&quot;与&quot;操作,如果都为1,则该像素为1,否则为0.

腐蚀的作用是消除物体边界点,使目标缩小,可以消除小于结构元素的噪声点

API:
cv.erode(img,kernel,iterations)
参数:
img:要处理的图像
kernel:核结构(结构元素)
iterations:腐蚀的次数,默认是1

'''

#膨胀
'''
具体操作:用一个结构元素扫描图像中的每一个像素,用结构元素中的的每一个像素与其覆盖的像素做&quot;与&quot;
操作,如果都为0,则该像素为0,否则为1.

膨胀的作用是将与物体接触的所有背景点合并到物体中,是目标增大,可添补目标中的孔洞

API:
cv.dilate(img,kernel,iterations)
参数:
img:要处理的图像
kernel:核结构(结构元素)
iterations:腐蚀的次数,默认是1
'''

#生成一张图片
img=np.zeros((500,500),np.uint8)

cv.putText(img,‘hello world~’,(50,250),cv.FONT_HERSHEY_DUPLEX,2,(255,255,255),5)

#创建核结构(结构元素) 5x5
kernel=np.ones((5,5),np.uint8)

#腐蚀
img_erosion=cv.erode(img,kernel)

#膨胀
img_dilate=cv.dilate(img,kernel)

plt.subplot(2,2,1)
plt.imshow(img,cmap=plt.cm.gray)
plt.title(‘原图’)

plt.subplot(2,2,2)
plt.imshow(img_erosion,cmap=plt.cm.gray)
plt.title(‘腐蚀图’)

plt.subplot(2,2,3)
plt.imshow(img_dilate,cmap=plt.cm.gray)
plt.title(‘膨胀图’)

plt.savefig(‘image/图像的腐蚀与膨胀.jpg’)

plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/d0ce9fc6c8f24d509336fb90b43b71e6.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="3-开闭运算">3.开闭运算</h2>
<pre><code class="language-python">import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

#开闭运算
'''
开运算和闭运算是将腐蚀和膨胀按照一定的次序进行处理,但这两者并不是可逆的,
即先开后闭并不能得到原来的图像
'''

#开运算
'''
开运算试试先腐蚀后膨胀,其作用是:分离物体,消除小区域,特点:消除噪点,去除小的
干扰快,而不影响原来的图像
'''

#闭运算
'''
闭运算与开运算相反,先是膨胀后腐蚀,作用是消除&quot;闭合&quot;物体里面的孔洞,特点:可以填充
闭合区域
'''

#API
'''
cv.morphologyEx(img,op,kernel)
参数:
img:要处理的图像
op:处理方式,开运算:cv.MORPH_OPEN;闭运算:cv.MORPH_CLOSE
kernel:核结构
'''

img_orign1=cv.imread(‘image/i.jpg’,1)
img_orign2=cv.imread(‘image/ii.jpg’,1)

#创建一个10x10的核结构
kernel=np.ones((10,10),np.uint8)

#开运算(消除噪点)
img_open=cv.morphologyEx(img_orign1,cv.MORPH_OPEN,kernel)

#闭运算(填充闭合物体内的孔洞)
img_close=cv.morphologyEx(img_orign2,cv.MORPH_CLOSE,kernel)

plt.subplot(2,2,1)
plt.imshow(img_orign1[:,:,::-1])
plt.title(‘原图(有噪点)’)

plt.subplot(2,2,2)
plt.imshow(img_open[:,:,::-1])
plt.title(‘开运算’)

plt.subplot(2,2,3)
plt.imshow(img_orign2[:,:,::-1])
plt.title(‘原图(闭合区域内有孔洞)’)

plt.subplot(2,2,4)
plt.imshow(img_close[:,:,::-1])
plt.title(‘闭运算’)

plt.savefig(‘image/开闭预算.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/ddca0eb1465244408405814cc1fce112.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>
<h2 id="4-礼帽和黑帽">4.礼帽和黑帽</h2>
<pre><code class="language-python">import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
plt.rcParams[‘font.sans-serif’] = [‘SimHei’] # 用来正确显示中文

#礼帽和黑帽
'''
礼帽运算:
原图像与&quot;开运算&quot;的结果图之差,如下计算公式:
dst=tophat(src,element)=src-open(src,element)

因为开运算带来的结果是放大了裂缝或者局部低亮度的区域,因此,从原图中,减去开运算后的
图,得到的效果图突出了比原图轮廓周围的区域更明亮的区域,且这一操作和选择的核大小相关.

礼帽运算用来分离比邻近点亮一些的斑块.当一副图像具有大幅的背景的时候,而微小物品比较
有规律的情况下,可以使用礼帽运算进行背景提取.

黑帽运算:
为&quot;闭运算&quot;的结果图与原图像之差,数学表达式为:
dst=blackhat(src,element)=close(src,element)-src

黑帽运算后的效果图突出了比原图轮廓周围区域更暗的区域,且这一操作和选择的核大小有关.
黑帽预算用来分离比邻近点暗一些的斑块.

'''

#API
'''
cv.morphologyEx(img,op,kernel)
参数:
img:要处理的图像
op:处理方式:
开运算:cv.MORPH_OPEN
闭运算:cv.MORPH_CLOSE
礼帽运算:cv.MORPH_TOPHAT
黑帽运算:cv.MORPH_BLACKHAT
kernel:核结构

'''

img_orign1=cv.imread(‘image/i.jpg’)
img_orign2=cv.imread(‘image/ii.jpg’)

#核结构
kernel=np.ones((10,10),np.uint8)

#礼帽运算
img_tophat=cv.morphologyEx(img_orign1,cv.MORPH_TOPHAT,kernel)

#黑帽运算
img_blackhat=cv.morphologyEx(img_orign2,cv.MORPH_BLACKHAT,kernel)

plt.subplot(2,2,1)
plt.imshow(img_orign1[:,:,::-1])
plt.title(‘原图’)

plt.subplot(2,2,2)
plt.imshow(img_tophat[:,:,::-1])
plt.title(‘礼帽运算后’)

plt.subplot(2,2,3)
plt.imshow(img_orign2[:,:,::-1])
plt.title(‘原图’)

plt.subplot(2,2,4)
plt.imshow(img_blackhat[:,:,::-1])
plt.title(‘黑帽运算后’)

plt.savefig(‘image/礼帽和黑帽运算.jpg’)
plt.show()
</code></pre>
<p><img src="https://img-blog.csdnimg.cn/b3f7815ca2fd476493bffdd9f82a8e69.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" /></p>

