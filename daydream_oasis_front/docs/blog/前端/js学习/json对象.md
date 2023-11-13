---

next: false

---



<BlogInfo id="208"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>json对象</title>
    <script src="tools.js"></script>

<script>
    /*
    *
    * json对象
    *
    * JSON.stringify() 数据结构-->json对象
    * JSON.parse()   json对象-->数据结构
    *
    *
    * */
    var arr=[1,'we',true,1.2,new Object()];
    alert(arr);
    //数组转成 json对象
    arrTojson=JSON.stringify(arr);
    alert(arrTojson);
    //json对象转成数组
    jsonToArr=JSON.parse(arrTojson);
    alert(jsonToArr[0]);
    //其他数据类型的转换与之类似

    $ajax('post','my.js',{},null,null);


</script>
</head>
<body>

</body>
</html>
```



<ActionBox />
