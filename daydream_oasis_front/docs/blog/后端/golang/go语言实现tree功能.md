---

next: false

---



<BlogInfo id="406"/>

最近在学go语言，刚好学到了文件操作这一块，上班摸鱼间隙实现了一个类似于tree的功能。


```golang
package main

import (
	"fmt"
	"os"
)

func dir_r(dir string, n int) {
	f, err := os.Open(dir)
	if err != nil {
		fmt.Printf("err: %v
", err)
		return
	}
	fi, err2 := f.Readdir(0)
	if err2 != nil {
		fmt.Printf("err2: %v
", err2)
		return
	}
	for _, f_obj := range fi {

		for i := 0; i < n; i++ {
			print("    ")
		}
		print("└──")
		fmt.Println(f_obj.Name())
		if f_obj.IsDir() {
			// n += 1
			dir_r(dir+"/"+f_obj.Name(), n+1)
		}
	}

}

func main() {

	dir_r(".", 0)

}
```

效果如下，还算不错：

![image.cc6edb2ad48711edb70fcd63b0e7ad35.png](http://www.lll.plus/media/image/2023/04/06/image.cc6edb2ad48711edb70fcd63b0e7ad35.png)





<ActionBox />
