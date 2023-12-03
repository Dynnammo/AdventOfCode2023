import pytest
import adventofcode2023.day_1 as day_1
def test_extract_line_correctly():
    assert day_1.concatenate_digits('1abc2') == '12'
    assert day_1.concatenate_digits('pqr3stu8vwx') == '38'
    assert day_1.concatenate_digits('a1b2c3d4e5f') == '15'
    assert day_1.concatenate_digits('tre7buchet') == '77'

def test_sum_correctly():
    assert day_1.sum_all_digits(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'tre7buchet']) == 142