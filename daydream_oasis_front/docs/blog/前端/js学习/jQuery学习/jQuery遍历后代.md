---

next: false

---



<BlogInfo id="325"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>jQuery遍历-后代</title>

    <script src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js"></script>

    <script>
        /*
        *
        * 后代是子,孙,曾孙等等
        * 向下遍历DOM树的jQuery方法
        * children() 返回被选元素的所有直接子元素
        * find() 返回被选元素的后代元素,一路向下直到最后一个后代
        * */


        $(function () {

            let grandparents = $("#grandparents");
            let chaildOfGrandparents = grandparents.children();
            let allChaildrenOfGrandparents = grandparents.find("*");
            alert(chaildOfGrandparents.attr("id"));
            for (let i = 0; i < allChaildrenOfGrandparents.length; i++) {

            }


        });


    </script>


</head>
<body>

<div id="grandparents">
    祖父母
    <div id="parents">
        父母
        <div id="children">
            孩子
            <div id="grandchildren">外祖孙</div>
        </div>
    </div>
</div>


</body>
</html>
```



<ActionBox />
