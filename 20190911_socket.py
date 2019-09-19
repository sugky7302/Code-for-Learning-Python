import socket
import threading


class SocketClient(threading.Thread):
    '''
    開啟Socket客戶端，與服務端連線，並使用多線程獨立執行。

    Attributes:
        __client (Socket) - 客戶端。
        __close (bool) - 控制線程啟動或終止。
        __data (string) - 儲存服務端來的數據。
    '''

    def __init__(self, host="localhost", port=8000):
        super(SocketClient, self).__init__()
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__close = False
        self.__data = None

        try:
            self.__client.connect((host, port))
            self.__client.setblocking(False)
            self.__client.settimeout(1.)
        except Exception as e:
            print(e)

    @property
    def data(self):
        return self.__data

    def run(self):
        # 確保線程一定會執行一次
        while (not self.__data or not self.__close):
            bit = self.__client.recv(1)
            if bit == b'/':
                data = ''

                while True:
                    c = self.__client.recv(1)
                    if c != b'\r':
                        data += str(c, encoding='utf8')
                    else:
                        break

                # 收滿才更新數據
                self.__data = data
                print(self.__data)
            elif bit == b'':
                break

    def close(self):
        self.__close = True
        self.__client.close()


def main():
    a = SocketClient("172.31.16.63", 8787)
    a.start()

    while True:
        try:
            print(a.data)
        except KeyboardInterrupt as e:
            print(e)
            a.close()
            break


if __name__ == "__main__":
    main()
