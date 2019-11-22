import string
import secrets
import pyperclip


def length_check(components):
    if components > length:
        print("That exceeds the desired password length. Please re-enter.")
        variables_input()


def variables_input():
    while True:
        components = 0

        lower_chars = int(input("How many lowercase characters?  "))
        components += lower_chars
        length_check(components)

        upper_chars = int(input("How many uppercase characters?  "))
        components += upper_chars
        length_check(components)

        numbers = int(input("How many numbers?  "))
        components += numbers
        length_check(components)

        symbols = int(input("How many symbols?  "))
        components += symbols
        length_check(components)
        if components < length:
            print("Password is shorter than desired!")
            continue
        break
    return length, lower_chars, upper_chars, numbers, symbols


def generate_password(length, lower_chars, upper_chars, numbers, symbols):
    alphanums = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = "".join(secrets.choice(alphanums) for i in range(length))
        if (
            sum(character.islower() for character in password) >= lower_chars
            and sum(character.isupper() for character in password) >= upper_chars
            and sum(character.isdigit() for character in password) >= numbers
            and sum(character in string.punctuation for character in password)
            >= symbols
        ):
            break
    pyperclip.copy(password)
    print(f"\nPassword is: {password}")
    print("\n(This has been copied to your clipboard.)")


length = int(input("Password length?  "))
generate_password(*variables_input())
