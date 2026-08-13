import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict_disease

app = Flask(__name__)
CORS(app)  # Cross-Origin requests allow karne ke liye

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "AI Service Running Successfully!"})

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    file_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(file_path)

    result = predict_disease(file_path)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)