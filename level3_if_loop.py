# LISTS
bags = ['Hand Bag', 'Shoulder Bag']


#in Search for a bag

look_for = "Hand Bag"
for i,bag in enumerate(bags):
    if look_for == bag:
        print("found!")
        break

print("--------------------")

#SHORT VER.
if look_for in bags:
    print("found!")
else:
    print("didnt found bag")


while True:
    print("Hello")


