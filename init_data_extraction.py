from data_extractor import extract_courses_plan_html, get_and_save_faculty4_courses
from sitemap_extractor import save_study_courses_url

#Get and save the url of all study courses for faculty 4.
get_and_save_faculty4_courses()

#Download some html content from the plan of course.
extract_courses_plan_html()

#Extract and save some urls
save_study_courses_url()