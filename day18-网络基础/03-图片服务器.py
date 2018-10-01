"""__author__ = 唐宏进 """
import socket

# 1.创建套接字对象
server = socket.socket()

# 2.绑定IP地址和端口
server.bind(('10.7.153.120', 8080))

# 3.监听
server.listen(512)

while True:
    # 4.接收请求
    connect,addr = server.accept()

    # 5.发送数据
    with open('./files/cat.jpg', 'rb') as f:
        data = f.read()
    connect.send(data)

    # 6.接收数据
    # connect.recv(512)

    # 7.关闭连接
    connect.close()