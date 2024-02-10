def pair_with_sum(arr, target):
    # ваша функция pair_with_sum

 def main():
    n = int(input("Введите количество тестов: "))  # вводим количество тестов

    for _ in range(n):
        x = int(input("Введите целевую сумму: "))  # вводим целевую сумму
        arr = list(map(int, input("Введите элементы массива через пробел: ").split()))  # вводим элементы массива через пробел
        result = pair_with_sum(arr, x)
        print(*result)  # выводим результат

 if __name__ == "__main__":
    main()

n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = pair_with_sum(arr, x)
print(*result)   
   