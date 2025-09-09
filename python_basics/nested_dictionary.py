my_nested_dict = {
    "user": {
        "name": "Roberto",
        "occupation": "Developer"
    },
    "stack": {
        "backend": ["Python", "Django", "FastAPI"],
        "frontend": ["HTML", "CSS", "JavaScript"]
    }
}

print(my_nested_dict["stack"]) 
# Saída: {'backend': ['Python', 'Django', 'FastAPI'], 'frontend': ['HTML', 'CSS', 'JavaScript']}

print(my_nested_dict["stack"]["frontend"]) 
# Saída: ['HTML', 'CSS', 'JavaScript']

# Alterando valores no dicionário 

my_nested_dict["stack"]["backend"].append("Flask") # adiciona ao caminho passado
print(my_nested_dict["stack"]["backend"])
# Saída: ['Python', 'Django', 'FastAPI', 'Flask']

my_nested_dict["stack"]["tools"] = "Docker" # adiciona mais um campo ao dicionário de acordo com o caminho
print(my_nested_dict["stack"])
# Saída: {'backend': ['Python', 'Django', 'FastAPI', 'Flask'], 'frontend': ['HTML', 'CSS', 'JavaScript'], 'tools': 'Docker'}

del my_nested_dict["stack"]["tools"] # deleta do dicionário de acordo com o caminho
print(my_nested_dict["stack"])
# Saída: {'backend': ['Python', 'Django', 'FastAPI', 'Flask'], 'frontend': ['HTML', 'CSS', 'JavaScript']}

