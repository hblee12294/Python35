from io import BytesIO

f = BytesIO()
f.write(b"hello")
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

data = "Standing cowardly, I can feel your breath.".encode("utf-8")
f = BytesIO(data)
print(f.read())