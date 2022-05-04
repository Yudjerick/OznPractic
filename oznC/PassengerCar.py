from Car import Car

class PassengerCar(Car):
    def __init__(self, mark, voltage, year, passengers):
        super().__init__(mark, voltage, year)
        self.passengers = passengers
        self.repair_book = {}

    def __str__(self):
        return "mark: " + str(self.mark) + "; voltage: " + str(self.voltage) + "; year: " + str(self.year) + "; passengers: " + str(self.passengers)
        
    def add_detail(self, detail, year):
        self.repair_book[detail] = year

    def get_changeyear(self, detail):
        return self.repair_book[detail]
    def print_book(self):
        for i in sorted(self.repair_book, key = self.repair_book.get):
            print(i, " ", self.repair_book[i])
    def str_book(self):
        s = "repair book:\n"
        for i in sorted(self.repair_book, key = self.repair_book.get):
            s += "  "+ i + " " + self.repair_book[i] + "\n"
        return s
