import logging
from const import *
from init import *


def list_pdf_files(directory_path):
    """
    List all PDF files in the given directory.

    Args:
    - directory_path (str): Path to the directory to search for PDF files.

    Returns:
    - List[str]: A list of filenames (including the relative path) for all PDF files in the directory.
    """
    pdf_files = [file for file in os.listdir(directory_path) if file.endswith('.pdf')]
    return pdf_files

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
   


# Function to handle embedding creation
def create_embeddings(embedding_type, category):
    success=False
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
            create_pdf_embedding_with_openai(pdf_directory=pdf_directory)
            return True
        elif embedding_type == alternative_embedding_text:
            create_pdf_embedding_with_alternative(pdf_directory=pdf_directory)
            return True
    except Exception as e:
        logging.error(e)
        return False