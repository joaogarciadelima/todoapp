from operator import itemgetter

from flask import Flask, jsonify, request, abort

app = Flask ('TODO')
tarefas = []


@app.route ('/task')
def listar():
    return jsonify (sorted(tarefas, key=itemgetter('estado')))


@app.route('/task', methods=['POST'])
def criar():
    titulo = request.json.get('titulo')
    descricao = request.json.get('descricao')
    if not descricao or not titulo:
        abort(400)
    tarefa = {
        'id': len(tarefas) + 1,
        'titulo': titulo,
        'descricao': descricao,
        'estado': False
    }
    tarefas.append(tarefa)
    return jsonify(tarefa), 201

@app.route('/task/<int:id_tarefa>', methods=['DELETE'])
def remover(id_tarefa):
    tarefa = [tarefa for tarefa in tarefas if tarefa['id'] == id_tarefa]
    if not tarefa:
        abort(404)
    tarefas.remove(tarefa[0])
    return '', 204

