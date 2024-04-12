import logging
import time
from const import *
from embedding_app_init import *
from utils_function import add_or_update_entry_in_json

urlcate=""

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # End time
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        current_datetime = datetime.now()
        timer_report = f"on {current_datetime} : {func.__name__} took {end_time - start_time:.4f} seconds to execute." 
        print(timer_report)
        add_or_update_entry_in_json(report_json, "{current_datetime}", timer_report )
    
        return result
    return wrapper

#create Vector by using openAI embedding for urls
@timeit
def create_openai_embeddings(url_type):
        global urlcate 
        urlcate = url_type
        if url_type== study_program_text:
            openai_create_vect_studycourses()
        elif url_type==courses_planning_text:
            openai_create_vect_courses()
   

#create Vector by using HuggingFace Embedding for urls
@timeit
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
@timeit
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