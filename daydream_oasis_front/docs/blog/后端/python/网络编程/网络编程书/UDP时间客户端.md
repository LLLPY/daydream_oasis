---

next: false

---



<BlogInfo id="889"/>

```python
from socket import socket,AF_INET,SOCK_DGRAM

host='127.0.0.1'
port=1112
bufsize=1024
addr=(host,port)

#创建udp客户端套接字
udpclisockcet=socket(AF_INET,SOCK_DGRAM)
#绑定服务器端口
udpclisockcet.bind(addr)
#连接服务端
while True:
    data=input('>')
    if not data:
        udpclisockcet.sendto(data,addr)
        data,addrs=udpclisockcet.recvfrom(bufsize)
    #print(data)
udpclisocket.close()

```



<ActionBox />
