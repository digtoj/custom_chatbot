import requests
import logging
import json
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from utils_function import *
from const import sitemap_url, pdf_docs_url, sitemaps_dir


json_file_path = './data/'

site_map_files =['contact.xml', 'glossar.xml', 'news.xml', 'press.xml', 'project.xml', 'studycourses.xml']
prefix_course_plan = 'https://m-server.fk5.hs-bremen.de/plan/'
url_course_faculty4 = 'https://m-server.fk5.hs-bremen.de/plan/auswahl.aspx?semester=ss24&team=4'

# Define a global variable
global_extracted_urls = []


def get_all_course_from_faculty(url):
    complete_urls=[]
    if url:
        extracted_urls = extract_urls(url)
        if extracted_urls:
            logging.info('Extracted URLs:')
            for extracted_url in extracted_urls:
                # Use a different variable name here to avoid confusion
                full_url = urljoin(prefix_course_plan, extracted_url)
                complete_urls.append(full_url)
        else:
            logging.error('No URLs found or an error occurred.')
    else:
        logging.error('Please enter a URL.')
    
    return complete_urls

def extract_urls_from_sitemap():
    logging.info('Starting url extraction from sitemap.xml')
    for value in site_map_files:
        file_path=sitemaps_dir+''+value
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Adjust for namespace
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        # Extract sitemap URLs
        sitemap_urls = [loc.text for loc in root.findall('.//ns:loc', namespaces)]
        name = value.split('.')[0]
        json_url = json_file_path+name+'.json'
        save_urls_on_json(json_url, sitemap_urls)


def extract_urls_from_courses():
    faculty4 = get_all_course_from_faculty(url_course_faculty4)
    if faculty4:
        json_url = './data/courses.json'
        for value in faculty4:
            add_url_to_json(json_url, value)
