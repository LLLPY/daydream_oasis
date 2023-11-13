---

next: false

---



<BlogInfo id="249"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script>
        var arr = [1, 2, 4, 53, 5];

        arr.forEach(function (value, index, arr) {

            document.write(value + ',' + index + ',' + arr + '<br>');
        });


        for (var i = 0; i < arr.length; i++) {

            document.write(arr[i] + ',' + i + arr + '<br>');            
        }


        /*map方法(映射)*/
        var Newarr=arr.map(function (value, index, array) {
            return value*10;  /*这里写映射关系，这里的映射关系是将数组中每个元素扩大10倍*/
        })
        alert(Newarr);
        alert(arr);
    </script>
</head>
<body>


</body>
</html>
```



<ActionBox />
