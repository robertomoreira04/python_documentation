username = 'Roberto Moreira'

print(username[:])      # 'Roberto Moreira'
# Retorna toda a string (equivalente a não usar slicing)

print(username[:2])     # 'Ro'
# Pega do início até o índice 2 **não incluso** (0 e 1)

print(username[0:9])    # 'Roberto M'
# Pega do índice 0 até o 9 **não incluso** (0 a 8), espaços contam

print(username[::2])    # 'RbtoMrei'
# Pega **todos os caracteres**, mas de 2 em 2 (passo 2)

print(username[1::2])   # 'oer oaa'
# Começa do índice 1 e vai de 2 em 2 (ou seja, caracteres nos índices ímpares)

print(username[::-1])   # 'arieroM otreboR'
# Inverte a string (passo -1 percorre de trás para frente)




