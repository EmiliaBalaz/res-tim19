class ListaKontrolera():
    Dict={}

    @staticmethod
    def Dodaj_kontroler(port,imekontrolera):
       
        ListaKontrolera.Dict[port]=imekontrolera
        Cuvanje()
        pass


    @staticmethod
    def Ukloni_kontroler(port): 
        ListaKontrolera.Dict.pop(port) 
        pass


    @staticmethod
    def Izlistaj_sve():
        Cuvanje()
        for x in ListaKontrolera.Dict.keys():
            print("NAME: "+ListaKontrolera.Dict[x]+"  PORT: "+str(x))
            pass



def Cuvanje():
    Cuvanje.Dict=getattr(Cuvanje,'Dict',{})
    for x in ListaKontrolera.Dict.keys():
        Cuvanje.Dict[x]=ListaKontrolera.Dict[x]

    ListaKontrolera.Dict=Cuvanje.Dict
    