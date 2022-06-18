import socket
from typing import Dict
import xml.etree.ElementTree as ET
from datetime import datetime
import sys
#import LOKALNI_UREDJAJ.Digitalni_Analogni
#from LOKALNI_UREDJAJ import Digitalni_Analogni


def Klijent_konekcija():
    print("Izaberite jedan od uredjaja: ")
    print("1.Analogni")
    print("2.Digitalni")
    localDeviceNum = input()
    if localDeviceNum == "1":
        return "ANALOGNI"
    elif localDeviceNum == "2":
        return "DIGITALNI"
    else:
        print("GRESKA U UNOSU!POKUSAJTE PONOVO!")
        print()
        return "ERROR"

def UnosAnalognogUredjaja():
    print("Odabrali ste Analogni uredjaj.")
    print("Id: ")
    idAnalog = input()
    print("Stanje: ")
    stateAnalog = input()
    if(intTryParse(stateAnalog)=="ERROR"):
        print("GRESKA U UNOSU,STANJE MORA BITI CEO BROJ!")
        print()
        return "","ERROR"

    msg = "{0}/{1}/{2}".format(idAnalog, str(datetime.now()), stateAnalog)
    return idAnalog,msg

def UnosDigitalnogUredjaja():
    print("Odabrali ste Digitalni uredjaj.")
    print("Id: ")
    idDigital = input()
    print("Izaberite neko od sledecih stanja: ON, OFF, OPEN, CLOSE")
    stateDigital = input()
    if (stringTryParse(stateDigital)== "ERROR"):
        print("POGRESAN UNOS STANJA.POKUSAJTE PONOVO!")
        print()
        return "","ERROR"
    msg = "{0}/{1}/{2}".format(idDigital, str(datetime.now()), stateDigital)
    return idDigital,msg

def PromenaStanjeDigitalnogUredjaja(idDigital):
        print("Promenite stanje uredjaja(ON,OFF,OPEN,CLOSE): ")
        stateDigital = input()
        if (stringTryParse(stateDigital) == "ERROR"):
            print("NESTE UNELI PODRZANU VREDNOST,POKUSAJTE PONOVO!")
            print()
            return "ERROR"
        msg = "{0}/{1}/{2}".format(idDigital, str(datetime.now()), stateDigital)
        return msg

def PromenaStanjaAnalognogUredjaja(idAnalog):
        print("Promenite vrednost uredjaja: ")
        stateAnalog = input()
        if(intTryParse(stateAnalog)=="ERROR"):
            print("NESTE UNELI PODRZANU VREDNOST,POKUSAJTE PONOVO!")
            print()
            return "ERROR"
        msg = "{0}/{1}/{2}".format(idAnalog, str(datetime.now()), stateAnalog)
        return msg

def PosaljiPoruku(msg,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", port))
    client.send(bytes(msg, 'utf-8'))
    client.close()
    return msg

def Primi_Kontrolere():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost",50098))
    msg="t"
    client.send(bytes(msg, 'utf-8'))
    msg=client.recv(1024)
    msg = msg.decode("utf-8")
    client.close()
    return msg

def Upisi_Kontrolere(msg):
    lista = ET.parse("C:\\Users\\MSI\\Documents\\GitHub\\res-tim19\\LOKALNI_UREDJAJ\\LokalnaListaKontrolera.xml")
    root = lista.getroot()
    root.clear()
    a=msg.split('&')

    for x in range(0, len(a)-1):
        y=a[x].split('/')

        kontroler = ET.SubElement(root, 'Kontroler')

        portt = ET.SubElement(kontroler, 'port')

        naziv = ET.SubElement(kontroler, 'naziv')
        portt.text = y[0]

        naziv.text = y[1]
        lista.write("C:\\Users\\MSI\\Documents\\GitHub\\res-tim19\\LOKALNI_UREDJAJ\\LokalnaListaKontrolera.xml")




def Izlistaj_Kontrolere():
     lista=ET.parse("C:\\Users\\MSI\\Documents\\GitHub\\res-tim19\\LOKALNI_UREDJAJ\\LokalnaListaKontrolera.xml")
     root=lista.getroot()
     Dict ={}
     index = 0
     for x in root:
         print("KONTROLER: "+x[1].text+"   PORT:   "+x[0].text)
         Dict[x[0].text] = x[1].text
         pass
     pass
     return Dict

def SviKontroleri():
    lista=ET.parse("C:\\Users\\MSI\\Documents\\GitHub\\res-tim19\\LOKALNI_UREDJAJ\\LokalnaListaKontrolera.xml")
    root=lista.getroot()
    Dict={}
    index=0
    for x in root:
        Dict[x[0].text]=x[1].text
        pass
    pass
    return Dict

def PonovoUnesiStanjeA(state):
    print("Za stanje morate uneti ceo broj: ")
    state = input()
    return intTryParse(state)

def intTryParse(state):
    try:
        return int(state)
    except ValueError:
        return "ERROR"

def PonovoUnesiStanjeD(state):
    print("Za stanje morate uneti ON/OFF/OPEN/CLOSE: ")
    state = input()
    return stringTryParse(state)

def stringTryParse(state):
    if(state == "ON" or state == "OFF" or state =="OPEN" or state == "CLOSE"):
        return "True"
    else:
        return "ERROR"

def Unos_porta():
        print("UNESITE PORT:")
        port = input()
        Dict = {}
        Dict = SviKontroleri()
        for xx in Dict.keys():
            if (port == str(xx)):
                print("POVEZIVANJE SA KONTROLEROM...")
                return(port)

        print("KONTROLER KOJI STE ZAHTEVALI NIJE DOSTUPAN.UNESITE DRUGI PORT:")
        return("ERROR")





