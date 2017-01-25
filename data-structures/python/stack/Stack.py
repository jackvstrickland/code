#Stack where the updates are to the beginning.
class Stack(object):
	#__init__() will run upon instantiation of the Stack(object) class.
	def __init__(self):
		self.items = []
	#True if empty
	def isEmpty(self):
		return self.items == []
	
	def push(self, x):
		self.items.insert(0, x)

	def pop(self):
		self.items.pop(0)

	def peek(self):
		return self.items[0]
		
	def size(self):
		return len(self.items)
