import requests, smtplib, ssl
from bs4 import BeautifulSoup

# Σύνδεση με τον σέρβερ


# Function ανάκτησης ανακοινώσεων από την ιστοσελίδα
def get_content():
    # Get website's content using requests module
    URL = 'http://www.food.teithe.gr/anakoinwseis/'
    page = requests.get(URL)

    # Filter html content with BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find specific items through class and attribute. Place all of them a list
    """anakoinwseis = soup.find_all('ol', class_= 'nlposts-wrapper nlposts-olist nav nav-tabs nav-stacked')"""
    return soup.find_all('h3', class_= 'nlposts-olist-title')

