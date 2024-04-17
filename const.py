import os
from utils_function import load_urls_from_json


report_json = './data/report.json'

data_origin = "'- [108 HTML Seiten aus dem ]  : [Vorlesungverzeichniss (Semesterverbände) Sommersemester 24 Fakultät 4](https://m-server.fk5.hs-bremen.de/plan/auswahl.aspx?semester=ss24&team=4)'"




#site map information
hs_website = "https://www.hs-bremen.de/"

study_course='studycourses'
study_course_file="./data/studycourses.json"


course_catalog='course_catalog'
courses_file='./data/courses.json'

url_course_faculty4 = load_urls_from_json(courses_file)

#pdf documents information
pdf_docs_url = './data/documents_url.json'
pdf_directory="./data/documents/"

#Model tools information
openai_embedding_text="OpenAI Embedding model"
alternative_embedding_text="bge-m3"
model_name = "./model/bge-m3"

#Some value 
study_program_text="Studiengangsbeschreibung"
courses_planning_text="Vorlesungsverzeichnis"

#File type
doc_type_html = 'html'
doc_type_url = 'url'

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