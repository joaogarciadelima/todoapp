from todo import app
from todo import tarefas
from flask import request

def test_listar_tarefas_deve_retornar_status_200():
    with app.test_client() as cliente:
        resposta = cliente.get('/task')
        assert resposta.status_code == 200

def test_listar_tarefas_deve_ter_formato_json():
    with app.test_client() as cliente:
        resposta = cliente.get('/task')
        assert resposta.content_type == 'application/json'

def test_lista_de_tarefas_vazia_retorna_lista_vazia():
    with app.test_client() as cliente:
        resposta = cliente.get('/task')
        assert resposta.data == b'[]\n'

def test_lista_de_tarefas_nao_vazia_retorna_conteudo():
    tarefas.append({'id': 1, 'titulo': 'tarefa 1',
                    'descricao': 'tarefa de numero 1', 'estado': False})
    with app.test_client() as cliente:
        resposta = cliente.get('/task')
        assert resposta.data == (b'[\n  {\n    "descricao": '
                                 b'"tarefa de numero 1", \n    '
                                 b'"estado": false, \n    '
                                 b'"id": 1, \n    '
                                 b'"titulo": "tarefa 1"\n  }\n]\n')


def test_criar_tarefa_retorna_tarefa_inserida():
    tarefas.clear()
    cliente = app.test_client()
    # realiza a requisição utilizando o verbo POST
    resposta = cliente.post('/task', data=json.dumps({
        'titulo': 'titulo',
        'descricao': 'descricao'}),
        content_type='application/json')
    # é realizada a análise e transformação para objeto python da resposta
    data = json.loads(resposta.data.decode('utf-8'))
    assert data['id'] == 1
    assert data['titulo'] == 'titulo'
    assert data['descricao'] == 'descricao'
    # qaundo a comparação é com True, False ou None, utiliza-se o "is"
    assert data['estado'] is False