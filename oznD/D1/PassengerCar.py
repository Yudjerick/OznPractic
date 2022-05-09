from Car import Car
from Log import Log

class PassengerCar(Car):
    def __init__(self, mark, voltage, year, passengers):
        super().__init__(mark, voltage, year)
        self.passengers = passengers
        self.repair_book = {}
        Log("CRE","создание экземпляра класса PassengerCar")

    def __str__(self):
        Log("INF", "преобразование в строку информации об автомобиле")
        return "mark: " + str(self.mark) + "; voltage: " + str(self.voltage) + "; year: " + str(self.year) + "; passengers: " + str(self.passengers)
        
    def add_detail(self, detail, year):
        Log("INF", "добавление детали в ремонтную книжку")
        self.repair_book[detail] = year

    def get_changeyear(self, detail):
        Log("INF", "возврат года замены детали")
        return self.repair_book[detail]
    def print_book(self):
        Log("INF", "печать ремонтной книжки")
        for i in sorted(self.repair_book, key = self.repair_book.get):
            print(i, " ", self.repair_book[i])
    def str_book(self):
        Log("INF", "преобразование в строку ремонтной книжки")
        s = "repair book:\n"
        for i in sorted(self.repair_book, key = self.repair_book.get):
            s += "  "+ i + " " + str(self.repair_book[i]) + "\n"
        return s

def testPassengerCar():
    print("\nTesting PassengerCar:")
    car = PassengerCar("volvo",500,1999,4)
    print(car)
    car.add_detail("engine", 2005)
    print(car.get_changeyear("engine"))
    car.add_detail("roof", 2010)
    print("repairbook:")
    car.print_book()
    return car

#testPassengerCar()
