import socket

def client():
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("192.168.0.196", 8082))
        client_check = client_socket.recv(1024).decode("utf-8")
        if client_check == "1":
            client_socket.sendall("2".encode("utf-8"))
            data = client_socket.recv(1024)
            if data:
                print(data.decode("utf-8"))  
        elif client_check == "2":
            data = client_socket.recv(1024)
            if data:
                print(data.decode("utf-8"))
            client_socket.sendall("2".encode("utf-8"))
            