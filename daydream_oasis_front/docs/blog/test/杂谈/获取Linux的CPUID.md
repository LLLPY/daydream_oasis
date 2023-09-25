
<BlogInfo title="获取Linux的CPUID" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=19 category="杂谈" tag_list="['Linux', 'CPUID']" create_time="2021.07.29 21:10:49.189734" update_time="2021.07.29 21:10:49" />

^^^^^^^^^
<pre>#!/usr/bin/python<br># encoding: utf-8<br>import subprocess<br>def getCpuId():<br>    p = subprocess.Popen(["sudo dmidecode -t 4 | grep ID"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,<br>                         stderr=subprocess.PIPE)<br>    data = p.stdout<br>    lines = []<br>    while True:<br>        line = str(data.readline(), encoding="utf-8")<br>        if line == '
':<br>            break<br>        if line:<br>            d = dict([line.strip().split(': ')])<br>            lines.append(d)<br>        else:<br>            break<br>    return lines<br><br><br>if __name__ == '__main__':<br>    print(getCpuId())<br></pre>
