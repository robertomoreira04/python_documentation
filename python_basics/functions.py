# funções em python

def welcome():
    print('hello world')

welcome() # chamando a função welcome 

def sum():
    return 5 + 7 

print(sum()) #se o print não for executado dentro da função, precisará do lado de fora para visualizar em terminal 


def welcome_user(name, age):
    if age < 18:
        return f"Hello {name}, you are underage."
    elif age >= 18 and age < 65:
        return f"Hello {name}, you are an adult."
    else:
        return f"Hello {name}, you are a senior."
    
print(welcome_user("Roberto", 17)) # utulizando funções com parâmetros


def user(name="Roberto"):
    print(f"Meu nome é {name}")

user("Roberto") # se passado outro valor, é subscrito do valor padrão da função

