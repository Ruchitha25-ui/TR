#This code will convert the weight into different units
weight=float(input("Please enter the weight of the person"))
unit=input(" kilograms(k) or pounds(l)?")
if unit=="k":
    weight=round(weight*2.205,1)
    print(f"{weight} lbs")
elif unit=="l":
    weight=round(weight/2.205,1)
    print(f"{weight} lbs")
else:
    print(f"{unit} is not a valid unit")