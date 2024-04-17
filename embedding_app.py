import streamlit as st
import os
import base64
from const import *

from embedding_app_function import list_pdf_files, load_urls_from_json
from embedding_app_function import create_embeddings, create_pdf_embedding_by_embedding_type, list_pdf_files

st.set_page_config(layout="wide", page_title="Embedding Erstellen", page_icon="⚙️")

message=""



# Function to read and display the selected PDF file
def read_pdf_file(pdf_path):
    with open(os.path.join(pdf_directory, pdf_path), "rb") as f:
        pdf_bytes = f.read()
    st.write(pdf_bytes)

def app():
    pdf_files = list_pdf_files(pdf_directory)
    #Sidebar
    # Set page config at the top of your main app
    # Use sidebar for embedding selection and dropdown
    embedding_type = st.sidebar.radio(
        "Wählen Sie den Embedding Typ:",
        (openai_embedding_text, alternative_embedding_text)
    )
    
    category = st.sidebar.selectbox(
        "Wählen Sie die URLs Quelle:",
        ("--",study_program_text)
    )

    #URL:
    urls_value=[]
    for url in url_course_faculty4:
        urls_value.append("["+url+"]("+url+")")
        
    
    #Main page 
    st.title('Embedding Manager')

    # Texts
    st.text('Durch dieses App können sie die Embedding aus der Website der Hochschule Bremen erstellen.')
    
    texts = [
        "",
    ]



    texts.extend(pdf_files)
    # Display each text in the list
    text_to_display = "\n".join(texts)
    

    # Placeholder for loading symbol and messages
    placeholder = st.empty()

     # Upload PDF file
    uploaded_file = st.file_uploader("PDF Datei Hochladen", type="pdf")

    if st.sidebar.button(f'Erstellen {embedding_type} Embedding für {category} URLs'):
        if embedding_type and category!="--":
            # Use the environment variable for the Flask backend endpoint
            with st.spinner("Embeddings wird erstellt....."):
                response = create_embeddings(embedding_type, category)
            if response == True:
                st.success("Embedding erfolgreich erstellt.")
            else:
                st.error("Fehler beim Erstellen des Embeddings.")
        else:
            st.error("Bitte wählen sie eine Kategorie von URL aus.") 

        
      # SelectBox for uploaded PDFs, now reflecting the updated list
    selected_pdf = st.sidebar.selectbox("Wählen Sie ein PDF zur Erstellung des Embeddings:", pdf_files)

    if st.button("PDF Öffnen"):
         read_pdf_file(selected_pdf)

    if st.sidebar.button(f'Erstellen {embedding_type} Embedding des pdf'):
                file_directory = os.path.join(pdf_directory, selected_pdf)
                if file_directory:
                    isCreated=False
                    try:
                        with st.spinner("Embeddings wird erstellt....."):
                         isCreated = create_pdf_embedding_by_embedding_type(embedding_type, file_directory)
                    except Exception as e:
                        st.error(e)
                    if isCreated == True:
                        st.success("Embedding mit "+ embedding_type+" von "+selected_pdf+" wurde erfolgreich erstellt.")       
                    else:
                        st.error("Fehler bei der Erstellung des Embeddings")
                else:
                    st.error("Error by file directory path")     

    st.sidebar.write("Datenquellen:") 

    for url in urls_value:
        st.sidebar.write(url)
    

    if uploaded_file is not None:
        # Save PDF file to data/documents folder
        os.makedirs(pdf_directory, exist_ok=True)
        
        with open(os.path.join(pdf_directory, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Datei '{uploaded_file.name}' erfolgreich hochgeladen.")
        # Update the list of PDF files after uploading
        pdf_files.append(uploaded_file.name)
        pdf_files = sorted(set(pdf_files))  # Ensure the list is unique and sorted
        files_details = {
             "name": uploaded_file.name,
             "type": uploaded_file.type,
             "size": uploaded_file.size
        }
      
        st.markdown("<h2 style='text-align:center; color: grey;'>PDF Details </h2>", unsafe_allow_html=True)
        st.write(files_details)
    

if __name__ == '__main__':
    app()
