# funções recursivas em python

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1)) 

    
number = int(input("Digite o número para o fatorial: "))
print(f"O fatorial de {number} é {factorial(number)}")





    
