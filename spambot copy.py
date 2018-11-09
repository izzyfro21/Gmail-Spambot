
import smtplib
import time
import sys
import os



print("Before you start, you must go to this website: https://myaccount.google.com/lesssecureapps and check the box yes")

email = input("What is your email (must be gmail): ")
password = input("What is your password: ")
amount = int(input("How many emails would you like to send: "))
wait = int(input("How long before each message (in seconds): "))
recipient = input("What is the recipiant email: ")

print("Type in your message.")
lines = []
while True:
    line = input(">")
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

starttime = time.time()

for i in range(amount):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    smtpObj.starttls()

    smtpObj.login(email, password)

    smtpObj.sendmail(email, recipient, text)

    smtpObj.quit()

    time.sleep(wait)




