from calc_mini import calculation
import pytest, math

def test_sum_of_integer():
    """Тест: Сложение целых чисел"""
    assert calculation(2, 2,'+') == 4

def test_sum_of_float():
    """Тест: Умножение натуральных чисел"""
    assert calculation(2.2, 2.4, '*') == 5.28

def test_negative_numbers():
    """Тест: Сложение отрицательных чисел"""
    assert calculation (-76, -76, '+') == -152

def test_zero_division():
    """Тест: Деление на ноль"""
    assert calculation(1, 0, '/') == f"Ошибка! Деление на ноль!"

def test_zero_division_advance():
    """Искуственная ошибка деления на ноль для проверки общего except"""
    operations = {'/': lambda x, y: x / y}
    a, b, operation = 5, 0, '/'
    with pytest.raises(ZeroDivisionError):
        operations[operation](a, b) 
    
def test_unsupported_operation():
    """Тест ошибки неподдерживаемой операции"""
    assert calculation(1, 1, 'a') == f"Ошибка! Неизвестная операция: 'a'"

def test_type_error():
    """Тест ошибки несовместимых типов данных (искуственно)"""
    operations = {'+': lambda x, y: x + y}
    a, b, operation = 5, 'hello', '+'
    with pytest.raises(TypeError):
        operations[operation](a, b)

def test_value_error():
    """Тест некорректного преобразования (искуственно)"""
    operations = {'*': lambda x, y: float(x) * float(y)}
    a, b, operation = 'abc', 3, '*'
    with pytest.raises(ValueError):
        operations[operation](a, b)  

def test_overflow_error():
    """Тест ошибки переполнения (искуственнная)"""
    operations = {'**': lambda x, y: x ** y}
    a, b, operation = 10.0, 1000.0, '**'
    with pytest.raises(OverflowError):    
        operations[operation](a, b)  

def test_key_error():
    """Тест ошибки неподдерживаемой операции (искуственная)"""
    operations = {'+': lambda x, y: x + y}
    a, b, operation = 5, 3, '%'  
    with pytest.raises(KeyError):
        operations[operation](a, b)  

def test_lambda_def_error():
    """Тест ошибки лямбда-функции (искуственная)"""
    operations = {'+': lambda x, y: x + y if x > 0 else 1/0} 
    a, b, operation = -1, 5, '+'
    with pytest.raises(ZeroDivisionError):    
        operations[operation](a, b) 