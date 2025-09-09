# lendo arquivos txt existentes

with open("name.txt", "r", encoding="utf-8") as file: # se atentar a hierarquia de pastas
    for line in file:
        print(f'Olá, {line.strip()}') # retirar espaços 

