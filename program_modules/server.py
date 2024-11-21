import socket
import pickle
from .grid import Grid

def start_server():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        client_grid = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]
        ]

        client_grid2 = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]
        ]

        server_socket.bind(("SERVER_IP", 8082))

        server_socket.listen(2)
        print("connecting...")

        client_socket, adress = server_socket.accept()
        print("connected:", adress)
        
        client_socket2, adress2 = server_socket.accept()
        print("connected:", adress2)
        
        show = Grid(client_grid)
        print("player grid")
        show.show_grid()
        
        show2 = Grid(client_grid2)
        print("enemy grid")
        show2.show_grid()
        
        while True:
            data = client_socket.recv(1024)
            
            if data:
                print("player grid")
                show = Grid(pickle.loads(data))
                show.show_grid()
                print("enemy grid")
                show2.show_grid()
                client_grid = client_socket2.sendall(data)

            data2 = client_socket2.recv(1024)

            if data2:
                print("player grid")
                show.show_grid()
                print("enemy grid")
                show2 = Grid(pickle.loads(data2))
                show2.show_grid()
                client_grid2 = client_socket.sendall(data2)
               
start_server()