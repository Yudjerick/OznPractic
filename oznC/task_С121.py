"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Car с полями марка, мощность, год производства. Добавить конструктор класса.
Создать производный от Car класс PassengerCar. Новые поля: количество пассажиров, ремонтная книжка
    (словарь вида запчасти: год замены). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления замененной запчасти в ремонтную книжку, получения год замены по названию,
    форматированной печати всей ремонтной книжки. Переопределить метод преобразования в строку для печати
    основной информации (марка, мощность, год производства, количество пассажиров).
Создать производный от Car класс Truck. Новые поля: максимальная грузоподъемность, ФИ водителя, текущий груз
    (словарь вида название товара: вес). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения водителя, добавления и удаления груза, форматированной печати текущего груза.
    Переопределить метод преобразования в строку для печати основной информации (марка, мощность, год производства,
    максимальная грузоподъемность, ФИ водителя).
Создать класс Autopark. Поля: название автопарка, список легковых машин (список экземпляров класса PassengerCar),
    список грузовиков (список экземпляров класса Truck). Определить конструктор. Переопределить метод
    преобразования в строку для печати всей информации об автопарке (с использованием переопределения в классах
    PassengerCar и Truck). Переопределить методы получения количества грузовиков функцией len, получения грузовой
    машины по индексу, изменения по индексу, удаления по индексу (пусть номера у грузовых машин считаются с 1,
    а индекс 0 – список всех легковых машин). Переопределить операции + и - для добавления или удаления грузовой
    машины. Добавить функцию создания txt-файла и записи всей информации в него (в том числе ремонтных
    книжек и списка грузов).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""
class Car:
    def __init__(self, mark, voltage, year):
        self.mark = mark
        self.voltage = voltage
        self.year = year


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

car1 = Truck("m",2000, 2013, 4000, "bobSmith")
car1.add_good("wood", 200)
car1.add_good("gold", 3)
car1.add_good("rocks", 100)
car1.print_goods()
print(str(car1))















