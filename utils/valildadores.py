import re
import datetime

def cpf_validador(cpf: str) -> bool:
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

def email_validador(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def algum_campo_e_vazio(valores: dict) -> bool:
    return any(
        not value.strip() if isinstance(value, str) else value is None
        for value in valores.values()
    )

def campo_numerico_validador(valores: dict) -> bool:
    if all(val.isnumeric() for val in valores.values()):
        return True
    return False


def data_validador(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False
