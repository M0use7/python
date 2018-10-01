"""__author__ = 唐宏进 """
import socket

server = socket.socket()

server.bind(('10.7.153.120', 1234))

server.listen(512)

while True:
    while True:
        connect,addr = server.accept()
        print('正在监听')
        print(addr)

        data = connect.recv(512)
        if data.decode() == '拜拜':
            break
        print(data.decode())

        msg = input('服务器:')
        if msg == '拜拜':
            break
        connect.send(msg.encode())
server.close()


