# ============================================================
#   PASSWORD GENERATOR
#   Oasis Infobyte Python Internship - Task 2
#   Author: Yuvaraj.T.K
# ============================================================

import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("  Enter password length (min 6): "))
            if length < 6:
                print("  ❌ Password length must be at least 6.\n")
            else:
                return length
        except ValueError:
            print("  ❌ Invalid input! Please enter a number.\n")


def get_character_types():
    while True:
        print("\n  Select character types:")
        print("  " + "-" * 38)
        print("  ⬜  1.  Uppercase Letters    ( A - Z )")
        print("  ⬜  2.  Lowercase Letters    ( a - z )")
        print("  ⬜  3.  Numbers              ( 0 - 9 )")
        print("  ⬜  4.  Special Characters   ( @ # $ )")
        print("  " + "-" * 38)
        print("  💡 Enter choices separated by comma")
        print("     e.g.  1,2  or  1,3,4  or  1,2,3,4")

        choice = input("\n  Your choice: ").strip()

        # Bug Fix 1: handle empty input
        if not choice:
            print("  ❌ Input cannot be empty! Please enter your choices.\n")
            continue

        # split by comma and clean spaces
        parts = [c.strip() for c in choice.split(',')]

        # remove empty parts caused by extra commas like "1,,2"
        parts = [p for p in parts if p != '']

        if not parts:
            print("  ❌ Input cannot be empty! Please enter your choices.\n")
            continue

        # separate valid and invalid parts
        valid   = [p for p in parts if p in ['1', '2', '3', '4']]
        invalid = [p for p in parts if p not in ['1', '2', '3', '4']]

        # show error only for invalid ones
        if invalid:
            print(f"  ❌ Invalid choice(s): {', '.join(invalid)} — only 1,2,3,4 are allowed")

        # if no valid choices at all, ask again
        if not valid:
            print("  ❌ Please enter at least one valid choice!\n")
            continue

        selected = set(valid)

        # show result with tick and cross
        print("\n  Character types selected:")
        print("  " + "-" * 38)
        print(f"  {'✅' if '1' in selected else '❌'}  1.  Uppercase Letters    ( A - Z )")
        print(f"  {'✅' if '2' in selected else '❌'}  2.  Lowercase Letters    ( a - z )")
        print(f"  {'✅' if '3' in selected else '❌'}  3.  Numbers              ( 0 - 9 )")
        print(f"  {'✅' if '4' in selected else '❌'}  4.  Special Characters   ( @ # $ )")
        print("  " + "-" * 38)

        return '1' in selected, '2' in selected, '3' in selected, '4' in selected


def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(use_upper, use_lower, use_digits, use_special):
    count = sum([use_upper, use_lower, use_digits, use_special])
    if count == 1:
        return "Weak   🔴"
    elif count == 2:
        return "Medium 🟡"
    elif count == 3:
        return "Strong 🟢"
    else:
        return "Very Strong 💪"


def ask_generate_again():
    # Bug Fix 2: validate yes/no properly
    while True:
        again = input("\n  Generate another? (yes/no): ").strip().lower()
        if again == 'yes':
            return True
        elif again == 'no':
            return False
        else:
            print("  ❌ Invalid input! Please type 'yes' or 'no'.\n")


def main():
    print("=" * 50)
    print("    🔐 WELCOME TO PASSWORD GENERATOR 🔐")
    print("=" * 50)

    while True:
        print("\n  Customize your password:")
        print("-" * 50)

        length = get_password_length()
        use_upper, use_lower, use_digits, use_special = get_character_types()

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        strength = check_strength(use_upper, use_lower, use_digits, use_special)

        print("\n" + "=" * 50)
        print("         🔑  GENERATED PASSWORD")
        print("=" * 50)
        print(f"  Password : {password}")
        print(f"  Length   : {length} characters")
        print(f"  Strength : {strength}")
        print("\n  ✅ Copy and save your password safely!")
        print("=" * 50)

        if not ask_generate_again():
            print("\n  👋 Stay safe online! Goodbye.\n")
            break


if __name__ == "__main__":
    main()