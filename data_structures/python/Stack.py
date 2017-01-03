#Stack where the updates are to the beginning.
class Stack(object):
        #__init__() will run upon instantiation of the Stack(object) class.
	def __init__(self):
		self.items = []
	#True if empty
	def isEmpty(self):
		if (len(self.items) == 0):
			return True
		else:
			return False
	
	def push(self, x):
		self.items.insert(0, x)

	def pop(self):
		self.items.pop(0)

	def peek(self):
		return self.items[0]
		
	def size(self):
		return len(self.items)


##TEST CASES -- Highlight and press: (ALT + 4) to uncomment.
##newStack = Stack()
##print str(newStack.isEmpty())
##newStack.push(2)
##newStack.push(3)
##newStack.push(18)
##newStack.push(43)
##print "%d" % (newStack.size())
##print "%d" % (newStack.peek())
##newStack.pop()
##print "%d" % (newStack.size())
##print "%d" % (newStack.peek())
##print str(newStack.isEmpty())
