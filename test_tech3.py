from functools import reduce
import operator
from code import calc_sum, calc_mult, find_max, find_min
from random import randrange
import tracemalloc
import time


def test_sum():  # Проверка нахождения суммы
    data = [randrange(-(10 ** 6), 10 ** 6) for _ in range(10)]
    for _ in range(10000):
        assert calc_sum(data) == sum(data)


def test_mul():  # Проверка нахождения произведения
    data = [randrange(-(10 ** 6), 10 ** 6) for _ in range(10)]
    for _ in range(10000):
        assert calc_mult(data) == reduce(operator.mul, data)


def test_max():  # Проверка нахождения максимального
    data = [randrange(-(10 ** 6), 10 ** 6) for _ in range(10)]
    for _ in range(10000):
        assert find_max(data) == max(data)


def test_min():  # Проверка нахождения минимального
    data = [randrange(-(10 ** 6), 10 ** 6) for _ in range(10)]
    for _ in range(10000):
        assert find_min(data) == min(data)


def test_time_exp(limit=1):  # Проверка присроста времени
    test_data = []

    for _ in range(1000):
        test_data += [randrange(-(10 ** 6), 10 ** 6) for _ in range(10)]
        t0 = time.time()
        find_min(test_data)
        find_max(test_data)
        calc_sum(test_data)
        calc_mult(test_data)
        t1 = time.time()

        assert t1 - t0 <= limit


def test_memory_usage(memory_limit=10):  # Проверка прироста использования памяти
    test_data = []

    for _ in range(1000):
        test_data += [randrange(-(10 ** 6), 10 ** 6) for _ in range(10)]
        tracemalloc.start()
        find_min(test_data)
        find_max(test_data)
        calc_sum(test_data)
        calc_mult(test_data)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        assert peak / 10**6 <= memory_limit
