# Web-Scraping/Email-Automation
Sends email every time website uploads new announcement.

## Tools used
- webscraping: beautifulsoup4, requests
- emails: smtplib
- database: PostgreSQL/psycopg2


## General Idea
1. Scrapes website and fetches uploaded announcements (stores them in a database).
2. x minutes later 1. is repeated and a list of the newly dowloaded announcements is created.
3. Ιf any new announcements are found, an automated email is sent to notify the user.
