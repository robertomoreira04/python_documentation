# regex em python

import re

text = "Roberto Moreira, Desenvolvedor de Software"

match = re.search(r'Desenvolvedor', text)

print('Índice inicial: ', match.start()) # indice inicial da palavra buscada 
print('Índice final: ', match.end()) # indice final da palavra buscada 

pattern = "[a-m]"

result = re.findall(pattern, text) # retorna o padrão pedido anteriormente
print(text)
print(result)

rule_start = r'^R' # começa com R
rule_end = r'!$' # termina com !

phrases = ['Roberto é Desenvolvedor!', 'João é Marceneiro']

for phrase in phrases:
    if re.match(rule_start, phrase) and re.search(rule_end, phrase):
        print(f'Corresponde: {phrase}')
    else:
        print(f'Não corresponde: {phrase}')

