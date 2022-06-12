from Service.AMS import AMSService

if __name__ == "__main__":
    print("Kontroler pocinje sa radom!")
    print()
    print()

   
    AMSService = AMSService(50015)
    AMSService.Listen()