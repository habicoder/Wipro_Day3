'''

Exercise 7: Generate random secure token of 64 bytes and random URL

'''

import secrets
import string


secure_token = secrets.token_hex(32)  


random_string = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(10))  
url = f"https://example.com/{random_string}"

print("Random secure token:", secure_token)
print("Random URL:", url)