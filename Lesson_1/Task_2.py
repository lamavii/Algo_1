from collections import Counter

 #Эта строка импортирует класс Counter из модуля collections, 
#который используется для подсчета количества повторяющихся 
#элементов в последовательности.

N, K = map(int, input().split())
arr=list(map(int,input().split()))

def count_pairs(arr, t):
    count = 0
    f = Counter(arr) #
    for num in f: #идет по всему словарю freq
        if (t != 0 and num + t in f):
            count += 1
    return count 

c=count_pairs(arr, K)

print(c)
 