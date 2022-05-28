import socket
def Konekcija():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',50000))
    server.listen(10)
    print("--SERVER CEKA NOVE KONEKCIJE!--")
    while(True):
        client,client_address=server.accept();
        print()
        print()
        print("PODACI PRIMLJENI OD: "+str(client_address))
        client.send(bytes("SERVER JE USPESNO PRIMIO PODATKE","utf-8"))
        temp= client.recv(1024);
        msg=temp.decode("utf-8")
        print(str(msg))
        
        client.close()
        
        
       




