#This script is created to init, create and save the vector from the embedding model.
from langchain_community.document_loaders import WebBaseLoader, UnstructuredHTMLLoader

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from datetime import datetime
from const import *
from utils_function import add_or_update_entry_in_json

import logging
import time
import json
import logging
import os


load_dotenv()



#Vector database directory
openai_vectordb_directory = './openai_db'
alternative_vectordb_directory = './alternative_db'

#Embeddings Model
openai_embeddings = OpenAIEmbeddings()

model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
alternative_Embeddings = HuggingFaceEmbeddings(
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
        valuetime = f"on {current_datetime}"
        print(timer_report)
        add_or_update_entry_in_json(report_json, valuetime, timer_report )
    
        return result
    return wrapper

def get_data_from_url(url):
    try:
         # get the text in document form
        logging.info('Starting embedding creation for '+url)
        loader = WebBaseLoader(url)
        document = loader.load()
        # split the document into chunks
        text_splitter = RecursiveCharacterTextSplitter()

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
                print('Start for '+url)
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
            logging.info('Start Alternative Embedding for the page:'+url)
            print('Start for '+url)
            document_chunks = get_data_from_url(url)
            # create a vectorstore from the chunks
            vector_store = Chroma.from_documents(document_chunks, alternative_Embeddings, persist_directory=alternative_vectordb_directory)
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

def get_choised_vector(embedding_type):
    if embedding_type:
        if embedding_type==prototypA:
            return get_openai_embeddings()
        elif embedding_type==prototypB:
            return get_alternative_embeddings()
    else:
        logging.error("Give a existing value for the embedding typ.")
 
#Get openai saved embedding
def get_openai_embeddings():
    logging.info('Start get Openai embeddings vector.')
    if openai_vectordb_directory:
     return get_vector_from_directory(openai_vectordb_directory, openai_embeddings )
    else:
      logging.error('The embedding database for openai dont exist.')
      return None

def get_alternative_embeddings():
    logging.info('Start get Huggingface embeddings vector.')
    if alternative_vectordb_directory:
       return get_vector_from_directory(alternative_vectordb_directory, alternative_Embeddings)
    else:
       logging.error('The embedding database for huggingface dont exist.')
       return None



#To create embedding from pdf file
@timeit
def create_embedding_from_pdf_file(pdf_directory, embeddings, persist_directory): 
    
        if os.path.exists(pdf_directory):
            print('Start embedding for '+ pdf_directory)
            loader = PyPDFLoader(pdf_directory)

            data = loader.load()
             # Split  data up into smaller documents with Chunks
            text_splitter = CharacterTextSplitter(
                    separator="\n",
                    chunk_size=1500, 
                    chunk_overlap=200,
                    length_function=len
                )

            chunks = text_splitter.split_documents(data)

            vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=persist_directory)
            vectordb.persist()
        else:
            print("The Given path dont exist.")
  

def create_pdf_embedding_with_openai(pdf_directory): 
        if pdf_directory:
            print("start "+openai_embedding_text+"embedding for "+ pdf_directory)
            create_embedding_from_pdf_file(pdf_directory, openai_embeddings, openai_vectordb_directory)
        else:
            logging.error(pdf_directory+"is not correct")

def create_pdf_embedding_with_alternative(pdf_directory):
        if pdf_directory:
            print("start "+ alternative_embedding_text+" for "+ pdf_directory)
            create_embedding_from_pdf_file(pdf_directory, alternative_Embeddings, alternative_vectordb_directory)
        else:
            logging.error(pdf_directory+"is not correct")