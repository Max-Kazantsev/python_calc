""" Калькулятор на основе словаря """
import re


def my_diff(*args):
    result = args[0]
    for i in range(1, len(args)):
        result -= i
    return result


def my_sum(*args):
    result = args[0]
    for i in range(1, len(args)):
        result += i
    return result


def my_div(*args):
    result = args[0]
    for i in range(1, len(args)):
        result /= i
    return result


def my_mult(*args):
    result = args[0]
    for i in range(1, len(args)):
        result *= i
    return result


OPERATIONS = {
    '+': my_sum,
    '-': my_diff,
    '/': my_div,
    '*': my_mult
}


def calc(s):
    nums = re.split(f"[{''.join(OPERATIONS.keys())}]", s)
    # pos =


print(calc('3+4/2-12'))
