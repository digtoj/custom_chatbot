
from data_extractor import *
from embedding_manager import *

#Get the saved url on the json file
courses_urls = load_urls_from_json(courses_file)

studycourses_htmls = read_html_files_in_directory('./data/courses/')
#project_urls = load_urls_from_json(project_json)

def openai_create_vect_studycourses():
    print('Start studycourses html embedding process with openai embedding')
    create_vector_with_openai(studycourses_htmls, doc_type_html)
def openai_create_vect_courses():
    print('Start project urls embedding process with openai embedding')
    create_vector_with_openai(courses_urls, doc_type_url)
    

def hugging_create_vec_studycourses():
    print('Start studycourses html  embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(studycourses_htmls, doc_type_html)
def hugging_create_vect_courses():
    print('Start Project urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(courses_urls, doc_type_url)
