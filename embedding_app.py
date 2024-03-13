import streamlit as st
import requests
import os
from const import *
from embedding_app_function import *

message=""
pdf_directory="./data/documents/"

pdf_files = list_pdf_files(pdf_directory)


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

    texts.extend(pdf_files)
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
        if response == True:
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
    
        if st.button(f'Erstellen das {embedding_type} Embedding des Pdf'):
            file_directory = os.path.join(pdf_directory, uploaded_file.name)
            if file_directory:
                isCreated=False
                try:
                    isCreated = create_pdf_embedding_by_embedding_type(embedding_type, file_directory)
                except Exception as e:
                    st.error(e)
                if isCreated == True:
                    st.success("Embedding mit "+ embedding_type+" von "+ uploaded_file.name+" wurde erfolgreich erstellt.")       
                else:
                    st.error("Fehler bei der Erstellung des Embeddings")
            else:
                st.error("Error by file directory path")


if __name__ == '__main__':
    app()
