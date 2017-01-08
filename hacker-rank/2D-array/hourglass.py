#!/bin/python3

import sys

def getHourglassSum(arr, h_row, h_col):
	total = arr[h_row+1][h_col+1]
	for y in range(0,3,2):
		for x in range(h_col, h_col+3):
			total += arr[h_row+y][x]
	return total

arr = []
sums = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

hg_max= None

for row in range(0,4):
 	for col in range(0,4):
 		hg_sum = getHourglassSum(arr,row,col)
 		
 		if hg_max is None:
 			hg_max = hg_sum
 		elif hg_sum > hg_max:
 			hg_max = hg_sum

print(hg_max)

