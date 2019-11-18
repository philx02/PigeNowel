# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

import csv
import random

participants = []
rx = []

class Participant:
    def __init__(self, name, email, constraints):
        self.name = name
        self.email = email
        self.constraints = constraints

with open("participants.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        participants.append(Participant(row[0], row[1], row[2]))
        rx.append(row[0])

def fail_constraint(participants, rx):
    for i in range(0, len(participants)):
        if participants[i].name == rx[i] or participants[i].constraints == rx[i]:
            return True
    return False

while fail_constraint(participants, rx):
    random.shuffle(rx)

s = smtplib.SMTP(host="mailout.easydns.com", port=587)
s.login("spoluck.ca", "sg1240rj")
#s = smtplib.SMTP(host="spoluck.ca")
for i in range(0, len(participants)):
    msg = EmailMessage()
    msg['Subject'] = "Pige Noël 2019"
    msg['From'] = "ne-pas-repondre@spoluck.ca"
    msg['To'] = participants[i].email
    #msg['To'] = "pcayouette@spoluck.ca"
    msg.set_content("Yo " + participants[i].name + ", tu as pigé " + rx[i])
    s.send_message(msg)
    print("Email to " + participants[i].email + " sent.")
s.quit()
