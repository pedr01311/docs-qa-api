from fastapi import FastAPI

app = FastAPI()

consultas = [
    {"id": 1, "tipo": "dentista", "dia": "quarta"},
    {"id": 2, "tipo": "advogado", "dia": "quinta"}
]

@app.get("/")
def rota_padrao():
    return {"nome" : "pedro"}

@app.get("/consultas")
def rota_notas():
    return(consultas)

@app.get("/consultas/{consulta_id}")
def verificar_consulta(consulta_id: int):
    for con in consultas:
        if(con["id"] == consulta_id):
            return(con)
            