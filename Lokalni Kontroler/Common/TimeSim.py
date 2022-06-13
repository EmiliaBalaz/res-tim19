import time
import xml.etree.ElementTree as ET


def ReadSimTime():
    lista = ET.parse("Common\\TimeSimConfig.xml")
    root = lista.getroot()
    a = int(root[0].text)
    return a


class TimeSimulation():
    time_str = 0

    @staticmethod
    def COUNT_START():
        TimeSimulation.time_str = time.time()

    @staticmethod
    def TimePassed():
        return (time.time() - TimeSimulation.time_str) * ReadSimTime()






