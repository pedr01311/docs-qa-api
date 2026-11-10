from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

consultas = [
    {"id": 1, "tipo": "dentista", "dia": "quarta"},
    {"id": 2, "tipo": "advogado", "dia": "quinta"}
]


class Consulta(BaseModel):
    tipo: str
    dia: str


@app.get("/")
def rota_padrao():
    return {"nome" : "pedro"}

@app.get("/consultas")
def listas_consultas():
    return(consultas)

@app.get("/consultas/{consulta_id}")
def buscar_consultas(consulta_id: int):
    for con in consultas:
        if(con["id"] == consulta_id):
            return(con)
    raise HTTPException(status_code=404, detail="Consulta não encontrada")

@app.post("/consultas")
def criar_consulta(consulta: Consulta):   
    dados = consulta.model_dump()
    dados["id"] = len(consultas) + 1
    consultas.append(dados)
    return dados
    

    
       
            