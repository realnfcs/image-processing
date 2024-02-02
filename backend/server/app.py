from flask import Flask, request, after_this_request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import numpy as np
import cv2 as cv

projeto_path = os.path.abspath('..')

sys.path.append(projeto_path)

from improc import dissolve, negative, thresholding, pow_transformation, log_transformation, contrast_broadering, histogram_equalization, histogram_expansion, zoom_in, zoom_out, rotation, rebound, shear, filter, sobel, sharpening_laplacian, convolution

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

def read_image(file):
    image = cv.imdecode(np.frombuffer(file.read(), np.uint8), cv.IMREAD_GRAYSCALE)
    return image

def save_image(image, filename="response.jpg"):
    # Salvar a imagem usando OpenCV
    print(filename)
    filepath = os.path.join(os.getcwd(), filename)
    cv.imwrite(filepath, image)
    return filename

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/algebraic', methods=['POST'])
def algebraic():

    #print(request.form)
    #print(request.files)

    file1 = request.files['file1']
    file2 = request.files['file2']

    # Acessa os valores dos campos adicionais
    method = request.form.get('operation')
    parameter = request.form.get('parameter')

    #file1.save('./' + file1.filename)
    #file2.save('./' + file2.filename)

    image1 = read_image(file1)
    image2 = read_image(file2)

    print('Method:', method)
    print('Parameter:', parameter)

    if (method == "dissolver uniforme"):
        output = dissolve.uniform_closs_dissolve(image1, image2, float(parameter))
    elif (method == "dissolver cruzado"):
        height, width = image1.shape
        t = np.random.randint(0, 2, size=(height, width), dtype=np.uint8)
        output = dissolve.non_uniform_cross_dissolve(image1, image2, t)

    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200

@app.route('/intensity-transformation', methods=['POST'])
def intensity_transformation():

    print(request.form)
    print(request.files)

    operation = request.form.get('operation')
    file1 = request.files['file1']
    image1 = read_image(file1)

    output = np.empty((1, 1))

    if (operation == 'negativo'):
        output = negative.negative(image1)
    elif (operation == 'limiarizacao'):
        t = request.form.get('parameter1')
        output = thresholding.thresholding(image1, int(t))
    elif (operation == 'potencia'):
        c = request.form.get('parameter1')
        y = request.form.get('parameter2')
        output = pow_transformation.pow_transformation(image1, int(c), float(y))
    elif (operation == 'logaritmica'):
        c = request.form.get('parameter1')
        output = log_transformation.log_transformation(image1, float(c))
    elif (operation == 'alargamento'):
        smin = request.form.get('parameter1')
        smax = request.form.get('parameter2')
        output = contrast_broadering.contrast_broadering(image1, int(smin), int(smax))


    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200
    
@app.route('/histogram', methods=['POST'])
def histogram():
    print(request.form)
    print(request.files)

    operation = request.form.get('operation')
    file = request.files['file1']
    image = read_image(file)

    output = np.empty((1, 1))

    if (operation == 'expansao'):
        output = histogram_expansion.histogram_expansion(image)
    elif (operation == 'equalizacao'):
        output = histogram_equalization.histogram_equalization(image)
    
    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200

@app.route('/geometric', methods=['POST'])
def geometric():
    print(request.form)
    print(request.files)

    operation = request.form.get('operation')
    parameter = request.form.get('parameter')
    file = request.files['file1']
    image = read_image(file)

    output = np.empty((1, 1))

    if (operation == 'zoom in'):
        output = zoom_in.zoom_in_replication(image, float(parameter))
    elif (operation == 'zoom out'):
        output = zoom_out.zoom_out(image, float(parameter))
    elif (operation == 'cisalhamento'):
        output = shear.shear(image, float(parameter))
    elif (operation == 'rebatimento'):
        output = rebound.rebound(image, int(parameter))
    elif (operation == 'rotacao'):
        output = rotation.rotation(image, int(parameter))

    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200

@app.route('/filters', methods=['POST'])
def filters():
    print(request.form)
    print(request.files)

    operation = request.form.get('operation')
    file = request.files['file1']
    image = read_image(file)

    output = np.empty((1, 1))

    if (operation == "media"):
        output = filter.avg(image)
    elif (operation == "mediana"):
        output = filter.median(image)
    
    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200

@app.route('/edge-detectention', methods=['POST'])
def edgeDetectention():
    print(request.form)
    print(request.files)

    parameter = request.form.get('parameter')
    file = request.files['file1']
    image = read_image(file)

    output = sobel.sobel(image, int(parameter))
    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200

@app.route('/sharpening', methods=['POST'])
def sharpening():
    print(request.form)
    print(request.files)

    t = request.form.get('parameter1')
    k = request.form.get('parameter2')
    file = request.files['file1']
    image = read_image(file)

    output, _ = sharpening_laplacian.sharpening_laplacian(image, int(t), float(k))
    
    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200

@app.route('/convolution', methods=['POST'])
def convolutionRoute():
    print(request.form)
    print(request.files)

    operation = request.form.get('operation')
    file = request.files['file1']
    image = read_image(file)

    output = np.empty((1, 1))

    if (operation == 'agucamento'):
        output = convolution.convolution(image, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))
    elif (operation == 'relevo'):
        output = convolution.convolution(image, np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]]))
    elif (operation == 'bordas'):
        output = convolution.convolution(image, np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]]))

    filename = save_image(output)

    @after_this_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    response_data = {
        'message': 'Arquivos recebidos e salvos com sucesso',
        'status': 200,
        'image': filename
    }

    return jsonify(response_data), 200


@app.route('/images/<filename>')
def serve_image(filename):
    image_directory = os.getcwd()
    return send_from_directory(image_directory, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
