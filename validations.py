import re

def empty_input_validation(user_string):
    """
    Проверяет, что ввод не пустой. Если пустой — запрашивает повторный ввод.
    :param user_string: строка ввода
    :return: непустая строка
    """
    while not user_string.strip():
        print("Вы ничего не ввели, повторите попытку:")
        user_string = input("> ")
    return user_string.strip()


def is_number(user_number_string):
    """
    Проверяет, является ли строка корректным числом (int/float, с учётом экспоненты).
    :param user_number_string: строка для проверки
    :return: True, если строка — число, иначе False
    """
    # Улучшенный шаблон для чисел: 123, -123, 12.3, -.5, 1.2e-3 и т. п.
    pattern = r'^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$'
    return bool(re.match(pattern, user_number_string.strip()))


def is_operation(user_operator_string):
    """
    Проверяет, что строка содержит ровно один допустимый математический оператор.
    :param user_operator_string: строка для проверки
    :return: True, если строка — один из '+', '-', '*', '/', иначе False
    """
    return user_operator_string.strip() in ['+', '-', '*', '/']


def numbers_input_check(number_string):
    """
    Запрашивает у пользователя ввод числа, пока не будет введено корректное значение.
    :param number_string: начальный ввод (может быть пустым)
    :return: число (float или int)
    """
    number_string = empty_input_validation(number_string)
    
    while not is_number(number_string):
        print(f"Ошибка! '{number_string}' не является числом. Повторите ввод:")
        number_string = input("> ")
        number_string = empty_input_validation(number_string)  # Снова проверяем на пустоту
    
    return float(number_string)  # Возвращаем число


def operator_input_check(operator_string):
    """
    Запрашивает у пользователя ввод оператора, пока не будет введено корректное значение.
    :param operator_string: начальный ввод (может быть пустым)
    :return: оператор (строка: '+', '-', '*' или '/')
    """
    operator_string = empty_input_validation(operator_string)
    
    while not is_operation(operator_string):
        print(f"Ошибка! '{operator_string}' не является математическим оператором.")
        print("Используйте символы '+', '-', '*', '/'")
        operator_string = input("> ")
        operator_string = empty_input_validation(operator_string)  # Снова проверяем на пустоту
    
    return operator_string.strip()  # Возвращаем оператор


def brackets_check(s):
    """
    Docstring для brackets_check
    Функция приминает строку и выполняет проверку скобочной последовательности
    :param s: Входная строка
    :return meetings == 0 - True если проверка пройдена успешно
    """
    meetings = 0
    for c in s:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                return False

    return meetings == 0


def parse_expression(expr):
    """
    [ФУНКЦИЯ ЕЩЁ В РАЗРАБОТКЕ]
    Функция принимает строку, удаляет пробелы, проверяет баланс скобок в выражении, находит внутренние скобки.
    
    :param expr: входящая строка с математическим выражением (string)
    """
    expr = re.sub(r'\s', '', expr)
    print(f"[DEBUG] {expr}")
    if not brackets_check(expr):
        raise ValueError("[DEBUG] Проблемы со скобками!")
    else:    
        return expr