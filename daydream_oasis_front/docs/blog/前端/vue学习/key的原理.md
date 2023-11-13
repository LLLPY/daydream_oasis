---

next: false

---



<BlogInfo id="349"/>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>key的原理</title>
    <script src="js/vue.js"></script>

    <div id="root">
        <button @click.once="add">添加老刘</button>
        <ul>
            <li v-for="p in persons" :key="p.id">{{p.name}}-{{p.age}} <input type="text"></li>

        </ul>
    </div>
    <script>

        /*
        *
        * key的内部原理
        *   1.虚拟DOM中key的作用：
        *       key是虚拟DOM对象的标识，当数据发生变化时，Vue会根据新数据生成新的虚拟DOM，
        *       随后Vue进行新虚拟DOM与旧虚拟DOM的差异比较，比较规则如下：
        *           1.旧虚拟DOM中找到了与新虚拟DOM相同的key：
        *               1.若【虚拟DOM】中内容没有发生变化，直接使用之前的【真实DOM】
        *               2.若虚拟DOM中内容变了，则生成新的虚拟DOM，随后替换掉页面之前的真实DOM
        *           2.旧虚拟DOM中未找到与新虚拟DOM相同的key
        *               直接创建新的虚拟DOM，随后渲染到页面
        *
        *   2.用index做key可能会引发的问题（如果不指定key，vue默认使用index做key）：
        *       1.若对数据进行：逆序添加，逆序删除等破坏顺序的操作
        *           会产生没有必要的真实DOM更新 ===>界面效果没有问题，但是效率低！
        *       2.如果结构中还包含输入类的DOM：
        *           会产生错误DOM更新 ===> 界面会出现问题
        *
        *   3.如何选择key？
        *       1.最好使用每条数据的唯一标识作为key，比如手机号，身份证号，学号等
        *       2.如果不存在对数据的逆序添加，逆序删除等破坏顺序的操作，仅用于渲染列表来展示，
        *           使用index作为key即可
        *
        *
        *
        *
        * */


        new Vue({
            el: '#root',
            data: {
                persons: [
                    {id: 1, name: '张三', age: 18},
                    {id: 2, name: '李四', age: 19},
                    {id: 3, name: '王五', age: 20},
                ],
            },
            methods: {
                add() {
                    let liu = {id: 4, name: '老刘', age: 41}
                    //添加到头部
                    this.persons.unshift(liu)
                }
            }
        })
    </script>

</head>
<body>

</body>
</html>
```



<ActionBox />
