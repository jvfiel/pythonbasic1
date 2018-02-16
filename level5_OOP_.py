#OOP - Reusable code
from level5_OOP import Bag

b = Bag("Hand bag", "Blue", "XL", 1000.00)
b.discount(100)
print(b.price)

b.increase_price(50)
print(b.price)

#Q: What is the final price?

"""
Activity!
-Make a class name it GymParticipant
-has the following attributes/variables:
--Name
--Weight
--Endurance
-GymParticipant has method burnfat()
--burnfat() - will deduct weight
-GymParticipant has method jog()
--jog() - will increase Endurance
-Make a list of GymParticipants
--Names of Particpants
---Harris
---Nancy
--Stats of Particpants
---Harris, Endurance: 10, Weight: 50
---Nancy, Endurance: 8, Weight: 45
--Harris jogs x3
--Nancy burns fat x2
-Remove Nancy in the List
"""

#Note: Operators
# "*" - multiply
# "/" - divide
# "-" - minus/deduct
# "+" - add/plus
#Remove from list
#gym.remove(nancy)