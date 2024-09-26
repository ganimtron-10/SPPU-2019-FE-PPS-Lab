"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q5
To check whether input number is Armstrong number or not. An Armstrong number is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. Ex. 371.

Explaination Video Link: https://www.youtube.com/watch?v=teEoh90_h2U&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=6&pp=iAQB
"""

#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

# Method 1
# for i in range(int(input())):
# 	n = input()
# 	if len(n) == 3:
# 		fn = int(n[0])
# 		sn = int(n[1])
# 		tn = int(n[2])
# 		sumofc = fn**3+sn**3+tn**3
# 		if int(n) == sumofc:
# 			print("Its Armstrong NUmber.")
# 		else:
# 			print("Its not an Armstrong Number.")
# 	else:
# 		print('Give Three Digit Number.')


# Method2
for i in range(int(input())):
	n = int(input())
	if n>99 and n<1000:
		fn = (n%10)
		sn = ((n//10)%10)
		tn = ((n//10)//10)
	if n == (fn**3+sn**3+tn**3):
		print('Yes')
	else:
		print("no")