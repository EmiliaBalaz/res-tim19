from Model.LocalDevice import LocalDevice
from Common.XMLWritter import XMLWritter


class LocalDeviceStorage:
    def __init__(self):
        self.deviceValues = []


    def AddNewDeviceValue(self, deviceValue:LocalDevice):
        self.deviceValues.append(vars(deviceValue))
        values = {'DeviceValues': {'LocalDevice': self.deviceValues}}

        xmlWritter = XMLWritter(values)

        f = open("deviceValues.xml", "w")
        f.write(xmlWritter.doc.toxml("UTF-8").decode("UTF=8"))

