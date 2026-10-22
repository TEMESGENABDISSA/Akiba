
def minimum_length(password, min_length=8):
    if len(password) < min_length:
        return False
    return True


def uppercase_letter(password):
    count = 0
    character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for apps in password:
        if apps in character:
            count += 1

    if count > 0:
        return True

    return False


def lower_case(password):
    count = 0

    for character in password:
        if character.islower():
            count = count + 1

    if count == 0:
        return False
    else:
        return True


def digit(password):
    count = 0
    formss = '0123456789'

    for digit in password:
        if digit in formss:
            count += 1

    if count == 0:
        return False
    return True


def special_character(password):
    count = 0
    special = '!@#$%^&*()-_+=?'

    for character in password:
        if character in special:
            count = count + 1

    if count == 0:
        return False
    else:
        return True


def analyze_password(password, min_length=8):
    analyzer = {
        "minimum_length": minimum_length(password, min_length),
        "uppercase": uppercase_letter(password),
        "lowercase": lower_case(password),
        "digit": digit(password),
        "special_character": special_character(password)
    }

    missing = []

    for requirement, result in analyzer.items():
        if result == False:
            missing.append(requirement)

    return {
        "password": password,
        "requirements": analyzer,
        "missing_requirements": missing,
        "strong": len(missing) == 0
    }


passwords = [
    "Tom12@abc",
    "temesgen",
    "TEMESGEN123",
    "Abc@123",
    "12345678"
]

for password in passwords:
    print(analyze_password(password))
