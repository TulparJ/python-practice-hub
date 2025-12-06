def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Status: Underweight")
elif bmi < 25:
    print("Status: Normal weight")
elif bmi < 30:
    print("Status: Overweight")
else:
    print("Status: Obese")
