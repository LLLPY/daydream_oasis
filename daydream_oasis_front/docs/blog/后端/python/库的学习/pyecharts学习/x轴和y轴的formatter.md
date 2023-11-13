---

next: false

---



<BlogInfo id="627"/>

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

bar = (
    Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis('商家', Faker.values())
        .set_global_opts(
        title_opts=opts.TitleOpts(title='Bar formatter', subtitle='用于设置刻度的显示样式'),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(
            formatter="{value}/只"
        )),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(
            formatter="{value}/月"
        ))
    )
        .render('20.formatter的使用.html')
)

```



<ActionBox />
