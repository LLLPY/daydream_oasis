---

next: false

---



<BlogInfo id="391"/>

###
![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

### sort

sort包提供了排序切片和用户自定义数据集以及相关功能的函数。

sort包主要针对[]int，[]float64，[]string以及其他自定义的切片排序，对于任何类型的切片，只要实现了 **Len** ，
**Less** 和 **Swap** 接口就可以对其进行排序。

sort.Sort默认使用快速排序方法，因此平均时间复杂度为nlog(n)

```golang
// Sort sorts data in ascending order as determined by the Less method.
// It makes one call to data.Len to determine n and O(n*log(n)) calls to
// data.Less and data.Swap. The sort is not guaranteed to be stable.
func Sort(data Interface) {
	n := data.Len()
	quickSort(data, 0, n, maxDepth(n))
}
package main

import (
   "fmt"
   "sort"
)

type Person struct {
   name   string
   age    int
   weight float64
}

type PersonSlice []Person

//实现Len方法，返回切片的长度
func (ps PersonSlice) Len() int {
   return len(ps)
}

//实现Less方法，定义比较规则
func (ps PersonSlice) Less(i int, j int) bool {
   return ps[i].age < ps[j].age //按照年龄进行比较
}

//实现Swap方法，定义交换规则
func (ps PersonSlice) Swap(i int, j int) {
   ps[i], ps[j] = ps[j], ps[i]
}

func main() {

   //对int切片进行排序 []float64和[]string的使用方法同此
   var a []int
   a = []int{5, 1, 3, 2, 4}
   fmt.Printf("排序前:a: %v
", a)
   sort.Ints(a)
   fmt.Printf("排序后:a: %v
", a)
   fmt.Printf("sort.IntsAreSorted(a): %v
", sort.IntsAreSorted(a)) //判断[]int序列是不是增序序列
   fmt.Printf("sort.SearchInts(a, 3): %v
", sort.SearchInts(a, 3)) //查找某一个元素的位置 默认是二分法进行查找

   //对自定义数据类型的切片进行排序
   tom := Person{name: "Tom", age: 18, weight: 66.7}
   jerry := Person{name: "Jerry", age: 16, weight: 56.7}
   jack := Person{name: "Jack", age: 19, weight: 78.1}
   hank := Person{name: "Hank", age: 18, weight: 61.7}
   marry := Person{name: "Marry", age: 20, weight: 55.7}
   var ps PersonSlice
   ps = append(ps, tom, jerry, jack, hank, marry)
   fmt.Printf("排序前ps: %v
", ps)

   sort.Sort(ps)
   fmt.Printf("排序后ps: %v
", ps) //按年龄是增序序列

}
```


**运行结果**
```golang
排序前:a: [5 1 3 2 4]
排序后:a: [1 2 3 4 5]
sort.IntsAreSorted(a): true
sort.SearchInts(a, 3): 2
排序前ps: [{Tom 18 66.7} {Jerry 16 56.7} {Jack 19 78.1} {Hank 18 61.7} {Marry 20 55.7}]
排序后ps: [{Jerry 16 56.7} {Tom 18 66.7} {Hank 18 61.7} {Jack 19 78.1} {Marry 20 55.7}]
```






<ActionBox />
