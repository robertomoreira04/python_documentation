my_list = ["Roberto", "Desenvolvedor", "Python", "Django", "FastAPI"]

# iterando entre valores na lista com for
for i in my_list:
    print(i)

# atendendo condição e encerrando loop
for i in my_list:
    if i == "Python":
        break
    print(i)

# pulando condição atendida com o continue 

for i in my_list:
    if i == "Django":
        continue
    print(i)

# iterando até um número específico com range
for i in range(3):
    print(my_list[i])

