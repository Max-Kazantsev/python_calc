""" Калькулятор на основе словаря """


#pylint: disable=too-few-public-methods
class Calc:
    """ Класс расширяемого калькулятора на основе словаря """
    operators = {}

    @staticmethod
    def count(expr):
        """
        Функция рассчитывающая значение выражения
        на основе известных классу опереаторов
        """
        stack = []
        for token in expr.split(' '):
            if token in Calc.operators:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(Calc.operators[token][0](op1, op2))
            else:
                stack.append(float(token))
        if len(stack) > 0:
            raise ValueError
        return stack.pop()


def add_to_calc(operator_sign, priority):
    """ Add module to calculator"""

    def wrapper_add_to_calc(operator):
        Calc.operators[operator_sign] = (operator, priority)
        return operator
    return wrapper_add_to_calc


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
def my_mult(a, b):
    return a * b


def rpn(code: str):
    op_stack = []
    res = []
    for symbol in code.split(' '):
        if symbol in Calc.operators:  # i -бинарная операция
            token_tmp = ''
            if len(op_stack) > 0:
                token_tmp = op_stack[-1]  # смотрим на вверх стека
                while len(op_stack) > 0 and token_tmp in Calc.operators:  # пока стек >0
                    # сравнием приоритет токена в строке и приоритет операци  в стеке операций
                    if Calc.operators[symbol][1] <= Calc.operators[token_tmp][1]:
                        # если в стеке операция выше,то выталкиваем его в выходную строку
                        res.append(op_stack.pop())
                    else:  # иначе выходим из данного цикла
                        break
            op_stack.append(symbol)  # тогда выйдя из цикла,добавим операцию в стек        
        elif symbol == '(':
            op_stack.append(symbol)
        elif symbol == ')':  # закрывающая )
            for token_tmp in op_stack[::-1]:
                if token_tmp == '(':
                    op_stack.pop()
                    break
                res.append(op_stack.pop())
        else:
            int(symbol)
            res.append(symbol)

    while len(op_stack) > 0:
        token_tmp = op_stack.pop()
        if token_tmp == '(':
            raise RuntimeError("No right paren")
        res.append(token_tmp)

    return ' '.join(res)

