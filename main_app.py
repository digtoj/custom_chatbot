#The App where the user should be able to start the embedding app, the openai chatbot and the alternative version.
import streamlit as st

from init_app import app as embedding_app
from openai_based_chat import app as openai_chat
from huggingface_based_chat import app as alternative_chat


st.title("Chat Mit Eigenen Daten")

col1, col2, col3 = st.columns(3, gap="small") 

st.text("Starten sie eine von die 3 Anwendungen")

with col1:
    if st.button("Für die Erstellung von Embedding", key="1"):
        embedding_app()

with col2:
    if st.button("Chatbot A: Openai basierte Model", key="2"):
        openai_chat()

with col3:
    if st.button("Chatbot B: Open source basierte Model", key="3"):
        alternative_chat()
