import datetime
import time

from Service.AMS import izlistajSveAnalogneUredjaje, izlistajSveDigitalneUredjaje, brSatiPrekoKonfigurisaneVrednostiAnalogni, iscitavanjeRadnihMinuta, brSatiPrekoKonfigurisaneVrednostiDigitalni

if __name__ == '__main__':
    print("Meni: ")
    print("1. Lista svih uredjaja")
    print("2. Promene vrednosti za izabrani vremenski period za izabrani uredjaj.")
    print("3. Broj radnih sati za izabrani uredjaj za izabrani vremenski period.")
    print("4. Izlistavanje svih uredjaja čiji je broj radnih sati preko konfigurisane vrednosti")
    print("Unesite opciju: ")
    i = input()
    if i == "1":
        analogni = izlistajSveAnalogneUredjaje()
        digitalni = izlistajSveDigitalneUredjaje()
        print("Analogni uredjaji: ")
        for x in analogni:
            print(x[0])
        print("Digitalni uredjaji: ")
        for x in digitalni:
            print(x[0])
    if i == "2":
        print("Izaberite uredjaj: ")
        print("1.ANALOGNI")
        print("2.DIGITALNI")
        vrstaU = input()
        if vrstaU == "1":
            print("Unesite ime: ")
            uredjaj = input()
            print("Unesite pocetno vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            pocetno = input()
            print("Unesite krajnje vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            krajnje = input()
            promene = svePromeneUIntervaluAnalogni(uredjaj, pocetno, krajnje)
            suma = sumarnoAnalogni(uredjaj, pocetno, krajnje)
            print("Element " + promene[0][0])
            for x in promene:
                print(x[1])
            print("Suma je: " + str(suma[0][1]))
        elif vrstaU == "2":
            print("Unesite ime: ")
            uredjaj = input()
            print("Unesite pocetno vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            pocetno = input()
            print("Unesite krajnje vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            krajnje = input()
            promene = svePromeneUIntervaluDigitalni(uredjaj, pocetno, krajnje)
            suma = sumarnoDigitalni(uredjaj, pocetno, krajnje)
            print("Element " + promene[0][0])
            for x in promene:
                print(x[1])
            print("Suma je: " + str(suma[0][1]))
    if i == "3":
        print("Izaberite uredjaj: ")
        print("1.ANALOGNI")
        print("2.DIGITALNI")
        vrstaU = input()
        if vrstaU == "1":
            print("Unesite ime: ")
            uredjaj = input()
            print("Unesite pocetno vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            pocetno = input()
            print("Unesite krajnje vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            krajnje = input()
            vrednosti = brRadnihSatiAnalogni(uredjaj, pocetno, krajnje)
            minimalni = vrednosti[0][0]
            maximalni = vrednosti[0][1]
            sati = maximalni - minimalni
            asd = sati.total_seconds()
            minutiOdradjeni = divmod(asd, 60)[0]
            print("Odradjeni minuti uredjaja: " + str(minutiOdradjeni))
        elif vrstaU == "2":
            print("Unesite ime: ")
            uredjaj = input()
            print("Unesite pocetno vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            pocetno = input()
            print("Unesite krajnje vreme u formatu npr: gggg-mm-dd ss:mm:ss")
            krajnje = input()
            vrednosti = brRadnihSatiDigitalni(uredjaj, pocetno, krajnje)
            minimalni = vrednosti[0][0]
            maximalni = vrednosti[0][1]
            sati = maximalni - minimalni
            asd = sati.total_seconds()
            minutiOdradjeni = divmod(asd, 60)[0]
            print("Odradjeni minuti uredjaja: " + str(minutiOdradjeni))





    if i == "4":
        print("Izaberite uredjaj: ")
        print("1.ANALOGNI")
        print("2.DIGITALNI")
        vrstaU = input()
        if vrstaU == "1":
            vrednost = brSatiPrekoKonfigurisaneVrednostiAnalogni()
            print("Svi uredjaji preko konfigurisane vrednosti: ")
            for x in vrednost:
                maximum = x[1]
                minimum = x[2]
                minuti2 = maximum - minimum
                asd = minuti2.total_seconds()
                minutiOdradjeni2 = divmod(asd, 60)[0]
                dozvoljeniMinuti = iscitavanjeRadnihMinuta()
                dozvoljeniMinuti = float(dozvoljeniMinuti)
                if(minutiOdradjeni2 >= dozvoljeniMinuti):
                    print("Uredjaj: " + str(x[0]))
        if vrstaU == "2":
            vrednost = brSatiPrekoKonfigurisaneVrednostiDigitalni()
            print("Svi uredjaji preko konfigurisane vrednosti: ")
            for x in vrednost:
                maximum = x[1]
                minimum = x[2]
                minuti2 = maximum - minimum
                asd = minuti2.total_seconds()
                minutiOdradjeni2 = divmod(asd, 60)[0]
                dozvoljeniMinuti = iscitavanjeRadnihMinuta()
                dozvoljeniMinuti = float(dozvoljeniMinuti)
                if (minutiOdradjeni2 >= dozvoljeniMinuti):
                    print("Uredjaj: " + str(x[0]))



#2022-06-19 15:32:04
#2022-06-19 15:46:18

#2022-06-19 16:06:50
#2022-06-19 16:06:59


