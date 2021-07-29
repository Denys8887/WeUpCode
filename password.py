import secrets
import string

num = string.digits
upper = string.ascii_uppercase
lower = string.ascii_lowercase
symbols = string.punctuation

print("Welcome to password generator\n")
password_length = int(input("Enter the length of password:"))


def password_generator(cbl, length):
    printable = fetch_string_constant(cbl)

    printable = list(printable)
    random_password = "".join(secrets.choice(printable) for _ in range(length))
    if length < 8:
        return f"You password is not secure!\n{random_password} "
    else:
        return f"Password is secured:\n{random_password}"


def password_combination_choice():
    want_digits = input("Want digits ? (True or False) : ")
    want_letters_upper = input("Want letters Upper ? (True or False): ")
    want_letters_lower = input("Want letters lower ? (True or False): ")
    want_symbols = input("Want punctuation ? (True or False): ")

    try:
        want_digits = eval(want_digits.title())
        want_letters_upper = eval(want_letters_upper.title())
        want_letters_lower = eval(want_letters_lower.title())
        want_punts = eval(want_symbols.title())
        return [want_digits, want_letters_upper, want_letters_lower, want_punts]

    except NameError as e:
        print("Invalid value. Use either True or False")
        print("Invalidity returns a default, try again to regenerate")

    return [True, True, True,True]


def fetch_string_constant(choice_list):
    string_constant = ''
    string_constant += num if choice_list[0] else ''
    string_constant += upper if choice_list[1] else ''
    string_constant += lower if choice_list[2] else ''
    string_constant += symbols if choice_list[3] else ''
    return string_constant


if __name__ == '__main__':
    choice_list = password_combination_choice()
    password = password_generator(choice_list, password_length)
    print(password)
