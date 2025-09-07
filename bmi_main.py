from bmi_calculator import calculate_bmi , bmi_classify

weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your weight in meters : "))

bmi = calculate_bmi(weight , height)

classify = bmi_classify(bmi)

print(f"Your BMI : {bmi}")
print(f"Category : {classify}")