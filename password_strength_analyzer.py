import re
import random
import string

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Increase password length to at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    if len(password) >= 12:
        score += 2

    if score <= 2:
        strength = "Weak"
    elif score <= 5:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, suggestions

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

password = input("Enter Password: ")

strength, score, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)
print("Score:", score)

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)

    print("\nSuggested Strong Password:")
    print(generate_strong_password())
else:
    print("\nExcellent! Your password is secure.")