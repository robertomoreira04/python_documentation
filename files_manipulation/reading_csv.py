# lendo arquivos csv com python

with open("languages.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",") 
        print(f"{language} -{category}")
