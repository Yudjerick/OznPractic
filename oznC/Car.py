class Car:
    def __init__(self, mark, voltage, year):
        self.mark = mark
        self.voltage = voltage
        self.year = year

def testCar():
    car = Car("volvo", 700, 1999)