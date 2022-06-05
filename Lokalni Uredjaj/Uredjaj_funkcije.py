import socket
from datetime import datetime

def Klijent_konekcija(port):
    print("Izaberite jedan od uredjaja: ")
    print("1.Analogni")
    print("2.Digitalni")
    localDeviceNum = input()
    if localDeviceNum == "1":
        print("Odabrali ste Analogni uredjaj.")
        print("Id: ")
        idAnalog = input()
        print("Stanje: ")
        stateAnalog = input()
        msg="{0}/{1}/{2}".format(idAnalog,str(datetime.now()),stateAnalog)
        PosaljiPoruku(msg,port)
        while True:
            print("Promenite vrednost uredjaja: ")
            stateAnalog = input()
            msg="{0}/{1}/{2}".format(idAnalog,str(datetime.now()),stateAnalog)
            PosaljiPoruku(msg,port)
    elif localDeviceNum == "2":
        print("Odabrali ste Digitalni uredjaj.")
        print("Id: ")
        idDigital = input()
        print("Izaberite neko od sledecih stanja: ON, OFF, OPEN, CLOSE")
        stateDigital = input()
        msg = "{0}/{1}/{2}".format(idDigital, str(datetime.now()), stateDigital) 
        PosaljiPoruku(msg,port)
        while True:
            print("Promenite stanje uredjaja: ")
            stateDigital = input()
            msg="{0}/{1}/{2}".format(idDigital, str(datetime.now()), stateDigital)
            PosaljiPoruku(msg,port)

def PosaljiPoruku(msg,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", port))
    client.send(bytes(msg, 'utf-8'))
    client.close()
