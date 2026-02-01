from validations import numbers_input_check, operator_input_check, parse_expression, brackets_check
from config import operations


def calculate(a, b, operation):
    """
    Функция принимает два числа, выполняет математическую операцию и возвращает результат.
    
    :param a: первое число (int или float)
    :param b: второе число (int или float)
    :param operation: строка, обозначающая операцию ('+', '-', '*', '/')
    :raises ZeroDivisionError: Если b == 0 и operation == '/'.
    :raises ValueError: Если operation не входит в список поддерживаемых.
    :return: результат операции или сообщение об ошибке
    """
    # Отладка: вывести полученную операцию
    print(f"[DEBUG] Полученная операция: {operation}")

    # Проверка деления на ноль
    if operation == '/' and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    # Проверка, что операция поддерживается
    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    # Выполнение операции
    
    return operations[operation](a, b)


def user_input():
    """
    Запрашивает у пользователя два числа и операцию, проверяет ввод.
    :raises ValueError: Если ввод некорректен (не число или неподдерживаемая операция).
    :return: кортеж (a, b, operation) или (None, None, None) при ошибке
    """
    print("Введите первое число")
    a = numbers_input_check(input("> "))
    if a is None:
        raise ValueError("Operands must be numbers")
        return None, None, None

    print("Введите математический оператор (сложение: '+' вычитание: '-' умножение: '*' деление: '/')")
    operation = operator_input_check(input("> ").strip())
    if operation is None:
        raise ValueError(f"Unsupported operation: {operation}")
        return None, None, None

    print("Введите второе число")
    b = numbers_input_check(input("> "))
    if b is None:
        raise ValueError("Operands must be numbers")
        return None, None, None

    return a, b, operation



if __name__ == '__main__':
    try:
        a, b, operation = user_input()
        result = calculate(a, b, operation)
        print(f"Результат вычислений: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Ошибка: {e}")