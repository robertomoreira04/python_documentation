import random 


# Seleciona valor aleatório de uma lista 
list1 = [7, 2, 5, 4, 3] 
print(random.choice(list1))

# Gera um número aleatório entre um intervalo de valores
r1 = random.randint(5, 15)
print(r1)


# Seleciona um caractere aleatório de uma string 
name = "Roberto Moreira"
r2 = random.choice(name)
print(r2)

# Seleciona mais de um valor aleatório 
print(random.sample(list1, 2))
print(random.sample(name, 2))

