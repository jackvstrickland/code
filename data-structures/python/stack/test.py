from Stack import Stack

def runTest():
	s = Stack()
	print(s.isEmpty())
	s.push(2)
	s.push(3)
	s.push(18)
	s.push(43)

	print(s.size())
	print(s.peek())
	s.pop()
	print(s.size())
	print(s.peek())
	print(s.isEmpty())

if __name__ == "__main__":
	runTest()
	