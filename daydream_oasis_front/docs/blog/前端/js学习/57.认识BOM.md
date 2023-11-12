---

next: false

---



<BlogInfo id="264"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>认识BOM</title>
<script>
    /*
    * BOM: browser object model(浏览器对象模型)
    *
    *
    * 系统对话框:
    * window方法(一般情况下，window可以省略)
    * window.alert(); 弹出警告框
    *
    * window.confirm(); 弹出一个选择选择框(确定和取消)
    * 返回值:
    *       如果点击确定则返回:ture false
    *       如果点击取消则返回:false
    *
    * window.prompt(); 弹出一个带输入框的提示框
    * 参数:
    *       第一个参数:面板上显示的内容
    *       第二个参数:输入框内的默认值(可以不传入)
    *返回值:
    *       点击确定:返回输入框中的内容
    *       点击取消:返回null
    *
    *
    * */
    window.alert('hello world!');
   /* alert('hello world!');*/
    var res =window.confirm('确定离开吗?');
    alert(res);
    if(res){
        window.close();
    }

    var res2=prompt('你多大了?','18');
    alert(res2);



</script>

</head>
<body>

</body>
</html>
```



<ActionBox />
