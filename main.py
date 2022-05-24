from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

Estudiantes=[]

class EstudiantesModel(BaseModel):
    id_estudiante:int
    primer_nombre:str
    segundo_nombre:str
    habilidades:List[str]=[]

@app.get("/obtener-todos-los-estudiantes")
def get_students():
    return Estudiantes

@app.get("/obtener-estudiante/{id_estudiante}")
def get_student(id_estudiante:int):
    for estudiante in Estudiantes:
        if estudiante["id_estudiante"] == id_estudiante:
            return estudiante
    return "No existe el estudiante"

@app.post("/guardar_estudiantes/")
def save_students(estudiante:EstudiantesModel):
    Estudiantes.append(estudiante.dict())

    return "Estudiante registrado"

@app.put("/actualizar_estudiantes/{id_estudiante}")
def update_students(actualiza_estudiante:EstudiantesModel,id_estudiante:int):
    for estudiante in Estudiantes:
        if estudiante["id_estudiante"] == id_estudiante:
            estudiante["primer_nombre"]=actualiza_estudiante.primer_nombre
            estudiante["segundo_nombre"]=actualiza_estudiante.segundo_nombre
            estudiante["habilidades"]=actualiza_estudiante.habilidades
            return "Estudiante guardado correctamente"
    return "No existe el estudiante"

@app.delete("/eliminar-estudiante/{id_estudiante}")
def eliminar_estudiante(id_estudiante:int):
    for estudiante in Estudiantes:
        if estudiante["id_estudiante"] == id_estudiante:
            Estudiantes.remove(estudiante)
            return "Estudiante eliminado"
    return "No existe el estudiante"