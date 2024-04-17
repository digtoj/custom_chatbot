import requests
import os
import re
import xml.etree.ElementTree as ET
from utils_function import *
from const import  *



json_file_path = './data/'

prefix_course_plan = 'https://m-server.fk5.hs-bremen.de/plan/'

url_course_faculty4 = 'https://m-server.fk5.hs-bremen.de/plan/auswahl.aspx?semester=ss24&team=4'



def extract_courses_plan_html():
   try:
        cookie_name = "plan"
        cookie_value = "zeiten=True&bemerkungen=True&langnamen=True"
        
        new_html_content = get_html_with_cookie(url_course_faculty4, cookie_name, cookie_value)
        save_html_to_file(new_html_content, './data/courses/value.html')
        extracted_urls = extract_urls_from_html('./data/courses/value.html')
        for url in extracted_urls:
            newurl = prefix_course_plan+url
            add_url_to_json(study_course_file, newurl)
   except Exception as e:
       print(e)


def extract_urls_from_html(file_path):
    # Reading the HTML file content
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    urls = re.findall(r'<div id="Panel_verbaende_.*?">(.*?)</div>', html_content, re.DOTALL)
    if urls:
        all_urls = []
        for section in urls:
            found_urls = re.findall(r'href="(.*?)"', section)
            # Cleaning up the URLs by replacing '&amp;' with '&'
            cleaned_urls = [url.replace('&amp;', '&') for url in found_urls]
            all_urls.extend(cleaned_urls)
        return all_urls
    else:
        return []

def get_html_with_cookie(url, cookie_name, cookie_value):
    session = requests.Session()
    session.cookies.set(cookie_name, cookie_value)
    response = session.get(url)
    
   
    if response.status_code == 200:
        return response.text  
    else:
        return f"Failed to retrieve page: {response.status_code}"


def read_html_files_in_directory(directory_path):
    html_contents = []

    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} does not exist.")
        return html_contents

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if filename.endswith('.html'):
            # Read the HTML file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                html_contents.append(content)

    return html_contents





