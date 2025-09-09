# type hint em python 
# pip install mypy (para retornar verificação de tipo)


# Variável que recebe uma string
nome: str = "Roberto"

# Função que recebe e retorna string
def hello(name: str) -> str:
    return f'Olá, {name}!'

# Lista que recebe apenas strings
nomes: list[str] = ["Ana", "Bruno", "Carla"]

# Dicionário com chave string e valor string
contatos: dict[str, str] = {
    "email": "exemplo@email.com",
    "telefone": "12345"
}

print(contatos)