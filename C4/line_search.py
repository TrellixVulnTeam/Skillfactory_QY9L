def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

def count(array, element):
    k = 0
    for i in array:
        if i == element:
            k += 1

    if k == 0 :
        return False
    return k

array = list(map(int, input("Введите массив").split()))
element = int(input("Введите нужный элемент"))

print(f"Индекс элемента: {find(array, element)}")
print(f"Кол-во элементов: {count(array, element)}")

93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000