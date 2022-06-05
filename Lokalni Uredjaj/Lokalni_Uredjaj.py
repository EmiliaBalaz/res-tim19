import Uredjaj_funkcije
import ListaKontrolera as LK
if __name__ == "__main__":



    print("UREDJAJ JE USPESNO POKRENUT:")

    #TODO: logika za pravljenje lokalnog uredjaja-EMILIJIN DEO

    LK.ListaKontrolera.Dodaj_kontroler(50002,"KONTROLER_1")
    LK.ListaKontrolera.Dodaj_kontroler(50005,"AMS")
    print("LISTA DOSTUPNIH KONTROLERA:")
    LK.ListaKontrolera.Izlistaj_sve()
    
    print()
    print()
    print()
   
    x=0
    
    while x==0:
        
        print("UNESITE PORT:")
        port=input()
        for xx in LK.ListaKontrolera.Dict.keys():
            if(port==str(xx)):
                print("POVEZIVANJE SA KONTROLEROM...") 
                x=1
                pass
            pass

        if x==0:
            print("UREDJAJ SA PORTOM KOJI STE IZABRALI TRENUTNO NIJE DOSTUPAN.UNESITE DRUGI PORT!")
            pass
        pass

    Uredjaj_funkcije.Klijent_konekcija(int(port))