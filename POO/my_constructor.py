# classes com constructor

class Dev:
    def __init__(self, name, languages, stack):
        self.name = name
        self.languages = languages
        self.stack = stack

    # método que define como o objeto vai ser exibido
    def __str__(self):
        return (f"# Informações de {self.name} #\n"
                f"Nome do desenvolvedor: {self.name}\n"
                f"Linguagens que fala: {', '.join(self.languages)}\n"
                f"Stack: {', '.join(self.stack)}")
    

# ao usar o init sem adicionar um valor padrão, torna-se obrigatório aderir valor a todos os parâmetros
roberto = Dev(
    "Roberto Moreira",
    ("Portuguese", "English"),
    ("Python", "Django", "FastAPI")
)

print(roberto)  # podemos acessar o objeto "puro" graças a __str__




