""" Расширяемый калькулятор на основе словаря """
# pylint: disable=too-few-public-methods


class Calc:
    """ Класс расширяемого калькулятора на основе словаря """
    operators = {}

    @staticmethod
    def count(expr: str):
        """
        Функция рассчитывающая значение выражения
        на основе известных классу опереаторов
        """
        stack = []
        for token in rpn(expr).split(' '):
            if token in Calc.operators:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(Calc.operators[token][0](op1, op2))
            else:
                stack.append(float(token))
        if len(stack) != 1:
            raise ValueError
        return stack.pop()


def add_to_calc(operator_sign, priority):
    """ Add module to calculator"""
    def wrapper_add_to_calc(operator):
        Calc.operators[operator_sign] = (operator, priority)
        return operator
    return wrapper_add_to_calc


# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
@add_to_calc('-', 2)
def my_diff(a, b):
    return a-b


@add_to_calc('+', 2)
def my_sum(a, b):
    return a+b


@add_to_calc('/', 5)
def my_div(a, b):
    return a / b


@add_to_calc('^', 6)
def my_pow(a, b):
    return a**b


@add_to_calc('*', 5)
def my_mul(a, b):
    return a * b


def rpn(code: str):
    """
    Преобразование примеров из привычной записи
    в обратную польскую нотацию
    """
    op_stack = []
    res = []
    for symbol in code.split(' '):
        if symbol in Calc.operators:  # i -бинарная операция
            if op_stack:
                while op_stack and op_stack[-1] in Calc.operators:  # пока стек >0
                    # сравнием приоритет операции в строке и приоритет операции в стеке операций
                    if Calc.operators[symbol][1] <= Calc.operators[op_stack[-1]][1]:
                        # если в стеке операция выше,то выталкиваем его в выходную строку
                        res.append(op_stack.pop())
                    else:
                        break
            op_stack.append(symbol)
        elif symbol == '(':
            op_stack.append(symbol)
        elif symbol == ')':  # закрывающая )
            token_tmp = op_stack.pop()
            while token_tmp != '(':
                res.append(token_tmp)
                token_tmp = op_stack.pop()
        else:
            # Проверка что symbol - целочисленное
            int(symbol)
            res.append(symbol)

    while op_stack:
        token_tmp = op_stack.pop()
        if token_tmp == '(':
            raise RuntimeError("No right paren")
        res.append(token_tmp)

    return ' '.join(res)


if __name__ == '__main__':
    print(rpn('( 6 + 10 - 4 ) / ( 1 + 1 * 2 ) + 1'))
