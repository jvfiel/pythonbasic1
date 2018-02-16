simple_bag = {'name':'Hand Bag','price':100.00}
print(simple_bag['name'])
print(simple_bag['price'])

#LIST OF DICT
bags_dic = [
            {'name':'Hand Bag','price':100.00},
            {'name':'Shoulder Bag','price':500.00}
        ]
print(bags_dic)

print("--------------------")

for i,bag in enumerate(bags_dic):
    print("Bag: {0}, Price: {1}".format(bag['name'],bag['price']))

print("--------------------")
for i,bag in enumerate(bags_dic):
    # print("Bag: {0}, Price: {1}".format(bag['name'],bag['price']))
    bag.update({'price':1000.00})
    bag.update({'price':1000.00,'size':'XL'})