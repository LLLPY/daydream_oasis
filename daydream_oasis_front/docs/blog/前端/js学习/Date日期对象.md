---

next: false

---



<BlogInfo id="235"/>

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Date日期对象</title>
    <script>
        //Date() 日期对象 是一个构造函数 必须使用new来调用我们创建的日期对象
        //创建一个日期对象
        var date1 = new Date(); //如果没有加参数，返回当前系统时间
        console.log(date1);

        var year = date1.getFullYear(); //获取年份
        console.log(year);
        var month = date1.getMonth() + 1; //获取月份(0~11)
        console.log(month);
        var date = date1.getDate(); //获取日期
        console.log(date);
        var day = date1.getDay(); //获取星期(0-星期日，1-星期1,6-星期5)
        var day_arr = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
        console.log(day_arr[day]);
        var hour = date1.getHours(); //时
        console.log(hour);
        var minute = date1.getMinutes(); //分
        console.log(minute);
        var second = date1.getSeconds(); //秒
        console.log(second);
        var time = hour + ':' + minute + ':' + second + ' '
        now_time = year + '年' + month + '月' + date + '日 ' + time + day_arr[day];
        console.log('现在是: ', now_time);
    </script>
</head>

<body>

</body>

</html>
```



<ActionBox />
