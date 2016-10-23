from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, "utf-8").encode("utf-8"), addr))

from_addr = input("From: ")
password = input("Password: ")
to_addr = input("To: ")
smtp_server = input("STMP server: ")

msg = MIMEText("Hello, send by python...", "plain", "utf-8") # the content can be replaced with HTTP, "plain" to "http"
msg["From"] = _format_addr("Python fan <%s>" % from_addr)
msg["To"] = _format_addr("Admin <%s>" % to_addr)
msg["Subject"] = Header("From SMTP....", "utf-8").encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()