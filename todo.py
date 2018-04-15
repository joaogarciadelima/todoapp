from flask import Flask, jsonify

app = Flask('TODO')
tarefas = []
tarefas[1] = 'tarefa 1'
tarefas[2] = 'tarefa 2'
tarefas[3] = 'tarefa 3'
tarefas[4] = 'tarefa 4'

@app.route('/task')
def listar():
    return jsonify(tarefas)