# lambda function em python 

# Função de potência de um número
power = lambda num: num ** 2 

# Função que verifica se o número é par 
pair = lambda x: x % 2 == 0 

# Função que divide um número pelo outro 
divNum = lambda x, y : x / y

# Função que inverte uma string 
reverse = lambda s: s[::-1]

print(power(5))
print(pair(27))
print(divNum(10, 2))
print(reverse("Roberto"))
