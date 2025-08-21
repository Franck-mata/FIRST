# app.py
from flask import Flask, render_template, request, jsonify
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_document():
    file = request.files['document']
    img = Image.open(file.stream)
    text = pytesseract.image_to_string(img)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)