array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
k=0
for i in range(len(array)):  # проходим по всему массиву
    idx_max = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):  #
        if array[j] > array[idx_max]:
            idx_max = j
        k += 1
    if i != idx_max:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_max] = array[idx_max], array[i]

print(array, k)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
k = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i

    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        k += 1
    array[idx] = x


print(array, k)