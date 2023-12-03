import regex as re
from utils import extract_lines

def extract_digits(string):
    results = re.findall(r'\d', string)
    first_and_last = [results[0], results[-1]]

    return first_and_last

def extract_digits_improved(string):
    numbers_dict ={
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # extract all strings that are keys of numbers_dict
    results = re.findall(r'\d|' + '|'.join(numbers_dict.keys()), string.lower(), overlapped=True)

    first = results[0]
    last = results[-1]

    if first in numbers_dict.keys():
        first = numbers_dict[first]
    if last in numbers_dict.keys():
        last = numbers_dict[last]

    first_and_last = [first, last]

    return first_and_last
    # extract written numbers from string like one, two etc.


def concatenate_digits(string):
    return ''.join(extract_digits(string))

def concatenate_digits_improved(string):
    return ''.join(extract_digits_improved(string))

def sum_all_digits(list_of_strings):
    list_of_ints = [concatenate_digits(x) for x in list_of_strings]
    return sum([int(x) for x in list_of_ints])

def sum_all_digits_improved(list_of_strings):
    list_of_ints = [concatenate_digits_improved(x) for x in list_of_strings]
    return sum([int(x) for x in list_of_ints])


def day_1():
    print(sum_all_digits(extract_lines('inputs/day_1.txt')))

def day_1_part_2():
    print(sum_all_digits_improved(extract_lines('inputs/day_1.txt')))

day_1()
day_1_part_2()