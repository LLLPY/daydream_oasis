---

next: false

---



<BlogInfo id="81"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>css初始化</title>
    <style>
        /*css初始化*/
        /*1.去除所有的内外边距*/
        * {
           padding:0;
           margin:0;
            }
        /*2.去掉列表的小点*/
        ul {
            list-style:none;
            }
        /*3.清除浮动*/
        .clearfix:before,.clearfix:after {
            display:table;
            content:'';
            }
        .clearfix:after {
            clear:both;
            }
        /*兼容以前的浏览器*/
        .clearfix {
            *zoom:1;
            }



    </style>



</head>
<body>

</body>
</html>
```



<ActionBox />
