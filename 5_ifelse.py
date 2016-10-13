# -*- coding:utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight / height**2
tips = ("light", "normal", "overweight", "obesity", "severe obese")

if bmi < 18.5:
	print(tips[0])
elif bmi < 25:
	print(tips[1])
elif bmi < 28:
	print(tips[2])
elif bmi < 32:
	print(tips[3])
else:
	print(tips[4])
