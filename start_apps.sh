#!/bin/bash

#Start app
python init_data_extraction.py &
streamlit run embedding_app.py --server.port=8501 &
streamlit run chat_app.py --server.port=8502