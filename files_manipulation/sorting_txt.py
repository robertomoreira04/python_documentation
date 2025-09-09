# ordenando arquivos txt por alfabeto e retornando

names = []

with open("name.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.strip())

names.sort()  

with open("name.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(f"{name}\n")

