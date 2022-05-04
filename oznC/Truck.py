from Car import Car

class Truck(Car):
    def __init__(self, mark, voltage, year, capacity, driver_name):
        super().__init__(mark, voltage, year)
        self.capacity = capacity
        self.driver_name = driver_name
        self.goods = {}
        
    def __str__(self):
        return ("mark: " + str(self.mark) + "; voltage: " + str(self.voltage) + "; year: " + str(self.year) + "; capacity: " + str(self.capacity) + "; driver: " + str(self.driver_name))
        
    def change_diver(self, new_driver):
        self.driver = new_driver

    def add_good(self, freight_name, weight):
        self.goods[freight_name] = weight;

    def del_good(self, freight_name):
        del self.goods[freight_name]

    def print_goods(self):
        for i in sorted(self.goods, key = self.goods.get, reverse = True):
            print(i, " ", self.goods[i])

    def str_goods(self):
        s = "goods:\n"
        for i in sorted(self.goods, key = self.goods.get, reverse = True):
            s += "  " + str(i) + " " + str(self.goods[i]) + "\n"
        return s