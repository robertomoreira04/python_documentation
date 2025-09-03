# criando métodos de uma classe 

class Dev:
    def __init__(self, name, languages, stack):
        self.name = name
        self.languages = languages
        self.stack = stack

    # criando método para ser reaproveitado pelo __str__
    def get_description(self):
        return (f"# Informações de {self.name} #\n"
                f"Nome do desenvolvedor: {self.name}\n"
                f"Linguagens que fala: {', '.join(self.languages)}\n"
                f"Stack: {', '.join(self.stack)}")


    def __str__(self):
        return self.get_description()


roberto = Dev("Roberto Moreira", ("Português", "Inglês"), ("Python", "Django", "FastAPI"))

print(roberto)