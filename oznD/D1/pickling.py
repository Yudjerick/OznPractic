import pickle
from PassengerCar import  PassengerCar
from Truck import Truck
from Autopark import Autopark

car1 = Truck("WAZ",2000, 2013, 4000, "bobSmith")
car1.add_good("wood", 200)
car1.add_good("gold", 3)
car1.add_good("rocks", 100)
car2 = Truck("KAMAZ",3000, 2013, 4000, "bobSmith")
car2.add_good("rocks", 100)
car3 = PassengerCar("honda", 600, 2005, 4)
car3.add_detail("engine",2010)
ap = Autopark("Autopark")
ap+car1
ap+car2
ap+car3

pf = open("pickled.pickle","wb")
pickle.dump(ap,pf)
















