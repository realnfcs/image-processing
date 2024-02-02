from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "http://localhost:5173/algebraic"}})

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_file():

    print(request.form)
    print(request.files)

    file1 = request.files['file1']
    file2 = request.files['file2']

    # Acessa os valores dos campos adicionais
    method = request.form.get('operation')
    parameter = request.form.get('parameter')

    file1.save('./' + file1.filename)
    file2.save('./' + file2.filename)

    # Exemplo: Imprimir os valores dos campos adicionais
    print('Method:', method)
    print('Parameter:', parameter)

    return 'Arquivos recebidos e salvos com sucesso'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
