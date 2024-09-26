"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q3
To accept N numbers from user. Compute and display maximum in list, minimum in list, sum and average of numbers.

Explaination Video Link: https://www.youtube.com/watch?v=2vm4HL3_8AQ&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=4&pp=iAQB
"""

#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

n = int(input())

arr = []

for i in range(n):
	arr.append(int(input()))


print("Max Element is ",max(arr))
print("Min Element is ",min(arr))

print("Sum is ",sum(arr))
print("Avg is ",int(sum(arr)/n))