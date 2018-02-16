
#LIST OF DICT
bags_dic = [
            {'name':'Hand Bag','price':100.00},
            {'name':'Shoulder Bag','price':500.00}
        ]
print(bags_dic)


from level5_OOP import Bag
b = Bag('backpack','blue','L','999')
bags_dic.append(b.dict)
print("--------------------")
for i,bag in enumerate(bags_dic):
    print("Bag: {0}, Price: {1}".format(bag['name'],bag['price']))

"""
Activity!
Change price of backpack to 1,599.00
change name of backpack to "anti-thief backpack"
Discount the price of Hand Bag, less 50 USING discount()
Increase the price of Shoulder Bag, less 100 increase_price()
"""