from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():

    #自定义线程类

    class FileTransferHandler(Thread):

        def __init__(self,cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'

            my_dict['filedata'] = data

            json_str = dumps(my_dict)

            self.cclient.send(json_str.endcode('utf-8'))
            self.cclient.close()

    server = socket()

    server.bind(('0.0.0.0',1111))

    server.listen(512)
    print('服务器启动开始监听。。。')

    with open('guidao.jpg','rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()