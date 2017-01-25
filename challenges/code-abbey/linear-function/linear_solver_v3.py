test_cases = int(input("Input data:\n")) 
answers = ''

for x in range(0, test_cases):
	data = input().split()
	coord = list(map(int, data))
	slope = (coord[3]-coord[1])/(coord[2]-coord[0])
	answers += '(' + str(slope) + ' ' + str(coord[1]-slope*coord[0]) + ') '
	
print(answers)