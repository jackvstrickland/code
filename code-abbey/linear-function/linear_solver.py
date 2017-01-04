# This will solve for the linear equation y=ax+b when given two points as input
class Point:
	def __init__(self, x, y):
		self.x, self.y = int(x), int(y)

	def find_slope(self, another_point):
		slope = (another_point.y - self.y) / (another_point.x - self.x)
		return int(slope)

	def print_values(self):
		print("(" +self.x + ", " + self.y + ")")

test_cases = int(input("Input data:\n")) 
answers = []

for x in range(0, test_cases):
	data = input()
	coordinates = data.split(' ')

	# print(coordinates)
	
	p1 = Point(coordinates[0], coordinates[1])
	p2 = Point(coordinates[2], coordinates[3])

	slope = p1.find_slope(p2)
	b = p1.y - (slope * p1.x)

	answers.append(str(slope))
	answers.append(str(b))



for x in range(0, len(answers), 2):
	print("(" + answers[x] + " " + answers[x+1] + ")", " ", end="")