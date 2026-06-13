# 🏃 BMI Calculator

![Python](https://img.shields.io/badge/Python-3.x-FF6B6B)
![Level](https://img.shields.io/badge/Level-Beginner-FF9F43)
![Status](https://img.shields.io/badge/Status-Completed-FECA57)

## Description

A command-line **BMI (Body Mass Index) Calculator** built in Python. This project takes user inputs like weight and height, calculates the BMI, and classifies it into standard WHO health categories. It supports both **Metric** (kg/meters) and **Imperial** (lbs/inches) unit systems with proper input validation and error handling.

## Features

- Supports both Metric (kg / meters) and Imperial (lbs / inches) units
- Calculates BMI using the formula: `BMI = weight / (height × height)`
- Classifies BMI into WHO standard health categories
- Shows ideal weight range based on your height 💡
- Handles invalid inputs gracefully (letters, out of range, negative values)
- Validates yes/no responses properly
- Calculate multiple times in one session

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| `math` operations | BMI formula calculation |
| `float()` conversion | Handling decimal inputs |
| `try/except` | Input validation and error handling |

## How to Run

**Step 1** — Make sure Python is installed:
```bash
python --version
```

**Step 2** — Run the program:
```bash
python bmi_calculator.py
```

## Sample Output

```
===============================================
    🏃 WELCOME TO BMI CALCULATOR 🏃
===============================================

  📋 BMI Categories (WHO Standard):
  ----------------------------------
  Below 18.5   →  Underweight
  18.5 – 24.9  →  Normal weight
  25.0 – 29.9  →  Overweight
  30.0 & above →  Obese

  Select unit system:
  1. Metric   (kg / meters)
  2. Imperial (lbs / inches)
  Enter 1 or 2: 1

  Enter your weight (in kg)    : 70
  Enter your height (in meters): 1.75

===============================================
         📊  BMI CALCULATOR RESULT
===============================================
  Weight        : 70.0 kg
  Height        : 1.75 m
  Your BMI      : 22.86
  Category      : Normal weight
-----------------------------------------------
  ✅  Great! You have a healthy BMI. Keep it up!
-----------------------------------------------
  💡 Ideal weight : 56.7 kg  →  76.3 kg
===============================================
```

## Author

**Yuvaraj.T.K** — Python Intern @ Oasis Infobyte

#oasisinfobyte #oasisinfobytefamily #internship #python