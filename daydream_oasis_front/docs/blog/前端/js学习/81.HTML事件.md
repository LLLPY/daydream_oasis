---

next: false

---



<BlogInfo id="291"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML事件</title>
    <script src="tools.js"></script>
    <script>

        returnEvnetObject()

        /*
      * 事件类型的种类:
      * 一鼠标事件:
      *   click:单击
      *   dblclick:双击
      *   mouseover:鼠标移入
      *   mouseout:鼠标移出
      *
      *   mousemove:鼠标移动(会不停的触发)
      *   mouseenter:鼠标移入
      *   mouseleave:鼠标移出
      *   mouseup:鼠标抬起
      *
      * 二.
      *   键盘事件
      *   keydown 键盘按下(如果按下不松手会一直触发)
      *   keyup 键盘抬起
      *
      *   keypress 键盘按下(只支持字符键,比如像ctrl就不是字符键)
      *
      * 三.HTML事件
      *   1.window事件
      *    load 当界面加载完成以后会触发
      *    unload 当页面解构的时候会触发(例如刷新页面,关闭页面的时候) 仅IE浏览器兼容
      *    scroll 页面滚动的时候会触发
      *    resize 窗口大小发生变化后会触发
      *
      *
      *   2.表单事件
      *     blur 失去焦点时触发
      *     focus 获取焦点时触发
      *     select 输入框框中的内容被选中时触发
      *     change 输入框中的内容被修改并失去焦点时触发
      *
      *     [注]必须添加在form表单元素上的
      *     submit 当我们点击submit上的按钮才能触发
      *     reset 当我们点击reset上的按钮才能触发
      *
      *
      * */

        window.onload = function () {
            var i = 1;
            setInterval(function () {
                var newdiv = document.createElement('div');
                var BODY = document.body;
                newdiv.innerHTML = 'hello world!!!' + i.toString();
                // newdiv.style.display = 'inline-block';
                BODY.appendChild(newdiv);
                i += 1;
            }, 100)
            alert('页面加载完毕!!!');


            var input1 = document.getElementById('inpu1');
            input1.onblur = function () {
                this.placeholder = '失去焦点!!!';
            }
            input1.onfocus = function () {
                this.placeholder = '获取焦点!!!';
            }
            input1.onselect = function () {
                alert('被选中!!!');
            }
            input1.onchange = function () {
                alert('输入框中的内容被修改为:' + this.value);
            }

            var f1=document.getElementById('f1');
            f1.onsubmit=function () {
                alert('提交成功!!!');
            }
            f1.onreset=function () {
            alert('重置成功!!!');
            }



        }

        window.onscroll = function () {
            alert('您滚动了页面!!!');
        }


        window.onunload = function () {

            var r = window.confirm('是否确认关闭页面?');
            if (r === true) {
                alert('页面关闭!!!');
                a
            } else {
                alert('您取消了!!!');
            }
        }

        window.onresize = function () {
            alert('窗口大小发生了改变!!!');
        }


    </script>
</head>
<body>

<form action="#" id="f1">
    <input type="text" placeholder="请输入内容" id="inpu1">
    <input type="submit" placeholder="请输入内容" id="inpu2">
    <input type="reset" placeholder="请输入内容" id="inpu3">


</form>

</body>
</html>
```



<ActionBox />
