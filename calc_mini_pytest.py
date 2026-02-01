from calc_mini import calculate
import pytest

def test_sum_of_integer():
    """Тест: Сложение целых чисел"""
    assert calculate(2, 2,'+') == 4

def test_sum_of_float():
    """Тест: Умножение натуральных чисел"""
    assert calculate(2.2, 2.4, '*') == 5.28

def test_negative_numbers():
    """Тест: Сложение отрицательных чисел"""
    assert calculate (-76, -76, '+') == -152

def test_zero_division():
    """Тест: Деление на ноль"""
    with pytest.raises(ZeroDivisionError):
        calculate(1, 0, '/') 
    
def test_unsupported_operation():
    """Тест ошибки неподдерживаемой операции"""
    with pytest.raises(ValueError):
        calculate(1, 1, 'a')