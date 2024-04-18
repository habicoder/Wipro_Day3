'''

Exercise 8: Roll dice in such a way that every time you get the same number

'''

def roll_dice():
    return 6  

for i in range(5):
    result = roll_dice()
    print("Roll", i+1, ":", result)