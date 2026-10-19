#This code will find the third side of the right angle triangle

import math
a =float(input("Enter the side a value: "))
b=float(input("Enter the side b value: "))
c=round(math.sqrt(pow(a,2)+pow(b,2)),2)
print(f"the third side of the triangle is {c}")
