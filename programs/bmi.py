# Body Mass Index
# Metric formula: BMI = weight (kg) / height^2 (m^2)

weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))
bmi = weight_kg / (height_m ** 2)
print("Your BMI is:", bmi)
print(f"Your BMI is: {bmi:.2f}")
