# -*- coding: utf-8 -*-

import random

# ----------------- Initalize Student List ----------------

sortedStudent = [[62, 67, 75], [69, 66, 78, 81], [82, 87, 88, 90]]
unsortStudent = [64, 65, 70, 71, 72, 74, 76, 77, 79, 80, 83, 84, 85, 89, 100]
# print(len(unsortStudent))

# ----------------- Shuffle Studnet List -----------------

shuffledList = unsortStudent
random.shuffle(shuffledList)
random.shuffle(shuffledList)
# print(shuffledList)

# ---------------------Divide Groups ---------------------

groups = []

for group in sortedStudent:
	groups.append(group)

for i in range(5):
	groups.append(shuffledList[i::5])

random.shuffle(groups)
# print(groups)

# ------------------ Allocate Nations ------------------

nations = ["France", "Germany", "India", "Japan", "Russia", "America", "Britain", "China"]
finalList = {}

for i in range(8):
	finalList[nations[i]] = groups[i]

print()
print()
print()

for k, v in finalList.items():
	print(k, "=>", v)
	
print()
print()
print()

