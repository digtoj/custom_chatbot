
from data_extractor import *
from embedding_manager import *
from sitemap_extractor import save_study_courses_url
from const import study_course_file

#Extract the courses information from the website
extract_urls_from_courses()

#Extract and save some urls
save_study_courses_url()





#Get the saved url on the json file
courses_urls = load_urls_from_json(courses_json)

studycourses_urls = load_urls_from_json(study_course_file)
project_urls = load_urls_from_json(project_json)




def openai_create_vect_courses():
    print('Start courses urls embedding process with openai embedding')
    create_vector_with_openai(courses_urls)
def openai_create_vect_contact():
    print('Start contact urls embedding process with openai embedding')
    create_vector_with_openai(contact_urls)
def openai_create_vect_glossar():
    print('Start glossar urls embedding process with openai embedding')
    create_vector_with_openai(glossar_urls)
def openai_create_vect_news():
    print('Start news urls embedding process with openai embedding')
    create_vector_with_openai(news_urls)
def openai_create_vect_press():
    print('Start press urls embedding process with openai embedding')
    create_vector_with_openai(press_urls)
def openai_create_vect_studycourses():
    print('Start studycourses urls embedding process with openai embedding')
    create_vector_with_openai(studycourses_urls)
def openai_create_vect_project():
    print('Start project urls embedding process with openai embedding')
    create_vector_with_openai(project_urls)
    

def hugging_create_vect_courses():
    print('Start courses urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(courses_urls)
def hugging_create_vect_contact():
    print('Start contact urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(contact_urls)
def hugging_create_vect_glossar():
    print('Start glossar urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(glossar_urls)
def  hugging_create_vec_news():
    print('Start news urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(news_urls)
def  hugging_create_vec_press():
    print('Start press urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(press_urls)
def hugging_create_vec_studycourses():
    print('Start studycourses urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(studycourses_urls)
def hugging_create_vec_project():
    print('Start Project urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(project_urls)
