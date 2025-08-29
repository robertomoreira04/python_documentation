# dicionários em python 

my_dict = {
    "name": "Roberto", 
    "occupation":"Developer",
    "stack":["Python", "Django", "FastAPI"], #Possibilidade de valor ser uma lista
}

# Temos duas possibilidades de acesso a um valor do dicionário pela chave

print(my_dict["occupation"]) # Saída: Developer

print(my_dict.get('stack')) # Saída: ['Python', 'Django', 'FastAPI']

print(my_dict.keys()) # retorna todas as chaves do dicionário 

# Saída: dict_keys(['name', 'occupation', 'stack'])

print(my_dict.values()) # retorna todos os valores do dicionário

# Saída: dict_values(['Roberto', 'Developer', ['Python', 'Django', 'FastAPI']])

print(my_dict.items()) # retorna uma tupla para cada chave-valor 

# dict_items([('name', 'Roberto'), ('occupation', 'Developer'), ('stack', ['Python', 'Django', 'FastAPI'])])

# Adicionando chave-valor ao dicionário 

my_dict["age"] = 20
print(my_dict) 

# Saída: {'name': 'Roberto', 'occupation': 'Developer', 'stack': ['Python', 'Django', 'FastAPI'], 'age': 20}

# Atualizando valor ao dicionário 

my_dict.update({"age": 21})
print(my_dict)
# Saída: {'name': 'Roberto', 'occupation': 'Developer', 'stack': ['Python', 'Django', 'FastAPI'], 'age': 21}

# Removendo chave e valor do dicionário 
my_dict.pop("age")
print(my_dict)
# Saída: {'name': 'Roberto', 'occupation': 'Developer', 'stack': ['Python', 'Django', 'FastAPI']}

