from embedding_manager import *
from flask import Flask, jsonify
from const import openai_embedding_text

app = Flask(__name__)

@app.route('/get-vector')
def get_vector():
    vector_store = get_choised_vector(openai_embedding_text)
    if vector_store:
        # Assuming the vector_store object has a method to convert the vector to a dictionary or similar serializable format
        return jsonify(vector_store.to_dict())
    else:
        return jsonify({"error": "Failed to retrieve vector"}), 404

if __name__ == '__main__':
    app.run(debug=True)