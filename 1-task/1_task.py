'''
Написать функцию, которая проверяет является ли строка палиндромом.
'''


def is_palindrome(input_word: str) -> str:
    if len(input_word) < 2:
        raise ValueError('Слово должно быть длиной не менее 2 символов')
    return 'Палиндром' if input_word == input_word[::-1] else 'Не палиндром'


if __name__ == '__main__':
    print(is_palindrome('qwerty'))
    print(is_palindrome('aabbaa'))
    print(is_palindrome('q'))
