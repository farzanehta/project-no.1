unit = input("Are you using standard units(y/n)? ").lower()
weight = int(input("weight: "))
height = float(input("height: "))
BMI = weight / (height ** 2)


if unit == "n":
    BMI = BMI * 703

    print(BMI)
    if BMI < 18.5:
        print("Underweight")
    if 18.5 < BMI < 25:
        print("Normal")
    if 25 < BMI < 30:
        print("Overweight")
    if BMI > 30:
        print("Obesity")

else:
    print("sry, something is wrong!")

