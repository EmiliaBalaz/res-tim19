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

            


         
         
    
    kontroler_funkcije.Upisi_u_listu(port,naz)
    print()
    print()
    atexit.register(kontroler_funkcije.Exit_Handler,port)
    deviceStorage = LocalDeviceStorage()
    y=threading.Thread(target=kontroler_funkcije.Konekcija,args=(deviceStorage,int(port)),daemon=True)
    y.start()
    x=threading.Thread(target=kontroler_funkcije.Slanje_na_AMS,args=(50005,),daemon=True)
    x.start()
   
    kontroler_funkcije.Izadji_Iz_Aplikacije()
    
       

    
    
   









        
        



    
    







