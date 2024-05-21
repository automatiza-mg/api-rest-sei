from dotenv import load_dotenv
from fastapi import FastAPI
import os
from suds.client import Client
from suds import WebFault

load_dotenv()

token = os.getenv('TOKEN_SEI')
url = os.getenv('URL_SEI')
client = Client(url, faults=False)
app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}

@app.get('/lista_marcadores')
def lista_marcadores():
    dict_call = {
        'SiglaSistema': 'Automatiza_MG',
        'IdentificacaoServico': token,
        'IdUnidade': '110001002',
    }
    try:
        response = client.service.listarMarcadoresUnidade(**dict_call)
        return response
    except WebFault as error:
        return error
