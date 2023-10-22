
<BlogInfo id="1357" title="linux下程序重启脚本" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=103 category="杂谈" tag_list="['可控自启', 'Linux', '脚本']" create_time="2021.09.04 20:24:53.472234" update_time="2021.09.04 20:24:53" />

前言:最近一直在做一个项目,具体要求我就不一一概述了,但其中有一个功能是这样的:当程序的大部分采集功能丧失时,需要对程序进行重启恢复,但是由于程序启动了tcp服务端,在程序内部重启时,如果不将旧的程序kill掉,后来启动的程序由于端口一直被旧的程序占用着,所以tcp服务一直启动失败(这里程序的tcp服务使用的是固定的端口),即一直处于阻塞状态.

为了解决这个问题,我写了另外的一个脚本,其主要功能就是:先找到旧的程序的pid,通过pid将其kill掉,然后再启动新的程序.(同时启动新的程序的那个线程不能是阻塞的)

**大体流程:整个程序一直处于监听状态,每隔5秒钟读取指定的"dac_settings.json"文件,一旦接收到信号值signal=1时,就执行杀死旧程序的命令和重启新的程序(通过额外的线程来实现,否则程序会一直处于阻塞状态,监听功能就会失效),完成上述两个功能后,将signal的值赋为1并写入配置文件.**


源码如下:

```python
from re import findall
from os import system
from time import sleep
from json import load, dump
from threading import Thread


class MyJson:
    path = 'dac_settings.json'

    @classmethod
    def openFile(cls):
        return load(open(MyJson.path, 'r', encoding='utf8'))

    @classmethod
    def getdata(cls, key='signal'):
        try:
            data = MyJson.openFile()
            return data[key]
        except:  # 如果读取失败,默认返回1 即需要重启软件
            return 1

    @classmethod
    def setdata(cls, key, value):
        data = MyJson.openFile()
        data[key] = value
        dump(data, open(MyJson.path, 'w', encoding='utf8'), indent=2)


# 杀死并重启程序2--通过寻找到程序的pid之后,再对程序进行杀死
def killprocessAndsetup2(processPath):
    print(f'start to kill processing...')

    fileName = 'demo.txt'  # 将终端返回的内容保存在文件中
    system(f'ps aux | grep dac > {fileName}')
    with open(f'{fileName}', 'r', encoding='utf8') as f:

        content = f.read().split('
')

        for line in content:
            pidList = findall(r'.*./dac', line)  # 找到程序dac的pid并将其kill掉
            if len(pidList) > 0:
                lineList = line.split(' ')

                while True:
                    try:
                        if lineList.index('') != -1:
                            lineList.remove('')
                    except:
                        break
                pid = lineList[1]  # 进程的id
                print(f'{pid} be killed...')
                system(f'kill -9 {pid}')
    # 如果上述代码执行成功,说明已成功杀死旧程序 然后将signal的值设为0
    MyJson.setdata('signal', '0')  # 先将signal的设为0,否则程序会进入死循环


# 执行启动命令
def excute_setup(processPath):
    system(processPath)


# 重启程序 只要signal的值为1就对程序进行进行重启
def resetup(processPath):
    print('setup the dac...')
    th = Thread(target=excute_setup, args=(processPath,))

    th.start()  # 非阻塞

    print('setup the dac done...')
    sleep(5)


# 一直监听signal的值,只要signal的值变为了1,就将程序杀死并重新启动
def watch(processPath):
    while True:
        if str(MyJson.getdata()) == '1':  # 获取信号值
            try:
                killprocessAndsetup2(processPath=processPath)
                print('killed the dac...')

                resetupThread = Thread(target=resetup, args=(processPath,))
                resetupThread.start()

            except Exception as res:
                print(f'程序杀死失败!---{res}')

        sleep(5)


if __name__ == '__main__':
    processPath = './dac &'
    watch(processPath=processPath)
```


  

  

  

  


