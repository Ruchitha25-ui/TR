#This is a compound interest calculator
principle=0
rate=0
time =0
while True:
    principle=float(input("Enter the principle amount:₹"))
    if principle<0:
        print("Principle can't be less than zero")
    else:
        break
while True:
    rate=float(input("Enter the rate:"))
    if principle<0:
        print("Rate can't be less than zero")
    else:
        break
while True:
    time=float(input("Enter the time:"))
    if principle<0:
        print("time can't be less than zero")
    else:
        break

balance=principle*pow((1+rate/100),time)
print(f"The balance after {time} years is ₹{balance:.2f}")