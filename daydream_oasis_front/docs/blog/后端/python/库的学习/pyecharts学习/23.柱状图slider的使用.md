---

next: false

---



<BlogInfo id="610"/>

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

bar=(
    Bar()
    .add_xaxis(Faker.cars)
    .add_yaxis('商家',Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title='Bar-DataZoom(slider-水平)'),
        datazoom_opts=opts.DataZoomOpts(), #添加滑动块的功能 orient="vertical":为y轴添加滑动块
    )
    .render('12.bar(slider的使用).html')
)
```



<ActionBox />
