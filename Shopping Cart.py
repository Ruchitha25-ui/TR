#This program will take the input of the food and prices and prints the bill
foods = []
prices = []
total=0

while True:
    food=input("Enter the food to buy (press q to quit):")
    if food.lower()=="q":
        break
    else:
        price= int(input(f"Enter the price of {food}: "))
        foods.append("food")
        prices.append("price")

print("-----YOUR CART-------")
for food in foods:
    print(food, end=",")

for price in prices:
 total = total + price
print(f"Your total bill is {total} rupees")
