---

next: false

---



<BlogInfo id="621"/>

```python
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

line=(
    Line()
    .add_xaxis(Faker.country)
    .add_yaxis('国家',Faker.values())

    .set_global_opts(
        title_opts=opts.TitleOpts(title='x&y轴的相关配置') ,
        xaxis_opts=opts.AxisOpts(name='我是x轴',is_scale=True,),
        yaxis_opts=opts.AxisOpts(name='我是y轴',is_scale=True)
    )

    .render('17.bar(xy_config).html')
)
```



<ActionBox />
