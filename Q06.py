"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q6
To simulate simple calculator that performs basic tasks such as addition, subtraction, multiplication and division with special operations like computing x^y and x!.

Explaination Video Link: https://www.youtube.com/watch?v=1IUypxr5JGM&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=7&pp=iAQB
"""

# #Setup Code
# import sys

# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

# ###########################################
# #Real Code Starts

#Class Implementation

# class Calculator():
# 	def __init__(self):
# 		print('Calculator Initialsed!!')

# 	def add(self,*args):
# 		ans = sum(args)
# 		print("Addition = ",ans)

# 	def sub(self, *args):
# 		ans = sum(args)
# 		print("Substraction = ",ans)

# 	def mul(self, *args):
# 		ans = 1
# 		for i in args:
# 			ans *= i
# 		print("mul = ",ans)

# 	def div(self, a, b):
# 		print("div = ",int(a/b))

# 	def factorial(self, n):
# 		ans = 1
# 		while n>0:
# 			ans *= n #ans = ans * n
# 			n = n-1
# 		print("factorial is",ans)

# 	def raiseto(self, *args):
# 		#a,b,c = (a**b)**c
# 		ans = args[0]
# 		# print(ans,args,args[1:])
# 		for i in args[1:]:
# 			ans = ans**i
# 		print("ans = ",ans)

# cal = Calculator()
# cal.sub(100,-4,100,-200)
# cal.mul(100,3,45)
# cal.div(100,50)
# cal.factorial(5)
# cal.raiseto(2,3,2)

#fact = n! = n*(n-1)! 0! = 1 1!=1
#5! = 5*4*3*2*1 =120


#Interactive Implementation

#equ = a Op b
# equ = input()
# equ = equ.split(' ')

# a = int(equ[0])
# b = int(equ[2])

# op = equ[1]

# if op == '+':
# 	print("Addition = ",a+b)
# elif op == '-':
# 	print("SUB = ",a-b)
# # print(equ)

print('Calculator Started!!')

while True:

	equ = input("Enter Equation: ")

	if equ == '':
		print("Calculator Stopped!!!")
		break

	print("Answer is",eval(equ))

