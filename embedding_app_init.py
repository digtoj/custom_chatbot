
from data_extractor import load_urls_from_json
from embedding_manager import create_vector_with_openai, create_vector_with_huggingface, courses_file, study_course_file

#Get the saved url on the json file
courses_urls = load_urls_from_json(courses_file)

studycourses_urls = load_urls_from_json(study_course_file)

#project_urls = load_urls_from_json(project_json)

def openai_create_vect_studycourses():
    print('Start studycourses html embedding process with openai embedding')
    create_vector_with_openai(studycourses_urls)
def openai_create_vect_courses():
    print('Start project urls embedding process with openai embedding')
    create_vector_with_openai(courses_urls)
    

def hugging_create_vec_studycourses():
    print('Start studycourses html  embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(studycourses_urls)
def hugging_create_vect_courses():
    print('Start Project urls embedding process with HuggingFaceEmbedding')
    create_vector_with_huggingface(courses_urls)
