---

next: false

---



<BlogInfo id="182"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>map映射</title>
</head>
<script>

    window.onload = function () {
        
        /*
        *
        * map也是一种集合,但是它每个元素的格式和set不同
        *
        *
        * */

        //创建一个map对象
        let map = new Map();

        //添加数据 map.set(key,value)
        map.set('张三', '打鱼的');
        map.set('李四', '挖煤的');
        map.set('王五', '种地的');
        map.set('张三', '开公司的');

        //取数据 map.get(key)
        alert(map.get('张三'));

        //map的遍历
        for (let [key, value] of map) {
            alert(key + value);
        }


    }


</script>
<body>

</body>
</html>
```



<ActionBox />
