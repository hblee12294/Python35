from io import StringIO


f = StringIO()
f.write("hello")
f.write(" ")
f.write("world!")
print(f.getvalue())

f = StringIO("I know\nWhere you stand\nSilent\nIn the trees")
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
