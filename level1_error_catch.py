#Variables
name = "Shoulder Bag"
price = 1000
price_f = 1000.50
color = 'blue'

#BASIC OPERATIONS
size = "XL"
print("-----------------")
print(size + " " + name)
try:
    print("Price: ", price - "500")
except Exception as e:
    print(e, " critical error!")
    #catch for not to crash or
    #print("Price: ", price - float("500"))

#Note: you can convert the variable to another type