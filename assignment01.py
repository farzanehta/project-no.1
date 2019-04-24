weight = int(input("weight in kilograms: "))
height = float(input("height in metres: "))

BMI = weight / (height ** 2)
print(BMI)

if BMI < 18.5:
    print("Underweight")
elif 18.5 < BMI < 25:
    print("Normal")
elif 25 < BMI < 30:
    print("Overweight")
elif BMI > 30:
    print("Obesity")
