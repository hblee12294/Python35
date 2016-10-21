# -*- coding:utf-8 -*-
import hashlib

db = {
	'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def calcMD5(password):
	md5 = hashlib.md5()
	md5.update(password.encode("utf-8"))
	return md5.hexdigest()

def login(user, password):
	if calcMD5(password) == db[user]:
		print("Clear!")
	else:
		print("Password incorrect.")

un = input("> input user name:")
pwd = input("> enter your password:")

login(un, pwd)