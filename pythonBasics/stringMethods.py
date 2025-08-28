username = "Roberto Moreira"

print(username.upper())      
# Saída: 'ROBERTO MOREIRA' → todas as letras em maiúsculas

print(username.lower())      
# Saída: 'roberto moreira' → todas as letras em minúsculas

print(username.capitalize()) 
# Saída: 'Roberto moreira' → primeira letra da string maiúscula, resto em minúsculas

print(username.title())      
# Saída: 'Roberto Moreira' → primeira letra de cada palavra em maiúscula

print(username.center(30, '-')) 
# Saída: '-------Roberto Moreira--------' → centraliza em 30 caracteres, preenchendo com '-'

print(username.find('a'))    
# Saída: 11 → índice da primeira ocorrência de 'a', -1 se não encontrado

print(username.count('a'))   
# Saída: 2 → quantidade de vezes que 'a' aparece na string

print(username.replace("Roberto", "Jorge")) 
# Saída: 'Jorge Moreira' → substitui "Roberto" por "Jorge"

print(username.split(','))   
# Saída: ['Roberto Moreira'] → divide a string pelo separador ','; se não houver, retorna lista com a string inteira
