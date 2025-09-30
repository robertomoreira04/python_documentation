# criando uma api simples com fastapi

from fastapi import FastAPI

app = FastAPI()

jogadores = {
    1:{
        "nome": "Fernandinho",
        "idade": 30,
        "time": "Flamengo"
    },
    2:{
        "nome": "Amaral",
        "idade": 20,
        "time": "Seviila"
    },
    3:{
        "nome": "Gonzalo",
        "idade": 35,
        "time": "Santos"
    },
}

@app.get('/')
def menu():
    return {"Mensagem": "Olá mundo!"}

@app.get('/jogadores')
def lista_jogadores():
    return jogadores

# path parameter
@app.get('/busca-jogador/{jogador_id}')
def busca_jogador(jogador_id: int):
    return jogadores[jogador_id]

# query parameter
@app.get('/busca-jogador-nome')
def busca_jogador_nome(nome: str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]['nome'] == nome:
            return jogadores[jogador_id]
    return {"Dados": "Não foi encontrado nenhum jogador"}


