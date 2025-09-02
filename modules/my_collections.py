# Explorando módulo collection

from collections import Counter, deque

fruits = ["Maçã", "Banana", "Uva", "Pera", "Banana", 
          "Uva", "Maçã", "Laranja", "Banana", "Abacaxi"]

counted_fruits = Counter(fruits) # Contabiliza o número de repetição de cada item 
print(counted_fruits)
# Saída: Counter({'Banana': 3, 'Maçã': 2, 'Uva': 2, 'Pera': 1, 'Laranja': 1, 'Abacaxi': 1})

# Frutas mais comuns
print(counted_fruits.most_common(2)) 
 # Saída: [('Banana', 3), ('Maçã', 2)]

# Acessar contagem de um item específico
print(counted_fruits['Uva'])  # Saída: 2

# usando deque
d = deque([1, 2, 3])
d.append(4)       # adiciona no final
d.appendleft(0)   # adiciona no início
d.pop()           # remove do final
d.popleft()       # remove do início

print(d)  # deque([1, 2, 3])

