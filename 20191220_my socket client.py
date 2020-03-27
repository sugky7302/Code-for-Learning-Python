import socket
import time

HOST = '192.168.31.163'  # 服务器的主机名或者 IP 地址
PORT = 7000        # 服务器使用的端口

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setblocking(False)
    while (errno := s.connect_ex((HOST, PORT))) != 0:
        print(f"{errno}錯誤，重新連線中...")
        time.sleep(2.)

    s.sendall(b'hello world')
    data = s.recv(1024)
    print('Received', repr(data))
    time.sleep(5.)

