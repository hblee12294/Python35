def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

for n in primes():
	if n < 20:
		print(n)
	else:
		break

# practice 1
# my version
def isPalindrome(n):
	strn = str(n)
	i , j = 0, len(strn) - 1
	while i < j:
		if strn[i] != strn[j]:
			return False
		i += 1
		j -= 1
	return True

output = filter(isPalindrome, range(1, 200))
print(list(output))

# one-line version
def isPalindrome2(n):
	return str(n) == str(n)[::-1]

output = filter(isPalindrome2, range(1, 200))
print(list(output))