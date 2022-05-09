from Log import Log

class Car:
    def __init__(self, mark, voltage, year):
        Log("CRE", "создание экземпляра Car")
        self.mark = mark
        self.voltage = voltage
        self.year = year

def testCar():
    car = Car("volvo", 700, 1999)