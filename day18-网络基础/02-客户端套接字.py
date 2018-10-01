"""__author__ = 唐宏进 """
import socket


def create_client():
    # 1.创建套接字对象
    client = socket.socket()

    # 2.连接服务器
    client.connect(('10.7.153.120', 8081))
    while True:
        # 3.接收服务器消息
        data = client.recv(1024)
        print(data.decode(encoding='utf-8'))

        # 4.给服务器发送消息
        message = input('客户端:')
        client.send(message.encode())

    # 5.断开连接
    client.close()

create_client()