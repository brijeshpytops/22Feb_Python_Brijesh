age = input("Enter your age: ")
age = int(age)


if age >= 18:
    weight = input("Enter your weight: ")
    weight = float(weight)
    if  weight >= 50:
        print("You can donate")
    else:
        print("You can not donate(weight<50)")
else:
    print("You can not donate(age<18)")