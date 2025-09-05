# usando decorator em python 

from my_decorator import my_decorator_func, uppercase_decorator

@my_decorator_func
def my_gift():
    print("Abrindo o presente")

my_gift()

@uppercase_decorator
def my_string():
    return "Hello world"

print(my_string())

