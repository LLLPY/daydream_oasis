
<BlogInfo title="oracle的PL练习" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=27 category="数据库编程" tag_list="['oracle', 'pl', '变量']" create_time="2021.10.14 11:19:46.892824" update_time="2021.10.14 11:19:46" />

^^^^^^^^^
<p>set serveroutput on;<br>declare<br>v_name varchar2(20):='张三';<br>v_age number;<br>v_addr varchar2(200);<br><br>begin<br>v_age:=18; --直接赋值<br>select loc into v_addr from dept where deptno=10;  --语句赋值<br><br>dbms_output.put_line('姓名:'||v_name||' 年龄:'||v_age||' 地址:'||v_addr); --打印输出<br>end;<br><br><br>select * from emp;<br><br><br>--引用型变量<br>declare <br>v_name emp.ename%type;<br>v_sal emp.sal%type;<br><br>begin<br>select ename,sal into v_name,v_sal from emp where empno=7369;<br>dbms_output.put_line('姓名:'||v_name||' 薪水:'||v_sal);<br>end;<br><br>--<br>declare<br>v_emp emp%rowtype;<br>begin<br>select * into v_emp  from emp where empno=7369;<br>dbms_output.put_line('姓名:'||v_emp.ename||' 薪水:'||v_emp.sal);<br>end;<br><br><br><br><br><br><br><br><br><br></p>
