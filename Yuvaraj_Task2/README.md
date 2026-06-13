# 🔐 Password Generator

![Python](https://img.shields.io/badge/Python-3.x-8B5E34)
![Level](https://img.shields.io/badge/Level-Beginner-D4A017)
![Status](https://img.shields.io/badge/Status-Completed-6A994E)

## Description

A command-line **Password Generator** built in Python. This project generates a random secure password based on user preferences like length and character types. It supports uppercase letters, lowercase letters, numbers and special characters with a built-in **password strength checker** and an intuitive **comma-based selection menu**.

## Features

- Choose password length (minimum 6)
- Select character types using comma-separated input (e.g. `1,2,4`)
- Visual ✅ ❌ feedback for selected and unselected types
- Handles invalid choices — accepts valid ones, rejects invalid ones
- Handles empty input and double comma inputs gracefully
- Password strength indicator (Weak / Medium / Strong / Very Strong)
- Validates yes/no responses properly
- Generate multiple passwords in one session

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| `random` module | Generating random password characters |
| `string` module | Accessing character sets (uppercase, digits, punctuation) |
| `set` operations | Managing selected character types |
| `try/except` | Input validation and error handling |

## How to Run

**Step 1** — Make sure Python is installed:
```bash
python --version
```

**Step 2** — Run the program:
```bash
python password_generator.py
```

## Sample Output

```
==================================================
    🔐 WELCOME TO PASSWORD GENERATOR 🔐
==================================================

  Enter password length (min 6): 12

  Select character types:
  --------------------------------------
  ⬜  1.  Uppercase Letters    ( A - Z )
  ⬜  2.  Lowercase Letters    ( a - z )
  ⬜  3.  Numbers              ( 0 - 9 )
  ⬜  4.  Special Characters   ( @ # $ )
  --------------------------------------
  💡 Enter choices separated by comma
     e.g.  1,2  or  1,3,4  or  1,2,3,4

  Your choice: 1,2,3,4

  Character types selected:
  --------------------------------------
  ✅  1.  Uppercase Letters    ( A - Z )
  ✅  2.  Lowercase Letters    ( a - z )
  ✅  3.  Numbers              ( 0 - 9 )
  ✅  4.  Special Characters   ( @ # $ )
  --------------------------------------

==================================================
         🔑  GENERATED PASSWORD
==================================================
  Password : aB3@kLmN7#pQ
  Length   : 12 characters
  Strength : Very Strong 💪

  ✅ Copy and save your password safely!
==================================================
```

## Author

**Yuvaraj.T.K** — Python Intern @ Oasis Infobyte

#oasisinfobyte #oasisinfobytefamily #internship #python
