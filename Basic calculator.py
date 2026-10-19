#This is a basic python calculator
operator=input("Enter the operation you would like to perform(+,-,*,/): ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if operator=="+":
    result=round(num1+num2,3)
    print(f"The sum of {num1} and {num2} is {result}")
elif operator=="-":
    result=round(num1-num2,3)
    print(f"The difference of {num1} and {num2} is {result}")
elif operator=="*":
    result=round(num1*num2,3)
    print(f"The product of {num1} and {num2} is {result}")
elif operator=="/":
    result=round(num1/num2,3)
    print(f"The quotient of {num1} and {num2} is {result}")
else:
    print(f"The operator {operator} is invalid")
