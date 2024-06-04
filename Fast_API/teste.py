from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# @app.get("/")
# def root():
#     return {'mensagem': 'home page'}

# @app.get("/cadastro")
# def cadastro():
#     return {'mensagem': 'cadastro'}

# @app.get("/login")
# def login():
#     return {'mensagem': 'login'}


# usuarios =  [(1, 'caio','minhasenha1'),(2, 'joão','minhasenha2')]

# @app.post('/usuario')
# def main(nome):
#     for i in usuarios:
#         if i[1] == nome:
#             return i
    
#     return "usuario não existe"


class Usuario(BaseModel):
    id: int
    nome: str
    

@app.post('/usuario')
def main(nome):
    return {'nome': nome}