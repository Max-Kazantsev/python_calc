def my_decorator(smt):
    print(smt)
    def wrapper(func):
        print("Something is happening before the function is called.")
        return func
    return wrapper


@my_decorator(1)
def say_whee():
    print("Whee!")