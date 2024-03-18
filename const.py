import os
openai_embedding_text="OpenAI Embedding model"
alternative_embedding_text="all-MiniLM-L6-v2 model"
study_program_text="Studiengangsbeschreibung"
courses_planning_text="Vorlesungsverzeichnis"
pdf_directory="./data/documents/"


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