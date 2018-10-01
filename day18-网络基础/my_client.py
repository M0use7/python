"""__author__ = 唐宏进 """
import socket

client = socket.socket()

client.connect(('10.7.153.120', 1234))

while True:
    msg = input('客户端:')
    client.send(msg.encode())
    # if msg == '拜拜':
    #     break

    data = client.recv(512)
    print(data.decode())
client.close()
