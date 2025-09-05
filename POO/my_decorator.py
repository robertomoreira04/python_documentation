# criando um decorator em python 

def my_decorator_func(func):
    def wrapper():
        print("🎀 Antes de abrir o presente")
        func()  
        print("🎀 Depois de abrir o presente")
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

