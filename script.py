import pandas as pd
import smtplib


e = pd.read_excel (r'email.xlsx');

SenderAddress = "email"
password = "pass";

emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(SenderAddress, password)
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()