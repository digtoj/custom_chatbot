import streamlit as st
import requests
import os
import base64
from const import *
from embedding_app_function import *

st.set_page_config(layout="wide", page_title="Embedding Erstellen", page_icon="⚙️")

message=""

def  displayPDF(file):
     # Opening the file from path
     with open(file, "rb") as f:
          base64_pdf = base64.b64encode(f.read()).decode('utf-8')
     
     pdf_display = F'<iframe scr="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'

     st.markdown(pdf_display, unsafe_allow_html=True)




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
        ("--",study_program_text, courses_planning_text)
    )

    
    #Main page 
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

     # Upload PDF file
    uploaded_file = st.file_uploader("PDF Datei Hochladen", type="pdf")

    if st.sidebar.button(f'Erstellen {embedding_type} Embedding für {category} URLs'):
        if embedding_type and category!="--":
            # Use the environment variable for the Flask backend endpoint
            response = create_embeddings(embedding_type, category)
            if response == True:
                st.success("Embedding erfolgreich erstellt.")
            else:
                st.error("Fehler beim Erstellen des Embeddings.")
        else:
            st.error("Bitte wählen sie eine Kategorie von URL aus.") 

        
      # SelectBox for uploaded PDFs, now reflecting the updated list
    selected_pdf = st.sidebar.selectbox("Wählen Sie ein PDF zur Erstellung des Embeddings:", pdf_files)

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
        st.markdown("<h2 style='text-align:center; color: grey;'> PDF Preview </h2>", unsafe_allow_html=True)
        displayPDF(os.path.join(pdf_directory, uploaded_file.name))
             
    
  

        
if __name__ == '__main__':
    app()
