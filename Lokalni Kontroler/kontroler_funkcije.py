from ast import parse
import socket
import time
import sys
import xml.etree.ElementTree as ET
import threading
from Model.LocalDeviceStorage import LocalDeviceStorage
from Model.LocalDevice import LocalDevice
#sys.path.insert(0,'..\\AMS\\TimeSim')
from Common.TimeSim import TimeSimulation

putanja_razlika="MSI"


def Konekcija(localDeviceStorage:LocalDeviceStorage,port, naziv, semaphore: threading.Semaphore):
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
        #values = msg.split("/")
        #localDeviceValue = LocalDevice(values[0], values[1], values[2])
        #localDeviceStorage.AddNewDeviceValue(localDeviceValue)
        Upisi_UXML(msg, naziv, port)
        client.close()
        semaphore.release(1)

def napraviXML(naziv, port):
    root = ET.Element("DeviceValues")
    tree = ET.ElementTree(root)
    fileName = str(naziv) + "_" + str(port) + ".xml"
    with open(fileName, "wb") as file:
        tree.write(file)

def Upisi_UXML(msg, naziv, port):
    lista = ET.parse("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\Lokalni Kontroler\\" + naziv + "_" + str(port) + ".xml")
    root = lista.getroot()

    a=msg.split('/')

    uredjaj = ET.SubElement(root, 'DeviceValue')

    tip = ET.SubElement(uredjaj, 'tip')

    deviceCode = ET.SubElement(uredjaj, 'DeviceCode')

    vreme = ET.SubElement(uredjaj, 'TimeStamp')

    value = ET.SubElement(uredjaj, 'ActualValue')

    tip.text = a[0]

    deviceCode.text = a[1]

    vreme.text = a[2]

    value.text = a[3]
    lista.write("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\Lokalni Kontroler\\" + naziv + "_" + str(port) + ".xml")


def IscitavanjePodataka(port, naziv):
    lista = ET.parse("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\Lokalni Kontroler\\" + naziv + "_" + str(port) + ".xml")
    root = lista.getroot()
    while len(root) == 0:
        try:
            lista = ET.parse("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\Lokalni Kontroler\\" + naziv + "_" + str(port) + ".xml")
            root = lista.getroot()
        finally:
            pass

    for x in root:
        tip = x[0].text
        code = x[1].text
        timeStamp = x[2].text
        value = x[3].text
        pass
    pass
    print("Podaci koji su iscitani iz XML-a")
    print(tip, code, timeStamp, value)
    return tip, code, timeStamp, value


       
def Slanje_na_AMS(port, kontrolerPort, naziv, semaphore: threading.Semaphore):
    while (True):
        semaphore.acquire()

        TimeSimulation.COUNT_START()
        while (TimeSimulation.TimePassed() <= 300):  # 300 sekundi-5 minuta
            pass
        xx = TimeSimulation.TimePassed()  # provera samo da li radi
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", port))
        tip, code, timeStamp, value = IscitavanjePodataka(kontrolerPort, naziv)

        msg = "{0}/{1}/{2}/{3}".format(tip, code, timeStamp, value)
        client.send(bytes(msg, 'utf-8'))
        client.close()

        


     
def Exit_Handler(Port,devname):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 50099))

    msg = "{0}/{1}/{2}".format("DELETE", Port, devname)
    client.send(bytes(msg, 'utf-8'))
    client.close()
    return msg


    
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

def Javi_Se_NA_AMS(port,devname):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 50099))


    msg = "{0}/{1}/{2}".format("ADD",port,devname)
    client.send(bytes(msg, 'utf-8'))
    client.close()
    return msg

    




