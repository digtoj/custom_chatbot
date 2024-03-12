
#The App where the user should be able to start the openai chatbot and the alternative version.
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Set page config
st.set_page_config(page_title="Hauptseite", page_icon="📁")

# Main title for the page
st.title("Hauptanwendung")

# HTML template for the button that opens a link in a new tab
button_template = """
<a href="{url}" target="_blank">
    <button style="background-color: #4CAF50; border: none; color: white; padding: 10px 24px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">
        {button_text}
    </button>
</a>
"""

# OpenAI Chat App Button
openai_chat_app_url = "https://your_openai_chat_app_url.com" 
openai_chat_button_html = button_template.format(url=openai_chat_app_url, button_text="Openai-basierte Chatbot")
st.markdown(openai_chat_button_html, unsafe_allow_html=True)

# Open source App Button
open_source_chat_app_url = "https://your_embedding_app_url.com" 
open_source_button_html = button_template.format(url=open_source_chat_app_url, button_text="Open-Source-basierte Chatbot")
st.markdown(open_source_button_html, unsafe_allow_html=True)

