unit = input("Are you using standard units(y/n)? ").lower()
weight = int(input("weight: "))
height = float(input("height: "))
BMI_SD = weight / (height ** 2)
BMI_non = (weight / (height ** 2)) * 703

if unit == "y":
    print(BMI_SD)
    if BMI_SD < 18.5:
        print("Underweight")
    if 18.5 < BMI_SD < 25:
        print("Normal")
    if 25 < BMI_SD < 30:
        print("Overweight")
    if BMI_SD > 30:
        print("Obesity")
elif unit == "n":
    print(BMI_non)
    if BMI_non < 18.5:
        print("Underweight")
    if 18.5 < BMI_non < 25:
        print("Normal")
    if 25 < BMI_non < 30:
        print("Overweight")
    if BMI_non > 30:
        print("Obesity")
else:
    print("sry, something is wrong!")

