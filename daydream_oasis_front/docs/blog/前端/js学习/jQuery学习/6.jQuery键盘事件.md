---

next: false

---



<BlogInfo id="334"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>jQuery键盘事件</title>
    <script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js"></script>

    <script>
        /*键盘事件
        *
        * 1.keypress 键被按下
        *   keypress不会触发所有的键(比如alt,ctrl,shift,esc).可以使用keydown()来检查这些键
        * 2.keydown 键按下的过程
        * 3.keyup 键被松开
        *
        * */

        /*文档预加载*/
        $(
            function () {
                var span_tag = $('span');
                $('html').keypress(
                    function (event) {
                        /*显示按下的键的键码*/
                        alert(event.which);
                        span_tag.innerHTML = value;
                    }
                );


            }
        );

    </script>
</head>

<body>

<input type="text">
<span>1</span>
</body>
</html>
```



<ActionBox />
