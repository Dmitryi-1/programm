from typing import List
import re


def my_t9(digits) -> List[str]:
    with open('/usr/share/dict/words', 'r') as file:
        word_list = file.read().splitlines()

    digit_letters = {'2': 'abc',
                     '3': 'def',
                     '4': 'ghi',
                     '5': 'jkl',
                     '6': 'mno',
                     '7': 'pqrs',
                     '8': 'tuv',
                     '9': 'wxyz'}

    def find_words(combination, remaining_digits):
        if len(remaining_digits) == 0:
            if combination in word_list:
                return [combination]
            else:
                return []

        current_digit = remaining_digits[0]
        letters = digit_letters[current_digit]
        words = []
        for letter in letters:
            new_combination = combination + letter
            words += find_words(new_combination, remaining_digits[1:])
        return words

    digits = re.sub('[^2-9]', '', digits)  # Оставляем только цифры от 2 до 9
    result = find_words('', digits)
    return result


if __name__ == '__main__':
    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')