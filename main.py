import random
import string

def generate_password(*, letters=True, symbols=False, numbers=False, duplicates=False, pass_length=8):
    if pass_length < 8:
        print("Довжина паролю має бути не менше 8 символів.")
        return

    characters = ''

    if letters:
        characters += string.ascii_letters

    if symbols:
        characters += "!@#$%^&*()+"

    if numbers:
        characters += string.digits

    if not characters:
        print("Виберіть хоча б один тип символів для паролю.")
        return

    password = ''
    while len(password) < pass_length:
        char = random.choice(characters)
        if duplicates:
            password += char
        else:
            if char not in password:
                password += char

    return password

password = generate_password(letters=True, symbols=True, numbers=True, duplicates=True, pass_length=12)
print("Згенерований пароль:", password)
