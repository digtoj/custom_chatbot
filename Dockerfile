FROM python-base:latest

WORKDIR /user/src/app

COPY  embedding_app.py ./
COPY website_url_extractor.py ./
COPY embedding_manager.py ./

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "embedding_app.py", "--server.port=8501", "--server.address=0.0.0.0"]