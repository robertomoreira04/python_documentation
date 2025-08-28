username = "Roberto Moreira"

print(username.upper())
print(username.lower())
print(username.capitalize()) # primeiro caractere da string em maiúsculo, demais em minúsculo 
print(username.title()) # similar ao capitalize, usando letras maiúsculas em cada inicio de palavra
print(username.center(30, '-')) # usado para preencher espaços até um determinado número de caracteres
print(username.find('a')) # encontra caracteres na string e retorna sua posição
print(username.count('a')) # como o nome diz, conta caracteres
print(username.replace("Roberto", "Jorge")) # substitui caracteres 
print(username.split(',')) # quebra a linha de acordo com o caractere especificado (Obs: necessita estar presente na string)

