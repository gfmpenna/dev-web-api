from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {'mensagem': 'Home Page'}

@app.get("/cadastro")
def cadastro():
    return {'mensagem': 'Cadastro'}

@app.get("/login")
def login():
    return {'mensagem': 'Login'}


usuarios =  [(1, 'Caio','Minhasenha1'),(2, 'João','Minhasenha2')]

@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i
    
    return "Usuario não existe"