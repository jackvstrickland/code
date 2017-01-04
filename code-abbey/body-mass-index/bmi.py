test_cases = int(input("input data:\n"))
bmi_list = []
for person in range(0,test_cases):
	weight, height = input().split()
	bmi = float(weight)/(float(height)**2)
	if bmi < 18.5:
		bmi_list.append("under")
	elif bmi < 25.0:
		bmi_list.append("normal")
	elif bmi < 30.0:
		bmi_list.append("over")
	else:	
		bmi_list.append("obese")

print("answer:\n")
print(bmi_list)