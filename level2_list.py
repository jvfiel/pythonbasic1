#LISTS
bags = ['Hand Bag','Shoulder Bag']
print(bags)
print("---------------------")


for bag in (bags):
    print(bag)

print("--------------------")

#Looping through the list and enumerate
for i,bag in enumerate(bags):
    print(i, bag)

#In principle index always starts at 0

print("--------------------")
#split by comma to list/array
bags = 'Hand Bag,Shoulder Bag'
bags = bags.split(',')
print(bags)