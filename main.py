from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest

result = requests.get( "https://wuzzuf.net/search/jobs/?q=python&a=hpb" )
Job_titles = []
Company_names = []
Location_name = []
Job_skills_name = []

## this to save the content from the webpage
src = result.content
print( src )
# 4th step create a soup object to parse content

soup = BeautifulSoup( src, 'lxml' )

##find the element that you want .
## job titles,job skills, comapny names,location names.

job_titles = soup.find_all( "h2", {"class": "css-m604qf"} )  ##it return a list. the second paramert is dic
company_names = soup.find_all( "a", {"class": "css-17s97q8"} )
location_name = soup.find_all( "span", {"class": "css-5wys0k"} )
job_skills = soup.find_all( "div", {"class": "css-y4udm8"} )

for i in range( len( job_titles ) ):
    Job_titles.append( job_titles[i].text )
    Company_names.append( company_names[i].text )
    Location_name.append( location_name[i].text )
    Job_skills_name.append( job_skills[i].text )


##create  csv file to save the data .

with open( "employee1.csv", "w" ) as job_file:
    wr = csv.writer( job_file )
    wr.writerow( ["job title,", "company name", "location", "Job_skills"] )
    wr.writerows([Job_titles,Company_names,Location_name,Job_skills_name])
