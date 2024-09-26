"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q16
To copy contents of one file to other. While copying a) all full stops are to be replaced with commas b) lower case are to be replaced with upper case c) upper case are to be replaced with lower case.

Explaination Video Link: https://www.youtube.com/watch?v=xJ2kW59dffk&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=17&pp=iAQB
"""

inputfile = open("FE-PPS-LAB/input.txt",'r')
outputfile = open("FE-PPS-LAB/output.txt",'w')

content = list(inputfile.read())

print("".join(content))

for i in range(len(content)):
	if content[i] == ".":
		content[i] = ","
	if content[i].islower():
		content[i] = content[i].upper()
	else:
		content[i] = content[i].lower()

outputfile.write("".join(content))