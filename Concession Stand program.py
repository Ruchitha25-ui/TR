#Concession Stand program

menu={"pizza":200,
      "burger":125,
      "ice-cream":50,
      "chicken":350,
      "samosa":30,
      "coke":40,
      "milkshake":145}
cart=[]
total=0
print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f} rupees")
print("------------------------")

while True:
    food = input("Select an item(press q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------------------------------------------------")
for food in cart:
    total+=menu.get(food)
    print(food, end=", ")

print()
print(f"Total cost: {total:.2f} rupees")
print("------------------------------------------------")


