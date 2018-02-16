# LISTS
bags = ['Hand Bag', 'Shoulder Bag']


#in Search for a bag

#1 Q: what is the result?
look_for = "Hand Bag"
if look_for in bags:
    print("found!")
else:
    print("didnt found bag")

#2 Q: what is the result?
look_for = "Sling Bag"
if look_for in bags:
    print("found!")
else:
    print("didnt found bag")


#3 Q: what is the result?
look_for = "Hand bag"
if look_for in bags:
    print("found!")
else:
    print("didnt found bag")


#4 Adding a bag to the list
look_for = "Backpack"
if look_for in bags:
    print("found!")
else:
    print("didnt found bag")
    bags.append(look_for)


#SORTING
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.sort();
print("List : ", aList)

