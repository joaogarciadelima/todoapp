from flask import Flask, jsonify

app = Flask('TODO')
tarefas = []

@app.route('/task')
def listar():
    return jsonify(tarefas)