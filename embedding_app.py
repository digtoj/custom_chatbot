import streamlit as st
import os
from init import *

message=""
pdf_directory="./data/documents"

#create Vector by using openAI embedding for urls
def create_openai_embeddings(url_type):
    if url_type=='Kontakte':
        openai_create_vect_contact()
    elif url_type=='Glossar':
        openai_create_vect_glossar()
    elif url_type=='News':
        openai_create_vect_news()
    elif url_type=='Press':
        openai_create_vect_press()
    elif url_type=='Projekt':
        openai_create_vect_project()
    elif url_type=='Studiengangsbeschreibung':
        openai_create_vect_studycourses()
    elif url_type=='Vorlesungsverzeichnis':
        openai_create_vect_courses()

#create Vector by using HuggingFace Embedding for urls
def create_huggingface_embeddings(url_type):
    try:
        if url_type=='Kontakte':
            hugging_create_vect_contact()
        elif url_type=='Glossar':
            hugging_create_vect_glossar()
        elif url_type=='News':
            hugging_create_vec_news()
        elif url_type=='Press':
            hugging_create_vec_press()
        elif url_type=='Projekt':
            hugging_create_vec_project()
        elif url_type=='Studiengangsbeschreibung':
            hugging_create_vec_studycourses() 
        elif url_type=='Vorlesungsverzeichnis':
            hugging_create_vect_courses()
    except:
      logging.error("Error by creation of {url_type} embedding with a huggingface model")


def app():
    # Set page config at the top of your main app
    st.set_page_config(page_title="Embedding Erstellen", page_icon="⚙️")
    # Use sidebar for embedding selection and dropdown
    embedding_type = st.sidebar.radio(
        "Wählen Sie den Embedding Typ:",
        ("OpenAI Embedding", "HuggingFace Embedding")
    )
    
    category = st.sidebar.selectbox(
        "Wählen Sie die URLs Quelle:",
        ("Kontakte", "Glossar", "News", "Press", "Projekt", "Studiengangsbeschreibung", "Vorlesungsverzeichnis", "Andere Seite")
    )

    st.title('Embedding Initiator')

    # Texts
    st.text('Durch dieses App können sie die Embedding aus der Website der Hochschule Bremen erstellen.')
    st.text('Die URLs wurden aus dem Sitemap Datei: https://www.hs-bremen.de/sitemap.xml extrahiert')

    texts = [
        "- [347 URLs] Die Projekt Seite wurde aus: https://www.hs-bremen.de/sitemap.xml?sitemap=project&cHash=0690019fee9ec568818fe44c6b7403cf extrahiert.",
        "- [481 URLs] Die Vorlesungsverzeichnis der Fakultät 4 wurde aus: https://m-server.fk5.hs-bremen.de/plan/auswahl.aspx?semester=ws23&team=4 für der Wi 23/24 ",
        "- [826 URLs] Die Kontakt (Person) wurde aus: https://www.hs-bremen.de/sitemap.xml?sitemap=contact&cHash=b23784ba1f12fa172b61af58583cd671 extrahiert",
        "- [73 URLs] Die Glossar URL https://www.hs-bremen.de/sitemap.xml?sitemap=glossar&cHash=821bc4bce499c109a85c2ec020ab3640 extrahiert.",
        "- [76 URLs] Die News (Nachrichten) wurde aus URL: https://www.hs-bremen.de/sitemap.xml?sitemap=news&cHash=680af44b739a7f0d0708e02b344c9d30 extrahiert.",
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
        if embedding_type == 'OpenAI Embedding':
            create_openai_embeddings (category)
            message=st.text('Das Embedding für {category} wurde erfolgreich erstellt.')
        elif embedding_type == 'HuggingFace Embedding':
            try:
                create_huggingface_embeddings(category)
                message=st.text('Das Embedding für {category} wurde erfolgreich erstellt.')
            except:
                logging("Error by Hugginface embedding process.")
    
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
