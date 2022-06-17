import select, socket
import xml.etree.ElementTree as ET

        
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

def Konekcija(port):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind(('localhost',port))

    server.listen(10)
    print("--SERVER CEKA NOVE KONEKCIJE!--")
    while(True):


      client,client_address=server.accept();
      print()
      print()
      print("PODACI PRIMLJENI OD: "+str(client_address))
      temp= client.recv(1024);
      msg=temp.decode("utf-8")
      print(str(msg))
      client.close()
    server.close()


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
        "C:\\Users\\Cvijetin Glisic\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")

    root = lista.getroot()

    forTest="NONE"
    for x in root:
        if (x[0].text == str(port)):
            forTest=x[0].text
            root.remove(x)
    lista.write("C:\\Users\\Cvijetin Glisic\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")
    return forTest

def Add_Controler(devname,port):
    lista = ET.parse("C:\\Users\\Cvijetin Glisic\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml");

    root=lista.getroot()

    kontroler=ET.SubElement(root,'Kontroler')

    portt=ET.SubElement(kontroler,'port')

    naziv=ET.SubElement(kontroler,'naziv')
    portt.text=str(port)
    naziv.text=str(devname)
    lista.write("C:\\Users\\Cvijetin Glisic\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")
    return root[len(root)-1][0],root[len(root)-1][1]


def Svi_Kontroleri():
        lista = ET.parse("C:\\Users\\Cvijetin Glisic\\Documents\\GitHub\\res-tim19\\AMS\\ListaKontrolera.xml")
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



