"""__author__ = 唐宏进 """
import socket

client = socket.socket()
client.connect(('10.7.153.120', 8080))

# 创建一个空的二进制数据
all_data = bytes()

# 接收从服务器传回来的数据
data = client.recv(1024)
while data:
    print('接收到数据')
    all_data += data
    data = client.recv(1024)

with open('./files/new.jpg', 'wb') as f:
    f.write(all_data)
client.close()