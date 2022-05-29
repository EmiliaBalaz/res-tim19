import socket


def Klijent_konekcija():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",50000))
    client.send(bytes("1,18:03,5","utf-8"))
    temp=client.recv(1024)
    msg=temp.decode("utf-8")
    print(str(msg))
   
    client.close()

