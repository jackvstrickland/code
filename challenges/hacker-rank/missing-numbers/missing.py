n = int(input().strip())
list_A = [int(arr_temp) for arr_temp in input().strip().split(' ')]

m = int(input().strip())
list_B = [int(arr_temp) for arr_temp in input().strip().split(' ')]

freq_diff = [0]*10000

for x in list_A:
	freq_diff[x] -= 1

for x in list_B:
	freq_diff[x] += 1

for x in range(10000):
	if freq_diff[x] != 0:
		print(x, end=" ")