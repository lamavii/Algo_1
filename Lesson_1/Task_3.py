from random import choice

def pair(arr, t):
    num_index = {}
    pairs = []
    for i, num in enumerate(arr):
        complement = t - num
        if complement in num_index:
            pairs.append((num_index[complement] + 1, i + 1))
        num_index[num] = i
    if pairs:
        return choice(pairs)  # возвращает случайную пару чисел из списка pairs
    else:
        return -1

n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = pair(arr, x)
print(*result) 


