---

next: false

---



<BlogInfo id="641"/>

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),  # 区域缩放
        # title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）"), #区域缩放+slider
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        # datazoom_opts=opts.DataZoomOpts(type_="inside"),
    )
        .render("25.区域缩放.html")
)

```



<ActionBox />
