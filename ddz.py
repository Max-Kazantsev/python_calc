""" Калькулятор на основе словаря """


class Calc:
    operators = {}

    @staticmethod
    def count(expr):
        stack = [0]
        for token in expr.split(' '):
            if token in Calc.operators:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(Calc.operators[token][0](op1, op2))
            else:
                stack.append(float(token))
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


def opn(code: str):
    op_stack = []
    res = []
    for c in code:
        if c in '0123456789':
            res.append(c)
        elif c in Calc.operators:  # i -бинарная операция
            token_tmp = ''  # смотрим на вверх стека
            if len(op_stack) > 0:
                token_tmp = op_stack[len(op_stack) - 1]  # смотрим на вверх стека
                while len(op_stack) > 0 and token_tmp in Calc.operators:  # пока стек >0
                    # сравнием приоритет токена в строке и приоритет операци  в стеке операций
                    if Calc.operators[c][1] <= Calc.operators[token_tmp][1]:
                        res.append(op_stack.pop())  # если в стеке операция выше,то выталкиваем его в выходную строку
                    else:  # иначе выходим из данного цикла
                        break
            op_stack.append(c)  # тогда выйдя из цикла,добавим операцию в стек        
        elif c == '(':
            op_stack.append(c)
        elif c == ')':  # закрывающая )
            token_tmp = op_stack[len(op_stack) - 1]  # смотрим на вверх стека
            while token_tmp != '(' or len(op_stack) > 1:
                res.append(op_stack.pop())
                token_tmp = op_stack[len(op_stack) - 1]
                if token_tmp == '(':
                    op_stack.pop()
        else:
            raise ValueError
    while len(op_stack) > 0:
        token_tmp = op_stack[len(op_stack) - 1]
        if token_tmp == "(":
            raise RuntimeError("No right paren")
        res.append(op_stack.pop())
    return res


print(opn('(3+6)/2'))
print(opn('3+6/2^2'))
print(' '.join(opn('3+6/2^2')))
print(Calc.count(' '.join(opn('3+6/2^2'))))
# print(Calc.count('6 10 + 4 - 1 1 2 * + / 1 +'))
