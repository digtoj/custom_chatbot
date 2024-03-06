# app/Dockerfile

# Base image
FROM python:3.9-slim

WORKDIR /custom_chat

COPY requirements.txt /custom_chat/requirements.txt

# Install dependencies conditionally
RUN if [ "$(uname -s)" = "Linux" ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    else \
        pip install --no-cache-dir -r requirements.txt; \
    fi


EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "init_app.py", "--server.port=8501", "--server.address=0.0.0.0"]