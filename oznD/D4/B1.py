# Один из способов придумать пароль – взять фразу и оставить первые буквы
# каждого слова. Написать функцию make_password, выполняющую задачу генерации
# такого пароля из заданной фразы, при этом буквы i и I заменить на цифру 1,
# буквы o и O на цифру 0, буквы s и S на цифру 5.
#
# Примеры:
# make_password("The future belongs to those, Who believe in beauty of their dreams") ==> "TfbttWb1b0td"

import traceback


def make_password(phrase):
    pas = ""
    pas += phrase[0]
    for i in range(len(phrase)):
        if phrase[i-1] == ' ':
            pas += phrase[i]
    pas = change(pas)
    return pas

def change(word):
    r = ""
    for i in word:
        if i == 'i' or i == 'I':
            r += '1'
        elif i == 'o' or i == 'O':
            r += '0'
        elif i == 's' or i == 'S':
            r += '5'
        else:
            r += i
    return r



# Тесты
try:
    assert make_password("Give me liberty or give me sweets") == "Gml0gm5"
    assert make_password("Keep Calm and Carry On") == "KCaC0"
    assert make_password("The future belongs to those, Who believe in beauty of their dreams") == "TfbttWb1b0td"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
