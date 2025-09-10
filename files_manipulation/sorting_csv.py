# ordenando arquivos csv com python 
languages = []

with open("languages.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",")
        languages.append((language, category))  # salva como tupla

languages.sort()

with open("languages.csv", "w", encoding="utf-8") as file:
    for language, category in languages:
        file.write(f"{language},{category}\n")

