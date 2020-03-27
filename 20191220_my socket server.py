import socket

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65432        # 监听的端口 （非系统级的端口：大于 1023)
clients = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    s.setblocking(False)
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print("Received")
                break
            conn.sendall(data)
