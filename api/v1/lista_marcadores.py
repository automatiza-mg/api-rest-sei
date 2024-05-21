from api import (
    client,
    token,
    APIRouter,
    WebFault,
)

router = APIRouter()

@router.get('/v1/lista_marcadores')
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
