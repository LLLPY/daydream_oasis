---

next: false

---



<BlogInfo id="210"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JsonP跨域操作</title>

    <script>
        // JSONP的使用流程
        /*
        * 1.先声明一个函数,这个函数有一个变量,这个形参会拿到我们想要的数据
        * 2.在需要下载相应数据的时候,动态创建script标签,将标签src的属性值设为要下载的数据的链接
        * 3.当script插入到页面上的时候,就会调用已经封装好的函数,将我们需要的数据传过来
        *
        *
        * */
        //个人理解:其实就是本地创建一个和异域上相同的函数,需要的时候,在本地调用异域上的那个函数即可

        function download(data) {
            alert('下载的数据:' + data);
        }

    </script>
    <script>
        window.onload = function () {
            var bu = document.getElementById('bu');
            bu.onclick = function () {
            var scriptTag=document.createElement('script');
            scriptTag.src='jsonp.js';
            document.body.appendChild(scriptTag);
            }


        }
    </script>

</head>
<body>
<button id="bu">下载数据</button>
</body>
</html>
```



<ActionBox />
