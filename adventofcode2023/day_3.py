import re
from utils import extract_lines

MATRIX = []
NUMBER_COORDINATES = []
VALID_NUMBERS = []

def create_matrix(list):
    for i in range(len(list[0])):
        line = []
        for j in range(len(list)):
            line.append(list[i][j])
        MATRIX.append(line)

def get_value(i,j):
    if i < 0 or j < 0:
        return None
    if i >= len(MATRIX) or j >= len(MATRIX[0]):
        return None
    return MATRIX[i][j]

def find_valid_numbers_in_matrix():
    for i in range(len(MATRIX)):
        line = ''.join(MATRIX[i])
        numbers_coordinates = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        for number_coordinates in numbers_coordinates:
            surrounding_values = get_surrounding_values(i, number_coordinates[0], number_coordinates[1])
            if not is_valid_character(surrounding_values):
                VALID_NUMBERS.append(int(line[number_coordinates[0]:number_coordinates[1]]))

def get_surrounding_values(line_index,start, end):
    surrounding_values = []
    for j in range(start-1, end+1):
        surrounding_values.append(get_value(line_index-1, j))
        surrounding_values.append(get_value(line_index+1, j))
    surrounding_values.append(get_value(line_index, start-1))
    surrounding_values.append(get_value(line_index, end))
    return surrounding_values

def is_valid_character(values):
    for value in values:
        if value not in ['.',None]:
            return False
    return True

def compute_result():
    result = 0
    for number in VALID_NUMBERS:
        result += number
    print(result)

create_matrix(extract_lines('inputs/day_3.txt'))
find_valid_numbers_in_matrix()
compute_result()
