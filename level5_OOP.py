#OOP - Reusable code
class Bag:

    def __init__(self, name, color, size, price):
        self.name = name
        self.color = color
        self.size = size
        self.price = price
        self.dict = {"name":name,"color":color,"size":size,"price":price}

    def discount(self,amount):
        self.price -= amount
        self.update_dict()

    def increase_price(self,amount):
        self.price += amount
        self.update_dict()

    def update_dict(self):
        self.dict = {"name": self.name, "color": self.color, "size": self.size, "price": self.price}


b = Bag("Hand bag", "Blue", "XL", 1000.00)
b.discount(100)
print(b.price)

b.increase_price(50)
print(b.price)

#Q: What is the final price?