#  classes em python

# a classe é um modelo, que instanciado se torna um objeto mostrado abaixo
class Dev:
    name = ""
    languages = ""
    stack = "Python"


roberto = Dev() # instanciando com base na classe Dev

roberto.name = "Roberto Moreira" # adicionando nome 
roberto.languages = "Portuguese", "English"
roberto.stack = "Python", "Django", "FastAPI" # o padrão da classe necessita ser reescrito para manter ("Python")

print("# Informações de Roberto #")
print(f"Nome do desenvolvedor: {roberto.name}")
print(f"Linguagens que fala: {', '.join(roberto.languages)}")
print(f"Stack: {', '.join(roberto.stack)}")

