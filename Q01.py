"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q1
To calculate salary of an employee given his basic pay (take as input from user). Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary payable after deductions.

Explaination Video Link: https://www.youtube.com/watch?v=YKuda5SDodo&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=2&pp=iAQB
"""

# Setup Code
import os
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

###########################################
# Real Code Starts

basic_pay = int(input("Enter your Basic Pay: "))

hra = 10/100 * basic_pay
ta = 5/100 * basic_pay

gross_salary = int(basic_pay + hra + ta)

print("Your Gross Salary is: ", gross_salary)

pt = 2/100 * gross_salary

net_salary = gross_salary - int(pt)

print("Your Net Salary is: ", net_salary)

for p in os.walk("."):
    print(p)
