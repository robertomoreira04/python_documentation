class Dev:
    def __init__(self, name, languages, stack):
        self.name = name
        self.languages = languages
        self.stack = stack

    def __str__(self):
        return (f"# {self.name} #\n"
                f"Linguagens: {', '.join(self.languages)}\n"
                f"Stack: {', '.join(self.stack)}")

    # classmethod que cria um Dev "padrão"
    @classmethod
    def dev_python(cls, name):
        return cls(name, ("Português", "Inglês"), ("Python", "Django", "FastAPI"))


# criando de forma normal
roberto = Dev("Roberto Moreira", ("Português", "Inglês"), ("Python", "Django"))
print(roberto)

print("-"*40)

maria = Dev.dev_python("Maria Silva")
print(maria)
