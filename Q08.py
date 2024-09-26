"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q8
To accept two numbers from user and compute smallest divisor and Greatest Common Divisor of these two numbers.

Explaination Video Link: https://www.youtube.com/watch?v=30gN_Usoztc&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=9&pp=iAQB
"""

#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

def findlcm(a,b):
	for i in range(2,min(a,b)):
		if a%i == 0 and b%i == 0:
			return i
	return 1

def findhcf(a,b):
	for i in range(min(a,b),1,-1):
		if a%i == 0 and b%i == 0:
			return i
	return 1


for i in range(int(input())):
	a,b = map(int,input().split())
	print(f'Lcm of {a} and {b} is {findlcm(a,b)}')
	print(f'HCF of {a} and {b} is {findhcf(a,b)}',"\n")