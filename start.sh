#!/bin/bash
streamlit run embedding_app.py --server.port 8501
streamlit run openai_based_chat.py --server.port 8502
streamlit run huggingface_based_chat.py --server.port 8503
streamlit run main_app.py --server.port 80
