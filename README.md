# WebScrape-EmailAutomation
Beginner level app. Sends email every time university's website uploads new announcements.

# App DESCRIPTION
# General Idea
procedure 1: web scrapes website (university) and fetches the announcements that the website has uploaded. Announcements are saved in a database.

procedure 2: every x mins/hours procedure 1 is repeated and a list of the newly dowloaded announcements is created.

procedure 3: if there are any new announcements, an automated email is sent to notify the user. The new announcements become the 'old' ones.

Procedures 2 and 3 repeat.

# Programming languages, packages and other tools used
WebScraping: Python -> bs4, requests

EmailAutomation: smtplib, ssl, MIMEText & MIMTEMultipart

Database: SQL(PostgreSQL) -> psycopg2

# File description
STANDARD.py(ignored): Connects with postgresql database. Fetches announcements from website using get_content(). Inserts them into the database (as text). Also contains some notes (sql queries for testing purposes).

functions.py: Contains function get_content() that fetches announcements from website. Anns are fecthed in the following form -> """<h3><a href='link'>text</a></h3>""".

REPEATED.py: Connects with postgres database. Fetches announcements from website using get_content(). Saves them temporarily in a list(called 'new'). Anns are saved in the following form -> '<a href='link'>text</a>'. Old anns are retrieved from database and are also temporarily saved in a list (called 'old'). The two lists are compared. If there is an ann in the new list that has no match in the old list, python sends email with this ann as link. It also adds it to the database.

requirements.txt: Contains packages used in python script. Must exist for cloud platform to be able to execute the script properly.

Procfile: worker and clock files (repeated.py) must be specified in order to have the script (repeated.py) run at a scheduled time (every x mins/hours).
