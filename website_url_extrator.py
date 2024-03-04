import requests
import logging
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

json_file_path = './data/'


sitemaps_dir = './data/sitemaps/'

site_map_files =['contact.xml', 'glossar.xml', 'news.xml', 'press.xml', 'project.xml', 'studycourses.xml']

prefix_course_plan = 'https://m-server.fk5.hs-bremen.de/plan/'

url_course_faculty4 = 'https://m-server.fk5.hs-bremen.de/plan/auswahl.aspx?semester=ws23&team=4'

# Define a global variable
global_extracted_urls = []


def extract_urls(url):
    """Function to extract URLs from a given webpage."""
    global global_extracted_urls  # Indicate that we are using the global variable
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting all anchor tags
        anchor_tags = soup.find_all('a')
         # Clear previous URLs from the global list
        global_extracted_urls.clear()

        # Extracting URLs from the href attribute of anchor tags
        urls = [tag.get('href') for tag in anchor_tags if tag.get('href') is not None]
        
        return urls
    except Exception as e:
        return [str(e)]

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

    faculty4 = get_all_course_from_faculty(url_course_faculty4)
    if faculty4:
        json_url = './data/courses.json'
        save_urls_on_json(json_url, faculty4)


# Replace 'your_sitemap_path.xml' with the path to your sitemap file
def save_urls_on_json(json_file_path, urls):
     if json_file_path and urls:
        # Write the list of URLs to the JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(urls, json_file)
            print(f"Sitemap URLs have been saved to {json_file_path}.")
     else: 
         print('The json_file_path or the urls are empty')

def load_urls_from_json(json_file_path):
    # Read the JSON file and return the list of URLs
    if json_file_path:
        with open(json_file_path, 'r') as json_file:
            urls = json.load(json_file)
    else:
        logging.error('The file dont exist')
    return urls


#extract_urls_from_sitemap()