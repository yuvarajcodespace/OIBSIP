# ============================================================
#   BMI CALCULATOR - Oasis Infobyte Python Internship
#   Task 1: Beginner Level
#   Author: Yuvaraj.T.K
# ============================================================


def get_weight(unit):
    while True:
        try:
            if unit == '1':
                weight = float(input("  Enter your weight (in kg)    : "))
                if weight < 2 or weight > 300:
                    print("  ❌ Please enter a realistic weight (2 kg – 300 kg).\n")
                else:
                    return weight
            else:
                weight = float(input("  Enter your weight (in lbs)   : "))
                if weight < 5 or weight > 660:
                    print("  ❌ Please enter a realistic weight (5 lbs – 660 lbs).\n")
                else:
                    return weight
        except ValueError:
            print("  ❌ Invalid input! Please enter a number only.\n")


def get_height(unit):
    while True:
        try:
            if unit == '1':
                height = float(input("  Enter your height (in meters) : "))
                if height < 0.5 or height > 2.5:
                    print("  ❌ Please enter a realistic height (0.5 m – 2.5 m).\n")
                else:
                    return height
            else:
                height = float(input("  Enter your height (in inches) : "))
                if height < 20 or height > 100:
                    print("  ❌ Please enter a realistic height (20 – 100 inches).\n")
                else:
                    return height
        except ValueError:
            print("  ❌ Invalid input! Please enter a number only.\n")


def get_unit_choice():
    while True:
        print("\n  Select unit system:")
        print("  1. Metric   (kg / meters)")
        print("  2. Imperial (lbs / inches)")
        choice = input("  Enter 1 or 2: ").strip()
        if choice in ['1', '2']:
            return choice
        print("  ❌ Please enter 1 or 2.\n")


def convert_to_metric(weight_lbs, height_inches):
    weight_kg = weight_lbs * 0.453592
    height_m  = height_inches * 0.0254
    return round(weight_kg, 2), round(height_m, 2)


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️  You may need to gain some weight. Consult a doctor."
    elif 18.5 <= bmi < 25.0:
        return "Normal weight", "✅  Great! You have a healthy BMI. Keep it up!"
    elif 25.0 <= bmi < 30.0:
        return "Overweight", "⚠️  You may need to lose some weight. Consider diet & exercise."
    else:
        return "Obese", "🚨  Please consult a healthcare professional for guidance."


def ideal_weight(height_m):
    min_w = round(18.5 * (height_m ** 2), 1)
    max_w = round(24.9 * (height_m ** 2), 1)
    return min_w, max_w



def show_bmi_chart():
    print("\n  📋 BMI Categories (WHO Standard):")
    print("  ----------------------------------")
    print("  Below 18.5   →  Underweight")
    print("  18.5 – 24.9  →  Normal weight")
    print("  25.0 – 29.9  →  Overweight")
    print("  30.0 & above →  Obese")
    print()


def display_result(weight, height, bmi, category, advice):
    min_w, max_w = ideal_weight(height)

    print("\n" + "=" * 47)
    print("         📊  BMI CALCULATOR RESULT")
    print("=" * 47)
    print(f"  Weight        : {weight} kg")
    print(f"  Height        : {height} m")
    print(f"  Your BMI      : {bmi}")
    print(f"  Category      : {category}")
    print("-" * 47)
    print(f"  {advice}")
    print("-" * 47)
    print(f"  💡 Ideal weight : {min_w} kg  →  {max_w} kg")
    print("=" * 47)


def main():
    print("=" * 47)
    print("    🏃 WELCOME TO BMI CALCULATOR 🏃")
    print("=" * 47)

    show_bmi_chart()

    while True:
        print("-" * 47)

        unit = get_unit_choice()

        if unit == '1':
            weight = get_weight('1')
            height = get_height('1')
        else:
            weight_lbs    = get_weight('2')
            height_inches = get_height('2')
            weight, height = convert_to_metric(weight_lbs, height_inches)
            print(f"\n  (Converted → {weight} kg, {height} m)")

        bmi = calculate_bmi(weight, height)
        category, advice = classify_bmi(bmi)
        display_result(weight, height, bmi, category, advice)

        print("\n  Do you want to calculate again?")
        again = input("  Type 'yes' to continue or 'no' to exit: ").strip().lower()

        if again != 'yes':
            print("\n  👋 Stay healthy! Goodbye.\n")
            break

        print()


if __name__ == "__main__":
    main()