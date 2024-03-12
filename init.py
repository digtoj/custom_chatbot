
from website_url_extractor import load_urls_from_json
from embedding_manager import *


courses_json = './data/courses.json'
contact_json = './data/contact.json'
glossar_json = './data/glossar.json'
news_json = './data/news.json'
press_json = './data/press.json'
project_json = './data/project.json'
studycourses_json = './data/studycourses.json'


#Get the saved url on the json file
courses_urls = load_urls_from_json(courses_json)
contact_urls = load_urls_from_json(contact_json)
glossar_urls = load_urls_from_json(glossar_json)
news_urls = load_urls_from_json(news_json)
press_urls = load_urls_from_json(press_json)
studycourses_urls = load_urls_from_json(studycourses_json)
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
