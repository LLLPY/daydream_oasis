
<BlogInfo title="oracle中存储过程的练习" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=20 category="数据库编程" tag_list="['oracle', '存储过程']" create_time="2021.10.27 09:27:04.542097" update_time="2021.10.27 09:27:04" />

^^^^^^^^^
<p><br></p><p>set serveroutput on;<br><br>--定义一个过程（查询指定员工编号的工资）<br>create or replace procedure p_sal_suery <br>(v_pno in emp.empno%type,v_sal out emp.sal%type)<br>as <br>begin<br>select sal into v_sal from emp where empno=v_pno;<br>dbms_output.put_line('内部输出---编号为：'||v_pno||'的工资为：'||v_sal);<br>end;<br><br>--声明两个变量用来接收员工的编号和工资<br>declare<br>v_pno emp.empno%type;<br>v_sal emp.sal%type;<br><br>begin<br>v_pno:=7369;<br>p_sal_suery(v_pno,v_sal);<br>dbms_output.put_line('外部输出---编号为：'||v_pno||'的工资为：'||v_sal);<br>end;​</p>
