import kontroler_funkcije
from Model.LocalDeviceStorage import LocalDeviceStorage
import sys
sys.path.insert(0,'C:\\Users\\Cvijetin Glisic\\Desktop\\GIT_REPOZITORIJUM\\GIT\\Lokalni Uredjaj')
import ListaKontrolera
if __name__ == "__main__":
    print("Kontroler pocinje sa radom!")
    print()
    print("Unesite naziv kontrolera:")
    naz=input()
   
    port=0 
    x=False
    while x==False:
         
        print("Unesite port: (! unesi 50002 !)")
        port=input()
        try:
            
            port=int(port)
            x=True

        except ValueError:
            x=False
            print("UNETA NEISPRAVNA VREDNOST!")

            


         
         
    ListaKontrolera.ListaKontrolera.Dodaj_kontroler(int(port),naz)
    ListaKontrolera.ListaKontrolera.Izlistaj_sve()
    print()
    print()

    deviceStorage = LocalDeviceStorage()
    kontroler_funkcije.Konekcija(deviceStorage,int(port))








        
        



    
    







