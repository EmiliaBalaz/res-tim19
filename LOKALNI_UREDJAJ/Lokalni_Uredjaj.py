import sys

import LokalniUredjaj.Uredjaj_funkcije

if __name__ == "__main__":



    print("UREDJAJ JE USPESNO POKRENUT:")






   
    print(LokalniUredjaj.Uredjaj_funkcije.Primi_Kontrolere())
    LokalniUredjaj.Uredjaj_funkcije.Upisi_Kontrolere(LokalniUredjaj.Uredjaj_funkcije.Primi_Kontrolere())
    print("LISTA DOSTUPNIH KONTROLERA:")
    LokalniUredjaj.Uredjaj_funkcije.Izlistaj_Kontrolere()
    print()
    print()
    print()
   
    port=""
    port=LokalniUredjaj.Uredjaj_funkcije.Unos_porta()
    while(port=="ERROR"):
        port=LokalniUredjaj.Uredjaj_funkcije.Unos_porta()
        pass




    f = LokalniUredjaj.Uredjaj_funkcije.Klijent_konekcija()


    while(f == "ERROR"):
         f = LokalniUredjaj.Uredjaj_funkcije.Klijent_konekcija()

    a=""
    ID=""
    if(f=="ANALOGNI"):
        ID,a=LokalniUredjaj.Uredjaj_funkcije.UnosAnalognogUredjaja()
        while(a =="ERROR"):
            ID,a = LokalniUredjaj.Uredjaj_funkcije.UnosAnalognogUredjaja()
            pass
        LokalniUredjaj.Uredjaj_funkcije.PosaljiPoruku(a,int(port))


    elif(f == "DIGITALNI"):
        ID,a = LokalniUredjaj.Uredjaj_funkcije.UnosDigitalnogUredjaja()
        while (a == "ERROR"):
            ID,a = LokalniUredjaj.Uredjaj_funkcije.UnosDigitalnogUredjaja()
            pass
        LokalniUredjaj.Uredjaj_funkcije.PosaljiPoruku(a, int(port))

    yy=""
    while(yy != "2"):
      print()
      print("OPCIJE")
      print("1.PROMENITE STANJE")
      print("2.IZLAZAK")
      yy = input()

      if(f=="ANALOGNI" and yy=="1" ):
          a=LokalniUredjaj.Uredjaj_funkcije.PromenaStanjaAnalognogUredjaja(ID)
          while(a=="ERROR"):
              a = LokalniUredjaj.Uredjaj_funkcije.PromenaStanjaAnalognogUredjaja( ID)
          LokalniUredjaj.Uredjaj_funkcije.PosaljiPoruku(a,int(port))


      elif(f == "DIGITALNI" and yy == "1"):
          a = LokalniUredjaj.Uredjaj_funkcije.PromenaStanjeDigitalnogUredjaja( ID)
          while (a == "ERROR"):
              a = LokalniUredjaj.Uredjaj_funkcije.PromenaStanjaDigitalnogUredjaja( ID)
          LokalniUredjaj.Uredjaj_funkcije.PosaljiPoruku(a, int(port))

      elif(yy !="2"):
          print("NEMOSTOJECA OPCIJA.POKUSAJTE PONOVO!")
          pass


    sys.exit()






