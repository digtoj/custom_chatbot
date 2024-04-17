import requests
import logging
import json
import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, parse_qs

def extract_parameter_value(url, parameter_name):
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the query string and convert it into a dictionary
    query_params = parse_qs(parsed_url.query)
    
    # Retrieve the value for the specified parameter
    parameter_value = query_params.get(parameter_name, [None])[0]  # Returns None if the parameter does not exist
    return parameter_value

def save_html_to_file(html_content, file_path):
    # Write the HTML content to a file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def load_urls_from_json(file_path):
    """
    Load URLs from a JSON file.
    
    The function assumes the JSON could either be an array of URLs or an object with URLs as values.
    It reads the JSON, checks its type, and returns the URLs in a list.
    """
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    # Initialize a list to hold URLs
    urls = []
    # Check if data is a list (direct array of URLs)
    if isinstance(data, list):
        urls = data
    # Check if data is a dictionary (keys with URL values)
    elif isinstance(data, dict):
        urls = list(data.values())
    else:
        raise ValueError("JSON format not recognized. It should be either an array or dictionary of URLs.")

    return urls



def download_sitemap(url, directory, filename):
    """
    Downloads an XML sitemap file from a specified URL into a given directory with a specified filename.
    Only downloads the file if it does not already exist.
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    # Full path to where the sitemap will be saved
    file_path = os.path.join(directory, filename)
 
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Sitemap saved to {file_path}")
        return True
    else:
        print(f"Failed to download sitemap: {response.status_code}")
        return False
    

def download_pdf(url, directory):
    """
    Downloads a PDF file from a specified URL into a given directory with the original filename.
    Only downloads the file if it does not already exist.
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    # Extract the original filename from the URL
    pdf_filename = os.path.basename(url)
    # Full path to where the PDF will be saved
    file_path = os.path.join(directory, pdf_filename)
    # Check if the file already exists
    if not os.path.exists(file_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"PDF saved to {file_path}")
        else:
            print(f"Failed to download PDF: {response.status_code}")
    else:
        print(f"File already exists: {file_path}")


def save_urls_on_json(json_file_path, urls):
     if json_file_path and urls:
        # Write the list of URLs to the JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(urls, json_file)
            print(f"Sitemap URLs have been saved to {json_file_path}.")
     else: 
         print('The json_file_path or the urls are empty')

def add_url_to_json(file_path, new_url):
    """
    Adds a new URL to an existing JSON file containing an array of URLs, if it doesn't already exist.
    Creates the JSON file if it does not exist.
    
    Parameters:
    - file_path (str): The path to the JSON file.
    - new_url (str): The URL to be added.
    
    Returns:
    - bool: True if the URL was added, False otherwise.
    """
    urls = []  # Default to an empty list if the file doesn't exist or is empty

    # Try to read the existing data from the file
    try:
        with open(file_path, 'r') as file:
            urls = json.load(file)
        if not isinstance(urls, list):
            print("The file does not contain a JSON array. Starting fresh.")
            urls = []
    except FileNotFoundError:
        print("File not found. Creating a new file.")
    except json.JSONDecodeError:
        print("File is not a valid JSON. Starting fresh.")
    # Check if the URL already exists in the list
    if new_url in urls:
        return False
    # Add the new URL to the list
    urls.append(new_url)
    # Write the updated list back to the file
    with open(file_path, 'w') as file:
        json.dump(urls, file, indent=4)

    return True


def extract_urls(url):
    """Function to extract URLs from a given webpage."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extracting all anchor tags
        anchor_tags = soup.find_all('a')
        # Extracting URLs from the href attribute of anchor tags
        urls = [tag.get('href') for tag in anchor_tags if tag.get('href') is not None]
        return urls
    except Exception as e:
        return [str(e)]
    
def add_or_update_entry_in_json(file_path, key, value):
    """
    Adds or updates a key-value pair in a JSON file. The file is expected to contain a dictionary.
    If the key exists, the value is updated. If the key does not exist, the key-value pair is added.
    Creates the JSON file if it does not exist.
    
    Parameters:
    - file_path (str): The path to the JSON file.
    - key (str): The key under which the value should be stored.
    - value (str): The value to be stored.
    
    Returns:
    - bool: True if the operation was successful, False otherwise.
    """
    data = {}  # Default to an empty dictionary if the file doesn't exist or is empty

    # Try to read the existing data from the file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if not isinstance(data, dict):
            print("The file does not contain a JSON dictionary. Starting fresh.")
            data = {}
    except FileNotFoundError:
        print("File not found. Creating a new file.")
    except json.JSONDecodeError:
        print("File is not a valid JSON. Starting fresh.")

    # Add or update the key-value pair
    data[key] = value

    # Write the updated dictionary back to the file
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Key-value pair added/updated successfully.")
        return True
    except Exception as e:
        print(f"Failed to write to the file: {e}")
        return False
    


    

