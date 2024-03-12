#The App where the user should be able to start the embedding app, the openai chatbot and the alternative version.
import streamlit as st

# Set page config at the top of your main app
st.set_page_config(page_title="Chat Mit der Hochschule Bremen", page_icon="💬")

from openai_based_chat import app as openai_chat
from huggingface_based_chat import app as alternative_chat


st.title("Chat Mit Eigenen Daten")

st.text("Starten sie eine von die 2 Chatbot Anwendungen.")

col1, col2, col3 = st.columns(2, gap="big") 

with col2:
    if st.button("Chatbot A: Openai basierte Model", key="2"):
        openai_chat()

with col3:
    if st.button("Chatbot B: Open source basierte Model", key="3"):
        alternative_chat()
