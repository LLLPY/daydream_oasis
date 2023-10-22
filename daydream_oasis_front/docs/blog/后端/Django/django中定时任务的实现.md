
<BlogInfo id="1333" title="django中定时任务的实现" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=58 category="Web开发编程" tag_list="['Django', '定时任务']" create_time="2021.10.28 20:50:00" update_time="2021.10.28 20:50:00" />

最近在浏览自己的网站时,发现自己有些地方的功能还是有些问题,体验起来极差,主要是后台数据的统计(一个页面需要等待几十秒后才能加载完成!!!),因为数据量有点大,统计起来非常的耗时,所以想到了能不能预先将数据处理好,然后在前端请求数据的时候,直接将预处理好的数据发过去就行了,然后几经百度后发现,原来django本身就支持这种功能,真不愧是企业级的web框架!!!考虑的周全~

![在这里插入图片描述](https://img-blog.csdnimg.cn/8acff6656ae94cffb03a8c5969bfac4b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)  

得到如图所示的柱状图,其数据量大概为30000(现有的访问量)*12(12个月)*30(30天)*9(9个页面),这个只是保守的估算,总之,在我之前统计的时候,绘制一个图下来需要40秒左右,真的等的花儿都谢了~好在这种折磨只有我一个人能体验到.但是,在加了一个定时任务后,大概1秒钟就能加载出来了!!

其次还有一个新增的功能也是逼得我迫不得已的去找这个"定时任务"的功能,估计如果不是为了新增这个功能,我也不会去处理这个加载慢的问题.

![在这里插入图片描述](https://img-blog.csdnimg.cn/8adf42a3072f42c3a37ec609a112c333.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)  

如图所示,我打算即将在"学习星球"页面新增热文排行榜功能,也是为了方便我后台统计的数据更好的展示,以及看看哪些文章更受大家的喜欢,这个数据的统计量相较于上面那个少一些,但是加载出来也大概需要10秒左右,而且这个功能是每个人都能使用到的,所以我不得不想想方法(如果是我一个人使用这个功能,我估计我还能忍受哈哈哈哈)

最后贴上功能源码:
```python
# 定时任务
from apscheduler.scheduler import Scheduler
from learningPlanet.views import doTopStat
from threading import Thread

# 实例化
sched = Scheduler()
# 每一小时执行一次
@sched.interval_schedule(seconds=60*60)
def sched_test():
    # 刷新排行榜
    th1 = Thread(target=doTopStat)
    # 刷新后台的统计数据
    th2 = Thread(target=drawPictureAndWriteToFile)
    # 启动任务
    th1.start()
    th2.start()
sched.start() #启动定时器
```