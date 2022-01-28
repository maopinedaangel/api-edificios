from fastapi import FastAPI
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.edificios_db import EdificioDB

api = FastAPI()

origins = [
    "http://localhost:8080"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@api.get("/saludo")
async def decir_hola():
    return {"mensaje": "Hola"}


@api.get("/edificios")
async def mostrar_edificios(db: Session = Depends(get_db)):
    lista_edificios = db.query(EdificioDB).all()
    return lista_edificios

@api.post("/nuevo")
async def crear_edificio(db: Session = Depends(get_db)):

    return { "mensaje": "Se creó el edificio correctamente." }