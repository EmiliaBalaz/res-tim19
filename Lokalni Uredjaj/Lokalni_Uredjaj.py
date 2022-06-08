import Uredjaj_funkcije

if __name__ == "__main__":



    print("UREDJAJ JE USPESNO POKRENUT:")

    #TODO: logika za pravljenje lokalnog uredjaja-EMILIJIN DEO
    Uredjaj_funkcije.Klijent_konekcija(50002)

   
    print("LISTA DOSTUPNIH KONTROLERA:")
    Uredjaj_funkcije.Izlistaj_Kontrolere()
    
    print()
    print()
    print()
   
    x=0
    
    while x==0:
        
        print("UNESITE PORT:")
        port=input()
        Dict={}
        Dict=Uredjaj_funkcije.SviKontroleri()
        for xx in Dict.keys():
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