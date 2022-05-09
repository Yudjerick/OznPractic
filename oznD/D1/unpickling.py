import pickle
from Log import Log
from Autopark import Autopark
from Truck import Truck
from PassengerCar import PassengerCar
pf = open("pickled.pickle","rb")
ap = pickle.load(pf)
pf.close
Log.clear()
ap+Truck("ZIL",3000,2012,5000, "jackTiller")
ap[3].add_good("planks",600)
ap[3].change_diver("jeremyHatter")
print(ap[2])
ap[0][0].add_detail("wheel", 2020)
print(ap[0][0].get_changeyear("wheel"))
ap[0][0].print_book()
print(ap)
ap.create_txt()
