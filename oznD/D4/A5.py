# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.

def InfoAll():
    parameters = ["id","model","year","color","power"]
    for i in cars:
        for j in parameters:
            print(j, ": ", i[j])
        print()
def InfoCar():
    parameters = ["id","model","year","color","power"]
    n = int(input("Enter number of car: "))
    for j in parameters:
        print(j, ": ", cars[n-1][j])
    print()

def Younger():
    y = int(input("Enter year: "))
    c = 0
    for i in cars:
        if int(i["year"]) > y:
            c += 1
    print(c)

def UpdateInfo():
    n = int(input("Enter number: "))
    parameters = ["id","model","year","color","power"]
    for i in parameters:
        cars[n-1][i] = input(("Enter new "+i+": "))

def Remove():
    n = int(input("Enter number: "))
    cars.pop(n-1)
            
    

cars = [
    {
        "id": 123,
        "model": "Lada",
        "year" : 2000,
        "color" : "cherry",
        "power" : 70
        },
    {
        "id": 145,
        "model": "Mercedes",
        "year" : 2014,
        "color" : "silver",
        "power" : 600
        },
    {
        "id": 204,
        "model": "Jiguli",
        "year" : 2000,
        "color" : "brown",
        "power" : 140
        },
    {
        "id": 999,
        "model": "Lamborgini",
        "year" : 2000,
        "color" : "purple",
        "power" : 20
        },
    {
        "id": 777,
        "model": "Hyundai",
        "year" : 2005,
        "color" : "orange",
        "power" : 800
        },
    {
        "id": 555,
        "model": "UAZ",
        "year" : 2020,
        "color" : "camoflage",
        "power" : 200
        },
    {
        "id": 666,
        "model": "KAMAZ",
        "year" : 2000,
        "color" : "red",
        "power" : 3000
        },
    {
        "id": 856,
        "model": "Audi",
        "year" : 2000,
        "color" : "blue",
        "power" : 345
        },
    {
        "id": 123,
        "model": "Niva",
        "year" : 1980,
        "color" : "green",
        "power" : 20
        },
    {
        "id": 423,
        "model": "Volkswagen",
        "year" : 1999,
        "color" : "grey",
        "power" : 500
        },
    ]

InfoAll()
"""
Remove()
print()
InfoAll()
print()
UpdateInfo()
print()
InfoCar()
print()
Younger()
print()
InfoAll()
"""