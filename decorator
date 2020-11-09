def my_decorator(func):
    def wrapper():
        return "<strong>" + func() + "</strong>"
    return wrapper


@my_decorator
def print_input(s=input()):
    return s


print(print_input())
