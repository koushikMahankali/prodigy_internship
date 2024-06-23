#Password_Complexity_Checker
import re
import getpass
print("Password Complexity Checking Tool")
def assess_password_strength(password):
    has_numbers = any(char.isdigit() for char in password)
    has_upper_lower_case = any(char.isupper() or char.islower() for char in password)
    meets_length_requirement = len(password) >= 8
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    met_criteria_count = sum([has_numbers, has_upper_lower_case, meets_length_requirement, has_special_characters])
    if met_criteria_count == 4:
        return "Password Strength Level: Very Strong (All criteria are met)."
    elif met_criteria_count == 3:
        return "Password Strength Level: Moderately Strong (Any 3 criteria are met)."
    elif met_criteria_count == 2:
        return "Password Strength Level: Strong (Any 2 criteria are met)."
    else:
        return "Password Strength Level: Weak (None or only one criterion is met)."
password_input = getpass.getpass("Enter your password: ")
masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1]
result = assess_password_strength(password_input)
print("Entered Password: {}".format(masked_password))
print("")
print(result)
print("")
tips = [
    "Here are some quick tips for creating a secure password:",
    "1. Length: Aim for at least 12 characters.",
    "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
    "3. Avoid Common Words: Don't use easily guessable information.",
    "4. No Personal Info: Avoid using names, birthdays, or personal details.",
    "5. Use Passphrases: Consider combining multiple words or a sentence.",
]
for tip in tips:
    print(tip)