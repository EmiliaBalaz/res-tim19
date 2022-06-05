import socket
from Model.LocalDeviceStorage import LocalDeviceStorage
from Model.LocalDevice import LocalDevice


def Konekcija(localDeviceStorage:LocalDeviceStorage,port):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',port))
    server.listen(10)
    print("--SERVER CEKA NOVE KONEKCIJE!--")
    while (True):
        client,client_address=server.accept();
        print()
        print() 
        print("PODACI PRIMLJENI OD: "+str(client_address))
        temp= client.recv(1024);
        msg=temp.decode("utf-8")
        print(str(msg))
        values = msg.split("/")
        localDeviceValue = LocalDevice(values[0], values[1], values[2])
        localDeviceStorage.AddNewDeviceValue(localDeviceValue)
        client.close()
        
        
       




