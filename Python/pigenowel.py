# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

import csv
import random

tx = []
rx = []

with open("participants.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        tx.append(row)
        rx.append(row)

def duplicate_exists(tx, rx):
    for i in range(0, len(tx)):
        if tx[i] == rx[i]:
            return True
    return False

while duplicate_exists(tx, rx):
    random.shuffle(rx)

s = smtplib.SMTP(host="mailout.easydns.com", port=587)
s.login("spoluck.ca", "sg1240rj")
#s = smtplib.SMTP(host="spoluck.ca")
for i in range(0, len(tx)):
    msg = EmailMessage()
    msg['Subject'] = "Pige Noël 2018"
    msg['From'] = "ne-pas-repondre@spoluck.ca"
    msg['To'] = tx[i][1]
    #msg['To'] = "pcayouette@spoluck.ca"
    msg.set_content("Yo " + tx[i][0] + ", tu as pigé " + rx[i][0])
    s.send_message(msg)
    print("Email to " + tx[i][0] + " sent.")
s.quit()
