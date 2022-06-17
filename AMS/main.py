import threading

import AMS.Service.AMS
import AMS.Service.Thread_Funkcije
from Service.AMS import Konekcija

if __name__ == "__main__":
    print("Kontroler pocinje sa radom!")
    print()
    print()


    y = threading.Thread(target=AMS.Service.AMS.Konekcija, args=(50015,), daemon=True)
    y.start()

    x = threading.Thread(target=AMS.Service.Thread_Funkcije.Logovanje_koraci, args=(), daemon=True)
    x.start()

    z = threading.Thread(target=AMS.Service.AMS.Slanje_liste_Kontrolera, args=(), daemon=True)
    z.start()
    a=input()



