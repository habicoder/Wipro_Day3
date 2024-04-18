#Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

'''
random.randrange(start, stop, step)


import random
print("Generating 3 random integer number between 100 and 999 divisible by 5")
for num in range(3):
    print(random.randrange(100, 999, 5), end=', ')
    '''
    
import random

random_integers = [random.randint(100, 999) for _ in range(3)]
random_integers_divisible_by_5 = [num for num in random_integers if num % 5 == 0]

print("Random integers divisible by 5:", random_integers_divisible_by_5)