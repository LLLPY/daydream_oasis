---

next: false

---



<BlogInfo id="224"/>

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>简易ATM</title>
    <script>
        var cash = 0;
        while (true) {
            var index = prompt('请输入您要的操作:\n1.存钱\n2.取钱\n3.显示余额\n0.退出');
            if (index == 1) {
                var money = prompt('请输入存入的金额:');
                cash += Number(money);
                alert('余额:' + '+' + money + ',存款成功!');

            } else if (index == 2) {
                var get_money = prompt('请输入您要取出的金额:');
                cash -= Number(get_money);
                alert('余额:' + '-' + money + ',取款成功!');
            } else if (index == 3) {
                alert('您当前余额为:' + cash);
            } else if (index == 0) {
                alert('欢迎再次使用!!!');
                break;
            } else {
                alert('您的输入有误，请重新输入!!!');

            }
        }
    </script>
</head>

<body>

</body>

</html>
```



<ActionBox />
