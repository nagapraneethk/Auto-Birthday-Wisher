import datetime as dt
import os
import random
import smtplib
import time
from email.mime.text import MIMEText

import pandas as pd
# Replace with your EMAIL and add env-variables for PASSWORD
EMAIL = "<EMAIL>"
PASSWORD = os.environ.get("EMAIL_PASSWORD")
# Replace with your name
YOURNAME = "<YOUR NAME>"

today = (dt.datetime.now().month, dt.datetime.now().day)
print(today)

bdays_list = pd.read_csv("./birthdays.csv")
birthdays_today = bdays_list[(bdays_list["month"] == today[0]) & (bdays_list["day"] == today[1])]
print(birthdays_today)

if not birthdays_today.empty:
    for index, row in birthdays_today.iterrows():
        try:
            with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter_temp:
                template = letter_temp.read()
                template = template.replace("[NAME]", row["name"])
                template = template.replace("[YOURNAME]", YOURNAME)

            # Create a personalized message
            message = MIMEText(template)
            message["Subject"] = f"Happy Birthday, {row["name"]}!"
            message["From"] = EMAIL
            message["To"] = row["email"]

            # To establish a secure SSL connection for sending your emails, port is used.
            # Change your smtp provider if you have other email provider like "@yahoo.com" or others.
            # Replace with your STMP server and respective port.
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(EMAIL, row["email"], message.as_string())

            print(f"Sent birthday email to {row['name']}")
            time.sleep(3)
        except Exception as e:
            print(f"Error sending email to {row['name']}: {e}")

else:
    print("No birthdays today")
