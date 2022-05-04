from Truck import Truck
from PassengerCar import PassengerCar
class Autopark:
    def __init__(self, name):
        self.name = name
        self.passengerCars = []
        self.trucks = []
    def __str__(self):
        s1 = ""
        for i in self.passengerCars:
            s1 += str(i) + "\n" + i.str_book()
        s2 = ""
        for i in self.trucks:
            s2 += str(i) + "\n" + i.str_goods()
        return self.name + ":\n\npassenger cars:\n" + s1 + "\ntrucks:\n" + s2
    def __len__(self):
        return len(self.trucks)
    def __getitem__(self, key):
        if key == 0:
            return self.passengerCars
        try:
            return self.trucks[key-1]
        except:
            print("exception called")
            return self.trucks[0]
    def __setitem__(self, key, value):
        if key == 0:
            self.passengerCars = value
        try:
            self.trucks[key-1] = value
        except:
            print("exception called")

    def __delitem__(self,key):
        try:
            del self.trucks[key]
        except:
            print("exception called")

    def __add__(self, other):
        if type(other) == Truck:
            self.trucks.append(other)
        elif type(other) == PassengerCar:
            self.passengerCars.append(other)
    def __sub__(self, other):
        if type(other) == Truck:
            self.trucks.remove(other)
        elif type(other) == PassengerCar:
            self.passengerCars.remove(other)
    def create_txt(self):
        self.txt = open("Autopark.txt","w+")
        self.txt.write(str(self))
        self.txt.close()