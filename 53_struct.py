# -*- coding: utf-8 -*-

import struct

with open(r"D:\Program\Python35\fishman.bmp", "rb") as f:
	header = f.read(30)
	print(header)
	info = struct.unpack("<ccIIIIIIHH", header)
	print(info)
	print(info[0] + info[1])
	if info[0] + info[1] == b"BM":
		print("Size:", info[2])
		print("Color size:", info[9])
	else:
		raise TypeError("Not a \'.bmp\'")
