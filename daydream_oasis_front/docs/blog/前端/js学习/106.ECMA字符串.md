---

next: false

---



<BlogInfo id="176"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ECMA6字符串</title>
</head>
<script>
    window.onload = function () {

        /*
        *
        * 传统字符串:所有由单引号或双引号括起来的都叫字符串
        * ECMA6字符串:由反引号括起来 ``
        *   1.ECMA6字符串,想怎么写就怎么写,换行,代码缩进都能在字符串中体现出来
        *   2.占位符的使用 ${变量/表达式/函数调用}
        *
        *
        *
        * */

        function show({name, age, sex}) {
            alert(`我叫${name},今年${Math.min(age, 20, 30, 40)}岁,是一名${sex}性`);
        }

        show({
            name: '小明',
            age: 18,
            sex: '男'
        })


    }


</script>
<body>

</body>
</html>
```



<ActionBox />
