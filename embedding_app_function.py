import logging
import time
from const import *
from embedding_app_init import *
from utils_function import add_or_update_entry_in_json
from embedding_manager import create_pdf_embedding_with_openai, create_pdf_embedding_with_alternative


#create Vector by using openAI embedding for urls

def create_openai_embeddings(url_type):
        add_or_update_entry_in_json(report_json, openai_embedding_text, url_type )
        if url_type== study_program_text:
            openai_create_vect_courses()
        elif url_type==courses_planning_text:
            openai_create_vect_studycourses()
   

#create Vector by using HuggingFace Embedding for urls

def create_huggingface_embeddings(url_type):
        add_or_update_entry_in_json(report_json, alternative_embedding_text, url_type )
        if url_type==study_program_text:
            hugging_create_vect_courses()
        elif url_type==courses_planning_text:
            hugging_create_vec_studycourses() 
   


# Function to handle embedding creation
def create_embeddings(embedding_type, category):
    try:
        if(embedding_type == openai_embedding_text):
            create_openai_embeddings(category)
            return  True
        elif embedding_type == alternative_embedding_text:
            create_huggingface_embeddings(category)
            return  True
    except Exception as e:
     logging.error('Error by creating embedding for '+embedding_type+' and '+category)
     logging.error(e)
     return False  # Return True if successful, False otherwise

#Function to handle embedding creation for a pdf file
def create_pdf_embedding_by_embedding_type(embedding_type, pdf_directory):
    try: 
        if embedding_type == openai_embedding_text:
            add_or_update_entry_in_json(report_json, embedding_type, pdf_directory )

            create_pdf_embedding_with_openai(pdf_directory=pdf_directory)
            return True
        elif embedding_type == alternative_embedding_text:
            add_or_update_entry_in_json(report_json, embedding_type, pdf_directory )

            create_pdf_embedding_with_alternative(pdf_directory=pdf_directory)
            return True
    except Exception as e:
        logging.error(e)
        return False