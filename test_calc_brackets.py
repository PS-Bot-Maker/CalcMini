from validations import brackets_check, parse_expression
import pytest
def test_brackets_check():
    """тест проверки скобок позитивный вариант"""
    assert brackets_check("(())()") == True

def test_brackets_check_unclosed():
    """тест проверки незакрытых скобок """
    assert brackets_check("(()") == False

def test_brackets_check_unopened():
    """тест проверки лишних закрывающих скобок"""
    assert brackets_check("())") == False

def test_parsing_delete_spaces():
    """Тест функции парсинга проверка очистки от пробелов"""
    assert parse_expression(' () () ()(())') == '()()()(())'

def test_parsing_unclosed_brackets_error():
    """Тест функции парсинга на поднятие ошибки ValueError"""
    with pytest.raises(ValueError):
        parse_expression('(()))')

def test_parsing_reverses_brackets_error():
    """Тест функции парсинга на поднятие ошибки ValueError"""
    with pytest.raises(ValueError):
        parse_expression(')()(')