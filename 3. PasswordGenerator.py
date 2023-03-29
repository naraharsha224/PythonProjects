# Example project: Password Generator

# This program generates a random password with a given length.

import random
import string
# Get the password length from the user
length = int(input("Enter the length of your password:"))

def generate_password(length):
    # Check if password length is at least 8
    if length < 8:
        return "Password length must be at least 8 characters."
    # Define the set of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by selecting random characters from the set
    while True:
        password = ''.join(random.choice(chars) for i in range(length))
        if (any(char.isupper() for char in password)
                and any(char.islower() for char in password)
                and any(char.isdigit() for char in password)
                and any(char in string.punctuation for char in password)
                and not password.isnumeric()
                and not password.isalpha()
                and not password.isalnum()):
            # Password meets complexity requirements
            return password

password = generate_password(length)
print(password)

'''
This Python code generates a random password of a given length by selecting characters randomly from a set of characters that includes letters (uppercase and lowercase), digits, and punctuation. The password generator ensures that the generated password meets certain complexity requirements, including:

- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one punctuation character
- Not entirely numeric
- Not entirely alphabetic
- Not entirely alphanumeric


Here is a step-by-step breakdown of the code:

1. The program starts by importing the random and string modules.
2. The user is prompted to enter the length of the password.
3. The generate_password function is defined, which takes the password length as an argument.
4. The function checks if the password length is at least 8 characters. If it's less than 8, it returns an error message.
5. A set of characters to choose from is defined, which includes letters (uppercase and lowercase), digits, and punctuation.
6. The function generates the password by selecting random characters from the set until it meets the complexity requirements. It uses a while loop with a True condition to keep generating passwords until a valid password is found.
7. The generated password is checked against the complexity requirements using a series of checks, including checking for the presence of uppercase and lowercase letters, digits, and punctuation. If the password meets all the requirements, it is returned from the function.
8. The main code calls the generate_password function with the password length provided by the user.
9. The generated password is printed to the console.
'''
