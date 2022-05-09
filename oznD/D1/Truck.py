from Car import Car
from Log import Log

class Truck(Car):
    def __init__(self, mark, voltage, year, capacity, driver_name):
        super().__init__(mark, voltage, year)
        self.capacity = capacity
        self.driver_name = driver_name
        self.goods = {}
        Log("CRE", "создание экземляра Truck")
        
    def __str__(self):
        Log("INF", "преобразование в строку Truck")
        return ("mark: " + str(self.mark) + "; voltage: " + str(self.voltage) + "; year: " + str(self.year) + "; capacity: " + str(self.capacity) + "; driver: " + str(self.driver_name))
        
    def change_diver(self, new_driver):
        self.driver_name = new_driver
        Log("INF", "изменение водителя")

    def add_good(self, freight_name, weight):
        Log("INF", "добавление груза")
        self.goods[freight_name] = weight;

    def del_good(self, freight_name):
        Log("INF", "удаление груза")
        del self.goods[freight_name]

    def print_goods(self):
        Log("INF", "печать информации о грузах")
        for i in sorted(self.goods, key = self.goods.get, reverse = True):
            print(i, " ", self.goods[i])

    def str_goods(self):
        Log("INF", "преобразование в строку информации о грузах")
        s = "goods:\n"
        for i in sorted(self.goods, key = self.goods.get, reverse = True):
            s += "  " + str(i) + " " + str(self.goods[i]) + "\n"
        return s

def testTruck():
    print("\nTesting Truck:")
    truck = Truck("KAMAZ",6000, 2007, 10000, "BobSmith")
    truck.change_diver("IvanIvanov")
    print(truck)
    truck.add_good("wood", 200)
    truck.add_good("rocks", 300)
    truck.add_good("iron", 500)
    truck.del_good("rocks")
    print("goods:")
    truck.print_goods()
    return truck

#testTruck()