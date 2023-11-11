---

next: false

---



<BlogInfo id="380" title="django关于数据库保存emoij符合的配置" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="40" category="Django" tag_list="['字符集', '              Django', '              mysql']" create_time="2022.01.20 15:14:28.927453" update_time="2022.07.11 10:57:23" />

不知道你们有没有踩过这个坑，反正我是亲身经历。我在自己的博客网站上编辑博客时，为了增加文章的生动性，时不时添加两个emoij符号也是理所当然的，可是，就当我在写完一篇博客后，满怀期待的点击发布的时候，一片黄底黑字映入了我的眼帘，对web开发有过了解的兄弟，这个场景对你们来说应该时似曾相识吧！???

具体报错如下：

django.db.utils.DataError: (1366, "Incorrect string value: '\xF0\x9F\x98\x80

看到报错，第一时间想到的就是度娘???

最终算是找到了一个比较合理的解释：

[普通的字符串或者表情都是占位3个字节，所以utf8足够用了，但是移动端的表情符号占位是4个字节，普通的utf8就不够用了，为了应对无线互联网的机遇和挑战、避免emoji 表情符号带来的问题、涉及无线相关的 MySQL 数据库建议都提前采用 utf8mb4字符集](https://www.jianshu.com/p/b0f5eb5d7cc3)



所以，解决方案就是将对应的数据库和数据表的字符集修改为utf8mb4，同时配置好django中的连接数据集即可。



### 1.修改数据库的字符集
```mysql
alter database 数据库名 default character set utf8mb4 collate utf8mb4_unicode_ci;**
```

### 2.修改数据表的字符集
```mysql
ALTER TABLE 表名 CONVERT TO CHARACTER SET utf8mb4;**
```

### 3.配置django中数据库连接的字符集
![](http://www.lll.plus/media/image/2022/02/02/image-20220202214819-1.png)

在settings文件的数据库相关配置中，添加options选项的配置，将字符集设置为utf8mb4即可！到这里就配置完成啦！???

如果这篇博客能发表成功就代表我修改成功了，好期待点击发布的那一刻嘿嘿???





















<ActionBox />
