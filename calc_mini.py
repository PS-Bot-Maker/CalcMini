from validations import numbers_input_check, operator_input_check
from config import operations


def calculation(a, b, operation):
    """
    Функция принимает два числа, выполняет математическую операцию и возвращает результат.
    
    :param a: первое число (int или float)
    :param b: второе число (int или float)
    :param operation: строка, обозначающая операцию ('+', '-', '*', '/')
    :return: результат операции или сообщение об ошибке
    """
    # Отладка: вывести полученную операцию
    print(f"[DEBUG] Полученная операция: {operation}")

    # Проверка деления на ноль
    if operation == '/' and b == 0:
        return "Ошибка! Деление на ноль!"

    # Проверка, что операция поддерживается
    if operation not in operations:
        return f"Ошибка! Неизвестная операция: '{operation}'"

    # Выполнение операции
    try:
        result = operations[operation](a, b)
        return result
    except Exception as e:
        return f"Ошибка при вычислении: {e}"



def user_input():
    """
    Запрашивает у пользователя два числа и операцию, проверяет ввод.
    :return: кортеж (a, b, operation) или (None, None, None) при ошибке
    """
    print("Введите первое число")
    a = numbers_input_check(input("> "))
    if a is None:
        print("Ошибка ввода первого числа!")
        return None, None, None

    print("Введите математический оператор (сложение: '+' вычитание: '-' умножение: '*' деление: '/')")
    operation = operator_input_check(input("> ").strip())
    if operation is None:
        print("Ошибка ввода оператора!")
        return None, None, None

    print("Введите второе число")
    b = numbers_input_check(input("> "))
    if b is None:
        print("Ошибка ввода второго числа!")
        return None, None, None

    return a, b, operation



if __name__ == '__main__':
    a, b, operation = user_input()

    if a is None or b is None or operation is None:
        print("Вычисление прервано из-за ошибки ввода.")
    else:
        cal_var = calculation(a, b, operation)
        print(f"Результат вычислений: {cal_var}")