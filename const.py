import os

#site map information
sitemap_name_file='sitemap.xml'
sitemaps_dir = './data/sitemaps/'
sitemap_file_dir = sitemaps_dir+sitemap_name_file
sitemap_url='https://www.hs-bremen.de/sitemap.xml'

study_course='studycourses'
study_course_file="./data/studycourses.json"

course_catalog='course_catalog'
courses_file='./data/courses.json'

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