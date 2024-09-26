"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q12
To accept list of N integers and partition list into two sub lists even and odd numbers.

Explaination Video Link: https://www.youtube.com/watch?v=ec4ibwDuaqo&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=13&pp=iAQB
"""

n = int(input("Enter number of elements: "))

glist = []
evenl = []
oddl = []
raisedlist = ["th","st","nd","rd"]

for i in range(n):
	if not i in [1,2,3]:
		raisei = 0
	else:
		raisei = i
	x = int(input(f"Enter {i}{raisedlist[raisei]} element: "))
	glist.append(x)

for num in glist:
	if num%2 == 0:
		evenl.append(num)
	else:
		oddl.append(num)

print("Even List: ",evenl)
print("Odd List: ",oddl)