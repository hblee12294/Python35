import subprocess

print("PS D:\Program\Python35> ")
p = subprocess.Popen(["nslookup"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = p.communicate(b"set q = mx\npython.org\nexit\n")
print(output.decode("gbk"))
print("Exit code:", p.returncode)