
import random

def password_generator(password_length):
    password = ""
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

    for _ in range(password_length):
        password += random.choice(charset)

    return f"Generated Password: {password}"

password_length = int(input("Enter the length of the password: "))

while password_length < 8:
    password_length = int(
        input("Password length should be at least 8 characters. Please enter a valid length: ")
    )

print(password_generator(password_length))
