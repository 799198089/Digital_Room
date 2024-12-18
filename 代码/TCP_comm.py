import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("服务器已启动，等待连接...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"连接来自: {addr}")
        data = client_socket.recv(1024)
        rev_str = data.decode()
        class_n = rev_str.split('_')[0]
        loc_x, loc_y, loc_z = float(rev_str.split('_')[1]), float(rev_str.split('_')[2]), float(rev_str.split('_')[3])
        print(f"收到数据: {rev_str}")
        print(f'class:{class_n}; loc_x:{loc_x}; loc_y:{loc_y}; loc_z:{loc_z}')
        client_socket.sendall(f"receiving data".encode())
        client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.27', 12345))
    client_socket.sendall(f"sending data".encode())
    data = client_socket.recv(1024)
    print(f"收到来自服务器的数据: {data.decode()}")
    client_socket.close()


if __name__ == "__main__":
    start_server()