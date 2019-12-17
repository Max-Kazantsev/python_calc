""" Пример решения pz_calc1 """


# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
def my_sum(a, b):
    return a + b
# pylint: enable=missing-function-docstring
# pylint: enable=invalid-name


if __name__ == '__main__':
    ANS = ''
    while ANS != 'exit':
        ANS = input('Введите пример:')
        A, B = ANS.split('+')
        print(f"По-моему это: {my_sum(int(A), int(B))}")
