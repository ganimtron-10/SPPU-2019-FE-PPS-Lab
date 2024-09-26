"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q21
Program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6 (Or other integer you prefer). Print that number. Request user to roll again. Set the min and max number that dice can show. For the average die, that means a minimum of 1 and a maximum of 6.

Explaination Video Link: https://www.youtube.com/watch?v=cnzJLXMdbFw&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=21&pp=iAQB
"""

# Program that simulates rolling dice. When the program runs, it will randomly choose a
# number between 1 and 6 (Or other integer you prefer). Print that number. Request user to
# roll again. Set the min and max number that dice can show. For the average die, that
# means a minimum of 1 and a maximum of 6.


import random

user_input = 'y'
while user_input == 'y':

	low = int(input("Enter a minimum value to be shown on dice: "))
	high = int(input("Enter a maximum value to be shown on dice: "))

	print("The Random Value is",random.randint(low, high))
	user_input = input("Wanna Roll the Dice Again(y/n): ")
