# ordenando csv para dicionário 

languages = []

with open("languages.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(",")
        language_dict = {}
        language_dict["language"] = language
        language_dict["category"] = category.lstrip()
        languages.append(language_dict)

def get_language(language_dict):
    return language_dict["language"]

def get_category(language_dict):
    return language_dict["category"]

for language_dict in sorted(languages, key=get_category): # a key quem diz pelo que ordenar
    print(f"{language_dict['language']} - {language_dict['category']}")


