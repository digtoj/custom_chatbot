from flask import Flask, request, jsonify
import logging
from const import *
from init import *

app = Flask(__name__)


#create Vector by using openAI embedding for urls
def create_openai_embeddings(url_type):
        if url_type== study_program_text:
            openai_create_vect_studycourses()
        elif url_type==courses_planning_text:
            openai_create_vect_courses()
   

#create Vector by using HuggingFace Embedding for urls
def create_huggingface_embeddings(url_type):
        if url_type==study_program_text:
            hugging_create_vec_studycourses() 
        elif url_type==courses_planning_text:
            hugging_create_vect_courses()
   


# Function to handle embedding creation (logic from your Streamlit app)
def create_embeddings(embedding_type, category):
    success=False
    try:
        if(embedding_type == openai_embedding_text):
            create_openai_embeddings(category)
            success = True
        elif embedding_type == alternative_embedding_text:
            create_huggingface_embeddings(category)
            success = True
    except Exception as e:
     logging.error('Error by creating embedding for '+embedding_type+' and '+category)
     logging.error(e)
     return success  # Return True if successful, False otherwise

@app.route('/create_embeddings', methods=['POST'])
def handle_create_embeddings():
    data = request.get_json()
    embedding_type = data.get('embedding_type')
    category = data.get('category')

    success = create_embeddings(embedding_type, category)
    if success:
        return jsonify({"message": "Embedding successfully created"}), 200
    else:
        return jsonify({"error": "Error creating embedding"}), 500

if __name__ == '__main__':
    app.run(debug=True)