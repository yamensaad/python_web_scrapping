
from bs4 import  BeautifulSoup


with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup( content, 'lxml' )
    course_cards = soup.findAll('div',class_= 'card')
    for course in course_cards:
        course_name = course.h5.text ##it will search for text attribute
        course_price = course.a #a tage install the information about course price.
        print(course_name)
        print(course_price)
        course_name = course.h5.text


    






