from fastapi import FastAPI
from typing import List, Dict

#criando instância do FastAPI
app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone que é inteligente",
        "preco": 1500.0,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um computador que é móvel",
        "preco": 3500.0,
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um computador que é móvel",
        "preco": 2500.0,
    }
]

#criando rotas
@app.get("/") # Request
def ola_mundo(): # Response
    return {"Olá": "Pessoal"}

@app.get("/produtos")
def listar_produtos():
    return produtos