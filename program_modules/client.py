import socket
import pickle

sea = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]]
sea_enemy = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]]

def client(sea, sea_enemy):
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 8082))
        #data = client_socket.recv(1024)
        check_list = client_socket.decode("utf-8")
        if check_list == "1":
            while True:
                row = int(input("куда поставить?")) 
                column = int(input("куда поставить?"))
                sea[row-1][column-1] = "X"
                message = pickle.dumps(sea)
                client_socket.sendall(message)
                print("-----------------------------------------")
                print("player grid")
                for row in sea:
                    print(row)
                print("-----------------------------------------")
                print("enemy grid")
                for row in sea_enemy:
                    print(row)
                print("-----------------------------------------")
                print(f"send: {sea}" )
                data = client_socket.recv(1024)
                if data:
                    print("-----------------------------------------")
                    print("player grid")
                    for row in sea:
                        print(row)
                    print("-----------------------------------------")
                    print("enemy grid")
                    for row in pickle.loads(data):
                        print(row)
                    print("-----------------------------------------")
                    sea_enemy = pickle.loads(data)
                    #
                    #sea = pickle.loads(data)
                    #sea[row-1][column-1] = "X"
                    #message = pickle.dumps(sea)
                    #
        elif check_list == "2":
            while True:
                data = client_socket.recv(1024)
                if data:
                    print("-----------------------------------------")
                    print("player grid")
                    for row in sea:
                        print(row)
                    print("-----------------------------------------")
                    print("enemy grid")
                    for row in pickle.loads(data):
                        print(row)
                    print("-----------------------------------------")
                    #
                    #sea = pickle.loads(data)
                    #sea[row-1][column-1] = "X"
                    #message = pickle.dumps(sea)
                    #
                row = int(input("куда поставить?")) 
                column = int(input("куда поставить?"))
                sea[row-1][column-1] = "X"
                message = pickle.dumps(sea)
                client_socket.sendall(message)
                print(f"send: {sea}" )
                print("-----------------------------------------")
                print("player grid")
                for row in sea:
                    print(row)
                print("-----------------------------------------")
                print("enemy grid")
                for row in pickle.loads(data):
                    print(row)
                print("-----------------------------------------")
#client()    
client(sea, sea_enemy)    