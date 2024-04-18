#Exercise 3: Generate 6 digit random secure OTP

import secrets

def generate_otp():
    return ''.join(secrets.choice('0123456789') for _ in range(6))

otp = generate_otp()
print("Generated OTP:", otp)
