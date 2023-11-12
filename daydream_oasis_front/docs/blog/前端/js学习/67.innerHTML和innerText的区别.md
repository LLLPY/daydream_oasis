---

next: false

---



<BlogInfo id="275"/>

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>innerHTML和innerText的区别</title>
    <script>
        window.onload = function () {

            /*
            * innerHTML:获取标签间的内容 会解析标签
            *
            * innerText:获取标签间的纯文本
            *
            * outerHTML:获取整个节点内容
            *
            *
            * */

            var ddd = document.getElementById('ddd');

            /*alert(ddd.innerHTML);
            alert(ddd.innerText);*/
            alert(ddd.outerHTML); /*<div id="ddd"><em>你好</em><strong>world!</strong></div> 整个标签*/

            ddd.innerHTML = '<h1>hello world!</h1>'; /*这里的h1标签会被解析*/

            ddd.innerText = '<a>你好,世界!</a>';   /*这里的a标签不会被解析,会被当做纯文本看待*/


        }


    </script>


</head>
<body>

<div id="ddd"><em>你好</em><strong>world!</strong></div>


</body>
</html>
```



<ActionBox />
