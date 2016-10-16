class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def getName(self):
		return self.__name

	def getScore(self):
		return self.__score

	def setScore(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError("Bad score")

	def getGrade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student("Bart Simpson", 59)
print("bart.getName() =", bart.getName())

bart.setScore(60)
print("bart.getScore() =", bart.getScore())

print("DO NOT USE bar._Student__name:", bart._Student__name)