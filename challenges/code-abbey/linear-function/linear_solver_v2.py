test_cases = int(input("Input data:\n")) 
answers = []

for x in range(0, test_cases):
	coordinates = input().split()
	slope = (int(coordinates[3])-int(coordinates[1])) / (int(coordinates[2]) - int(coordinates[0]))
	intercept = int(coordinates[1]) - (slope * int(coordinates[0]))
	answers.append(int(slope))
	answers.append(int(intercept))
	
for x in range(0, len(answers), 2):
	print("({:d} {:d})".format(answers[x], answers[x+1]), " ", end="")