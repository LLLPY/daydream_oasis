---

next: false

---



<BlogInfo id="30"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>认识preserve-3d</title>
    <style>

        body {
            perspective:1000px;  /*增加透视，近大远小 更有3d感*/
            }

        div {
        width:200px;
        margin:100px auto;
        border:3px solid red;
        transform:rotateY(-30deg);
        transform-style:preserve-3d; /*3d显示效果 默认是2d*/


        }

        img{
            border:3px solid blue;
            box-sizing:border-box;
            transform:rotateY(30deg); /*绕y轴旋转*/
        }


    </style>
</head>
<body>

<div>
    <img src="images/erha.gif">
</div>


</body>
</html>
```



<ActionBox />
