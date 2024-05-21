from fastapi import FastAPI
from api.v1 import (
    lista_marcadores,
)

app = FastAPI()

app.include_router(lista_marcadores.router)
