import socket


def Klijent_konekcija():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",50001))
    
    while(True):
        msg = input("Unesi vrednost : ")
        client.send(bytes(msg, 'utf-8'))
