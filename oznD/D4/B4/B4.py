"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
1 - прочитать файл построчно;
2 - непустые строки добавить в список;
3 - удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
4 - объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
5 - создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
6 - вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
7 - заменить все эти слова в строке на слово “PYTHON”;
8 - создать новый txt-файл;
9 - записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

def wiki_function():
    f = open("w.txt", "r")
    stroki = []
    x = f.readlines()
    f.close()#1
    
    for line in range (len(x)):
        if x[line] != "\n": 
            stroki.append(x[line]) #2
    
    for s in range(len(stroki)):
        for c in stroki[s]:
            if not(c.isalpha()) and c != ' ':
                stroki[s] = stroki[s].replace(c,"") #3

    united = " ".join(stroki) #4

    words = united.split()
    dictionary = {}
    for i in words:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1 #5

    popular = sorted(dictionary, key = dictionary.get, reverse = True)
    for i in range(10):
        print(i+1, " place --- ",popular[i], "--- ", dictionary[popular[i]]," times") #6

    united = " " + united + " "
    for i in range(10):
        toreplace = " "+popular[i]+" "
        united = united.replace(toreplace, " PYTHON ")
    united  = united[1:len(united)] #7

    f2 = open("e.txt", "w") #8

    spacepos = 0
    curlen = 0
    start = 0
    for i in range(len(united)):
        curlen += 1
        if united[i] == " ":
            spacepos = i
        if curlen >= 100:
            f2.write(united[start:spacepos])
            #f2.write(" -> ")
            #f2.write(str(spacepos-start))
            f2.write("\n")
            start = spacepos + 1
            curlen = i-start
    f2.write(united[start:len(united)]) #9
    

# Вызов функции
wiki_function()
