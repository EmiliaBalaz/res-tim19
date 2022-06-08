from ast import parse
import socket
import time
import sys
import xml.etree.ElementTree as ET
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
        
def Slanje_na_AMS(port):
    while(True):
        start=time.time()
        while((time.time()-start)<=300):
            pass
        xx=time.time()-start
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", port))
        msg=str(xx)
        client.send(bytes(msg, 'utf-8'))
        client.close()

        
def Upisi_u_listu(Port,Ime):
    lista=ET.parse("C:\\Users\\Cvijetin Glisic\\Desktop\\GIT_REPOZITORIJUM\\GIT\\Lokalni Uredjaj\\ListaKontrolera.xml")
    root=lista.getroot()
    
    kontroler=ET.SubElement(root,'Kontroler')
    
    port=ET.SubElement(kontroler,'port')
    
    naziv=ET.SubElement(kontroler,'naziv')
    port.text=str(Port)
    naziv.text=str(Ime)
    lista.write('C:\\Users\\Cvijetin Glisic\\Desktop\\GIT_REPOZITORIJUM\\GIT\\Lokalni Uredjaj\\ListaKontrolera.xml')
    
    
   
    pass

     
def Exit_Handler(Port):
    lista=ET.parse("C:\\Users\\Cvijetin Glisic\\Desktop\\GIT_REPOZITORIJUM\\GIT\\Lokalni Uredjaj\\ListaKontrolera.xml")
    root=lista.getroot()
    
    for x in root:
        if x[0].text==str(Port):
            root.remove(x)
            


    lista.write('C:\\Users\\Cvijetin Glisic\\Desktop\\GIT_REPOZITORIJUM\\GIT\\Lokalni Uredjaj\\ListaKontrolera.xml')

    pass
    
def Izadji_Iz_Aplikacije():
    print("DA BI STE IZASLI IZ APLIKACIJE U BILO KOM TRENUTKU UNESITE \"exit\" i pritisnite ENTER")
    a=0
    while a==0:
        text=input()
        if(str(text)=="exit"):
            a=1
            pass
        pass
    sys.exit()


    




