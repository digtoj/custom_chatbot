# app/Dockerfile

FROM python:3.9-slim

WORKDIR /custom_chat

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/digtoj/custom_chatbot.git .

RUN pip3 install -r requirements.txt

EXPOSE 8503

HEALTHCHECK CMD curl --fail http://localhost:8503/_stcore/health

ENTRYPOINT ["streamlit", "run", "huggingface_based_chat.py", "--server.port=8503", "--server.address=0.0.0.0"]