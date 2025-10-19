'''
Реализовать декоратор, который выводит в консоль время выполнения декорируемой функции. Протестировать работу декоратора на двух функциях:

Функция вычисляет сумму двух чисел a и b, выводит результат в консоль
Функция читает из файла input.txt значение двух чисел a и b, записывает результат вычисления в файл output.txt (файлы приложить к репозиторию)
'''
import time


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f'Время выполнения составило: {execution_time}')
        return result

    return wrapper


@time_counter
def add_two_numbers(a: float, b: float) -> None:
    result = a + b
    print(f'Сумма чисел: {a} + {b} = {result}')


@time_counter
def read_numbers_from_file(input_path: str = 'input.txt', output_path: str = 'output.txt'):
    with open(input_path, 'r', encoding='utf-8') as input_file:
        data = input_file.read().split()

    a, b = map(float, data[:2])
    result = a + b

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f'{result}')



if __name__ == '__main__':
    add_two_numbers(109, 200)

    read_numbers_from_file()
