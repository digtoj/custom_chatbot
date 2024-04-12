from utils_function import download_sitemap, save_urls_on_json, add_url_to_json
from const import *

import xml.etree.ElementTree as ET


def extract_urls_from_sitemap(file_path):
    # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        # Adjust for namespace
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        # Extract sitemap URLs
        sitemap_urls = [loc.text for loc in root.findall('.//ns:loc', namespaces)]
        return sitemap_urls


def save_urls_from_sitemap_by_category(category, category_json_file):
     isSiteMapsCreated = download_sitemap(sitemap_url, sitemaps_dir, sitemap_name_file)
     url = ""
     if isSiteMapsCreated:
        sitemapurls = extract_urls_from_sitemap(sitemap_file_dir)
        for value in sitemapurls:
            if category in value:
                    url=value
                    break
        if url:
            if download_sitemap(url, sitemaps_dir, category+'.xml') and category_json_file:
                category_urls = extract_urls_from_sitemap(sitemaps_dir+category+'.xml')
                for item in category_urls:
                    add_url_to_json(category_json_file, item)

def save_study_courses_url():
    save_urls_from_sitemap_by_category(study_course, study_course_file)           
             


           


