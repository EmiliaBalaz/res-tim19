import Service.AMS as ams


def Logovanje_koraci():
    while(True):
        data=ams.Logovanje_liste_kontrolera()
        operation,devport,devname=ams.Brisaje_Dodavanje_Kontrolera(data)
        if(operation=="ADD"):
            ams.Add_Controler(devname,devport)
        elif(operation=="DELETE"):
            ams.Delete_Kontroler(devname,devport)
        else:
            print("NE RADI")

    pass


