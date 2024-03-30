from flask import Flask, request, jsonify
import os
import base64
from const import pdf_directory
from embedding_app_function import create_embeddings, create_pdf_embedding_by_embedding_type, list_pdf_files

app = Flask(__name__)

@app.route('/create_embeddings', methods=['POST'])
def handle_create_embeddings():
    data = request.json
    embedding_type = data.get('embedding_type')
    category = data.get('category')
    response = create_embeddings(embedding_type, category)
    return jsonify({"success": response})

@app.route('/create_pdf_embedding', methods=['POST'])
def handle_create_pdf_embedding():
    data = request.json
    embedding_type = data.get('embedding_type')
    pdf_filename = data.get('pdf_filename')
    file_directory = os.path.join(pdf_directory, pdf_filename)
    is_created = create_pdf_embedding_by_embedding_type(embedding_type, file_directory)
    return jsonify({"success": is_created})

@app.route('/list_pdf_files', methods=['GET'])
def handle_list_pdf_files():
    files = list_pdf_files(pdf_directory)
    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True)
