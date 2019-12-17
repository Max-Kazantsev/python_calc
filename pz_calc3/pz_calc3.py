""" Пример решения pz_calc3 """


# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
def my_diff(a, b):
    return a - b


def my_sum(a, b):
    return a + b


def my_div(a, b):
    return a / b


def my_mul(a, b):
    return a * b


# pylint: enable=missing-function-docstring
# pylint: enable=invalid-name


OPERATIONS = {
    '+': my_sum,
    '-': my_diff,
    '/': my_div,
    '*': my_mul
}
if __name__ == '__main__':
    ANS = ''
    OPERATOR = None

    while ANS != 'exit':
        ANS = input('Введите пример:')
        # for
        for operator_sign in OPERATIONS:
            if operator_sign in ANS:
                A, B = ANS.split(operator_sign)
                OPERATOR = OPERATIONS[operator_sign]
                break
        if not OPERATOR:
            raise ValueError

        print(f"{ANS} = {OPERATOR(int(A), int(B))}")
