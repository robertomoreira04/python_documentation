# ordenando csv para dicionário com lambda

languages = []

with open("languages.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",")
        language_dict = {}
        language_dict["language"] = language
        language_dict["category"] = category.lstrip()
        languages.append(language_dict)

for language_dict in sorted(languages, key=lambda language_dict: language_dict["language"]): # a key quem diz pelo que ordenar
    print(f"{language_dict['language']} - {language_dict['category']}")


