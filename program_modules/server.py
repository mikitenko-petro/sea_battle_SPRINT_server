import socket

def start_server():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("192.168.1.14", 2232))

        server_socket.listen(2)
        print("connecting...")

        client_socket, adress = server_socket.accept()
        print("connected:", adress)

        client_socket.sendall("you connected".encode("utf-8"))
        
        client_socket2, adress2 = server_socket.accept()
        print("connected:", adress2)

        client_socket2.sendall("you connected".encode("utf-8"))

        while True:
            data = client_socket.recv(1024)
            
            if data:
                print("send data to client 2")
                client_socket2.sendall(data)

            data2 = client_socket2.recv(1024)

            if data2:
                print("send data to client 1")
                client_socket.sendall(data2)
               
start_server()