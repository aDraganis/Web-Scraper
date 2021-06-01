import os
import psycopg2
import requests, smtplib, ssl
from functions import get_content
from bs4 import BeautifulSoup


# STANDARD

# Σύνδεση με τον σέρβερ
conn = psycopg2.connect("dbname=myDB host=localhost user=postgres password=abcdefg")
cur = conn.cursor()

# CREATE TABLE,COLUMN
#cur.execute("CREATE TABLE anakoinwseis(anakoinwsh TEXT)")

# INSERT SINGLE RECORD
#cur.execute("INSERT INTO anakoinwseis(anakoinwsh) VALUES(5)")

# Ανάκτηση από ιστοσελίδα και έπειτα Αποστολή ανακοινώσεων στον σέρβερ
anakoinwseis = get_content()
for anakoinwsh in anakoinwseis: 
   for link_ann in anakoinwsh:
      my_query = "INSERT INTO anns_test(ann_test) VALUES(%s)"
      my_value = (str(link_ann), )
      cur.execute(my_query, my_value)
   
conn.commit()
# Διαγραφή σειρών από πίνακα
#cur.execute("DELETE FROM anakoinwseis WHERE anakoinwsh = 'Heyyoo'")
#conn.commit()

# Διαγραφή πίνακα
#cur.execute("DROP TABLE anakoinwseis")

# Ανάκτηση δεδομένων από πίνακα
#cur.execute("SELECT * FROM anakoinwseis")
#my_result = cur.fetchall()
#for x in my_result:
#    print(x)


# STANDARD # 