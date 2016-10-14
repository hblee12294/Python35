
def printScore(**kw):
	print("      Name Score")
	print("----------------")
	for name, score in kw.items():
		print("%10s %d" % (name, score))
		print()

printScore(Adam=99, Lisa=88, Bart=77)

data = {
	"Adam Lee": 99,
	"Lisa Wang": 88,
	"Ford Bart": 77
}

def printInfo(name, *, gender, city="Beijing", age): # args behind * are all key args
	print("Personal Info:")
	print("-------------")
	print("   Name: %s" % name)
	print(" Gender: %s" % gender)
	print("   City: %s" % city)
	print("    Age: %s" % age)
	print()

printInfo("Bob", gender="male", age=20)
printInfo("Lisa", gender="female", city="Shanghai", age=18)
printInfo("Oliva", gender="male", city="New York", age=35)