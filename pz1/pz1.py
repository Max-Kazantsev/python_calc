""" Пример решения pz1 """


def my_sum(a, b):
    return a + b


if __name__ == '__main__':
    ans = ''
    while ans != 'exit':
        ans = input('Введите пример:')
        a, b = ans.split('+')
        print(f"По-моему это: {my_sum(int(a), int(b))}")
