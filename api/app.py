from dotenv import load_dotenv
from fastapi import FastAPI
import os
from suds.client import Client
from zeep import Client as zeep_client

load_dotenv()

token = os.getenv('TOKEN_SEI')
url = os.getenv('URL_SEI')
client = Client(url)
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
    response = client.service.listarMarcadoresUnidade(**dict_call)
    # import ipdb;ipdb.set_trace(context=10)
    return response


