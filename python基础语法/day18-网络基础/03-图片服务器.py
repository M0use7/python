"""__author__ = 余婷"""
import socket

if __name__ == '__main__':
    # 1.创建套接字(创建一个座机)
    server = socket.socket()
    # 2.绑定地址(插电话线,绑定电话号码)
    server.bind(('10.7.153.103', 12344))
    # 3.监听(人坐在电话旁)
    server.listen(512)

    # 保证电话可以被打通(等电话)
    while True:
        # 4.接收请求(接电话)
        connect,addrr = server.accept()
        print(addrr)

        # 5.发送数据(讲电话)
        with open('./files/luffy.png','br') as f:
            data = f.read()

        connect.send(data)

        # 6.接收数据(听对方讲话)
        # connect.recv(1024)

        # 7.关闭连接(挂电话)
        connect.close()


