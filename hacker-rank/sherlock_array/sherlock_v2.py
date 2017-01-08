#!/usr/bin/py

def sumBothSides(arr,n):

	# answer = None

	left = 0
	right = sum(arr[1:])

	if left == right:
		return("YES")

	for i in range(1,n):
		left += arr[i-1]
		right -= arr[i]
		
		if left == right:
			return("YES")

	return("NO")

if __name__ == '__main__':

	t_cases = int(input().strip())

	for case in range(t_cases):

		n = int(input().strip())
		arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

		print(sumBothSides(arr,n))

