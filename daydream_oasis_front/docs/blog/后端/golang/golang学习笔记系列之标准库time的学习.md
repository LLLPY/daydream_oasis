
<BlogInfo id="1213" title="golang学习笔记系列之标准库time的学习" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=150 category="golang" tag_list="[]" create_time="2022.11.14 23:05:38.202807" update_time="2022.11.14 23:05:38" />

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp8.itc.cn%2Fq_70%2Fimages03%2F20210221%2Fd778753d6a0d4ab9b685aaf362810c0d.gif&refer=http%3A%2F%2Fp8.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1665661975&t=37860c72d333426b69c936abcb7d5473)

### time

Package time provides functionality for measuring and displaying
time.（用于时间的测量和显示）

#### 基本使用

```golang
//获取当前时间
now := time.Now()
fmt.Printf("now: %v\n", now)
year := now.Year()          //年
month := now.Month()        //月
day := now.Day()            //日
hour := now.Hour()          //时
minute := now.Minute()      //分
second := now.Second()      //秒
nsecond := now.Nanosecond() //纳秒
fmt.Printf("%v-%v-%v:%v:%v:%v:%v\n", year, month, day, hour, minute, second, nsecond)
```


**运行结果**


```shell script
now: 2022-11-14 21:53:00.435701792 +0800 CST m=+0.000115447
2022-November-14:21:53:0:435701792
```

#### 时间戳

时间戳是自1970年1月1日（08:00:00GMT）至当前时间的总秒数。它也被称为Unix时间戳。

```golang
//时间戳
fmt.Printf("now.Unix(): %v\n", now.Unix())           //秒数
fmt.Printf("now.UnixMicro(): %v\n", now.UnixMicro()) //毫秒
fmt.Printf("now.UnixNano(): %v\n", now.UnixNano())   //纳秒

//时间戳转成时间
fmt.Printf("time.Unix(now.Unix(), 0): %v\n", time.Unix(now.Unix(), 0))
```

**运行结果**

```shell script
now.Unix(): 1668434792
now.UnixMicro(): 1668434792741556
now.UnixNano(): 1668434792741556203
time.Unix(now.Unix(), 0): 2022-11-14 22:06:32 +0800 CST
```

#### 时间的"运算"

```golang
//时间的运算
today := now
tomorrow := today.Add(time.Hour * 24) //在当前时间上增加24小时
fmt.Printf("today: %v\n", today)
fmt.Printf("tomorrow: %v\n", tomorrow)

dif := today.Sub(tomorrow) //今天与昨天相差的时间
fmt.Printf("dif: %v\n", dif)

//比较两个时间是否相同
fmt.Printf("today.Equal(tomorrow): %v\n", today.Equal(tomorrow))

//判断当前时间是否在目标时间之前
fmt.Printf("today.Before(tomorrow): %v\n", today.Before(tomorrow))

//判断当前时间是否在目标时间之后
fmt.Printf("today.After(tomorrow): %v\n", today.After(tomorrow))
```

**运行结果**


```shell script
today: 2022-11-14 22:16:35.620284622 +0800 CST m=+0.000048094
tomorrow: 2022-11-15 22:16:35.620284622 +0800 CST m=+86400.000048094
dif: -24h0m0s
today.Equal(tomorrow): false
today.Before(tomorrow): true
today.After(tomorrow): false
```


#### Ticker和Timer

```golang
//定时器Ticker
c := time.Tick(time.Second) //设置一个间隔一秒的定时器
for i := range c {
    fmt.Printf("now: %v\n", i)             //每隔一秒打印一下当前时间
    if i.After(now.Add(time.Second * 3)) { //3秒后停止
        break
    }
}

//Timer
t := time.NewTimer(time.Second * 2)
fmt.Printf("now2: %v\n", time.Now())
<-t.C
fmt.Printf("now2 after 2 seconds: %v\n", time.Now()) //两秒后执行到这里
```


**运行结果**


```shell script
now: 2022-11-14 22:34:08.697290905 +0800 CST m=+1.000982288
now: 2022-11-14 22:34:09.697399128 +0800 CST m=+2.001090512
now: 2022-11-14 22:34:10.697623176 +0800 CST m=+3.001314560
now2: 2022-11-14 22:34:10.697739262 +0800 CST m=+3.001430647
now2 after 2 seconds: 2022-11-14 22:34:12.698702444 +0800 CST m=+5.002393830
```


#### 时间格式化

时间类型有一个自带的Format方法，需要注意的是Go语言中格式化的模板不是常见的Y-m-d
H:M:S，而是使用Go的诞生时间2006年1月2号15点04分（记忆口诀为：2006 1 2 3 4）。

```golang
//时间格式化
fmt.Printf("now.Format(\"2006-01-02 15:04:05.000 Mon Jan\"): %v\n", now.Format("2006/01/02 15:04:05.000 Mon Jan")) //24小时制
fmt.Printf("now.Format(\"Mon Jan 2006-01-02 3:4:4 PM\"): %v\n", now.Format("Mon Jan 2006-01-02 3:4:4.000 PM"))     //12小时制
```


**运行结果**

```shell script
now.Format("2006-01-02 15:04:05.000 Mon Jan"): 2022/11/14 22:44:56.882 Mon Nov
now.Format("Mon Jan 2006-01-02 3:4:4 PM"): Mon Nov 2022-11-14 10:44:44.882 PM
```

#### 解析字符串格式的时间


```golang
//解析字符串格式的时间
loc, _ := time.LoadLocation("Asia/Shanghai")

//第一个参数指定格式，第二参数为字符串格式的时间，第三个参数指定时区
t2, _ := time.ParseInLocation("2006/01/02 15:04:05.000 Mon Jan", "2022/11/11 22:44:56.882 Mon Nov", loc)
fmt.Printf("t2: %T", t2)
fmt.Printf("t2: %v", t2)
```

**运行结果**


```shell script
t2: time.Time
t2: 2022-11-11 22:44:56.882 +0800 CST
```





