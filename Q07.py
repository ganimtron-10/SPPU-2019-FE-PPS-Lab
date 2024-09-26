"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q7
To accept the number and Compute 
    a) square root of number, 
    b) Square of number, 
    c) Cube of number 
    d) check for prime, 
    d) factorial of number 
    e) prime factors

Explaination Video Link: https://www.youtube.com/watch?v=g7Qm6EJgeUQ&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=8&pp=iAQB
"""

#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts
import math


def isPrime(n):
	# 2 - (n-1) is dividing n or not
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

def findprimefactors(n):
	primelist = []
	for i in range(2,n):
		if isPrime(i) and n%i == 0:
			primelist.append(i)
	if isPrime(n):
		primelist.append(n)
	return primelist



for i in range(int(input())):
	n = int(input())

	print(f"Square root of {n} = {math.sqrt(n)}")
	print(f"Square of {n} = {n**2}")
	print(f"cube of {n} = {n**3}")

	if isPrime(n):
		print(f"{n} is prime")
	else:
		print(f"{n} is  not prime")

	print(f"factorial of {n} is {fact(n)}")

	print(f"Prime factors of {n} are :")
	for i in findprimefactors(n):
		print(i)

	print()