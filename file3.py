value = input("Enter number: ")
if value.isdigit() and int(value) % 2 == 0:
    print("The number", value, "is even")
elif value.isdigit() and int(value) % 2 != 0:
    print("The number", value, "is odd")
else:
    print("The value", value, "is not a number")
