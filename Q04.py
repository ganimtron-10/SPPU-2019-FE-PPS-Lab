"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q4
To accept student’s five courses marks and compute his/her result. Student is passing if he/she scores marks equal to and above 40 in each course. If student scores aggregate greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the grade if first division. If aggregate is 50>= and <60, then the grade is second division. If aggregate is 40>= and <50, then the grade is third division.

Explaination Video Link: https://www.youtube.com/watch?v=svxE0R7MOJM&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=5&pp=iAQB
"""

#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

def grade_cal(per):
	if per>75:
		return "Distinction"
	elif per >= 60 and per<75:
		return "First Div"
	elif per >= 50 and per<60:
		return "Second Div"
	elif per >= 40 and per<50:
		return "Third Div"

for i in range(int(input())):
	arr = list(map(int,input().split()))
	iseligible = all(x>=40 for x in arr)
	# print(iseligible)
	stud_per = sum(arr)/5
	# print(stud_per)
	if iseligible:
		print(f"You Obtained {stud_per}% and Your Grade is {grade_cal(stud_per)}")
	else:
		print("You failed!!")