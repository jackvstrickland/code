#!/bin/python3

import sys

def getHourglassSum(arr, h_col, h_row):
	total = 0
	for y in range(0,3,2):
		for x in range(h_col, h_col+3):
			total += arr[h_row+y][x]
	total += arr[h_col+1][h_row+1]
	return total



arr = []
sums = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

for row in range(0,4):
	for col in range(0,4):
		sums.append(getHourglassSum(arr, col, row))

print(arr)
print(sums)

