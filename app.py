from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decode_image
from cnnClassifier.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = PredictionPipeline(self.filename)

    @app.route('/', methods=['GET'])
    @cross_origin()
    def home():
        return render_template('index.html')

    @app.route('/train', methods=['GET', 'POST'])
    @cross_origin()
    def train_route():
        os.system('dvc repro')
        return 'Training done successfully!'

    @app.route('/predict', methods=['POST'])
    @cross_origin()
    def predict_route(self):
        image = request.json['image']
        decode_image(image, self.filename)
        result = self.classifier.predict()
        return jsonify(result)

if __name__ == '__main__':
    c1App = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True)

