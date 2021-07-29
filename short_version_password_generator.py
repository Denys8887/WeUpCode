import random
import secrets
import string

print("Welcome to password generator\n")

num = string.digits
upper = string.ascii_uppercase
lower = string.ascii_lowercase
symbols = string.punctuation


def password_generator():
    user_input = input("Do you want a strong? Yes/No: ")

    if user_input.title() == 'No':
        return random.choice(['London', 'Paris', 'Warsaw', 'Milan', 'Prague'])

    else:
        password_length = int(input("Enter the length of password:"))
        letters = f'{num}{upper}{lower}{symbols}'
        random_password = "".join(secrets.choice(letters) for _ in range(password_length))

        return random_password


print(password_generator())
