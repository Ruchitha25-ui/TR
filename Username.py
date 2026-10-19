Username=input("Enter the user name:")
#1.username should not be more than 12 characters
#2.username must not contain spaces
#3.username must not contain digits
if len(Username)>12:
    print("The username shouldn't be more than 12 characters ")
elif not Username.isalpha():
    print("The username should only contain letters")
else:
    print(f"Welcome {Username}")

