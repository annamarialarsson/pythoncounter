class Product:
	price = 0
	count = 0
	tax = 0
	def __init__ (self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax
	def price_with_tax(self):
		itemtotal = self.price * self.count * self.tax
		if itemtotal > 500:
			return 0.9 * itemtotal
		else:
			return itemtotal	

products = [Product(price = 900, count = 2, tax = 1.25), Product(price = 100, count = 1, tax = 1.06), Product(price = 1000, count = 1, tax = 1.25)]

total_price = 0

for product in products:
	total_price += product.price_with_tax()

print(total_price)