import kontroler_funkcije
from Model.LocalDeviceStorage import LocalDeviceStorage
import sys
import threading
import atexit


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

    kontroler_funkcije.napraviXML(naz, port)

            


         
         
    
    kontroler_funkcije.Javi_Se_NA_AMS(port,naz)
    print()
    print()
    atexit.register(kontroler_funkcije.Exit_Handler,port,naz)
    deviceStorage = LocalDeviceStorage()
    semaphore = threading.Semaphore(0)
    y=threading.Thread(target=kontroler_funkcije.Konekcija,args=(deviceStorage,int(port), naz, semaphore),daemon=True)
    y.start()
    x=threading.Thread(target=kontroler_funkcije.Slanje_na_AMS,args=(50015,port, naz, semaphore),daemon=True)
    x.start()
   
    kontroler_funkcije.Izadji_Iz_Aplikacije()
    
       

    
    
   









        
        



    
    







