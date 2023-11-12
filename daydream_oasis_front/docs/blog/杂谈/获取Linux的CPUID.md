---

next: false

---



<BlogInfo id="1076"/>


```python
#!/usr/bin/python
# encoding: utf-8
import subprocess
def getCpuId():
    p = subprocess.Popen(["sudo dmidecode -t 4 | grep ID"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    data = p.stdout
    lines = []
    while True:
        line = str(data.readline(), encoding="utf-8")
        if line == '
':
            break
        if line:
            d = dict([line.strip().split(': ')])
            lines.append(d)
        else:
            break
    return lines


if __name__ == '__main__':
    print(getCpuId())
```






<ActionBox />
