def find_min(arr: [float]) -> int:
    res = arr[0]

    for num in arr:
        res = num if num < res else res

    return res


def find_max(arr: [float]) -> int:
    res = arr[0]

    for num in arr:
        res = num if num > res else res

    return res


def calc_mult(arr: [float]) -> int:
    res = 1

    for num in arr:
        try:
            res *= num
        except ValueError:
            print('Произведение превышает ограничения типа данных')
            quit()

    return res


def calc_sum(arr: [float]) -> int:
    res = 0

    for num in arr:
        try:
            res += num
        except ValueError:
            print('Сумма чисел превышает ограничения типа данных')
            quit()

    return res


with open('input.txt', 'r') as file:
    raw_data = file.readline().split()
    input_data = []

    for number in raw_data:
        try:
            tmp = float(number)
            input_data.append(tmp)
        except ValueError:
            print('Одно из введеных чисел превышает ограничения типа данных')
            quit()
    print('=== Результат ===')
    print('Минимальное число:', find_min(input_data))
    print('Максимальное число:', find_max(input_data))
    print('Сумма:', calc_sum(input_data))
    print('Произведение:', calc_mult(input_data))
