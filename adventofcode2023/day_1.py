import re
from utils import extract_lines

def extract_digits(string):
    results = re.findall(r'\d', string)
    first_and_last = [results[0], results[-1]]
    print(first_and_last)
    return first_and_last

def concatenate_digits(string):
    return ''.join(extract_digits(string))

def sum_all_digits(list_of_strings):
    list_of_ints = [concatenate_digits(x) for x in list_of_strings]
    return sum([int(x) for x in list_of_ints])

def day_1():
    print(sum_all_digits(extract_lines('inputs/day_1.txt')))

day_1()