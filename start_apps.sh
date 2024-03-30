#!/bin/bash

#Start the Flask app in the background
flask run &
streamlit run embedding_app.py --server.port=8501 &
streamlit run chat_app.py --server.port=8502