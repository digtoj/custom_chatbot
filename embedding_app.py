import streamlit as st
import requests
import os
from const import *
from embedding_function import *

message=""
pdf_directory="./data/documents/"

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

# Function to handle embedding creation (logic from your Streamlit app)
def create_embeddings(embedding_type, category):
    success=False
    try:
        if(embedding_type == openai_embedding_text):
            create_openai_embeddings(category)
            success = True
        elif embedding_type == alternative_embedding_text:
            create_huggingface_embeddings(category)
            success = True
    except Exception as e:
     logging.error('Error by creating embedding for '+embedding_type+' and '+category)
     logging.error(e)
     return success  # Return True if successful, False otherwise


def app():
    # Set page config at the top of your main app
    st.set_page_config(page_title="Embedding Erstellen", page_icon="⚙️")
    # Use sidebar for embedding selection and dropdown
    embedding_type = st.sidebar.radio(
        "Wählen Sie den Embedding Typ:",
        (openai_embedding_text, alternative_embedding_text)
    )
    
    category = st.sidebar.selectbox(
        "Wählen Sie die URLs Quelle:",
        (study_program_text, courses_planning_text)
    )

    st.title('Embedding Manager')

    # Texts
    st.text('Durch dieses App können sie die Embedding aus der Website der Hochschule Bremen erstellen.')
    st.text('Die URLs wurden aus dem Sitemap Datei: https://www.hs-bremen.de/sitemap.xml extrahiert')

    texts = [
        "- [481 URLs] Die Vorlesungsverzeichnis der Fakultät 4 wurde aus: https://m-server.fk5.hs-bremen.de/plan/auswahl.aspx?semester=ws23&team=4 für der Wi 23/24 ",
        "- [76 URLs] Die Studiengänge wurde aus: https://www.hs-bremen.de/sitemap.xml?sitemap=studycourses&cHash=fd9afa2bc1b3673281c5cdc14ee21f1e extrahiert.",
    ]

    # Display each text in the list
    text_to_display = "\n".join(texts)
    
    # Display the text area with a scrollbar
    st.text_area("Datenquellen: ", text_to_display, height=200, disabled=True)

    # Placeholder for loading symbol and messages
    placeholder = st.empty()

     # 
    if st.button(f'Erstellen {embedding_type} für {category} URLs'):
        # Use the environment variable for the Flask backend endpoint
        response = create_embeddings(embedding_type, category)
        if response:
            st.success("Embedding erfolgreich erstellt.")
        else:
            st.error("Fehler beim Erstellen des Embeddings.")
           
           
    
     # Upload PDF file
    uploaded_file = st.file_uploader("PDF Datei Hochladen", type="pdf")

    if uploaded_file is not None:
        # Save PDF file to data/documents folder
        os.makedirs(pdf_directory, exist_ok=True)
        with open(os.path.join(pdf_directory, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Datei '{uploaded_file.name}' erfolgreich hochgeladen.")
    message=st.text("")

if __name__ == '__main__':
    app()
