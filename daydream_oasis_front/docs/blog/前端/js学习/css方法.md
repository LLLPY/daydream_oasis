---

next: false

---



<BlogInfo id="217"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>css()方法</title>
    <script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js"></script>
    <script>

        /*
        *
        * css()方法设置或返回被选元素的一个或多个样式属性
        *
        *
        * */

        $(function () {

            /*获取样式*/
            $("#bu1").click(function () {
                alert($('#test').css('width'));

            });

            /*设置样式*/
            $("#bu2").click(function () {
                let test = $('#test');
                test.css('backgroundColor', 'red'); /*一次性仅设置一个样式*/
                test.css({'border': '5px solid purple', 'marginTop': '100px'}); /*一次性设置多个标签*/


            });


        });


    </script>

    <style>
        div {
            width: 100px;
            height: 50px;
            text-align: center;
            border: 1px solid deepskyblue;
            line-height: 50px;
            margin: auto auto;
        }


    </style>

</head>
<body>

<div id="test">hello world!</div>

<button id="bu1">获取样式值</button>
<button id="bu2">设置样式</button>


</body>
</html>
```



<ActionBox />
