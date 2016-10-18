import os

os.name
os.uname() # Linux, Unix only
os.environ
os.environ.get("PATH")

os.path.abspath('.')
os.path.join("   ", "    ") # does not have to exist
os.mkdir("    ")
os.rmdir("    ")
os.path.split("    ") # does not have to exist
os.path.splittext("    ") # does not have to exist
os.rename("    ", "    ")
os.remove("    ")

[x for x in os.listdir('.') if os.path.isdir(x)]

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splittext(x)[1] == ".py"]