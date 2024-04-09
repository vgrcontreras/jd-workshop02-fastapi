from fastapi import FastAPI
from typing import List, Dict

#criando instância do FastAPI
app = FastAPI()

#criando rotas
@app.get("/") # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}