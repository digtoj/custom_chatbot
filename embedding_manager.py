#This script is created to init, create and save the vector from the embedding model.
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from datetime import datetime
import logging
import time
import json
import logging


load_dotenv()

#Report
report_json = './data/report.json'

#Vector database directory
openai_vectordb_directory = './openai_db'
alternative_vectordb_directory = './data/alternative_db'

#Embeddings Model
openai_embeddings = OpenAIEmbeddings()
model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
huggingFaceEmbeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # End time
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        current_datetime = datetime.now()
        timer_report = f"on {current_datetime} : {func.__name__} took {end_time - start_time:.4f} seconds to execute." 
        
        with open(report_json, 'w') as json_file:
            json.dump(timer_report, json_file)
            print(f"Sitemap URLs have been saved to {report_json}.")
        return result
    return wrapper

#Function to save vector from a url.
def get_data_from_url(url):
    try:
         # get the text in document form
        logging.info('Starting embedding creation for '+url)
        loader = WebBaseLoader(url)
        document = loader.load()
        # split the document into chunks
        text_splitter = RecursiveCharacterTextSplitter()
        logging.info(document)
        document_chunks = text_splitter.split_documents(document)
    except:
        logging.error("Error by getting data on the url : "+url)
    
    return document_chunks

#Create and save the vector by using openai embedding
@timeit
def create_vector_with_openai(urls):
    try:
        if urls:
            for url in urls:
                logging.info('Start Openai Embedding for the page:'+url)
                document_chunks = get_data_from_url(url)
                 # create a vectorstore from the chunks
                vector_store = Chroma.from_documents(document_chunks, openai_embeddings, persist_directory=openai_vectordb_directory)
                vector_store.persist()
                logging.info('Successful creation of  Openai Embedding for the page:'+url)
    except:
       logging.exception('Error by creation vector for '+openai_vectordb_directory)
    return None

#Create and save the vector by using HuggingfaceEmbedding
@timeit
def create_vector_with_huggingface(urls):
    try:
      if urls:
         for url in urls:
            logging.info('Start Sentence Embedding for the page:'+url)
            document_chunks = get_data_from_url(url)
            # create a vectorstore from the chunks
            vector_store = Chroma.from_documents(document_chunks, huggingFaceEmbeddings, persist_directory=alternative_vectordb_directory)
            vector_store.persist()
            logging.info('Successful creation of  Huggingsface Embedding for the page:'+url)
    except Exception as e:
      logging.exception('Error by creation vector for '+ str(e))
    return None

#Get saved embedding from disk
def get_vector_from_directory(persist_directory, embeddings):
    if persist_directory:
        logging.info('Get Vector from : '+ persist_directory)
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    vector_store.get()
    return vector_store
 
#Get openai saved embedding
def get_openai_embeddings():
    logging.info('Start get Openai embeddings vector.')
    if openai_vectordb_directory:
     return get_vector_from_directory(openai_vectordb_directory, openai_embeddings )
    else:
      logging.error('The embedding database for openai dont exist.')
      return None

def get_huggingFace_embeddings():
    logging.info('Start get Huggingface embeddings vector.')
    if alternative_vectordb_directory:
       return get_vector_from_directory(alternative_vectordb_directory, huggingFaceEmbeddings)
    else:
       logging.error('The embedding database for huggingface dont exist.')
       return None



