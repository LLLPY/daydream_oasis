---

next: false

---



<BlogInfo id="607"/>

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>

</head>
<body>
    <div id="c551d0f09401405ca5cf03d56b35fb86" class="chart-container" style="width:100%; height:800px;"></div>
    <script>
        var chart_c551d0f09401405ca5cf03d56b35fb86 = echarts.init(
            document.getElementById('c551d0f09401405ca5cf03d56b35fb86'), 'white', {renderer: 'canvas'});
        var option_c551d0f09401405ca5cf03d56b35fb86 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "bar",
            "name": "\u5546\u5bb61",
            "legendHoverLink": true,
            "data": [
                25,
                67,
                120,
                92,
                78,
                106,
                75
            ],
            "showBackground": false,
            "stack": "stack1",
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb62",
            "legendHoverLink": true,
            "data": [
                31,
                44,
                75,
                30,
                101,
                24,
                52
            ],
            "showBackground": false,
            "stack": "stack1",
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb63",
            "legendHoverLink": true,
            "data": [
                129,
                69,
                36,
                58,
                22,
                59,
                94
            ],
            "showBackground": false,
            "stack": "stack2",
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        },
        {
            "type": "bar",
            "name": "\u5546\u5bb64",
            "legendHoverLink": true,
            "data": [
                99,
                134,
                27,
                110,
                66,
                81,
                103
            ],
            "showBackground": false,
            "stack": "stack2",
            "barMinHeight": 0,
            "barCategoryGap": "20%",
            "barGap": "30%",
            "large": false,
            "largeThreshold": 400,
            "seriesLayoutBy": "column",
            "datasetIndex": 0,
            "clip": true,
            "zlevel": 0,
            "z": 2,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u5546\u5bb61",
                "\u5546\u5bb62",
                "\u5546\u5bb63",
                "\u5546\u5bb64"
            ],
            "selected": {
                "\u5546\u5bb61": true,
                "\u5546\u5bb62": true,
                "\u5546\u5bb63": true,
                "\u5546\u5bb64": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "showContent": true,
        "alwaysShowContent": false,
        "showDelay": 0,
        "hideDelay": 100,
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0,
        "padding": 5
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "axisLabel": {
                "show": true,
                "position": "top",
                "rotate": 30,
                "margin": 8
            },
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "\u540d\u5b57\u5f88\u957f\u7684X\u8f74\u6807\u7b7e1",
                "\u540d\u5b57\u5f88\u957f\u7684X\u8f74\u6807\u7b7e2",
                "\u540d\u5b57\u5f88\u957f\u7684X\u8f74\u6807\u7b7e3",
                "\u540d\u5b57\u5f88\u957f\u7684X\u8f74\u6807\u7b7e4",
                "\u540d\u5b57\u5f88\u957f\u7684X\u8f74\u6807\u7b7e5",
                "\u540d\u5b57\u5f88\u957f\u7684X\u8f74\u6807\u7b7e6"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ],
    "title": [
        {
            "text": "\u65cb\u8f6cx\u8f74\u6807\u7b7e",
            "subtext": "\u89e3\u51b3\u6807\u7b7e\u540d\u8fc7\u957f\u7684\u95ee\u9898",
            "padding": 5,
            "itemGap": 10
        }
    ]
};
        chart_c551d0f09401405ca5cf03d56b35fb86.setOption(option_c551d0f09401405ca5cf03d56b35fb86);
            window.addEventListener('resize', function(){
                chart_c551d0f09401405ca5cf03d56b35fb86.resize();
            })
    </script>
</body>
</html>

```



<ActionBox />
