import array
import random

N = int(input("Введіть розмір масиву N: "))

arr = array.array('d', [0.5**i for i in range(N)])

for _ in range(N):
    arr.append(random.uniform(-1, 3))

sorted_list = sorted(list(arr), reverse=True)

result_list = sorted_list[2:-2]

arr_result = array.array('d', result_list)

print("Результат обробки масиву:")
print(list(arr_result))
