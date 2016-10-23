from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, "utf-8").encode("utf-8"), addr))

from_addr = input("From: ")
password = input("Password: ")
to_addr = input("To: ")
smtp_server = input("STMP server: ")

msg = MIMEMultipart()
msg["From"] = _format_addr("Python fan <%s>" % from_addr)
msg["To"] = _format_addr("Admin <%s>" % to_addr)
msg["Subject"] = Header("From SMTP...", "utf-8").encode()

msg.attach(MIMEText("Send by python... with file", "plain", "utf-8"))

with open(r"D:\Program\Python35\fishman.bmp", "rb") as f:
	mime = MIMEBase("image", "bmp", filename = "fishman.bmp")

	mime.add_header("Content-Deposition", "attachment", filename = "fishman.bmp")
	mime.add_header("Content-ID", "<0>")
	mime.add_header("X-Attachment-Id", "0")
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()