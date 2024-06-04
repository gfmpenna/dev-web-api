from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()


class Todo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]


lista = []


@app.post("/inserir")
def inserir(todo: Todo):
    try:
        lista.append(todo)
        return {"Status": "Sucesso"}
    except:
        return {"Status": "Erro"}


@app.post("/listar")
def listar(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, lista))


@app.get("/listaid")
def listagem_unica(id: int):
    try:
        return lista[id]
    except:
        return {"Status": "Erro: Id não existe!"}

@app.post("/alteraStatus")
def alterar_tarefa(id :int):
    try:
        lista[id].realizada = not lista[id].realizada
        return {'Status': 'Sucesso, tarefa atualizada!'}
    except:
        return {'Status': 'Erro, Tarefa inexistente'}
    
@app.post("/deletar")
def excluir_tarefa(id :int):
    try:
        del lista[id]
        return {'Status': 'Tarefa excluida com sucesso'}
    except:
        return {'Status': 'Erro: ID não existe!'}