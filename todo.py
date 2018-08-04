from flask import Flask, jsonify, request

app = Flask ('TODO')
tarefas = []


@app.route ('/task')
def listar():
    return jsonify (tarefas)


@app.route('/task', methods=['POST'])
def criar():
    titulo = request.json.get('titulo')
    descricao = request.json.get('descricao')
    tarefa = {
        'id': len(tarefas) + 1,
        'titulo': titulo,
        'descricao': descricao,
        'estado': False
    }
    return jsonify(tarefa)
