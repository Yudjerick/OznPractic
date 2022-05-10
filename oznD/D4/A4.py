# Написать функцию change_arr(arr,n,q), которая получает список уникальных положительных целых чисел 
# и два дополнительных положительных целых числа и возвращает переставленный список.
# Переставить arr надо так, чтобы сумма любых n последовательных значений не превышала q. 
#
# Пример:
# change_arr((3,5,7,1,6,8,2,4),3,13)) ==> (4,7,1,5,6,2,3,8) --> 4+7+1<=13, 7+1+5<=13, 1+5+6<=13, ...


import traceback
import itertools

def sumN(arr, n , i):
	sum = 0
	for k in range(n):
		if k+i < len(arr):
			sum += arr[k+i]
	return sum

def change_arr(arr,n,q):
	for i in itertools.permutations(arr, len(arr)):
		flag = True
		for j in range(len(i)):
			if sumN(i,n,j) > q:
				flag = False
				break
		if flag:
			return i
	return []

print(change_arr((1,2,4,3,5),2,7))
print(change_arr((3,5,7,1,6,8,2,4),3,13))
# Тесты
#try:
#	assert change_arr((3,5,7,1,6,8,2,4),3,13) == (4,7,1,5,6,2,3,8)
#	assert change_arr((7,12,6,10,3,8,5,4,13,2,9),4,28) == (4,9,10,3,5,8,12,2,6,7,13)
#	assert change_arr((9,16,11,6,15,14,19,3,12,18,7),3,35) == (11,18,3,14,15,6,12,16,7,9,19)
#	assert change_arr((33,34,29,25,36,30,27,32,21,35,39),5,155) == (32,33,34,21,30,36,25,27,35,29,39)
#	assert change_arr((22,14,30,25,29,19,21,17,15,32,20),4,92) == (32,14,15,19,20,30,22,17,21,25,29)
#except AssertionError:
#    print("TEST ERROR")
#    traceback.print_exc()
#else:
#    print("TEST PASSED")