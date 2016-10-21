# -*- coding:utf-8 -*-
import hashlib

db = {
	'hblee': 'f04111c1a4b6bb45753fb80708dfc64f', # 123456 + hblee
}

salt = "hblee"

def calcMD5(pwd):
	md5 = hashlib.md5()
	md5.update(pwd.encode("utf-8"))
	return md5.hexdigest()

def login():
	user = input("User name> ")
	password = input("Password> ")

	while True:
		if user not in db.keys():
			print("\"%s\" is not exist!" % user)
			user = input("Enter user name again> ")
			continue
		elif calcMD5(password + salt) != db[user]:
			print("Password incorrect!")
			password = input("Enter password again> ")
			continue
		else:
			print("Welcome!")
			break

if __name__ == "__main__":
	login()