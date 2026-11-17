# Basal Metabolic Rate
# Men: BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5
# Women: BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161

weight_kg = int(input("Enter your weight in kilograms: "))
height_cm = int(input("Enter your height in centimeters: "))
age_years = int(input("Enter your age in years: "))

bmr_m = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) + 5
bmr_f = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) - 161
print("If Male your BMR is:", bmr_m)
print("If Female your BMR is:", bmr_f)
