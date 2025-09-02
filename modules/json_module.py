import json 

# JSON válido como string
person = '{"name": "Roberto", "languages": ["Python", "Javascript"]}'

# Converte de JSON (string) para dicionário Python
person_dict = json.loads(person)
print(person_dict)              # Saída: {'name': 'Roberto', 'languages': ['Python', 'Javascript']}
print(person_dict['languages']) # Saída: ['Python', 'Javascript']

# Converte de dicionário Python para JSON (string)
person_json = json.dumps(person_dict)
print(person_json)              # Saída: {"name": "Roberto", "languages": ["Python", "Javascript"]}
print(type(person_json))        # Saída: <class 'str'>

print(json.dumps(person_dict, indent=4, sort_keys=True)) # Imprimir o dicionário em formato JSON legível

# salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)

# lendo json externo 
with open("nome.json", "r") as f:
    data = json.load(f)
    print(data)

