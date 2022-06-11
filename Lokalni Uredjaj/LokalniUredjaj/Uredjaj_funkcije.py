import socket
from typing import Dict
import xml.etree.ElementTree as ET
from datetime import datetime
import sys
import LokalniUredjaj.Digitalni_Analogni
from LokalniUredjaj import Digitalni_Analogni


def Klijent_konekcija(port):
    print("Izaberite jedan od uredjaja: ")
    print("1.Analogni")
    print("2.Digitalni")
    localDeviceNum = input()
    if localDeviceNum == "1":
        UnosAnalognogUredjaja(port)
    elif localDeviceNum == "2":
        UnosDigitalnogUredjaja(port)

def UnosAnalognogUredjaja(port):
    print("Odabrali ste Analogni uredjaj.")
    print("Id: ")
    idAnalog = input()
    print("Stanje: ")
    stateAnalog = input()
    intTryParse(stateAnalog)
    msg = "{0}/{1}/{2}".format(idAnalog, str(datetime.now()), stateAnalog)
    PosaljiPoruku(msg, port)
    while True:
        PromenaStanjaAnalognogUredjaja(port, idAnalog)

def UnosDigitalnogUredjaja(port):
    print("Odabrali ste Digitalni uredjaj.")
    print("Id: ")
    idDigital = input()
    print("Izaberite neko od sledecih stanja: ON, OFF, OPEN, CLOSE")
    stateDigital = input()
    if (stringTryParse(stateDigital) != True):
        stringTryParse(stateDigital)
    msg = "{0}/{1}/{2}".format(idDigital, str(datetime.now()), stateDigital)
    PosaljiPoruku(msg, port)
    while True:
        PromenaStanjeDigitalnogUredjaja(port, idDigital)


def PromenaStanjeDigitalnogUredjaja(port, idDigital):
    print("Da li zelite da promenite stanje uredjaja? ")
    print("1.DA")
    print("2.NE")
    odgovor = input()
    if odgovor == "1":
        print("Promenite stanje uredjaja: ")
        stateDigital = input()
        if (stringTryParse(stateDigital) != True):
            stringTryParse(stateDigital)
        msg = "{0}/{1}/{2}".format(idDigital, str(datetime.now()), stateDigital)
        PosaljiPoruku(msg, port)
        return Digitalni_Analogni.Digitalni_Uredjaj(idDigital, str(datetime.now()), stateDigital)
    elif odgovor == "2":
        sys.exit();

def PromenaStanjaAnalognogUredjaja(port, idAnalog):
    print("Da li zelite da promenite stanje uredjaja? ")
    print("1.DA")
    print("2.NE")
    odgovor = input()
    if odgovor == "1":
        print("Promenite vrednost uredjaja: ")
        stateAnalog = input()
        intTryParse(stateAnalog)
        msg = "{0}/{1}/{2}".format(idAnalog, str(datetime.now()), stateAnalog)
        PosaljiPoruku(msg, port)
        return Digitalni_Analogni.Analogni_Uredjaj(idAnalog, str(datetime.now()), stateAnalog)
    elif odgovor == "2":
        sys.exit();

def PosaljiPoruku(msg,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", port))
    client.send(bytes(msg, 'utf-8'))
    client.close()

def Izlistaj_Kontrolere():
     lista=ET.parse("C:\\Users\\MSI\\Documents\\GitHub\\res-tim19\\Lokalni Kontroler\\Model\\ListaKontrolera.xml")
     root=lista.getroot()
     for x in root:
         print("KONTROLER: "+x[1].text+"   PORT:   "+x[0].text)
         pass
     pass

def SviKontroleri():
    lista=ET.parse("C:\\Users\\MSI\\Documents\\GitHub\\res-tim19\\Lokalni Kontroler\\Model\\ListaKontrolera.xml")
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
        return int(state), True
    except ValueError:
        return PonovoUnesiStanjeA(state)

def PonovoUnesiStanjeD(state):
    print("Za stanje morate uneti ON/OFF/OPEN/CLOSE: ")
    state = input()
    return stringTryParse(state)

def stringTryParse(state):
    if(state == "ON" or state == "OFF" or state =="OPEN" or state == "CLOSE"):
        return True
    else:
        return PonovoUnesiStanjeD(state)


