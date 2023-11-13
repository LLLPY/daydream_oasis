---

next: false

---



<BlogInfo id="156"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>input的常用新属性</title>
</head>
<body>
<form>
<table width="700" height="300" border="1" cellspacing="0">
    <caption>input的常用新属性</caption>
    <thead>
    <tr>
        <th>属性</th>
        <th>用法</th>
        <th>含义</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>placeholder</td>
        <td><input type="text"  placeholder="请输入用户名"></td>
        <td>占位符提供可描述输入字段预期值的提示信息(当用户输入的时候，里面的提示消息立即消失)</td>
    </tr>
    <tr>
        <td>autofocus</td>
        <td><input type="text" autofocus></td>
        <td>规定当页面加载时，input元素应该自动获得焦点(当打开一个页面时,将光标自动定位到该输入框)</td>
    </tr>
    <tr>
        <td>multiple</td>
        <td><input type="file" multiple></td>
        <td>多文件上传(可以同时上传多个文件,按住Ctrl键多选文件)</td>
    </tr>
    <tr>
        <td>autocomplete</td>
        <td><input type="text" autocomplete="on" name="user"></td>
        <td>规定表单是否应该启用自动完成功能，on:启用,off:不启用(就是在用户第一次输入后,在第二次输入时会提示自动补全),
            使用该功能有两个条件:1.必须要有提交按钮，2.必须给这个表单一个名字(名字随意取)
        </td>
    </tr>
    <tr>
        <td>required</td>
        <td><input type="text" required></td>
        <td>必填项(表单不能为空)</td>
    </tr>
    <tr>
        <td>accesskey</td>
        <td><input type="text" accesskey="s"></td>
        <td>规定激活(使元素获得焦点)元素的快捷键(就是跳转到指定输入框的快捷键),采用alt+字母的形式</td>
    </tr>


    </tbody>
</table>
<br>
<input type="submit">
</form>
</body>
</html>
```



<ActionBox />
