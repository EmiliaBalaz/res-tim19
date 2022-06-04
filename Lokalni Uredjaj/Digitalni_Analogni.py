from datetime import datetime
import uuid
from enum import Enum
from abc import ABC, abstractmethod

class Stanje(Enum):
  # DIGITALNO="DIGITALNO"
  # ANALOGNO="ANALOGNO"
   ON="ON"
   OFF="OFF"
   OPEN="OPEN"
   CLOSE="CLOSE"

class Lokalni_Uredjaj(ABC):
    dt=datetime.now()
    ts=datetime.timestamp(dt)
    def __init__(self,id,timestamp,state):
       self.id=id
       self.time=timestamp 
       self.state=state
    def set_state(self,state):
        self.state=state
    def get_state(self):
        return self.state
    @abstractmethod
    def timestamp(self):
        pass
    @abstractmethod
    def stateMethod(self):
        pass  

class Digitalni_Uredjaj(Lokalni_Uredjaj):
        def timestamp(self):
            dt=datetime.now()
            ts=datetime.timestamp(dt)
            print("Timestamp is:",ts)
        def stateMethod(self):
            if(self.get_state()==Stanje.ON.value):
                print("Uredaj je u stanju ON")
            elif(self.get_state()==Stanje.OFF.value):
                print("Uredja je u stanju OFF")
            elif(self.get_state()==Stanje.OPEN.value):
                print("Uredjaj je u stanju OPEN")
            elif(self.get_state()==Stanje.CLOSE.value):
                print("Uredjaj je u stanju CLOSE")
            else:
                print("Ovo stanje ne postoji")

class Analogni_Uredjaj(Lokalni_Uredjaj):
        def timestamp(self):
             dt=datetime.now()
             ts=datetime.timestamp(dt)
             print("Time stamp is",ts)
            
if __name__ == "__main__":
    id=uuid.uuid1()
    dt=datetime.now()
    ts=datetime.timestamp(dt)
    prekidac =  Digitalni_Uredjaj(id,ts,Stanje.OFF.value)
    prekidac.stateMethod()

    


   # print(ts)
   #print(id)
