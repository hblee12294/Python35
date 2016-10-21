from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
Position = namedtuple("Position", ['x', 'y', 'z'])
p = Point(1, 2)
ps = Position(4, 5, 6)
print("Point:", p.x, p.y)
print("Position:", ps.x, ps.y, ps.z)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd["key1"] = "abc"
print("dd[\"key1\"] =", dd["key1"])
print("dd[\"key2\"] =", dd["key2"])

from collections import Counter

c = Counter()
for ch in "programming":
	c[ch] = c[ch] + 1
print(c)