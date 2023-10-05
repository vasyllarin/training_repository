value = input("Enter value: ")
if value.isdigit() and int(value) % 2 == 0:
    print("Entered value", value, "is an even number")
elif value.isdigit() and int(value) % 2 != 0:
    print("Entered value", value, "is an odd number")
else:
    print("Entered value", value, "is a text with length", len(value))
