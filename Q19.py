"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q19
Create class STORE to keep track of Products ( Product Code, Name and price). Display menu of all products to user. Generate bill as per order.

Explaination Video Link: https://www.youtube.com/watch?v=Nsywo42zu0A&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=20&pp=iAQB
"""

# Create class STORE to keep track of Products ( Product Code, Name and price). Display
# menu of all products to user. Generate bill as per order.

class Product:
	def __init__(self,product_code, product_name, product_price):
		self.code = product_code
		self.name = product_name
		self.price = product_price



class Store:

	product_list = []
	order_list = []

	def __init__(self, name):
		self.name = name

	def add_product(self, p_code, p_name, p_price):
		self.product_list.append(Product(p_code, p_name, p_price))

	def display_menu(self):
		print("-"*90)
		print("Menu".center(90))
		print("-"*90)
		print("{}{}{}".format("Product Code".center(30),"Product Name".center(30),"Product Price(Rs.)".center(30)))
		print("-"*90)

		for p in self.product_list:
			print("{}{}{}".format(str(p.code).center(30),p.name.center(30),str(p.price).center(30)))

		print("-"*90)

	def pick_product(self, product_code, quantity):
		for p in self.product_list:
			if p.code == product_code:
				self.order_list.append((p,quantity))

	def generate_bill(self):
		print("-"*100)
		print("Bill".center(100))
		print("-"*100)
		print("{}{}{}{}{}".format("Product Code".center(20),"Product Name".center(20),
								"Per Product Price(Rs.)".center(20),"Quantity".center(20), "Total Product Price(Rs.)".center(20)))
		print("-"*100)

		total_bill_value = 0

		for t in self.order_list:
			p,q = t
			total_bill_value += p.price * q
			print("{}{}{}{}{}".format(str(p.code).center(20),p.name.center(20),str(p.price).center(20),
									str(q).center(20), str(p.price*q).center(20)))


		print("-"*100)

		print(f"Total Bill Amount = {total_bill_value} Rs.")

		print("-"*100)


s1 = Store("Python")


s1.add_product(1011, "Parle-G", 10.00)
s1.add_product(5093, "Potato Chips", 5.00)
s1.add_product(7865, "Toffee", 0.50)
s1.add_product(2393, "Shampoo", 1.00)
s1.add_product(4536, "Basmati Rice", 200)


s1.display_menu()

s1.pick_product(1011, 10)
s1.pick_product(7865, 5)
s1.pick_product(4536, 5)

s1.generate_bill()
