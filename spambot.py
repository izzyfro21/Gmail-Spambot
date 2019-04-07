import smtplib
import time
import sys
import os


#Asks the user for all the necessary inputs to make this program run
print("Before you start, you must go to this website: https://myaccount.google.com/lesssecureapps and check the box yes")
email = str(raw_input("What is your email (must be gmail): "))
password = raw_input("What is your password: ")
amount = int(raw_input("How many emails would you like to send: "))
wait = int(raw_input("How long before each message (in seconds): "))
recipient = raw_input("What is the recipiant email: ")

#creats the text editor
print("Type in your message.")
lines = []
while True:
    line = raw_input(">")
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

starttime = time.time()

#sends the email
for i in range(amount):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    smtpObj.starttls()

    smtpObj.login(email, password)

    smtpObj.sendmail(email, recipient, text)

    smtpObj.quit()

    time.sleep(wait)


