---

next: false

---



<BlogInfo id="178"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ECMA6合并对象的方法</title>
</head>
<script>
    window.onload = function () {

        var obj1 = {
            a: 10
        }
        var obj2 = {
            b: 20
        }
        var obj3 = {
            c: 30,
            show: function () {
                alert('show!!!');
            }
        }
        //将obj1,obj2,obj3的所有属性和方法合并到obj1
        Object.assign(obj1,obj2,obj3);
        alert(obj1.show());

    }
</script>
<body>

</body>
</html>
```



<ActionBox />
