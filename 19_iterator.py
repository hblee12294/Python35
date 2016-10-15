
from collections import Iterable, Iterator

def g():
	yield 1
	yield 2
	yield 3

print("Iterable? [1, 2, 3]:", isinstance([1, 2, 3], Iterable))
print("Iterable? \'abc\':", isinstance('abc', Iterable))
print("Iterable? 123:", isinstance(123, Iterable))
print("Iterable? g():", isinstance(g(), Iterable))

print("Iterator? [1, 2, 3]", isinstance([1, 2, 3], Iterator))
print("Iterator? iter([1, 2, 3])", isinstance(iter([1, 2, 3]), Iterator))
print("Iterable? \'abc\':", isinstance('abc', Iterator))
print("Iterable? 123:", isinstance(123, Iterator))
print("Iterable? g():", isinstance(g(), Iterator))