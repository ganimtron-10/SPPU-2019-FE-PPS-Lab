"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q18
Create class EMPLOYEE for storing details (Name, Designation, gender, Date of Joining and Salary). Define function members to compute a)total number of employees in an organization b) count of male and female employee c) Employee with salary more than 10,000 d) Employee with designation “Asst Manager”

Explaination Video Link: https://www.youtube.com/watch?v=icE1OBFkt6U&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=19&pp=iAQB
"""

# Create class EMPLOYEE for storing details (Name, Designation, gender, Date of Joining
# and Salary). Define function members to compute a)total number of employees in an
# organization b) count of male and female employee c) Employee with salary more than
# 10,000 d) Employee with designation “Asst Manager”

class Employee:

	employee_list = []

	def __init__(self, name,designation,gender, doj, salary):
		self.name = name
		self.designation = designation
		self.gender = gender
		self.date_of_joining = doj
		self.salary = salary

		self.employee_list.append(self)

	def calculate_employee(self):
		return len(self.employee_list)

	def gender_count(self):
		male_count = 0
		female_count = 0
		for emp in self.employee_list:
			if emp.gender == "M":
				male_count += 1
			elif emp.gender == "F":
				female_count += 1
		return male_count,female_count

	def salary_filter(self, salary=10000):
		emp_list = []
		for emp in self.employee_list:
			if emp.salary >= salary:
				# emp_list.append(emp)
				emp_list.append(emp.name)

		return emp_list

	def desgination_filter(self, designation="Asst Manager"):
		emp_list = []
		for emp in self.employee_list:
			if emp.designation == designation:
				# emp_list.append(emp)
				emp_list.append(emp.name)

		return emp_list



e1 = Employee("Rohan","Manager","M","15/02/1990",11000)
e2 = Employee("Monika","HR","F","29/08/1999",8000)
e3 = Employee("Ram","Clerk","M","30/12/2000",5000)
e4 = Employee("Priya","Assistant","F","11/05/2000",6000)
e5 = Employee("Shambhavi","Asst Manager","F","15/02/1990",12000)
e6 = Employee("Shruti","Asst Manager","F","19/11/1998",9000)


print(f"Employee Count = {e1.calculate_employee()}")
print("Male Count = {} and Female Count = {}".format(*e1.gender_count()))
print(e1.salary_filter())
print(e1.desgination_filter())

