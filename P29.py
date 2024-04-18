'''

Exercise 5: Generate random String of length 5

'''

import secrets
import string

def generate_random_string(length):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

random_string = generate_random_string(5)
print("Random string of length 5:", random_string)