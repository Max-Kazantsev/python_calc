"""
Пример функции для вычисления выражений записанных в виде обратной
польской нотации.
OPERATORS - список доступных операторов
RPNError  - класс для обработки исключений
FailTest  - класс для проерки тест-кейсов
OKTest    - класс для проерки тест-кейсов
reversed_polish_notation - главная функция вычисляющая выражение
"""

import re
import unittest

# Список доступных операторов связанных с реальными методами float
from ddz import Calc

OPERATORS = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__div__,
    '%': float.__mod__,
    '^': float.__pow__,
}


class RPNError(Exception):
    """Базовый класс для обработки исключений"""

    def __init__(self, message):
        """Сохранение текста исключения"""
        self._message = u"Ошибка вычисления выражения: %s" % message

    def _get_message(self):
        """Заглушка для свойства message"""
        return self._message

    message = property(_get_message)


class FailTest(unittest.TestCase):
    """Тесты с ошибочными исходными данными"""

    def runTest(self):
        """Проверка кейсов"""
        self.assertRaises(RPNError, reversed_polish_notation, "+")
        self.assertRaises(RPNError, reversed_polish_notation, "2 +")
        self.assertRaises(RPNError, reversed_polish_notation, "2 2")
        self.assertRaises(RPNError, reversed_polish_notation, "+ 2 2")
        self.assertRaises(RPNError, reversed_polish_notation, "a 2 -")
        self.assertRaises(RPNError, reversed_polish_notation, "2 2 +-")


class OKTest(unittest.TestCase):
    """Тесты с корректными исходными данными"""

    def runTest(self):
        """Проверка кейсов"""
        self.assertEqual(666, reversed_polish_notation("666"))
        self.assertEqual(2 * 3 + 4, reversed_polish_notation("2 3 * 4 +"))
        self.assertEqual(2 * (3 + 4), reversed_polish_notation("2 3 4 + *"))
        self.assertEqual((7.0 / 2).__pow__(4), reversed_polish_notation("7 2 / 4 ^"))
        self.assertEqual((2 ** 3) ** 4, reversed_polish_notation("2 3 ^ 4 ^"))
        self.assertEqual(2.0 + 3.5 - 6, reversed_polish_notation("2.0 3.5 + 6 -"))
        self.assertEqual(3 ** 4, reversed_polish_notation("3   3  *   3  *  3 *"))
        self.assertEqual(5 + ((1 + 2) * 4) - 3, \
                         reversed_polish_notation("5 1 2 + 4 * 3 -+"))


def reversed_polish_notation(expr):
    """
    Возвращает результат вычисленного выражения записанного в виде обратной
    польской нотации
    expr = string
    """
    ops = OPERATORS.keys()
    stack = []

    for atom in re.split(r"\s+", expr):
        try:
            atom = float(atom)
            stack.append(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops:
                    continue
                try:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                except IndexError:
                    raise RPNError(u"Маловато операндов")

                try:
                    oper = OPERATORS[oper](oper1, oper2)
                except ZeroDivisionError:
                    raise RPNError(u"Нельзя делить на 0")

                stack.append(oper)

    if len(stack) != 1:
        raise RPNError(u"Многовато операндов")

    return stack.pop()


def tokenize(code: str) -> list:
    return code.split()


# DOES NOT WORK
def opn(code: str):
    p = 0
    op_stack: list = []
    res: list = []
    for v in code:
        if re.match("[0-9]+[.]*[0-9]*", v) or re.match("[A-Z]+[a-z]+", v):
            res.append(v)
        elif v in Calc.operators:  # i -бинарная операция
            token_tmp = ''  # смотрим на вверх стека
            if len(op_stack) > 0:
                token_tmp = op_stack[len(op_stack) - 1]  # смотрим на вверх стека
                while len(op_stack) > 0 and token_tmp in Calc.operators:  # пока стек >0
                    # сравнием приоритет токена в строке и приоритет операци  в стеке операций
                    if Calc.operators[v][1] <= Calc.operators[token_tmp][1]:
                        res.append(op_stack.pop())  # если в стеке операция выше,то выталкиваем его в выходную строку
                    else:  # иначе выходим из данного цикла
                        break
            op_stack.append(v)  # тогда выйдя из цикла,добавим операцию в стек        
        elif v == '(':
            op_stack.append(v)
        elif v == ')':  # закрывающая )
            token_tmp = op_stack[len(op_stack) - 1]  # смотрим на вверх стека
            while token_tmp != '(' or len(op_stack) > 1:
                res.append(op_stack.pop())
                token_tmp = op_stack[len(op_stack) - 1]
                if token_tmp == '(':
                    op_stack.pop()
                    # if (len(op_stack)==0):
                    # raise RuntimeError("No left paren")                                                          
    while len(op_stack) > 0:
        token_tmp = op_stack[len(op_stack) - 1]
        if token_tmp == "(":
            raise RuntimeError("No right paren")
        res.append(op_stack.pop())
    return res


if __name__ == "__main__":
    unittest.main()
