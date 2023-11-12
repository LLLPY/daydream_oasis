---

next: false

---



<BlogInfo id="886"/>

```python
from socket import AF_INET, SOCK_STREAM, socket
from time import ctime

HOST = '127.0.0.1'  # HSOT变量是空白的，这是对bind()方法的标识，标识它可以使用任何可用的地址
PORT = 1111
BUFSIZ = 1024  # 将缓冲区的大小设置为1kb
ADDR = (HOST, PORT)  # 服务器地址

# 创建TCP服务器套接字
tcpserSocket = socket(AF_INET, SOCK_STREAM)
tcpserSocket.bind(ADDR)  # 绑定服务器地址
tcpserSocket.listen(5)  # 开启监听 listen()方法的参数是在连接被被转接或拒绝之前，传入请求的最大数
while True:
    print('waiting for connect....')
    tcpCliSock, addr = tcpserSocket.accept() #接受客户端的连接(若连接成功，返回客户端对象和其地址)
    print('...connected from:', addr) #客户端的地址信息
    while True:
        data = tcpCliSock.recv(BUFSIZ) #最大接收1kb大小的数据
        # if not data: #如果客户端发送过来的数据为空着退出循环，关闭连接(在这之前已经与客户端连接成功,但服务器未关闭，任处于服务状态)
        #     break
        print('(客户端):',(data.decode('utf-8'))) #打印来自客户端的消息
        content=input('(服务端):')
        data='(服务端):'+content
        tcpCliSock.send('{}'.format(data).encode('utf-8'))
    tcpCliSock.close()
tcpserSocket.close()

```



<ActionBox />
