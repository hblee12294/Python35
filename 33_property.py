class Screen(object):
	
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, wth):
		self._width = wth

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, hght):
		self._height = hght

	@property
	def resolution(self):
		return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution