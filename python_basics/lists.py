list = ["Roberto", "Desenvolvedor", "Python"]

print(len(list))          # 3 → retorna o tamanho da lista
print(list[0])            # "Roberto" → acessa o elemento no índice 0
print(list.index("Roberto")) # 0 → retorna o índice do elemento "Roberto"

list.append("Django")     # adiciona "Django" ao final da lista
print(list)               # ['Roberto', 'Desenvolvedor', 'Python', 'Django']

list.sort()               # ordena a lista em ordem alfabética
print(list)               # ['Desenvolvedor', 'Django', 'Python', 'Roberto']

new_list = list.copy()    # copia os itens de uma lista para outra

new_list.remove("Django") # remove um item específico da lista

new_list.clear() # remove todos os itens restantes

