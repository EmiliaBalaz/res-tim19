import socket
import select, socket
import xml.etree.ElementTree as ET


putanja_razlika="MSI"


#class AMSService:
    #def __init__(self, servicePort):
        #self.servicePort = servicePort
        #self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.server.setblocking(0)

        #self.server.bind(('localhost',self.servicePort))
        #self.server.listen(10)
        #self.inputs = [self.server]

    #def Listen(self):
        #print("--SERVER CEKA NOVE KONEKCIJE!--")
        #while self.inputs:
            #readable, _, _ = select.select(self.inputs, [],[])
            #for s in readable:
                #if s is self.server:
                    #connection, client_address = s.accept()
                    #connection.setblocking(0)
                    #self.inputs.append(connection)
                #else:
                    #data = s.recv(1024)
                    #if data:
                        #print(data)
                    #else:
                        #self.inputs.remove(s)
                        #s.close()
from Konekcija.KonekcijaSaBazom import konekcijaBaze


def Konekcija(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('localhost', port))

    server.listen(1000)
    print("--SERVER CEKA NOVE KONEKCIJE!--")
    while (True):
        client, client_address = server.accept();
        print()
        print()
        print("PODACI PRIMLJENI OD: " + str(client_address))
        temp = client.recv(1024);
        msg = temp.decode("utf-8")
        print(str(msg))
        try:
            upisUTabelu(msg)
        except:
            client.close()
        client.close()
    server.close()


def podelaPoruke(msg):
    values = msg.split('/')
    tip = values[0]
    localDeviceCode = values[1]
    vreme = values[2]
    actualValue = values[3]
    return tip, localDeviceCode, vreme, actualValue

def upisUTabelu(msg):
    tip, code, vreme, value = podelaPoruke(msg)
    if tip == "1":
        upitAnalogni = "INSERT INTO amsschema.localdevice (DeviceCode, Vreme, ActualValue) VALUES" + "(" + "\'" + code + "\'" + "," + "\'" + vreme + "\'" + "," + value + ")"
        konekcijaBaze(upitAnalogni)
    elif tip == "2":
        upitDigitalni = "INSERT INTO amsschema.localdevicedigital (DeviceCode, Vreme, ActualValue) VALUES" + "(" + "\'" + code + "\'" + "," + "\'" + vreme + "\'" + "," +"\'" + value + "\'" + ")"
        konekcijaBaze(upitDigitalni)

def izlistajSveAnalogneUredjaje():
    upitIzlistaj = "SELECT DISTINCT DeviceCode from amsschema.localdevice"
    return konekcijaBaze(upitIzlistaj)

def izlistajSveDigitalneUredjaje():
    upitIzlistaj = "SELECT DISTINCT DeviceCode from amsschema.localdevicedigital"
    return konekcijaBaze(upitIzlistaj)


def iscitavanjeRadnihMinuta():
    lista = ET.parse("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\AMS\\limitRadnihSati.xml")
    root = lista.getroot()
    radniMinuti = root[0].text
    return radniMinuti

def brSatiPrekoKonfigurisaneVrednostiAnalogni():
    upit = "SELECT DeviceCode, max(Vreme), min(Vreme) from amsschema.localdevice group by DeviceCode"
    return konekcijaBaze(upit)

def brSatiPrekoKonfigurisaneVrednostiDigitalni():
    upitD = "SELECT DeviceCode, max(Vreme), min(Vreme) from amsschema.localdevicedigital group by DeviceCode"
    return konekcijaBaze(upitD)

def Logovanje_liste_kontrolera():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('localhost', 50099))

    server.listen(10)


    client, client_address = server.accept();
    print()
    print()

    temp = client.recv(1024);
    msg = temp.decode("utf-8")
    client.close()
    server.close()
    return msg

def Brisaje_Dodavanje_Kontrolera(msg):
    temp=msg.split('/')
    operation = temp[0]
    devname=temp[2]
    devport=temp[1]
    if (operation == "ADD"):
        print("=================================")
        print("NOVI KONTROLER" + devname + " SA PORTOM" + devport + "JE AKTIVAN")
        print("=================================")
        print()
        print()

    if (operation == "DELETE"):
        print("=================================")
        print("KONTROLER" + devname + " SA PORTOM" + devport + "PRESTAJE SA RADOM")
        print("=================================")
        print()
        print()

    return operation,devport,devname


def Delete_Kontroler(devname,port):
    lista = ET.parse(
        "C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")

    root = lista.getroot()

    forTest="NONE"
    for x in root:
        if (x[0].text == str(port)):
            forTest=x[0].text
            root.remove(x)
    lista.write("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")
    return forTest

def Add_Controler(devname,port):
    lista = ET.parse("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml");

    root=lista.getroot()

    kontroler=ET.SubElement(root,'Kontroler')

    portt=ET.SubElement(kontroler,'port')

    naziv=ET.SubElement(kontroler,'naziv')
    portt.text=str(port)
    naziv.text=str(devname)
    lista.write("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")
    return root[len(root)-1][0],root[len(root)-1][1]


def Svi_Kontroleri():
        lista = ET.parse("C:\\Users\\"+putanja_razlika+"\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")
        root = lista.getroot()

        LISTA=""
        for x in root:
            LISTA+=x[0].text+"/"+x[1].text+"&"

            pass
        return LISTA
            
def Slanje_liste_Kontrolera():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(('localhost', 50098))

    server.listen(10)

    while(True):
      client, client_address = server.accept();
      print()
      print()

      temp = client.recv(1024);
      msg = temp.decode("utf-8")
      print(str(msg))
      print("ZAHTEV PRISTIGAO")
      text=Svi_Kontroleri()
      client.send(bytes(text, 'utf-8'))
      client.close()
    server.close()

def brRadnihSatiAnalogni(uredjaj, pocetak, kraj):
    upitCasovi = "SELECT min(Vreme), max(Vreme) from amsschema.localdevice WHERE Vreme BETWEEN" + "\'" + pocetak +"\'"+  "and" + "\'" + kraj +"\'" + "and DeviceCode= " + "\'" + uredjaj +"\'"
    return konekcijaBaze(upitCasovi)

def brRadnihSatiDigitalni(uredjaj, pocetak, kraj):
    upitCasovi = "SELECT min(Vreme), max(Vreme) from amsschema.localdevicedigital WHERE Vreme BETWEEN" + "\'" + pocetak + "\'" + "and" + "\'" + kraj + "\'" + "and DeviceCode= " + "\'" + uredjaj + "\'"
    return konekcijaBaze(upitCasovi)

def svePromeneUIntervaluAnalogni(uredjaj, pocetak, kraj):
    upitSvePromene = "SELECT DeviceCode, ActualValue from amsschema.localdevice WHERE Vreme BETWEEN" + "\'" + pocetak +"\'"+  "and" + "\'" + kraj +"\'" + "and DeviceCode= " + "\'" + uredjaj +"\'"
    return konekcijaBaze(upitSvePromene)

def svePromeneUIntervaluDigitalni(uredjaj, pocetak, kraj):
    upitSvePromene = "SELECT DeviceCode, ActualValue from amsschema.localdevicedigital WHERE Vreme BETWEEN" + "\'" + pocetak + "\'" + "and" + "\'" + kraj + "\'" + "and DeviceCode= " + "\'" + uredjaj + "\'"
    return konekcijaBaze(upitSvePromene)

def sumarnoAnalogni(uredjaj, pocetak, kraj):
    upitSumarno = "SELECT DeviceCode, count(ActualValue) from amsschema.localdevice WHERE Vreme BETWEEN" + "\'" + pocetak +"\'"+  "and" + "\'" + kraj +"\'" + "and DeviceCode= " + "\'" + uredjaj +"\'"
    return konekcijaBaze(upitSumarno)

def sumarnoDigitalni(uredjaj, pocetak, kraj):
    upitSumarno = "SELECT DeviceCode, count(ActualValue) from amsschema.localdevicedigital WHERE Vreme BETWEEN" + "\'" + pocetak + "\'" + "and" + "\'" + kraj + "\'" + "and DeviceCode= " + "\'" + uredjaj + "\'"
    return konekcijaBaze(upitSumarno)