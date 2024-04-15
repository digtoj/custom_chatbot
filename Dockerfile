FROM python-chatbot:latest

WORKDIR /user/src/app

COPY *.py ./
COPY .env ./
COPY ./data ./data
COPY start_apps.sh ./

EXPOSE 5000
EXPOSE 8501
EXPOSE 8502

RUN mkdir model

CMD ["sh", "start_apps.sh"]