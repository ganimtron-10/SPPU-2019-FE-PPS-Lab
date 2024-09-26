"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q15
Write a python program that accepts a string from user and perform following string operations- 
    i. Calculate length of string 
    ii. String reversal 
    iii. Equality check of two strings 
    iv. Check palindrome 
    v. Check substring

Explaination Video Link: https://www.youtube.com/watch?v=VlHl9JchxrE&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=16&pp=iAQB
"""

# Write a python program that accepts a string from user and perform following string
# operations- i. Calculate length of string ii. String reversal iii. Equality check of two
# strings iii. Check palindrome ii. Check substring

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

# count = 0
# for i in s:
# 	count+=1;
# print(count,len(s))
print(len(s1),len(s2))

# revstr = ''
# for i in s:
# 	revstr = i + revstr  # s= 'abc' -> i = a -> revstr = 'a' + '' -> revstr = 'a'
# 							#          i = b -> revstr = 'b' + 'a' -> revstr = 'ba'
# 							#          i = c -> revstr = 'c' + 'ba' -> revstr = 'cba'
# print(revstr)
revstr1 = s1[::-1]
revstr2 = s2[::-1]
print(revstr1,revstr2)

if s1 == s2:
	print("Strings are equal")
else:
	print("Strings are not equal")

# abba - abba -> palindrome eg. malayalam, racecar
if s1 == revstr1:
	print("String1 is palindrome")
if s2 == revstr2:
	print("String2 is palindrome")

substr1 = input("enter substring for str1: ")
if substr1 in s1:
	print(substr1,"is a substring!")
else:
	print(substr1,"is not a substring!")