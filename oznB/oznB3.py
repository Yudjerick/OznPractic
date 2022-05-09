# Написать функцию commas, которая преобразует заданное число в строку с добавлением
# запятых для удобства чтения. Число должно быть округлено до 3 значащих цифр,
# а запятые следует добавлять с интервалом в три цифры перед десятичной точкой.
#
# Примеры:
# commas(100.2346) ==> "100.235"
# commas(-1000000.123) ==> "-1,000,000.123"


import traceback


def commas(number):
    f = float(number)
    f = round(f,3)
    cel = int(f)
    drob = f - cel
    drob = round(drob,3)
    sp = []
    for i in str(cel):
        sp.append(i)
    sp.reverse()
    
    c = 1
    i = 1
    while i < len(sp):
        c+=1
        if c == 4:
            sp.insert(i,",")
            c = 0
        i+=1
    sp.reverse()
    
    if drob == 0:
        findr = ""
    else:
        findr = str(drob)[1:]
    fin = "".join(sp) + findr
    
    return fin

# Тесты
try:
    assert commas(1) == "1"
    assert commas(1000) == "1,000"
    assert commas(100.2346) == "100.235"
    assert commas(1000000000.23) == "1,000,000,000.23"
    assert commas(-999.9999) == "-1,000"
    assert commas(-1234567.0001236) == "-1,234,567"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

    
