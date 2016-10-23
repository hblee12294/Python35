from email.mime.text import MIMEText
msg = MIMEText("Hello, this is lblee, I'm a test mail from python. I hope it will be OK next time.", "plain", "utf-8")

from_addr = input("From: ")
password = input("Password: ")
to_addr = input("To: ")
smtp_server = input("SMTP server: ")

import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()