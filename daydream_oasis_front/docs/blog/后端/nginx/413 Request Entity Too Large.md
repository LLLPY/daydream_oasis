
<BlogInfo id="414" title="413 Request Entity Too Large" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="5" category="nginx" tag_list="['nginx', '              bug']" create_time="2022.02.02 22:09:54.982326" update_time="2023.03.25 20:00:14.900355" />

今天打算更新一下网站的背景音乐的，结果在上传音乐的时候踩到了这个坑：413 Request Entity Too Large。

原因很简单，如果在nginx中没有配置上传文件的大小，默认只有1M，而我上传的音乐至少都是5M，所有nginx会报错。


