from Service.AMS import Konekcija

if __name__ == "__main__":
    print("Kontroler pocinje sa radom!")
    print()
    print()

   
    AMSService = Konekcija(50015)
    AMSService.Listen()