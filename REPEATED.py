import os
import psycopg2
import requests, smtplib, ssl
from functions import get_content
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Αρχικοποίηση email
# Define credentials
port = 465  # For SSL
sender_email = "dacc7541@gmail.com"  
password = "dacc7541yolo^_"
receiver_email = "roshimaster942@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Update"
message["From"] = sender_email
message["To"] = receiver_email





# Σύνδεση με τον σέρβερ και ορισμός κέρσορα
conn = psycopg2.connect("dbname=dfpbge6ngou996 host=ec2-34-254-120-2.eu-west-1.compute.amazonaws.com user=wmlasnloqsbjqv port=5432 password=769e7c3bd77aad7811f98822318f4823ae54bccfc4c51b7065a936b9f5a66917")
cur = conn.cursor()


# ΕΠΑΝΑΛΑΜΒΑΝΟΜΕΝΟ #

# Ανάκτηση από ιστοσελίδα για έλεγχο νέων ανακοινώσεων (κατασκευή λίστας νέων ανακοινώσεων)
anakoinwseis = get_content()
new_ann_link_list = []
for anakoinwsh in anakoinwseis:
    for link_ann in anakoinwsh:
        new_ann_link_list.append(str(link_ann))


# Ανάκτηση παλιών ανακοινώσεων από βάση δεδομένων ως λίστα
cur.execute("SELECT * FROM anakoinwseis")
old_ann_tuple_list = cur.fetchall()
old_ann_list = [' '.join(item) for item in old_ann_tuple_list]
conn.commit()

# Έλεγχος ύπαρξης νέων ανακοινώσεων στην λίστα παλιών(από βδ)
for anakoinwsh in new_ann_link_list:
    if anakoinwsh in old_ann_list:
        continue
    else:
        # Αποστολή νέας ανακοίνωσης στην βδ
        my_query = '''INSERT INTO anakoinwseis(anakoinwsh) VALUES(%s)'''
        my_value = (anakoinwsh.strip(),)
        cur.execute(my_query, my_value)
        conn.commit()
    
        # Αποστολή ειδοποίησης με email
        # Create the plain-text and HTML version of your message
        text = """\
        Υπάρχει νέα ανακοίνωση!
        http://www.food.teithe.gr/anakoinwseis/
        """
        html = """\
        <html>
        <body>
            <p>Υπάρχει νέα ανακοίνωση: <br>
              {anakoinwsh} <br><br><br>
            
               Όλες οι ανακοινώσεις: www.food.teithe.gr/anakoinwseis <br>
               Επίσημος ιστότοπος του τμήματος: www.food.teithe.gr
            </p>
        </body>
        </html>
        """.format(anakoinwsh=anakoinwsh)
        context = ssl.create_default_context()

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
           server.login(sender_email, password)
           server.sendmail(
               sender_email, receiver_email, message.as_string().format(anakoinwsh=anakoinwsh).encode('utf-8'))

# ΕΠΑΝΑΛΑΜΒΑΝΟΜΕΝΟ