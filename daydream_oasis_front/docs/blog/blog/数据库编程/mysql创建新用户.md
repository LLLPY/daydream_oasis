
<BlogInfo title="mysql创建新用户" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=6 category="数据库编程" tag_list="[]" create_time="2022.07.06 16:22:08.575303" update_time="2022.07.06 16:34:39" />

^^^^^^^^^
<p><strong>1.创建用户</strong></p>

<h5>create user &#39;demo&#39;@&#39;localhost&#39; identified by &#39;1234&#39;;</h5>

<p><strong>2.授权(所有权利)</strong></p>

<h5>grant all privileges on *.* to &#39;demo&#39;@&#39;localhost&#39;;</h5>

<p><strong>3.刷新权限</strong></p>

<h5>flush privileges;</h5>

