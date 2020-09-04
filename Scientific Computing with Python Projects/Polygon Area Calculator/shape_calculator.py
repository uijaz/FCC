class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __str__(self):
		string = "Rectangle(width={}, height={})".format(self.width, self.height)
		return string

	def set_width(self, width):
		self.width = width
	
	def set_height(self, height):
		self.height = height

	def get_area(self):
		area = (self.width *self. height)
		return area

	def get_perimeter(self):
		perimeter = ((2 * self.width) + (2 * self.height))
		return perimeter

	def get_diagonal(self):
		diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
		return diagonal

	def get_picture(self):
		if (self.width > 50 or self.height > 50):
			return "Too big for picture."
		else:
			print_width = ""
			for i in range(self.height):
				for j in range(self.width):
					print_width += "*"
				print_width += '\n'
			return print_width

	def get_amount_inside(self, Shape):
		# Takes another shape (square or rectangle) as an argument.
		# Returns the number of times the passed in shape could fit inside the shape (with no rotations).
		# For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
		if self.get_area() > Shape.get_area():
			return self.get_area() // Shape.get_area()
		else:
			return 0
		# pass

###################################################################################################

class Square(Rectangle):
	def __init__(self, side):
		self.side = side
		super().__init__(side, side)

	def __str__(self):
		string = "Square(side={})".format(self.side)
		return string

	def set_side(self, side):
		self.__init__(side)

	def set_width(self, width):
		self.set_side(width)

	def set_height(self, height):
		self.set_side(height)

	def get_picture(self):
		return super().get_picture()

# Additionally, the `set_width` and `set_height` methods on the Square class should set both the width and height.