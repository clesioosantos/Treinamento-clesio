from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Lista de pacientes em memória
pacientes = []
id_counter = 1

# Registrar um novo paciente (POST)
@app.route('/pacientes', methods=['POST'])
def registrar_paciente():
    global id_counter
    data = request.get_json()
    
    if not data or not data.get('nome'):
        abort(400, description="Nome do paciente é obrigatório.")
    
    novo_paciente = {
        'id': id_counter,
        'nome': data['nome'],
        'idade': data.get('idade', None),
        'diagnostico': data.get('diagnostico', None)
    }
    pacientes.append(novo_paciente)
    id_counter += 1
    return jsonify(novo_paciente), 201

# Pegar um paciente pelo ID (GET)
@app.route('/pacientes/<int:paciente_id>', methods=['GET'])
def pegar_paciente(paciente_id):
    paciente = next((p for p in pacientes if p['id'] == paciente_id), None)
    if paciente is None:
        abort(404, description="Paciente não encontrado.")
    return jsonify(paciente), 200

# Atualizar um paciente pelo ID (PUT)
@app.route('/pacientes/<int:paciente_id>', methods=['PUT'])
def atualizar_paciente(paciente_id):
    data = request.get_json()
    paciente = next((p for p in pacientes if p['id'] == paciente_id), None)
    
    if paciente is None:
        abort(404, description="Paciente não encontrado.")
    
    paciente['nome'] = data.get('nome', paciente['nome'])
    paciente['idade'] = data.get('idade', paciente['idade'])
    paciente['diagnostico'] = data.get('diagnostico', paciente['diagnostico'])
    
    return jsonify(paciente), 200

# Deletar um paciente pelo ID (DELETE)
@app.route('/pacientes/<int:paciente_id>', methods=['DELETE'])
def deletar_paciente(paciente_id):
    global pacientes
    paciente = next((p for p in pacientes if p['id'] == paciente_id), None)
    
    if paciente is None:
        abort(404, description="Paciente não encontrado.")
    
    pacientes = [p for p in pacientes if p['id'] != paciente_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)