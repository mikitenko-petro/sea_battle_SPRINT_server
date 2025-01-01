import socket
import threading

def listen_client(client, other_client):
    while True:
        try:
            data = client.recv(1024)
            if data:
                other_client.sendall(data)

        except ConnectionResetError:
            SERVER.restart = True
            break

        except Exception as error:
            print(error)
            
class Server():
    def __init__(self):
        self.server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        self.IP = socket.gethostbyname(socket.gethostname())
        self.server_socket.bind((self.IP, 2232))
        print(self.IP)

        self.restart = False

    def start_server(self):
        while True:
            self.server_socket.listen()
            print("connecting...")

            client_socket, adress = self.server_socket.accept()
            print("connected:", adress)
            client_socket.sendall("1".encode("utf-8"))

            client_socket2, adress2 = self.server_socket.accept()
            print("connected:", adress2)
            client_socket2.sendall("2".encode("utf-8"))

            thread1 = threading.Thread(target = listen_client, args = (client_socket, client_socket2))
            thread1.start()
            
            thread2 = threading.Thread(target = listen_client, args = (client_socket2, client_socket))
            thread2.start()

            if self.restart:
                self.restart = False
                break     

SERVER = Server()