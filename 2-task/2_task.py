'''
Написать функцию, которая принимает два аргумента: лямбда функция для фильтрации массива, массив строк. Сделать вызов данной функции для следующих функций фильтрации:

Исключить строки с пробелами
Исключить строки, начинающиеся с буквы “a”
Исключить строки, длина которых меньше 5
'''

from typing import List, Callable


def filter_strings(my_filter: Callable[[str], bool], data: List[str]) -> List[str]:
    return [item for item in data if my_filter(item)]


if __name__ == '__main__':
    strings = ["apple", "banana", "audi", "  spaced", "cat", "alpha", "hello", "test"]

    no_spaces = filter_strings(lambda s: ' ' not in s, strings)
    print("Без пробелов:", no_spaces)

    not_start_with_a = filter_strings(lambda s: not s.lower().startswith('a'), strings)
    print("Не начинаются с 'a':", not_start_with_a)

    length_gte_5 = filter_strings(lambda s: len(s) >= 5, strings)
    print("Длина ≥ 5:", length_gte_5)
