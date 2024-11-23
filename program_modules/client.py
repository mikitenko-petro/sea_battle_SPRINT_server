import socket
import pickle



def client():
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 8082))
        
