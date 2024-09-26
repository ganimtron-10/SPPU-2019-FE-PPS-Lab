"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q14
To accept from user the number of Fibonacci numbers to be generated and print the Fibonacci series.

Explaination Video Link: https://www.youtube.com/watch?v=dy5BuYOL3DM&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=15&pp=iAQB
"""

# Fibonacci Series
#  0        1        1     2 3 5 8 13 ....
# (i-2)0  (i-1)=1  i=2

n = int(input("Enter number of Fibonacci terms required: "))

fiboseries = [0,1]

for i in range(2,n):
	fiboseries.append(fiboseries[i-2]+fiboseries[i-1])

for i in fiboseries:
	print(i,end=" ")