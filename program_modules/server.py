import socket

def start_server():
    try:
        with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
            server_socket.bind(("192.168.1.14", 2232))

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
                    client_socket2.sendall(data)

                data2 = client_socket2.recv(1024)

                if data2:
                    client_socket.sendall(data2)

    except:
        print("end of work")
               
start_server()