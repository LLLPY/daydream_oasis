---

next: false

---



<BlogInfo id="149"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Label标签</title>
</head>
<body>
1.解释: <br>
<h4>用于绑定一个表单元素,当点击label标签的时候,被绑定的表单元素就会获得输入焦点</h4> <br>
2.例(当点击'输入账号'的时候,会自动跳到输入框): <br>
<label>输入账号: <input type="text" value="123456"></label> <br>
<label>输入密码: <input type="password" value="123"></label> &nbsp;&nbsp;<input type="submit">
<hr> <br>
<!--想要直接定位到某个输入框，可以使用for id的方法实现-->
<label for="two">输入账号: <input type="text" value="123456" id="one"><input id="two" type="text" value="123456"></label> <br>


</body>
</html>
```



<ActionBox />
