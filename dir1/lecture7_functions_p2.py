# ***** function params ***** #
# def get_user_data(name, last_name, age=18, secret_number=7):
#     print(f"User: {name} {last_name} {age}")
#     if secret_number != 7:
#         print(f"User has changed the secret number")
#
#
# get_user_data("Vasyl", "Larin")
# get_user_data("Vasyl", "Larin", 32)
# get_user_data("Vasyl", "Larin", age=32)
# get_user_data("Vasyl", "Larin", secret_number=30)


# !====== python unpacking ===== #
# a, b, *c = [1, 2, 3, 4, 5]
# print(a, b, c)

# ===== function arguments: *args ===== #
# def get_user_data(name, last_name, *args):
#     print(f"User: {name} {last_name}. Other arguments: {args}")


# get_user_data("Vasyl", "Larin", 18, 77, "I love Python!")


# ===== function arguments: **kwargs ===== #
# def get_user_data(name, last_name, **kwargs):
#     print(f"User: {name} {last_name} {kwargs.get('age')}")
#     secret_number = kwargs.get('secret_number')
#     if secret_number and secret_number != 7:
#         print(f"User has changed the secret number")
#
#
# get_user_data("Vasyl", "Larin",
#               age=18, secret_number=77, text="I love Python!")

# !===== args and kwargs namings ===== #
# def get_user_data(name, last_name, *pin_codes, **other_user_data):
#     print(f"User: {name} {last_name}")
#     print(f"Pin codes: {pin_codes}")
#
#     age = other_user_data.get("age")
#     if age:
#         print(f"User is {age} years old.")
#
#
# get_user_data("Vasyl", "Larin", 123, 4444, 5555, 6,
#               age=18, secret_number=77, text="I love Python!")


# ===== Python scope ===== #
# Local scope, Enclosing, Global scope, Built-in scope
# global scope
# a = 1

# def test():
#     # local scope
#     a = 2

# built-in scope
# print(max)


# !===== high order functions ===== #

# def validate_length(value):
#     if len(value) < 2 or len(value) >= 10:
#         print("Value should be from 2 to 10 characters")
#         return False
#     return True
#
#
# def validate_alnum(value):
#     if not value.isalnum():
#         print("Value should contain only letters and digits")
#         return False
#     return True
#
#
# def set_password(validators, password):
#     for validator in validators:
#         if validator(password):
#             continue
#         else:
#             print("Could not save password.")
#             return None
#
#     print("Valid password")
#
#
# password = input("Enter a password: ")
# set_password((validate_length, validate_alnum), password)


# ===== closures ===== #

# def closure(message):
#     def print_message():
#         print(message)    # value closes here
#     return print_message
#
#
# say_hello = closure("Hello!")
# say_goodbye = closure("Good Bye!")
# hello_world = closure("Hello, World!")
# say_hello()
# say_goodbye()
# hello_world()


# ===== lambdas ===== #
# def multiply(x):
#     return x*2
#
#
# multiply1 = lambda x: x * 2
#
# print(multiply(4))
# print(multiply1(4))

# +====== entrypoint ===== #
















































