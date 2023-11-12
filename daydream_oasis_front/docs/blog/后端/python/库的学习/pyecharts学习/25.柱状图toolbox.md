---

next: false

---



<BlogInfo id="612"/>

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
        datazoom_opts=opts.DataZoomOpts(), #添加滑动块的功能
        toolbox_opts=opts.ToolboxOpts(), #添加toolbox选项,toolbox中提供了一些对图片的操作工具
    )
    .render('13.bar(toolbox).html')
)
```



<ActionBox />
