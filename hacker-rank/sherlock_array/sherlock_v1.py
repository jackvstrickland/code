#!/usr/bin/py

def sumBothSides(arr,n):

	answer = None

	if sum(arr[1:n]) == 0:
		answer = "YES"
		return answer
	else:

		for x in range(1,n):

			if (sum(arr[:x]) == sum(arr[x+1:])):
				answer = "YES"
				return answer

	if answer is None:
		answer = "NO"

	return answer




if __name__ == '__main__':

	t_cases = int(input().strip())

	for case in range(t_cases):

		n = int(input().strip())
		arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

		print(sumBothSides(arr,n))

