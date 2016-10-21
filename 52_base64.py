import base64

print(base64.b64encode(b"binary\x00string"))
print(base64.b64decode(b"YmluYXJ5AHN0cmluZw=="))

print(base64.b64encode(b"i\xb7\x1d\xfb\xef\xff"))
print(base64.b64decode(b"abcd--__"))


def safe_base64_decode(s):
	while len(s) % 4 != 0:
		s += "="
	return base64.b64decode(s)

print(safe_base64_decode("YmluYXJ5AHN0cmluZw"))