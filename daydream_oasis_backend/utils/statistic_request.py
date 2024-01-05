# -*- coding: UTF-8 -*-
'''
   *****************LLL*********************
   * @Project ：MyBlog                       
   * @File    ：statistic_request.py
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/6/14 16:36             
   *****************************************
'''
# 统计网站的访问情况
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line
from random import randint

# 时间线
time_list = [str(d) + "年" for d in range(1993, 2003)]
#
maxNum = 97300
minNum = 30

data = [{
    "time": f"{time}",
    "data": [
        {"name": "广东", "value": [randint(minNum, maxNum)]},
        {"name": "江苏", "value": [randint(minNum, maxNum)]},
        {"name": "山东", "value": [randint(minNum, maxNum)]},
        {"name": "辽宁", "value": [randint(minNum, maxNum)]},
        {"name": "浙江", "value": [randint(minNum, maxNum)]},
        {"name": "河北", "value": [randint(minNum, maxNum)]},
        {"name": "河南", "value": [randint(minNum, maxNum)]},
        {"name": "上海", "value": [randint(minNum, maxNum)]},
        {"name": "四川", "value": [randint(minNum, maxNum)]},
        {"name": "湖北", "value": [randint(minNum, maxNum)]},
        {"name": "湖南", "value": [randint(minNum, maxNum)]},
        {"name": "黑龙江", "value": [randint(minNum, maxNum)]},
        {"name": "福建", "value": [randint(minNum, maxNum)]},
        {"name": "安徽", "value": [randint(minNum, maxNum)]},
        {"name": "北京", "value": [randint(minNum, maxNum)]},
        {"name": "广西", "value": [randint(minNum, maxNum)]},
        {"name": "云南", "value": [randint(minNum, maxNum)]},
        {"name": "江西", "value": [randint(minNum, maxNum)]},
        {"name": "吉林", "value": [randint(minNum, maxNum)]},
        {"name": "山西", "value": [randint(minNum, maxNum)]},
        {"name": "陕西", "value": [randint(minNum, maxNum)]},
        {"name": "重庆", "value": [randint(minNum, maxNum)]},
        {"name": "天津", "value": [randint(minNum, maxNum)]},
        {"name": "内蒙古", "value": [randint(minNum, maxNum)]},
        {"name": "新疆", "value": [randint(minNum, maxNum)]},
        {"name": "贵州", "value": [randint(minNum, maxNum)]},
        {"name": "甘肃", "value": [randint(minNum, maxNum)]},
        {"name": "海南", "value": [randint(minNum, maxNum)]},
        {"name": "青海", "value": [randint(minNum, maxNum)]},
        {"name": "宁夏", "value": [randint(minNum, maxNum)]},
        {"name": "西藏", "value": [randint(minNum, maxNum)]},
    ],
} for time in time_list]

# 全国每一年的访问总量
total_num = [
    3.4,
    4.5,
    5.8,
    6.8,
    7.6,
    8.3,
    8.8,
    9.9,
    10.9,
    12.1,
]


def get_year_chart(year: str):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == year
    ][0]
    min_data, max_data = (minNum, maxNum)
    data_mark: List = []
    i = 0
    for x in time_list:
        if x == year:
            data_mark.append(total_num[i])
        else:
            data_mark.append("")
        i = i + 1

    map_chart = (
        Map()
            .add(
            series_name="",
            data_pair=map_data,
            zoom=1,
            center=[119.5, 34.5],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="" + str(year) + "全国分地区访问情况 数据来源：后台统计",
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="30",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    line_chart = (
        Line()
            .add_xaxis(time_list)
            .add_yaxis("", total_num)
            .add_yaxis(
            "",
            data_mark,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"全国访问总量{time_list[0]}-{time_list[-1]}", pos_left="72%", pos_top="5%"
            )
        )
    )
    bar_x_data = [x[0] for x in map_data]
    bar_y_data = [{"name": x[0], "value": x[1][0]} for x in map_data]
    bar = (
        Bar()
            .add_xaxis(xaxis_data=bar_x_data)
            .add_yaxis(
            series_name="",
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
        )
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    pie_data = [[x[0], x[1][0]] for x in map_data]
    pie = (
        Pie()
            .add(
            series_name="",
            data_pair=pie_data,
            radius=["15%", "35%"],
            center=["80%", "82%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
            ),
        )
            .add(
            line_chart,
            grid_opts=opts.GridOpts(
                pos_left="65%", pos_right="80", pos_top="10%", pos_bottom="50%"
            ),
        )
            .add(pie, grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"))
            .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


if __name__ == "__main__":
    timeline = Timeline(
        init_opts=opts.InitOpts(width="100%", height="600px", theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_year_chart(year=y)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=5000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )

    timeline.render("china_gdp_from_1993_to_2018.html")
