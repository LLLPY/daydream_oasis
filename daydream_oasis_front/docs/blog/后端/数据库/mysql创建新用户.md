
<BlogInfo id="997" title="mysql创建新用户" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="6" category="数据库编程" tag_list="['']" create_time="2022.07.06 16:22:08.575303" update_time="2022.07.06 16:34:39" />

**1.创建用户**

##### create user 'demo'@'localhost' identified by '1234';

**2.授权(所有权利)**

##### grant all privileges on *.* to 'demo'@'localhost';

**3.刷新权限**

##### flush privileges;


