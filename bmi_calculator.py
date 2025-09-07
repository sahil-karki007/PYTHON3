def calculate_bmi(weight , height):

    a = weight / (height**2)
    return a
def bmi_classify(bmi):
    #Classify BMI according to WHO standards.

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    elif 30.0 <= bmi <= 34.9:
        return "Obesity (Class I)"
    elif 35.0 <= bmi <= 39.9:
        return "Obesity (Class II)"
    else:
        return "Obesity (Class III - Severe)"