from data_extractor import extract_urls_from_courses
from sitemap_extractor import save_study_courses_url

#Extract the courses information from the website
extract_urls_from_courses()

#Extract and save some urls
save_study_courses_url()