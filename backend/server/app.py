from flask import Flask, request, after_this_request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

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

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': 'lena_gray_512.tif'
    }

    return jsonify(response_data), 200

@app.route('/images/<filename>')
def serve_image(filename):
    image_directory = os.getcwd()
    return send_from_directory(image_directory, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
