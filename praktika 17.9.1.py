array = [int(x) for x in input("Введите числа от 1 до 999 в любом порядке, через пробел: ").split()]


def merge_sort(array):  # "разделяй"
    if len(array) < 2:  # если кусок массива равен 2,
        return array[:]  # выход из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))


def binary_search(arraynew, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if arraynew[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < arraynew[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(arraynew, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(arraynew, element, middle + 1, right)


element = int(input('Введите любое целое число от 1 до 999: '))
array.append(element)
arraynew = sorted(array)


print(arraynew)
print('Индекс введенного элемента:', element, 'в списке равен:', arraynew.index(element))



# while True:
#     try:
#         element = int(input("Введите число от 1 до 999: "))
#         if element < 0 or element > 999:
#             raise Exception
#         break
#     except ValueError:
#         print("Нужно ввести число!")
#     except Exception:
#         print("Неправильный диапазон!")


print('предыдущее число в списке', binary_search(arraynew, element, 0,  len(arraynew)))