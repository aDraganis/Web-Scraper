# Web-Scraping/Email-Automation
Sends email every time website uploads new announcements.

# Technologies used
Web-Scraping: bs4, requests

Email-Automation: smtplib, ssl, MIMEText & MIMTEMultipart

Database: SQL(PostgreSQL) -> psycopg2


# General Idea
Step #1: Scrapes website and fetches uploaded announcements (saves them in a database).

Step #2: x minutes later #1 is repeated and a list of the newly dowloaded announcements is created.

Step #3: if any new announcements are found, an automated email is sent to notify the user.

#2 and #3 repeat.


# File description
STANDARD.py(ignored): Connects with postgresql database. Fetches announcements from website. Inserts them into the database (as text). Also contains some notes (sql queries for testing purposes).

functions.py: Contains function get_content() that fetches announcements from website.

REPEATED.py: Connects with postgres database. Fetches announcements from website using get_content(). Saves them temporarily in a list. Anns are saved as hyperlinks. Old anns are retrieved from database and are also temporarily saved in a list. The two lists are compared. If there is an ann in the new list that has no match in the old list, python sends email with this ann. It also adds it to the database.

requirements.txt: Contains packages used in python script. Must exist for cloud platform to be able to execute the script properly.

Procfile: worker and clock files must be specified in order to have the script run at a scheduled time.
