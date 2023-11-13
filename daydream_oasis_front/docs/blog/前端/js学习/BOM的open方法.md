---

next: false

---



<BlogInfo id="265"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BOM的open方法</title>
<script>

    /*
    * open()方法
    * 参数:
    *     第一个参数:跳转的url,打开一个新窗口，加载的url
    *     第二个参数: 字符串 给打开的新窗口起一个名(传入这个参数后，浏览器就只会为该url打开一个窗口
    *     ，如果是第一次open，则浏览器会加载一个新的窗口，如果是第n次open(n>1),浏览器这回直接跳转
    *     到已经加载的窗口上去)
    *     第三个参数:
    *            一串特殊含义的字符串(width:新开的窗口的宽度，height:新开的窗口的高度,
    *            left:距离你电脑窗口左边框我的距离，top：距离你电脑窗口顶部的距离(等等还有很多其他属性))
    *
    * */


   window.onload=function () {

        var ts=document.getElementById('ts');
    ts.onclick=function () {
        window.open('https://www.max-lvll.cn/','ts','width=400,height=400,left=100,top=100');

    }

   }
</script>
</head>
<body>
<a id="ts" href="#">打开新标签</a>

</body>
</html>
```



<ActionBox />
