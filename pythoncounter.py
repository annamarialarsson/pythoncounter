class Product:
	price = 0
	count = 0
	tax = 0
	name = "0"
	def __init__ (self, price, count, tax, name):
		self.price = price
		self.count = count
		self.tax = tax
		self.name = name
	def price_with_tax(self):
		itemtotal = self.price * self.count * self.tax
		if itemtotal > 500:
			return 0.9 * itemtotal
		else:
			return itemtotal	

products = [Product(price = 900, count = 2, tax = 1.25, name = "Mattsson"), Product(price = 100, count = 1, tax = 1.06, name = "Instruktionsbok"), Product(price = 1000, count = 1, tax = 1.25, name = "Husvagn"), Product(price = 100, count = 1, tax = 1.25, name = "Luftballong")]

total_price = 0

for product in products:
	total_price += product.price_with_tax()

for product in products:
	print(product.name, product.price_with_tax())

print(total_price)