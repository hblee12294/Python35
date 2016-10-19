# -*- coding: utf-8 -*-

import re

print("Test: 010-12345")
m = re.match(r"^(\d{3})-(\d{3,8})$", "010-1235")
print(m.group(1), m.group(2))

t = "19:05:30"
print("Test:", t)
m = re.match(r"^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$", t)
print(m.groups())


# practice 1 and 2

eml = re.match(r"^([0-9a-zA-Z\_\.]+)@([0-9a-z]+).(\w+)$", "hblee12294@gmail.com")
print(eml.groups())
print("username:", eml.group(1))
print("Server:", eml.group(2))