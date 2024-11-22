import socket
import pickle

def start_server():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("127.0.0.1", 8082))

        server_socket.listen(2)
        print("connecting...")

        client_socket, adress = server_socket.accept()
        print("connected:", adress)
        client_socket.sendall("1".encode("utf-8"))
        client_socket2, adress2 = server_socket.accept()
        print("connected:", adress2)
        client_socket2.sendall("2".encode("utf-8"))
        while True:
            data = client_socket.recv(1024)
            
            if data:
                print("send data")
                client_grid = client_socket2.sendall(data)

            data2 = client_socket2.recv(1024)

            if data2:
                print("send data")
                client_grid2 = client_socket.sendall(data2)
               
start_server()