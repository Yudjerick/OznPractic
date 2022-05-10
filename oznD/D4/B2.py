# Написать функцию blocks, которая получает строку, состоящую из букв и цифр и возвращает строку в виде блоков,
# разделенных символом дефис. Элементы блока должны быть отсортированы по принципу, указанному ниже, и
# каждый блок не может содержать несколько экземпляров одного и того же символа.
# Порядок блоков:
# строчные буквы (a - z) в алфавитном порядке
# заглавные буквы (A - Z) в алфавитном порядке
# цифры (0 - 9) в порядке возрастания
#
#
# Примеры:
# blocks("21AxBz") ==> "xzAB12"
# blocks("abacad") ==> "abcd-a-a"

import traceback

def blocks(s):
    sp = mySorted(s)
    nsp = []
    rem = []
    nsp.append(sp[0])
    for i in range(1,len(sp)):
        if(sp[i]==sp[i-1]):
            rem.append(sp[i])
        else:
            nsp.append(sp[i])
    
    while rem != []:
        nsp.append('-')
        sp = rem
        rem = []
        nsp.append(sp[0])
        for i in range(1,len(sp)):
            if(sp[i]==sp[i-1]):
                rem.append(sp[i])
            else:
                nsp.append(sp[i])
        
        
    return "".join(nsp)

def mySorted(s):
    s = sorted(s)
    ns = ""
    for i in s:
        if i.islower():
            ns += i
    for i in s:
        if i.isupper():
            ns += i
    for i in s:
        if i.isdigit():
            ns += i
    return ns

#print(blocks("heyitssampletestkk"))
# Тесты
try:
    assert blocks("21AxBz") == "xzAB12"
    assert blocks("abacad") == "abcd-a-a"
    assert blocks("heyitssampletestkk") == "aehiklmpsty-ekst-est"
    assert blocks("6zjX9qcwTIuYNvdmL3CtElHa2n0rogKsSVPRWG4QAMUOe8JkyfxZDiBpb1Fh75GUTLMcbio7HO6rvn1NtDRmPJAejuXVFgaZI3pK90s4fBzqwEd5yWCQh8Sl2kxY") == \
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
