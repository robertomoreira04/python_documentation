# criando arquivos txt em python 

name = input("Digite o seu nome: \n")

"""

Arquivos:
w = write 
r = read
a = append

"""

file = open('name.txt', 'a')
file.write(f'{name}\n')
file.close()

# Forma recomendada abaixo

with open('names2.txt', 'a') as file:
    file.write(f'{name}\n')

