from Car import Car

class PassengerCar(Car):
    def __init__(self, mark, voltage, year, passeners):
        super().__init__(mark, voltage, year)
        self.passengers = passengers
        self.repair_book = {}
        
    def add_detail(self, detail, year):
        self.repair_book[detail] = year

    def get_changeyear(self, detail):
        return self.repair_book[detail]
